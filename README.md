# Leto s dm — Letná e-mailová kampaň 2026

Kompletný koncept letnej e-mailovej kampane pre dm drogerie markt — od obchodného
zadania cez automatizačnú architektúru až po funkčný HTML newsletter. Portfóliová
práca z oblasti e-mail marketingu a kampaňovej stratégie.

**Autor:** Samuel Zenko · Máj 2026

---

## Čo je v tomto repozitári

| Súbor | Čo to je |
|---|---|
| `prezentacia.html` | Interaktívna 20-slidová prezentácia celej stratégie. Otvor v prehliadači, listuj šípkami ← → alebo bočnými bodkami. |
| `newsletter.html` | Reálny, e-mailovo bezpečný HTML newsletter „Leto s dm" — table layout, inline štýly, responzívny. Pripravený na nasadenie cez ESP. |
| `dm-logo.png` | Logo dm. |
| `img-nl0…nl5-*.png` | Šesť hotových vizuálov newsletterov — jeden na každý diel série. |
| `img-festival/beauty/rodina/priatelia-*.png` | Segmentové a atmosférické fotky použité v prezentácii. |
| `README.md` | Tento dokument — sprievodná štúdia stratégie. |

---

## Sprievodná štúdia

### 1. Východisko a ciele

Leto je pre drogériu najsilnejší príbeh roka. Mení sa nákupné správanie, pribúdajú
sezónne potreby (opaľovacia kozmetika, after-sun, cestovné balenia) a zákazník je
otvorený inšpirácii. E-mail je kanál, ktorý ho dokáže prevedieť celým letom — nie
jedným výkrikom, ale ako sprievodca.

**Ciele kampane:**
- **+18 %** medziročný obrat letných kategórií z e-mailu
- **+25 %** nárast zapojených odberateľov vo Svete výhod dm
- **35 %+** priemerný open rate naprieč sériou
- **< 0,3 %** miera odhlásení — relevancia pred frekvenciou

Tieto čísla sú zároveň východiskom aj záverom — kampaň sa nimi začína (zadanie)
a končí (meranie). Kruh sa uzatvára.

### 2. Veľká myšlienka

> **„Leto má 92 dní. dm je pri každom z nich."**

Kampaň nie je séria zliav — je to **sprievodca letom**. Každý newsletter je jedna
kapitola: príprava, festivaly, dovolenka, mesto, doznievanie. Zákazník neotvára
reklamu, otvára ďalšiu časť svojho leta. A dm je tá samozrejmá vec, ktorá tam celý
čas je.

Tri princípy, ktoré z toho vychádzajú:
- **Sprievodca, nie predajca** — najprv reálna letná situácia, potom produkt.
- **Kapitoly na seba nadväzujú** — každý e-mail teasuje ďalší, vzniká očakávanie.
- **Jedna niť cez celé leto** — vernostná „Letná cesta výhod" drží sériu pokope.

### 3. Cieľové skupiny — päť letných persón

Jeden master e-mail, viacero segmentových verzií. Hero vizuál, hlavný produkt a CTA
sa menia podľa persóny — štruktúra a brand ostávajú rovnaké.

| Persóna | Kto to je | Čo rieši |
|---|---|---|
| **Festivalová Ema** (18–26) | Žije Instagramom | Trblietky, výrazný makeup, suchý šampón, mini balenia |
| **Rodina na dovolenke** (30–45) | Rodičia s deťmi | Detské SPF, lekárnička, dmBio snacky na cesty |
| **Beauty nadšenkyňa** (25–40) | Hľadá kvalitu | alverde, after-sun rituály, ochrana vlasov a pleti |
| **Mestský typ** (25–50) | Ostal v meste | Osvieženie, hydratácia, pikniky, „leto na balkóne" |
| **Zberateľ výhod** (naprieč vekom) | Srdce Sveta výhod dm | Body, personalizované zľavy |

Persóny nie sú portréty do šuflíka — sú to priamo vetvy automatizačného systému
a verzie hero bloku.

