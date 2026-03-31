---
name: biznisoft-db-analyst-v1
description: >-
  Autonomna analiza BizniSoft ERP MySQL/MariaDB baza podataka — import dump-ova,
  razumevanje multi-tenant arhitekture (opp + oppXXXYYYY), analiza integriteta,
  poslovne logike, storno obrazaca i dokumentovanje nalaza. Aktivira se kada
  korisnik traži analizu BizniSoft baze, import SQL dump-a, proveru integriteta
  podataka, pregled finansijskih knjiženja, robno-materijalnog poslovanja ili
  bilo koju operaciju nad BizniSoft ERP bazom.
allowed-tools:
  - FileRead
  - FileWrite
  - Bash
  - CodeExecution
  - WebSearch
---

## Jezik komunikacije
- Sva komunikacija sa korisnikom: **srpski jezik, latinica, ekavski dijalekt**
- Isporuka svih rezultata i izveštaja: srpski jezik
- Bez reči bosanskog/hrvatskog porekla
- Interna dokumentacija i reference ostaju na engleskom gde je potrebno

---

## Svrha skill-a

Ovaj skill omogućava agentu da autonomno radi sa BizniSoft ERP bazama podataka:
- **Postavi MariaDB okruženje** iz nule (instalacija, konfiguracija, import)
- **Razume arhitekturu** BizniSoft sistema bez dodatnih objašnjenja
- **Analizira integritet** podataka prema poznatim pravilima sistema
- **Primenjuje poslovnu logiku** (storniranja, FIFO, PDV, finansijska ravnoteža)
- **Dokumentuje nalaze** strukturirano za dalju upotrebu
- **Uči iterativno** — beleži nova saznanja kroz rad sa konkretnim bazama

---

## Tri baze znanja

### Baza 1: Tehnička dokumentacija baze (`knowledge/`)
**Lokacija:** `knowledge/` folder
**Tip:** Statička referenca — ažurira se ručno ili pri otkrivanju novih struktura
**Kako se koristi:** Ovo je "memorija" agenta o arhitekturi BizniSoft baze — tabele, procedure, trigeri, implicitne relacije, šifarnici i operativne skripte. Agent čita ove fajlove pre svake analize kao tehničku referencu.

**Sadrži:** 14 fajlova sa kompletnom dokumentacijom strukture baze (detalji u sekciji Knowledge fajlovi ispod).

### Baza 2: BizniSoft uputstva sa sajta (`biznisoft_docs/`)
**Lokacija:** `biznisoft_docs/` folder
**Tip:** Automatski ažurirana — poseban agent preuzima sadržaj sa https://www.biznisoft.com/podrska
**Kako se koristi:** Korisnička uputstva proizvođača — kako korisnici koriste sistem i šta pojedine funkcije rade iz korisničke perspektive. Ovaj skill čita ove fajlove kao **read-only referencu**.

**Struktura:**
```
biznisoft_docs/
├── README.md                  ← opis strukture i konvencije
├── tekstualna_uputstva/       ← uputstva sa sajta (MD format)
├── video_uputstva/            ← opisi i linkovi video uputstava
└── verzije_i_novosti/         ← novosti o verzijama BizniSoft-a
```

**Napomena:** Ažurira ga drugi agent (BizniSoft docs scraper). Videti `biznisoft_docs/README.md` za detalje o formatu i konvencijama. Stari fajl `knowledge/biznisoft_dokumentacija.md` je zamenjen ovom strukturom.

### Baza 3: Iterativno učenje kroz rad (`learning/`)
**Lokacija:** `learning/` folder
**Tip:** Dinamička — gradi se automatski kroz rad agenta
**Kako se koristi:** Svaki put kada agent otkrije nešto novo o konkretnoj bazi (neočekivane vrednosti, specifične konfiguracije firme, nestandardni obrasci), beleži to ovde. Pre svake analize, agent čita postojeća saznanja da ne ponavlja iste korake.

**Fajlovi:**
- `learning/session_log.md` — hronološki log svih sesija i ključnih nalaza
- `learning/discovered_patterns.md` — otkriveni obrasci specifični za konkretne baze
- `learning/known_issues.md` — poznati problemi i kako ih rešiti
- `learning/query_cookbook.md` — korisni SQL upiti koji su se pokazali vrednim

**Knowledge fajlovi (14):**

