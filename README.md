# Leto s dm — Letná e-mailová kampaň 2026

Komplexný návrh letnej e-mailovej kampane pre dm drogerie markt — od strategického zadania a návrhu automatizácií až po finálny HTML newsletter. Ide o portfóliový projekt zameraný na e-mail marketing, CRM komunikáciu a kampaňovú stratégiu. 

**Autor:** Samuel Zenko · Máj 2026

---

# Čo projekt obsahuje

| Súbor                                        | Popis                                                                                                |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `prezentacia.html`                           | Interaktívna prezentácia celej kampane. Funguje priamo v prehliadači a obsahuje približne 20 slidov. |
| `newsletter.html`                            | Responzívny HTML newsletter „Leto s dm“, pripravený na nasadenie cez e-mailingový systém.            |
| `dm-logo.png`                                | Logo značky dm.                                                                                      |
| `img-nl0…nl5-*.png`                          | Vizuály jednotlivých newsletterov v sérii.                                                           |
| `img-festival/beauty/rodina/priatelia-*.png` | Atmosférické a segmentové vizuály použité v prezentácii.                                             |
| `README.md`                                  | Sprievodná dokumentácia a opis stratégie kampane.                                                    |

---

# Sprievodná štúdia

## 1. Východisko a ciele kampane

Leto patrí v drogérii medzi najsilnejšie sezónne obdobia. Zákazníci počas neho viac riešia dovolenky, festivaly, ochranu pred slnkom či cestovné balenia produktov. Zároveň sú otvorenejší novým produktom aj inšpirácii.

Cieľom kampane preto nie je len posielať predajné newslettery, ale vytvoriť sériu e-mailov, ktoré budú zákazníka sprevádzať počas celého leta.

### Hlavné ciele kampane

* zvýšiť medziročný obrat letných kategórií z e-mailového kanála o **18 %**
* zvýšiť aktivitu používateľov vo vernostnom programe **Svet výhod dm** o **25 %**
* dosiahnuť priemerný open rate minimálne **35 %**
* udržať mieru odhlásení pod **0,3 %**

Tieto KPI zároveň určujú smer celej kampane — od prvotného návrhu až po vyhodnotenie výsledkov. 

---

## 2. Hlavná idea kampane

> „Leto má 92 dní. dm je pri každom z nich.“

Kampaň nestojí iba na produktoch a zľavách. Je postavená na letných situáciách a momentoch, v ktorých sa zákazník prirodzene nájde. Každý newsletter predstavuje jednu časť leta — od príprav na dovolenku cez festivaly až po záver prázdnin.

Používateľ tak neotvára ďalší reklamný e-mail, ale pokračovanie príbehu, ktorý ho sprevádza počas celého leta.

### Základné princípy kampane

* **Sprievodca namiesto predajcu** — najskôr situácia alebo potreba, až potom produkt.
* **Newslettery na seba nadväzujú** — každý diel prirodzene pokračuje v predchádzajúcom.
* **Jedna spoločná línia** — celú sériu prepája koncept „Letnej cesty výhod“. 

---

## 3. Cieľové skupiny a segmentácia

Kampaň pracuje s jedným hlavným newsletterom, ktorý sa následne personalizuje podľa typu zákazníka. Mení sa hero vizuál, CTA aj odporúčané produkty, no celková štruktúra a branding ostávajú jednotné.

| Persóna                 | Charakteristika                    | Čo rieši                               |
| ----------------------- | ---------------------------------- | -------------------------------------- |
| **Festivalová Ema**     | mladší lifestyle segment           | makeup, mini balenia, suché šampóny    |
| **Rodina na dovolenke** | rodičia s deťmi                    | SPF produkty, snacky, cestovná výbava  |
| **Beauty nadšenkyňa**   | zákazníčka orientovaná na skincare | after-sun, ochrana vlasov a pleti      |
| **Mestský typ**         | trávi leto doma alebo v meste      | hydratácia, osvieženie, letné aktivity |
| **Zberateľ výhod**      | aktívny člen vernostného programu  | body, odmeny, personalizované zľavy    |

Tieto persóny neslúžia len ako marketingové archetypy. Priamo ovplyvňujú segmentáciu databázy, obsah jednotlivých e-mailov aj automatizačné vetvy kampane. 

---

## 4. Celková logika kampane

Šesť newsletterov nefunguje ako šesť samostatných kampaní. Celá séria tvorí jeden prepojený funnel, v ktorom každý newsletter posúva používateľa ďalej.

```text
Spoznaj → Aktivuj → Profiluj → Naplň košík → Udrž → Ostaň
 NL 0      NL 1      NL 2        NL 3          NL 4    NL 5
```

Prvá polovica kampane je zameraná hlavne na zber dát a zisťovanie preferencií zákazníkov. Druhá polovica tieto dáta využíva na presnejšiu personalizáciu a relevantnejšie ponuky.

Vďaka tomu sú augustové newslettery výrazne presnejšie a efektívnejšie než tie na začiatku leta.

### Kampaň funguje v troch vrstvách

1. **Kalendárová vrstva** — hlavná séria newsletterov.
2. **Vernostná vrstva** — Letná cesta výhod a zbieranie odmien.
3. **Reakčná vrstva** — automatizácie reagujúce na správanie používateľov. 

---

## 5. Automatizačný systém kampane

Celá kampaň je postavená na automatizovaných scenároch. Základná myšlienka je doručiť správny obsah správnemu človeku v správny čas.