### 4. Logika celku — jeden lievik cez celé leto

Šesť newsletterov nie je šesť kampaní. Je to **jeden lievik** — seriál, kde každý
diel posúva zákazníka ďalej a stojí na predošlom:

```
Spoznaj → Aktivuj → Profiluj → Naplň košík → Udrž → Ostaň
 NL 0      NL 1      NL 2        NL 3          NL 4    NL 5
```

**Dátový kolobeh** je jadro celej logiky:
- **1. polovica leta ZBIERA** — NL 0 a kvíz v NL 2 vyťahujú, čo zákazníka zaujíma
  a aký je letný typ.
- **2. polovica leta VYUŽÍVA** — NL 3, 4 a 5 tieto dáta používajú na
  personalizovanú ponuku, ktorá konvertuje.

Preto je kampaň v auguste múdrejšia ako v máji. To je rozdiel medzi „6 emailov"
a „kampaňou".

Kampaň beží v troch vrstvách naraz:
1. **Kalendárová** — 6 newsletterov, raz za ~2–3 týždne.
2. **Vernostná** — Letná cesta výhod beží na pozadí celý čas.
3. **Reakčná** — automatizácie reagujú na správanie, nie na kalendár.

### 5. Newsletteringový systém — automatizačná architektúra

Lievik nie je ručná práca — beží na automatizácii. Princíp: *správna správa,
správnemu človeku, v správny čas.*

```
Nový odberateľ → Vitaj v dm → Segmentácia záujmov
                                      │
        ┌──────────┬──────────┬───────┴────┬─────────────┐
     Festival    Rodina     Beauty    Mesto+Vernosť   Neaktívni
        │          │          │            │              │
   Festival NL  Family NL  Beauty NL   Mestské NL    We miss you!
        │          │          │            │              │
   Interakcia?  Interakcia? Interakcia? Interakcia?     Reakcia?
    ├ áno → pokračuje v sérii                ├ áno → späť do segmentu
    └ nie → re-engagement                    └ nie → Posledná šanca → odstránenie
```

Päť persón = päť reálnych vetiev systému. Naprieč všetkými vetvami bežia vernostné
odmeny a špeciálne kampane (narodeniny, výročie odberu, exkluzívne akcie).

### 6. Kampaňová mapa — šesť kapitol leta

| NL | Názov | Kedy | Úloha | Mechanika |
|---|---|---|---|---|
| **NL 0** | Leto klope na dvere | koniec mája | spoznaj & zbieraj | naladenie, súťaž, zber preferencií |
| **NL 1** | Priprav sa na leto | začiatok júna | aktivuj | opaľováky, segmentový hero |
| **NL 2** | Festivalové leto | koniec júna | profiluj | kvíz „Aký si letný typ" |
| **NL 3** | Dovolenka bez starostí | polovica júla | naplň košík | interaktívny checklist do kufra |
| **NL 4** | Leto v meste | začiatok augusta | udrž | osvieženie, pre tých čo ostali doma |
| **NL 5** | Doznievanie leta | koniec augusta | ostaň | after-sun, bodová odmena, spätná väzba |

**Spojovacia niť — Letná cesta výhod:** každý newsletter odomyká pečiatku v rámci
Sveta výhod dm. Kto „prejde leto" s dm, v NL 5 si vyberá finálnu odmenu — dôvod
otvárať každý jeden e-mail.

Popri hlavnej osi bežia automatizované toky: uvítací rad, opustené prezeranie,
bodový míľnik, narodeniny v lete.

### 7. Automatizácia podľa fáz

Každý newsletter nie je len odoslaný — má naprogramované, čo sa stane, keď zákazník
zareaguje a keď nie. Schéma každej fázy: **Spúšťač → E-mail → Podmienka → vetva
áno / nie.**

Kľúčový moment je NL 2: vetva „Áno" (dokončený kvíz) vytvára profilový tag, ktorý
priamo riadi personalizáciu NL 3, 4 a 5. Tu sa rozhoduje, ako múdra bude druhá
polovica kampane.