| Fajl | Sadržaj | Kada čitati |
|------|---------|-------------|
| `knowledge/BIZNISOFT_MASTER_REFERENCE.md` | Kompletna arhitektura, šifarnici, 95 tipova dok., procedure, trigeri, relacije, storno logika | **UVEK PRVI** — glavni referentni dokument |
| `biznisoft_docs/` (folder) | Uputstva sa sajta proizvođača (tekstualna, video, verzije) | Kada treba razumeti korisničku perspektivu |
| `knowledge/biznisoft_tables_reference.md` | Struktura 116 ključnih tabela transakcione baze | Kada se analizira struktura tabela |
| `knowledge/biznisoft_opp_tables_reference.md` | Struktura 38 master tabela | Kada se radi sa opp bazom |
| `knowledge/biznisoft_opp_sifarnici.md` | Sadržaj 33 šifarnika | Kada treba validirati šifre |
| `knowledge/biznisoft_stored_procedures.md` | 105 procedura iz transakcione baze | Kada se analizira poslovna logika |
| `knowledge/biznisoft_opp_stored_procedures.md` | 11 procedura iz master baze | Za cross-database operacije |
| `knowledge/biznisoft_functions.md` | 44 funkcije (FIFO, PDV, NBC) | Za kalkulacije i obračune |
| `knowledge/biznisoft_triggers.md` | 265 trigera (operdoc_*, zak_*) | Za razumevanje automatskih akcija |
| `knowledge/biznisoft_dependency_map.md` | Mapa zavisnosti opp ↔ oppXXXYYYY | Za cross-database analizu |
| `knowledge/biznisoft_table_comparison.md` | Poređenje tabela između baza | Za identifikaciju razlika |
| `knowledge/storno_patterns.md` | Logika storniranja (/1, /2 sufiksi) | Za analizu storno parova |
| `knowledge/implicit_relations.md` | Kako se tabele povezuju bez FK | **KLJUČNO** za JOIN-ove |
| `knowledge/dump_parsing_tips.md` | Saveti za parsiranje SQL dump-ova | Pri importu novih baza |

---

## Workflow za analizu baza

### Faza 0: Priprema okruženja
1. Proveri da li MariaDB radi: `bash scripts/check_status.sh`
2. Ako ne radi — pokreni setup: `bash scripts/setup_mariadb.sh`
3. Ako je VM resetovan — brzi restart: `bash scripts/restart_mariadb.sh`
4. Za performance tuning: raspakovati `tools/mariadb_toolkit_v2.zip` i primeniti konfiguraciju

**MariaDB pristup:** UVEK koristiti `sudo mysql -u root` (bez lozinke).

### Faza 1: Import dump-a
1. Dump fajlovi se očekuju u `/home/ubuntu/db_dumps/`
2. Ako je ZIP — raspakuj: `bash scripts/unzip_and_detect.sh /home/ubuntu/db_dumps/naziv.zip`
3. Detektuj SQL fajlove i prepoznaj opp vs oppXXXYYYY obrasce u nazivima
4. Importuj sa `--force`: `bash scripts/import_database.sh <sql_fajl> <ime_baze>`
5. Uvek importuj **opp PRVU** (master baza mora postojati pre transakcione)

**Formula imena baze:** `opp` + `{šifra_firme}` + `{godina}` → npr. `opp7102025` = firma 710, godina 2025

### Faza 2: Orijentacija
1. Pročitaj `knowledge/BIZNISOFT_MASTER_REFERENCE.md` za pregled arhitekture
2. Pročitaj `learning/session_log.md` za prethodna saznanja (ako postoje)
3. Izlistaj sve baze: `SHOW DATABASES;`
4. Za svaku bazu proveri: `SHOW TABLES;` i `SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='ime_baze';`
5. Identifikuj master (opp) i transakcione baze (oppXXXYYYY pattern)

### Faza 3: Strukturna analiza
1. Prebroj tabele, procedure, trigere i funkcije u svakoj bazi
2. Uporedi sa očekivanim brojevima (opp: ~195 tabela, oppXXXYYYY: ~643 tabele)
3. Proveri `opp.documents` za definicije 95 tipova dokumenata
4. Za nepoznate tabele — konsultuj `knowledge/biznisoft_tables_reference.md`