Po prihlásení do databázy používateľ prechádza segmentáciou podľa záujmov a následne vstupuje do konkrétnej vetvy komunikácie. Ak reaguje a interaguje, pokračuje ďalej v sérii. Ak nie, systém spustí re-engagement alebo posledný pokus o aktiváciu.

Naprieč všetkými vetvami zároveň fungujú:

* vernostné mechaniky,
* narodeninové kampane,
* trigger-based automatizácie,
* špeciálne akcie a odmeny. 

---

## 6. Kampaňová mapa

| Newsletter                        | Timing           | Hlavný cieľ                  |
| --------------------------------- | ---------------- | ---------------------------- |
| **NL 0 – Leto klope na dvere**    | koniec mája      | naladenie a zber preferencií |
| **NL 1 – Priprav sa na leto**     | začiatok júna    | aktivácia používateľa        |
| **NL 2 – Festivalové leto**       | koniec júna      | profilovanie používateľov    |
| **NL 3 – Dovolenka bez starostí** | polovica júla    | zvýšenie hodnoty košíka      |
| **NL 4 – Leto v meste**           | začiatok augusta | udržanie engagementu         |
| **NL 5 – Doznievanie leta**       | koniec augusta   | retencia a spätná väzba      |

Celú sériu prepája mechanika „Letnej cesty výhod“, v rámci ktorej používateľ postupne zbiera body a odomyka odmeny. 

---

## 7. Automatizácia podľa fáz

Každý newsletter má vlastnú automatizačnú logiku. Nejde teda len o jednorazové odoslanie e-mailu, ale o systém, ktorý ďalej pracuje s reakciou používateľa.

Základná schéma každej fázy vyzerá nasledovne:

**Spúšťač → E-mail → Podmienka → vetva áno / nie**

Ak používateľ na newsletter zareaguje, pokračuje ďalej v hlavnej sérii alebo sa presunie do presnejšieho segmentu. Ak nereaguje, systém môže spustiť re-engagement komunikáciu alebo upravený obsah.

Najdôležitejším bodom celej série je newsletter **NL 2 – Festivalové leto**, v ktorom používateľ vyplní kvíz „Aký si letný typ“. Na základe odpovedí získa profilový tag, ktorý následne ovplyvní obsah newsletterov NL 3, NL 4 a NL 5.

Druhá polovica kampane tak nefunguje univerzálne pre všetkých, ale pracuje s dátami získanými priamo z interakcie používateľa. 

---

## 8. Personalizácia a interaktivita

Kampaň využíva viacero interaktívnych a personalizačných prvkov, aby newslettery nepôsobili staticky a genericky.

### Použité mechaniky

* kvíz „Aký si letný typ“
* interaktívny checklist do kufra
* gamifikácia (BINGO, stieracie karty)
* dynamické hero bloky podľa segmentu
* personalizované oslovenia a odmeny
* A/B testovanie predmetov a CTA
* optimalizované načasovanie odosielania. 

---

## 9. Formáty newsletterov

Kampaň využíva tri základné typy newsletterov:

### Formát A — Produktový

Newsletter zameraný na sezónne produkty a odporúčania.

### Formát B — Interaktívny

Obsahuje kvízy, checklisty alebo gamifikované prvky.

### Formát C — Vzťahový

Buduje komunitu, lojalitu a pracuje s vernostnými benefitmi.

Každý newsletter zároveň používa rovnakú základnú štruktúru:
preheader → logo → hero sekcia → hlavný obsah → produktové karty → vernostný blok → teaser ďalšieho newslettera → footer. 

---

## 10. Vizuálna identita

Vizualita kampane vychádza z existujúceho brandingu dm:

* dominantná modrá,
* typická žlto-červená vlnka,
* svetlé vzdušné pozadia,
* zaoblené karty,
* jednoduchý a priateľský tone of voice.

Komunikácia používa kratšie a prirodzenejšie formulácie, aby značka pôsobila menej korporátne a viac ľudsky. 

---

## 11. Harmonogram kampane

| Obdobie | Aktivita                                       |
| ------- | ---------------------------------------------- |
| Máj     | štart kampane + uvítací flow                   |
| Jún     | hlavná aktivácia + A/B testovanie              |
| Júl     | interaktívne newslettery + promo automatizácie |
| August  | retencia, odmeny a feedback                    |

Frekvencia je nastavená na maximálne dva newslettery mesačne pre jeden segment, aby komunikácia nepôsobila agresívne alebo spamovo. 

---

## 12. Vyhodnocovanie a KPI

Kampaň pracuje s kombináciou engagement metrík, obchodných výsledkov aj CRM dát.

### Hlavné sledované metriky

* open rate,
* click-through rate,
* obrat letných kategórií,
* aktivita vo vernostnom programe,
* completion rate kvízu,
* priemerná hodnota košíka,
* unsubscribe rate,
* úspešnosť A/B testov. 

---

## Ako si projekt pozrieť

Prezentácia kampane sa otvára cez súbor `prezentacia.html` priamo v prehliadači. Navigácia funguje pomocou šípok, bočných bodiek alebo navigačných tlačidiel.

Newsletter sa nachádza v súbore `newsletter.html`. Ide o funkčný HTML výstup pripravený na ďalšie úpravy alebo nasadenie cez e-mailingový nástroj.

### Poznámky k produkčnému nasadeniu

V ukážkach je použité logo dm, pričom pri reálnom nasadení by bolo potrebné pracovať s oficiálnymi brand podkladmi.

Placeholder odkazy označené ako `#` je potrebné nahradiť reálnymi URL adresami.

Newsletter je pripravený na napojenie na ESP systém, merge tagy a segmentáciu podľa používateľských dát.
