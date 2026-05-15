#!/usr/bin/env python3
"""
update_data.py — generuje data.json z reálnych Google Trends SK dát.

Metodológia (sezónny index):
  Pre každý keyword stiahneme celoročný Trends index (týždenné body)
  a vypočítame, o koľko % je priemer letných týždňov (jún–august)
  nad priemerom celého roka.

  → "summer vs. annual average" — štandardný marketingový sezónny index.

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
# SK trh je malý — niektoré úzke queries nemajú dosť dát. Mixujeme
# DM produktové termy + širšie sezónne lifestyle queries pre vyšší
# hit rate. Skript automaticky odfiltruje tie, čo nemajú signál.
KEYWORDS = [
    # DM / drogéria termy
    ("SPF",                   "SPF"),
    ("Balea (dm brand)",      "Balea"),
    ("Nivea",                 "Nivea"),
    ("Repelent",              "repelent"),
    ("Opaľovací krém",        "opaľovací krém"),
    ("After-sun",             "after sun"),
    # Letné lifestyle / sezónne signály
    ("Plavky",                "plavky"),
    ("Festival",              "festival"),
    ("Kúpalisko",             "kúpalisko"),
    ("Dovolenka",             "dovolenka"),
    ("Chorvátsko",            "Chorvátsko"),
    ("Klimatizácia",          "klimatizácia"),
]

# Referenčný rok — posledný uzavretý rok (všetky mesiace majú dáta).
YEAR = date.today().year - 1

GEO = "SK"
SLEEP_BETWEEN_REQUESTS = 5.0  # sekundy — Google trends rate-limituje
SORT_DESCENDING = True

DATA_PATH = Path(__file__).parent / "data.json"


def fetch_year_series(pytrends: TrendReq, keyword: str, year: int):
    """Stiahne celoročnú Trends timeseries pre keyword v SK. None ak prázdne."""
    timeframe = f"{year}-01-01 {year}-12-31"
    try:
        pytrends.build_payload([keyword], timeframe=timeframe, geo=GEO)
        df = pytrends.interest_over_time()
        if df is None or df.empty:
            return None
        # filtruj nedokončené týždne na konci
        if "isPartial" in df.columns:
            df = df[~df["isPartial"]]
        return df[keyword]
    except Exception as e:
        print(f"  ⚠ Trends fetch zlyhal pre '{keyword}': {e}", file=sys.stderr)
        return None


def fetch_related_top(pytrends: TrendReq, keyword: str, top_n: int = 5):
    """Top related queries pre posledný build_payload. Best-effort — ak zlyhá, vráti []."""
    try:
        rq = pytrends.related_queries()
        top = rq.get(keyword, {}).get("top") if rq else None
        if top is None or top.empty:
            return []
        out = []
        for _, row in top.head(top_n).iterrows():
            out.append({"q": str(row["query"]), "v": int(row["value"])})
        return out
    except Exception as e:
        print(f"    ⚠ Related queries fail pre '{keyword}': {e}", file=sys.stderr)
        return []


def seasonal_lift_percent(series) -> tuple:
    """Vráti (summer_avg, year_avg, lift_percent).
    lift_percent = o koľko % je leto (jún–aug) nad celoročným priemerom.
    """
    if series is None or len(series) == 0:
        return (0.0, 0.0, 0)
    year_avg = float(series.mean())
    summer_mask = (series.index.month >= 6) & (series.index.month <= 8)
    summer_series = series[summer_mask]
    if len(summer_series) == 0:
        return (0.0, year_avg, 0)
    summer_avg = float(summer_series.mean())
    if year_avg <= 0:
        # Celoročný priemer je 0 — nemôžeme normalizovať
        return (summer_avg, year_avg, 0)
    lift = int(round((summer_avg - year_avg) / year_avg * 100))
    return (summer_avg, year_avg, lift)


def main() -> int:
    print(f"Sťahujem Google Trends SK · sezónny index pre {len(KEYWORDS)} kľúčových slov…")
    print(f"  Rok:           {YEAR}")
    print(f"  Geo:           {GEO}")
    print(f"  Metodológia:   priemer letných týždňov (jún–aug) vs. celoročný priemer")
    print()

    pytrends = TrendReq(hl="sk-SK", tz=120)

    results = []
    for label, query in KEYWORDS:
        print(f"  → {label}  (query: '{query}')")
        series = fetch_year_series(pytrends, query, YEAR)
        # related queries — best-effort hneď po build_payload pre ten istý keyword
        related = fetch_related_top(pytrends, query, top_n=5) if series is not None else []
        time.sleep(SLEEP_BETWEEN_REQUESTS)
        summer_avg, year_avg, lift = seasonal_lift_percent(series)
        sign = "+" if lift >= 0 else ""
        rel_count = len(related)
        print(f"    leto={summer_avg:.1f}  rok={year_avg:.1f}  index={sign}{lift} %  · {rel_count} related")
        entry = {"label": label, "change": lift}
        if series is not None:
            # Týždenné hodnoty pre sparkline (zaokrúhlené, aby JSON nebol obrovský)
            entry["weekly"] = [round(float(v), 1) for v in series.values]
        if related:
            entry["related"] = related
        results.append(entry)

    # Sanity check — potrebujeme aspoň 2 keywords s pozitívnym sezónnym indexom.
    positive = sum(1 for r in results if r["change"] > 0)
    if positive < 2:
        print(f"\n✗ Iba {positive}/{len(results)} keywords má pozitívny sezónny index.", file=sys.stderr)
        print("  Pravdepodobne 429 / nízky SK search volume. Skús o ~15 min alebo uprav KEYWORDS.", file=sys.stderr)
        print("  data.json som nezmenil.", file=sys.stderr)
        return 1

    # Slide ukazuje "leto vs ročný priemer" — necháme len pozitívne.
    results = [r for r in results if r["change"] > 0]

    if SORT_DESCENDING:
        results.sort(key=lambda x: -x["change"])

    # Agregácia top related queries naprieč všetkými keywords — top 10 podľa súčtu hodnôt.
    agg = {}
    for r in results:
        for rel in r.get("related", []):
            agg[rel["q"]] = agg.get(rel["q"], 0) + rel["v"]
    top_related = [{"q": q, "v": v} for q, v in sorted(agg.items(), key=lambda x: -x[1])[:10]]

    existing = {}
    if DATA_PATH.exists():
        try:
            existing = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass

    new_data = {
        "lastUpdated": date.today().isoformat(),
        "source": f"Google Trends SK · {YEAR} (leto vs. ročný priemer) · auto-update",
        "trends": results,
        "topRelated": top_related,
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