### Faza 4: Analiza integriteta
Koristi znanje iz `knowledge/implicit_relations.md` i `knowledge/storno_patterns.md`:

1. **Referentni integritet šifarnika:**
   - Partneri: svaki `sifpar`/`sifkup` u transakcijama mora postojati u `kupci`
   - Artikli: svaki `sifra`/`sifart` mora postojati u `artikli`
   - Konta: svaki `racun`/`konto` mora postojati u `kontniplan`
   - Objekti: svaki `sifobj` mora postojati u opp.sifobj ili lokalnom šifarniku

2. **Storno parovi:**
   - Svaki dokument sa sufiksom /1 mora imati odgovarajući original
   - Neparni sufiksi (/1, /3, /5) = storno, parni (/2, /4, /6) = re-knjiženje
   - Kolona `stornirano` NIJE uvek pouzdana — proveri i kroz `storniranja` tabelu
   - Satelitski nalozi mogu imati storno sufikse ali se NE loguju u `storniranja`

3. **Finansijska ravnoteža:**
   - U `finprom`: SUM(duguje) mora biti = SUM(potrazuje) za svaki nalog
   - Proveri po kontima, periodima i tipovima dokumenata

4. **Statusna konzistentnost:**
   - Status flow: 1 (aktivan) → 2 (potvrđen) → 9 (storniran)
   - Stornirani dokumenti ne smeju imati aktivne stavke

### Faza 5: Analiza poslovne logike
Po potrebi, dublja analiza specifičnih modula:
- **Robno-trgovinsko:** kalkulacije, fakture, nivelacije — `knowledge/biznisoft_stored_procedures.md`
- **Finansijsko:** nalozi, izvodi, IOS — `knowledge/biznisoft_functions.md`
- **PDV:** evidencija, rekapitulacija — procedure `eeopdvp`, `eeppdvp`, `RekapitulacijaPDV`
- **FIFO:** obračun nabavne cene — `fifo_calc`, `PreracunajNC`
- **Trigeri:** razumevanje automatskih akcija — `knowledge/biznisoft_triggers.md`

### Faza 6: Dokumentovanje nalaza
1. Kreiraj `/home/ubuntu/session_findings/` ako ne postoji
2. Za svaku sesiju generiši izveštaj sa:
   - Datum i vreme analize
   - Koje baze su analizirane
   - Pronađeni problemi (sa primerima SQL upita)
   - Preporuke za korekciju
3. Ažuriraj `learning/` fajlove sa novim saznanjima (videti sekciju Iterativno učenje)

---

## Mehanizam iterativnog učenja

Agent beleži korisne informacije kroz rad u `learning/` folderu. Ovo omogućava da svaka naredna sesija bude efikasnija.

### Kada beležiti

- **Novo saznanje o strukturi:** Otkrivena tabela ili kolona koja nije u dokumentaciji
- **Specifičan obrazac firme:** Firma koristi nestandardne šifre, specifičan kontni plan
- **Uspešan upit:** SQL upit koji je dao korisne rezultate za čest zadatak
- **Pronađen problem:** Greška u podacima koja se može pojaviti i u drugim bazama
- **Rešenje problema:** Kako je problem dijagnostikovan i rešen

### Gde beležiti

| Fajl | Šta se beleži | Format |
|------|---------------|--------|
| `learning/session_log.md` | Svaka sesija: datum, baza, šta je rađeno, ključni nalaz | Hronološki, najnovije na vrhu |
| `learning/discovered_patterns.md` | Obrasci specifični za konkretne baze/firme | Po kategorijama (struktura, podaci, logika) |
| `learning/known_issues.md` | Problemi i njihova rešenja | Problem → Dijagnoza → Rešenje |
| `learning/query_cookbook.md` | Korisni SQL upiti | Opis → SQL → Kada koristiti |

### Kako beležiti

1. Na početku sesije — pročitaj sve `learning/` fajlove
2. Tokom rada — kada otkriješ nešto vredno, odmah zapiši
3. Na kraju sesije — sumiraj ključne nalaze u `session_log.md`
4. **Ne upisuj broj redova** u dokumentaciju (varira između baza)
5. Beleži samo **strukturu i obrasce**, ne konkretne podatke

---

## Ključna pravila rada

### Pristup bazi
- UVEK: `sudo mysql -u root` (bez lozinke, bez socketa)
- NIKAD ne menjaj podatke u bazi bez eksplicitnog zahteva korisnika
- Za import UVEK koristi `--force` flag (zbog data truncation upozorenja)

