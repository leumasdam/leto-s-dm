#!/usr/bin/env python3
"""
update_data.py — generuje data.json z reálnych Google Trends SK dát.

Pre každý keyword porovná priemerný záujem v lete (jún–august) vs. január toho
istého roka a vyráta % nárast. Výsledok zapíše do data.json (zachová ostatné
polia ako openTimes, ak existujú).

Použitie:
    pip install -r requirements.txt
    python update_data.py

Pozn.: pytrends je neoficiálna knižnica, Google občas rate-limituje (429).
Skript medzi requestmi spí, prípadne stačí ho pustiť znova o pár minút.
"""

import json
import sys
import time
from datetime import date
from pathlib import Path

try:
    from pytrends.request import TrendReq
except ImportError:
    print("Chýba knižnica pytrends. Spusti:\n  pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

# ---- konfigurácia ----
# Každá položka = (display label, search query).
# Display label sa ukáže v slide; query je čo posielame do Google Trends.
#
# POZOR: SK trh je malý — niektoré úzke queries (napr. "krém na opaľovanie")
# nemajú dosť search volume na to, aby Trends vrátil dáta. Používame
# širšie/populárnejšie termy. Ak chceš iné, daj sem termy, ktoré reálne
# vidíš v Google Trends s nenulovým grafom.
KEYWORDS = [
    ("Opaľovací krém",        "opaľovací krém"),
    ("SPF",                   "SPF"),
    ("Balea (dm brand)",      "Balea"),
    ("After-sun",             "after sun"),
    ("Repelent",              "repelent"),
    ("Kufor / cestovné",      "kufor"),
]

# Pre referenčné porovnanie použijeme posledný uzavretý rok (aby všetky mesiace mali dáta).
YEAR = date.today().year - 1
SUMMER_RANGE = f"{YEAR}-06-01 {YEAR}-08-31"
BASELINE_RANGE = f"{YEAR}-01-01 {YEAR}-01-31"

GEO = "SK"
SLEEP_BETWEEN_REQUESTS = 5.0  # sekundy — Google trends rate-limituje (skús zvýšiť ak 429)
SORT_DESCENDING = True        # najväčší nárast hore (lepší vizuál)

DATA_PATH = Path(__file__).parent / "data.json"


def fetch_average_interest(pytrends: TrendReq, keyword: str, timeframe: str) -> float:
    """Priemerný Google Trends index (0–100) pre keyword v danom časovom okne."""
    try:
        pytrends.build_payload([keyword], timeframe=timeframe, geo=GEO)
        df = pytrends.interest_over_time()
        if df is None or df.empty:
            return 0.0
        col = df[keyword]
        if "isPartial" in df.columns:
            col = col[~df["isPartial"]]
        return float(col.mean()) if len(col) else 0.0
    except Exception as e:
        print(f"  ⚠ Trends fetch zlyhal pre '{keyword}' / {timeframe}: {e}", file=sys.stderr)
        return 0.0


def percent_change(summer: float, baseline: float) -> int:
    # Žiadne dáta v oboch oknách — nemá zmysel počítať.
    if summer <= 0 and baseline <= 0:
        return 0
    # Letné okno má dáta, baseline nie → growth z prakticky nuly. Použijeme
    # floor 1.0 pre stabilný výpočet; cap na +999 % aby čísla nelietali.
    if baseline <= 0:
        return min(999, int(round(summer / 1.0 * 100)))
    # Štandardný výpočet (môže byť aj záporný — pokles).
    return int(round((summer - baseline) / baseline * 100))


def main() -> int:
    print(f"Sťahujem Google Trends SK pre {len(KEYWORDS)} kľúčových slov…")
    print(f"  Letné okno:    {SUMMER_RANGE}")
    print(f"  Baseline:      {BASELINE_RANGE}")
    print(f"  Geo:           {GEO}")
    print()

    pytrends = TrendReq(hl="sk-SK", tz=120)

    results = []
    for label, query in KEYWORDS:
        print(f"  → {label}  (query: '{query}')")
        summer_avg = fetch_average_interest(pytrends, query, SUMMER_RANGE)
        time.sleep(SLEEP_BETWEEN_REQUESTS)
        baseline_avg = fetch_average_interest(pytrends, query, BASELINE_RANGE)
        time.sleep(SLEEP_BETWEEN_REQUESTS)
        change = percent_change(summer_avg, baseline_avg)
        print(f"    leto={summer_avg:.1f}  január={baseline_avg:.1f}  zmena={'+' if change >= 0 else ''}{change} %")
        results.append({"label": label, "change": change})

    # Sanity check — potrebujeme aspoň 2 keywords s pozitívnym nárastom, inak
    # je dáta-set prakticky prázdny.
    positive = sum(1 for r in results if r["change"] > 0)
    if positive < 2:
        print(f"\n✗ Iba {positive}/{len(results)} keywords má pozitívny letný nárast.", file=sys.stderr)
        print("  Pravdepodobne 429 / nízky SK search volume. Skús o ~15 min alebo uprav KEYWORDS.", file=sys.stderr)
        print("  data.json som nezmenil.", file=sys.stderr)
        return 1
    # Odfiltrujeme tie, čo nemajú pozitívny letný signál — slide ukazuje "nárast vs. január".
    # Pre negatívne výsledky (kufor v zime > leto) by sme potrebovali iný vizuál.
    results = [r for r in results if r["change"] > 0]

    if SORT_DESCENDING:
        results.sort(key=lambda x: -x["change"])

    existing = {}
    if DATA_PATH.exists():
        try:
            existing = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass

    new_data = {
        "lastUpdated": date.today().isoformat(),
        "source": f"Google Trends SK · {YEAR} (jún–august vs. január) · auto-update",
        "trends": results,
        "openTimes": existing.get("openTimes", [
            {"slot": "utorok 9–11 h", "percent": 28},
            {"slot": "streda 10–12 h", "percent": 23},
            {"slot": "nedeľa 19–21 h", "percent": 18},
        ]),
    }

    DATA_PATH.write_text(
        json.dumps(new_data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"\n✓ Zapísané: {DATA_PATH}")
    print(f"  {len(results)} trend bodov · lastUpdated = {new_data['lastUpdated']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