### 8. Mechaniky a personalizácia

Štyri vrstvy, ktoré zo statického newslettera robia interaktívny, merateľný
a osobný zážitok:
- **Gamifikácia** — kvíz „Aký je tvoj letný typ", letné BINGO / stieracia karta,
  odklikávací checklist do kufra.
- **Personalizácia** — segmentový hero blok, oslovenie menom, zostatok bodov,
  geo/počasie blok („u vás bude 31 °C — nezabudni na SPF").
- **A/B testovanie** — predmet e-mailu, farba a text CTA, poradie blokov.
- **Časovanie a triggery** — countdown na promo, automatizované toky,
  send-time optimalizácia.

### 9. Varianty newsletterov — tri formáty

Spoločná kostra, iná náplň a mechanika — efektívna výroba, pestrý zážitok.
- **Formát A · Produktový** — sezónny sprievodca (NL 1, NL 4).
- **Formát B · Interaktívny** — hravý newsletter s kvízom/checklistom (NL 2, NL 3).
- **Formát C · Vzťahový** — komunita a vernosť (NL 0, NL 5).

Spoločná kostra každého e-mailu: preheader → logo dm + vlnka → hero (segmentový)
→ hlavný blok / mechanika → produktové karty → vernostný pruh → teaser ďalšieho NL
→ pätička.

### 10. Vizuálna identita

Vychádza z reálnej identity dm: modrá ako základ, žlto-červená vlnka ako podpis,
vzdušné svetlé pozadia, biele zaoblené karty a priateľský tón.

- **Paleta:** dm modrá `#003A78`, svetlá modrá `#0A6FC2`, žltá vlnka `#FFCC00`,
  červená vlnka `#E2001A`, beauty pink `#E6007E`, bio zelená `#1FAA6F`.
- **Tón:** priateľský, ľudský — „tu som človekom, tu nakupujem". Tykanie, krátke
  vety, sprievodca nie predajca.

### 11. Harmonogram

| Mesiac | Obsah |
|---|---|
| **Máj** | NL 0 + štart uvítacieho radu |
| **Jún** | NL 1, NL 2, A/B test predmetov |
| **Júl** | NL 3, trigger opustené prezeranie, countdown promo −20 % |
| **August** | NL 4, NL 5, výber bodovej odmeny + prieskum |

Frekvencia: max. 2 newslettery mesačne na segment — relevancia pred objemom.
Automatizované toky bežia nezávisle a nepočítajú sa do tohto stropu.

### 12. Meranie a KPI

| Metrika | Cieľ |
|---|---|
| Open rate (priemer série) | 35 %+ |
| Click-through rate | 7 %+ (interaktívne NL až 9 %) |
| Obrat letných kategórií | +18 % medziročne |
| Zapojenie vo Svete výhod | +25 % |
| Dokončenie kvízu (NL 2) | 22 % |
| Priemerná hodnota košíka (NL 3) | +15 % |
| Miera odhlásení | < 0,3 % |
| Podiel NL s A/B testom | 100 % |

---

## Ako si to pozrieť

1. **Prezentácia** — otvor `prezentacia.html` v prehliadači. Listuj šípkami
   ← → / ↑ ↓, bočnými bodkami alebo veľkými navigačnými tlačidlami. Obsah na
   2. slide je klikateľný.
2. **Newsletter** — otvor `newsletter.html` v prehliadači. Je to živý, klikateľný
   HTML výstup, nie obrázok.

## Poznámky k produkčnému nasadeniu

- V deku aj v ukážke je použité reálne logo dm; v produkcii sa berie oficiálny
  súbor z brand manuálu.
- Placeholder odkazy (`#`) v newsletteri treba nahradiť reálnymi URL.
- Newsletter je pripravený na napojenie na ESP — merge tagy a segmenty.

---

*Portfóliová práca — e-mail marketing & kampaňová stratégia. Samuel Zenko, 2026.*