### Redosled importa
1. **Prvo opp** (master baza) — mora postojati pre transakcione
2. **Zatim oppXXXYYYY** — transakciona baza zavisi od opp za trigere na `robno`

### Imenovanje kolona — zamke
Isti entitet ima različita imena u različitim tabelama:
- **Partner:** `sifkup`, `sifpar`, `partner`, `posp`, `kupac`, `sifra` (u kupci tabeli)
- **Artikal:** `sifra` (u artikli), `sifart`, `artikal`, `sifrob`
- **Konto:** `racun`, `konto`, `kontod`, `kontop`
- **Objekat:** `sifobj`, `objekat`, `lokacija`

Uvek konsultuj `knowledge/implicit_relations.md` za tačne mapiranja.

### Više tipova dokumenata na istoj tabeli
- Tabela `fakture` služi za 5 tipova: RN, NI, OT, PF, RA — razlikuju se po `tipdokfakt`
- Tabela `finprom` služi za sve finansijske dokumente
- Uvek filtriraj po tipu dokumenta pre analize

### TIER zavisnosti od opp baze
- **TIER 1 (Kritične):** `documents`, `zirklista`, `rnpartnkli`, `datkl`, `pdvstope`
- **TIER 2 (Aplikativne):** `operateri`, `ovlpofirmama`, `drzave`, `opstine`, `sifval`
- **TIER 3 (Interne/log):** `logfile`, `bcklog`, `arh_log`

### Direktorijumi
- Dump fajlovi: `/home/ubuntu/db_dumps/`
- Nalazi sesije: `/home/ubuntu/session_findings/`
- Knowledge (ovaj skill): relativno `knowledge/`

---

## Skripte

| Skripta | Namena | Poziv |
|---------|--------|-------|
| `scripts/setup_mariadb.sh` | Kompletna instalacija i pokretanje MariaDB | `bash scripts/setup_mariadb.sh` |
| `scripts/restart_mariadb.sh` | Brzi restart (posle VM reseta) | `bash scripts/restart_mariadb.sh` |
| `scripts/import_database.sh` | Import SQL dump-a u bazu | `bash scripts/import_database.sh <sql_fajl> <ime_baze>` |
| `scripts/unzip_and_detect.sh` | Raspakivanje ZIP-a i detekcija SQL fajlova | `bash scripts/unzip_and_detect.sh <zip_fajl>` |
| `scripts/check_status.sh` | Provera da li MariaDB radi | `bash scripts/check_status.sh` |
| `scripts/apply_config.sh` | Primena performance konfiguracije | `bash scripts/apply_config.sh` |

## Alati

| Alat | Lokacija | Opis |
|------|----------|------|
| MariaDB Toolkit v2 | `tools/mariadb_toolkit_v2.zip` | `quick_setup.sh` + `mariadb_performance.cnf` — brza instalacija i optimalna konfiguracija |

---

## Primeri korišćenja

### Primer 1: Korisnik daje ZIP sa dump-om
```
Korisnik: Analiziraj ovu BizniSoft bazu [upload ZIP]
Agent:
1. Raspakuje ZIP → detektuje opp.sql i opp7102025.sql
2. Pokrene MariaDB (ako nije aktivan)
3. Importuje opp pa opp7102025
4. Čita BIZNISOFT_MASTER_REFERENCE.md
5. Pokrene strukturnu analizu i proveru integriteta
6. Generiše izveštaj u /home/ubuntu/session_findings/
```

### Primer 2: Korisnik pita o specifičnom modulu
```
Korisnik: Proveri da li se finansijska knjiženja poklapaju (duguje = potražuje)
Agent:
1. Čita knowledge o finprom tabeli
2. Pokrene SQL za proveru ravnoteže po nalozima
3. Identifikuje naloge gde duguje ≠ potrazuje
4. Dokumentuje nalaze
```

### Primer 3: VM je resetovan
```
Korisnik: Baza ne radi
Agent:
1. bash scripts/check_status.sh → potvrđuje da MariaDB ne radi
2. bash scripts/restart_mariadb.sh → pokreće server
3. Proveri da li su baze još uvek importovane
4. Ako nisu — ponovo importuje iz /home/ubuntu/db_dumps/
```
