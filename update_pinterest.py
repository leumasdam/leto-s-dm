#!/usr/bin/env python3
"""
update_pinterest.py — pridá Pinterest Trends dáta (top growing + monthly) do data.json.

Metodológia:
  Pinterest API v5 endpoint /v5/trends/keywords/{region}/top/{trend_type}
  vracia top trending keywords pre daný región a typ trendu.

  Region: AT (Rakúsko) — najbližšia geograficky aj kultúrne k SK,
  ktorú Pinterest API podporuje. SK samostatne API neponúka.

  Trend types:
    - growing  → najrýchlejšie rastúce queries (year-over-year)
    - monthly  → top vyhľadávané za posledný mesiac

Autorizácia:
  Bearer token v env var PINTEREST_ACCESS_TOKEN.
  Ak chýba, skript tichý exit (workflow pokračuje bez chyby).

Použitie:
    export PINTEREST_ACCESS_TOKEN="pina_…"
    python update_pinterest.py
"""

import json
import os
import sys
from datetime import date
from pathlib import Path
from urllib import request, parse, error

REGION = "AT"
TREND_TYPES = ["growing", "monthly"]
TOP_N = 8  # koľko queries z každého trend_type uložiť
API_BASE = "https://api.pinterest.com/v5"
DATA_PATH = Path(__file__).parent / "data.json"

# Voliteľné filtre — Pinterest podporuje napr. interests, ages, genders.
# Pre dm beauty/lifestyle dáva zmysel zúžiť na beauty + home interest.
# Ak filter vráti 0 výsledkov, fallback bez filtra.
INTEREST_IDS = []  # napr. ["beauty"] — necháme prázdne, sledujeme celý market


def fetch_trends(token: str, trend_type: str, region: str = REGION):
    """Zavolá Pinterest Trends API a vráti list dictov {keyword, pct_growth, ...}."""
    url = f"{API_BASE}/trends/keywords/{region}/top/{trend_type}"
    qs = {}
    if INTEREST_IDS:
        qs["interests"] = ",".join(INTEREST_IDS)
    if qs:
        url += "?" + parse.urlencode(qs)

    req = request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    })
    try:
        with request.urlopen(req, timeout=20) as r:
            payload = json.loads(r.read().decode("utf-8"))
    except error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:200]
        print(f"  ✗ Pinterest API {e.code} ({trend_type}): {body}", file=sys.stderr)
        return None
    except (error.URLError, TimeoutError) as e:
        print(f"  ✗ Pinterest API network error ({trend_type}): {e}", file=sys.stderr)
        return None

    items = payload.get("trends") or payload.get("data") or []
    out = []
    for it in items[:TOP_N]:
        # Pinterest podľa verzie vracia rôzne polia — vezmeme to, čo nájdeme.
        kw = it.get("keyword") or it.get("query") or it.get("term")
        if not kw:
            continue
        growth = it.get("pct_growth_wow") or it.get("pct_growth_mom") or it.get("pct_growth_yoy")
        out.append({
            "q": str(kw),
            "growth": int(growth) if isinstance(growth, (int, float)) else None,
        })
    return out


def main() -> int:
    token = os.environ.get("PINTEREST_ACCESS_TOKEN", "").strip()
    if not token:
        print("ℹ PINTEREST_ACCESS_TOKEN nie je nastavený — preskakujem Pinterest update.")
        return 0

    print(f"Sťahujem Pinterest Trends · region={REGION} · top {TOP_N} z {len(TREND_TYPES)} typov…")

    pin_data = {"region": REGION, "lastUpdated": date.today().isoformat()}
    any_success = False
    for tt in TREND_TYPES:
        print(f"  → trend_type={tt}")
        items = fetch_trends(token, tt)
        if items is None:
            continue  # už zalogované
        if not items:
            print(f"    žiadne items vrátené")
            continue
        pin_data[tt] = items
        any_success = True
        print(f"    ✓ {len(items)} keywords")

    if not any_success:
        print("✗ Žiadny trend_type nevrátil dáta — data.json nemenený.", file=sys.stderr)
        return 1

    # Merge do existujúceho data.json (Google Trends sekciu nechávame nedotknutú).
    existing = {}
    if DATA_PATH.exists():
        try:
            existing = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("⚠ data.json je poškodený, prepisujem.", file=sys.stderr)

    existing["pinterest"] = pin_data
    DATA_PATH.write_text(
        json.dumps(existing, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"\n✓ Pinterest dáta zapísané do {DATA_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
