# Pinterest Trends API — setup pre projekt Leto s dm

Tento návod ťa prevedie získaním Pinterest access tokenu, ktorý GitHub Action
použije na týždenné sťahovanie trending keywords pre **AT** (Rakúsko) ako
najbližšieho proxy pre slovenský trh.

> **Realistický odhad času:** prvé 3 kroky 10 minút, schvaľovanie môže
> trvať **niekoľko dní až 2 týždne** (Pinterest review).

---

## Čo Pinterest API ponúka pre nás

Endpoint:
```
GET /v5/trends/keywords/{region}/top/{trend_type}
```

- `region` = `AT` (Pinterest poskytuje národné dáta — SK samostatne nemá)
- `trend_type` = `growing` (rastúce queries) alebo `monthly` (top za posledný mesiac)
- Vracia top trending search queries s percentom rastu

**Prečo AT a nie SK?**
Pinterest Trends API neposkytuje samostatné dáta pre SK trh. AT je geograficky
aj kultúrne najbližší podporovaný región (DACH zóna, podobné letné produkty,
prekrývajúce sa kampane s nemecky hovoriacim trhom). DM samotná operuje
v AT ako materský trh, takže preferencie sú reálne relevantné.

---

## Krok 1 — Vytvor Pinterest Business účet

1. Choď na **https://business.pinterest.com/**
2. *Sign up free* → vyplň základné údaje
3. Ako *business type* daj **Brand** alebo **Agency**
4. Potvrď email

> Existujúci osobný Pinterest účet vieš previesť na business cez Settings →
> Account management → Convert to business account.

## Krok 2 — Vytvor developer app

1. Choď na **https://developers.pinterest.com/apps/**
2. Klikni **Connect app**
3. Vyplň:
   - **App name:** `Leto s dm — Trends fetcher`
   - **App description:** `Pulls weekly Pinterest Trends data for marketing campaign visualization. Read-only, server-to-server.`
   - **Website URL:** odkaz na tvoju GitHub Pages stránku (napr. `https://samuelzenko.github.io/leto-s-dm/`)
   - **Redirect URIs:** `https://samuelzenko.github.io/leto-s-dm/` (pre OAuth callback — aj keď ho nebudeš živo používať, musí byť vyplnené)

4. Pri **App permissions / scopes** zaškrtni:
   - ✅ `trends:read` (kritické — bez toho Trends API nepôjde)
   - ✅ `boards:read` (užitočné na neskôr)
   - ✅ `pins:read`

5. Odošli na review.

> **Pozor:** Pinterest schvaľuje Trends scope manuálne. Schválenie môže trvať
> **3–14 dní**. Príde email. Pokiaľ ešte nemáš schválené, dostaneš pri prvom
> volaní `403 Forbidden`.

## Krok 3 — Vygeneruj access token (raz)

Po schválení appu:

1. V developer portáli klikni na svoj app → **Generate access token**
2. Vyber scopes (`trends:read` minimum)
3. Stiahne ti token typu `pina_…` — **toto je tvoj access token**
4. **Skopíruj ho hneď** — Pinterest ho zobrazí len raz

> Token má cca **30-dňovú expiráciu**. Refresh token Pinterest nemá v jednoduchom
> flow — keď expiruje, vygeneruješ nový a aktualizuješ GitHub secret. Pre
> portfolio projekt OK; pre produkciu by sa to dalo automatizovať cez OAuth refresh.

## Krok 4 — Pridaj token ako GitHub Secret

1. V repo na GitHube → **Settings** → **Secrets and variables** → **Actions**
2. **New repository secret**
3. **Name:** `PINTEREST_ACCESS_TOKEN`
4. **Value:** vlož `pina_…` token zo Step 3
5. **Add secret**

## Krok 5 — Otestuj workflow

1. **Actions** tab → **Update data.json from Google Trends**
2. **Run workflow** → vyber `master` branch → **Run workflow**
3. Sleduj log — krok *Fetch Pinterest Trends (AT proxy)* by mal:
   - **Pri správnom tokene:** vypísať `✓ N keywords` pre `growing` a `monthly`
   - **Bez tokenu:** vypísať `ℹ PINTEREST_ACCESS_TOKEN nie je nastavený — preskakujem` a tichý exit 0

Po push commitu `chore(data): auto-update Google Trends SK` sa `data.json`
prebije a tvoja stránka pri ďalšom načítaní zobrazí v Pinterest panely
**reálne queries z AT regiónu** namiesto fallback chips.

---

## Lokálne testovanie (voliteľné)

```powershell
$env:PINTEREST_ACCESS_TOKEN = "pina_…"
python update_pinterest.py
```

Skript vypíše do `data.json` nový kľúč `pinterest`:
```json
"pinterest": {
  "region": "AT",
  "lastUpdated": "2026-05-15",
  "growing": [{"q": "festival outfit", "growth": 240}, ...],
  "monthly": [{"q": "sommer make-up", "growth": null}, ...]
}
```

---

## Čo robiť ak Pinterest review zamietne `trends:read`

Pinterest schvaľuje Trends scope hlavne väčším brandom. Pre osobný portfolio
projekt sa stáva, že to zamietnu. Fallback stratégie:

1. **Použiť dáta zo screenshotov Pinterest Trends webu** ([trends.pinterest.com](https://trends.pinterest.com))
   — manuálne každý mesiac, ale autentické.
2. **Zostať len pri Google Trends** (Phase 1–5 už funguje) a Pinterest reprezentovať
   curated boardami (čo prezentácia už má).
3. **Skúsiť `pins:read` namiesto `trends:read`** — vieš z public profilov dm
   na Pinterest analyzovať, ktoré piny majú najviac saves.

Voľba č. 2 je legitímna — recruiter ocení Google Trends pipeline rovnako
ako Pinterest, a transparentne pomenovaný proces "Pinterest Trends prístup
v review" demonštruje, že vieš pracovať s reálnymi API constraintmi.
