# Biznisoft — Mapa zavisnosti: opp ↔ opp7102025

**Datum analize:** 2026-03-29

---

## 1. Pregled arhitekture

```
opp (MASTER)                          opp7102025 (TRANSAKCIONA)
═══════════════                       ═════════════════════════
195 tabela                            643 tabele
11 procedura                          105 procedura (15 čita opp)
0 trigera                             265 trigera (2 čita opp)
```

**Veza je jednosmerna:** `opp7102025` → čita iz → `opp`
Nema obrnutih referenci (opp NE referencira opp7102025).
Nema foreign key-eva između baza (veze su na nivou koda — procedure i trigeri).

---

## 2. Tačna mapa: Koje opp tabele čita opp7102025

### 2.1 Direktne reference iz PROCEDURA (15 procedura)

| opp tabela | Procedura u opp7102025 | Šta čita | Kategorija |
|---|---|---|---|
| **`opp.documents`** | `checkdokpary` | Tipove dokumenata, tabele | Definicije dokumenata |
| | `checkForeignKeys` | Strukture dokumenata | |
| | `CheckPrometPoSifri` | Tip dokumenta za promet | |
| | `dajmidokumente` | Lista dokumenata | |
| | `getEvidencijaStorno` | Evidencija storna | |
| | `GetNabCena` | Nabavnu cenu po tipu dok. | |
| | `obracunPotvrdjeno` | Tip dokumenta + sifobj | |
| | `ProveraIntegriteta` | Integritet dokumenata | |
| | `sefknjizenjanew` | Knjiženje po tipu dok. | |
| | `sefknjizenjaold` | Knjiženje (stari) | |
| | `trigoperdoc` | Operater-dokument veze | |
| | `trigoperdocx` | Operater-dokument veze | |
| **`opp.rnpartnkli`** | `AzurRnPartKli` | Registar partnera/klijenata | Šifarnik partnera |
| **`opp.bsnotif`** | `bsnotif` | Notifikacije | Sistemske obavesti |
| **`opp.datkl`** | `checkvpcenovnik` | Datumske kursne liste | Kursevi valuta |
| **`opp.zirklista`** | `checkvpcenovnik` | Zvanični kursevi | Kursevi valuta |
| **`opp.tabakciza`** | `getakciza` | Akcizne stope | PDV/Akcize |
| **`opp.arh_locations`** | `GetArchiveParentUID` | Lokacije arhive | Arhiviranje |
| **`opp.kplprevod`** | `GetKplPrevod`, `GetKplPrevodRacun` | Prevod kontnog plana | Finansije |
| **`opp.pdvstope`** | `getpdv` | PDV stope | PDV/Porezi |
| **`opp.sifobj`** | `obracunPotvrdjeno` | Šifarnik objekata | Organizacija |

### 2.2 Direktne reference iz TRIGERA (2 trigera)

| opp tabela | Triger u opp7102025 | Na tabeli | Šta čita |
|---|---|---|---|
| **`opp.zirklista`** | `insstanje` | `robno` | EUR, USD, CHF kurs za datum transakcije |
| **`opp.zirklista`** | `updstanje` | `robno` | EUR, USD, CHF kurs za datum transakcije |

**Kritičan uvid:** Svaki INSERT/UPDATE na `robno` tabeli (robno-materijalno knjiženje) automatski čita kursnu listu iz opp baze za preračun cena u strane valute!

---

## 3. Mapiranje tipova dokumenata → fizičke tabele u opp7102025

`opp.documents` definiše 95 tipova dokumenata. Svaki tip mapira na fizičku tabelu u opp7102025.

### 3.1 Status mapiranja

| Status | Broj |
|---|---|
| ✅ Tabela postoji u opp7102025 | **93** |
| ❌ Tabela ne postoji (`nema`) | **2** (PR, RC — virtuelni dokumenti) |

### 3.2 Kompletno mapiranje (grupisano po fizičkim tabelama)

Više tipova dokumenata može koristiti istu fizičku tabelu (razlikuju se po `sifra` polju):

| Fizička tabela u opp7102025 | Tipovi dokumenata (šifra → naziv) |
|---|---|
| **`fakture`** | NI (Nalog za izdavanje), OT (Otpremnica), PF (Profaktura), RA (Avansni račun), RN (Izlazna faktura) |
| **`tblfaktakcrab`** | FA (Faktura s akcijskim rabatom), NA (Nalog za izdavanje s akc.rab.), OA (Otpremnica s akc.rab.) |
| **`tblpovracaj`** | NO (Nalog za povraćaj kupca), PK (Povraćaj robe od kupca) |
| **`tblizvoz`** | ZA (Izvoz-avansni), ZP (Izvoz-profaktura), ZZ (Izvoz robe) |
| **`putninalog`** | IN (Putni nalog inostranstvo), PN (Putni nalog zemlja) |
| **`robno`** | PC (Promena cene), PS (Početno stanje) |
| **`radnal`** | GN (Grupni radni nalog), RD (Radni nalog) |
| **`kalkulacije`** | KL (Kalkulacija/prijemnica) |
| **`nivelacije`** | NC (Nivelacija cene) |
| **`nivkalkulacije`** | KI (Kalkulacija sa nivelacijom) |
| **`popis`** | PL (Višak/manjak po popisnoj listi) |
| **`pazari`** | PZ (Dnevni pazari) |
| **`kasa`** | KA (Kasa u maloprodaji) |
| **`blgpromet`** | BL (Blagajničko poslovanje) |
| **`intprijem`** | IP (Interni prijem robe) |
| **`intracun`** | IR (Interni prenos dobara) |
| **`tblpovracajdob`** | PD (Povraćaj robe dobavljaču) |
| **`tblpovracajdobnovi`** | NP (Povraćaj dob. novi promet) |
| **`tblodobdob`** | OD (Odobrenje/zaduženje dobavljača) |
| **`tblodobkup`** | OK (Knjižno odobrenje) |
| **`tblodobinodob`** | ZD (Odobrenje/zaduženje ino dobavljača) |
| **`tblodobinokup`** | ZO (Odobrenje/zaduženje ino kupca) |
| **`tblkomkalk`** | KK (Kalkulacija komisione robe) |
| **`tblkomfakture`** | KF (Izdavanje fakture komisionaru) |
| **`komnivelacije`** | KN (Nivelacija komisione robe) |
| **`tblkomvrac`** | KV (Vraćanje komisione robe) |
| **`tblambintpr`** | AA (Interni prenos ambalaže) |
| **`tblamprijdob`** | AJ (Prijem ambalaže od dobavljača) |
| **`tblamizdkup`** | AM (Izdavanje ambalaže) |
| **`tblampovkup`** | AP (Povraćaj ambalaže od kupca) |
| **`tblampovdob`** | AV (Povraćaj ambalaže dobavljaču) |
| **`nabambalaze`** | NB (Nabavka ambalaže) |
| **`tblprodamb`** | RM (Prodaja ambalaže) |
| **`tblnardobavljacima`** | ND (Narudžbine dobavljačima) |
| **`tblnarkupaca`** | NK (Narudžbine kupaca) |
| **`tbltrebovanje`** | TB (Trebovanje robe) |
| **`tblintizdavanje`** | II (Interno izdavanje robe) |
| **`tblizdavanje`** | TI (Izdavanje tuđe robe) |
| **`tblotkup`** | TO (Prijem tuđe robe) |
| **`tblotkupss`** | TS (Otkup sekundarnih sirovina) |
| **`tblpoljoprivreda`** | PP (Otkup poljopr. proizvoda) |
| **`tblisplata`** | LL (Isplata poljopr. proizvođaču) |
| **`tbluvoz`** | UK (Uvozna kalkulacija) |
| **`faktureos`** | FS (Izlazna faktura za OS) |
| **`tblposotpremnice`** | PO (Fakturisanje po POS otpremnicama) |
| **`tblprodmat`** | FM (Prodaja repromaterijala) |
| **`tblprodfakture`** | DF (Fakture iz D.O.) |
| **`prodkalkulacije`** | DK (Kalkulacija iz D.O.) |
| **`prodnivelacije`** | DN (Nivelacija iz D.O.) |
| **`prodpovracajdob`** | DD (Povraćaj dobavljaču iz D.O.) |
| **`prodintracun`** | PI (Interni račun iz D.O.) |
| **`tblprodajagp`** | GP (Prodaja gotovih proizvoda) |
| **`tblfaktbezobr`** | RB (Fakturisanje bez obračuna nabavke) |
| **`tblrobtransf`** | TF (Transformacije artikala) |
| **`tblsopsttros`** | RT (Račun sopstvenih troškova) |
| **`tblnabsitinv`** | SK (Nabavka sitnog inventara) |
| **`tblsitanizd`** | SU (Izdavanje sitnog inventara) |
| **`sitinvzad`** | SZ (Zaduženje sitnog inventara) |
| **`sitinvpov`** | SP (Povraćaj sitnog inventara) |
| **`sitinvras`** | SR (Rashodovanje sitnog inventara) |
| **`tblotpisnz`** | ON (Otpis mimo zakonskih stopa) |
| **`tblotpisz`** | OZ (Otpis po zakonskim stopama) |
| **`tblmatobrdor`** | MO (Slanje materijala na obradu) |
| **`tblmatobrdorprij`** | MP (Prijem materijala sa obrade) |
| **`tblrobobrdor`** | RO (Slanje robe na obradu) |
| **`tblrobobrdorprij`** | DP (Prijem robe sa obrade) |
| **`tblproizvobrdor`** | VO (Slanje proizvoda na obradu) |
| **`tblproizvobrdorprij`** | VP (Prijem proizvoda sa obrade) |
| **`tblkooizdavanje`** | KO (Izdavanje kooperantu) |
| **`tblreversizdavanje`** | UI (Izdavanje na tuđe skladište) |
| **`tblreversprijem`** | UP (Prijem sa tuđeg skladišta) |
| **`tblpovracajinokup`** | ZI (Povraćaj robe ino kupca) |
| **`dt_srv_rnpojed`** | SN (Servisni nalog) |
| **`frmgk_avans`** | AR (Fin.trans. prijem avansnog računa) |
| **`frmgk_carina`** | CR (Fin.trans. carina) |
| **`frmgk_ed`** | ED (Fin.trans. elektronske dopune) |
| **`frmgk_faktura`** | FK (Fin.trans. izlazna faktura) |
| **`frmgk_nefak`** | NR (Fin.trans. nefakturisana roba) |
| **`frmgk_osnsred`** | OS (Fin.trans. nabavka OS) |
| **`frmgk_prijemfakture`** | RK (Prijem računa komitenta) |
| **`frmgk_troskovi`** | TR (Fin.trans. troškovi) |
| **`nema`** | PR (Preknjižavanje), RC (Korekcija nab.cene) — **virtuelni, bez tabele** |

---

## 4. Šifarnici koji su ISKLJUČIVO master u opp

Ove tabele postoje **SAMO u opp** i čitaju se od strane opp7102025 procedura/trigera:

| opp tabela | Redova | Čita je | Opis/Funkcija |
|---|---|---|---|
| `documents` | 95 | 12 procedura | **CENTRALNA** — definicije svih tipova dokumenata |
| `rnpartnkli` | 167,690 | 1 procedura | Registar partnera/klijenata (sva preduzeća) |
| `datkl` | 138,204 | 1 procedura | Datumski kursevi valuta |
| `zirklista` | 10 | 1 proc + 2 trigera | Kursna lista (EUR/USD/CHF) |
| `pdvstope` | 9 | 1 procedura | PDV stope |
| `tabakciza` | 0 | 1 procedura | Akcize (pripremljeno, nepopunjeno) |
| `kplprevod` | 2,133 | 2 procedure | Prevod kontnog plana |
| `sifobj` | 19 | 1 procedura | Šifarnik objekata/magacina |
| `arh_locations` | 1 | 1 procedura | Lokacije arhive |
| `bsnotif` | 26,369 | 1 procedura | Sistemske notifikacije |

### Šifarnici u opp koji se NE referenciraju direktno (ali su implicitno potrebni):

Ove tabele se verovatno čitaju na APLIKATIVNOM nivou (Delphi klijent), a ne kroz SQL:

| opp tabela | Redova | Verovatna upotreba |
|---|---|---|
| `drzave` | 252 | Padajuća lista država u formama |
| `opstine` | 207 | Izbor opštine |
| `pbrmesto` | 1,525 | Autocomplete za poštanske brojeve |
| `ptt_brojevi` | 1,994 | PTT validacija |
| `sifval` | 37 | Izbor valute |
| `sifzanimanja` | 2,963 | Izbor zanimanja u kadrovskoj evidenciji |
| `sifplac` | 200 | Tipovi plaćanja |
| `oskateg` / `osamgzag` / `osamgdet` | 15/123/1,460 | OS amortizacione grupe |
| `operateri` | 134 | Login i ovlašćenja |
| `ovlpofirmama` | 66,486 | Pristup firmama po operateru |
| `ovlpoizvest` | 46,552 | Pristup izveštajima po operateru |
| `cnfg_*` | ~3,476 | Svi konfigurabilni parametri |

---

## 5. Dijagram zavisnosti

```
╔════════════════════════════════════════════════════════════════════════╗
║                        opp (MASTER BAZA)                            ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  ┌──────────────────────────────────────────────────────────────┐    ║
║  │ TIER 1: Kritične zavisnosti (referencirane iz SQL koda)     │    ║
║  │                                                              │    ║
║  │  documents ──────────── 12 procedura čita (tip→tabela map)  │    ║
║  │  zirklista ──────────── 2 trigera + 1 proc (kurs valuta)    │    ║
║  │  rnpartnkli ─────────── 1 procedura (sync partnera)        │    ║
║  │  datkl ──────────────── 1 procedura (datumski kursevi)      │    ║
║  │  pdvstope ───────────── 1 procedura (PDV obračun)           │    ║
║  │  kplprevod ──────────── 2 procedure (prevod kont. plana)    │    ║
║  │  sifobj ─────────────── 1 procedura (obračun po objektima)  │    ║
║  └───────────────────────────────┬──────────────────────────────┘    ║
║                                  │                                    ║
║  ┌───────────────────────────────┤                                   ║
║  │ TIER 2: Aplikativne zavisn.  │ (čitane kroz Delphi klijent)     ║
║  │                               │                                   ║
║  │  operateri, ovlpofirmama,    │                                   ║
║  │  ovlpoizvest, drzave,       │                                   ║
║  │  opstine, sifval, sifplac,  │                                   ║
║  │  cnfg_*, pdvstopelabele...  │                                   ║
║  └───────────────────────────────┤                                   ║
║                                  │                                    ║
║  ┌───────────────────────────────┤                                   ║
║  │ TIER 3: Interne/log tabele   │ (nema direktnu vezu)             ║
║  │                               │                                   ║
║  │  logfile, bcklog, arh_log,   │                                   ║
║  │  favorites, scheduler,       │                                   ║
║  │  reports, fiz_* (fin.izv.)   │                                   ║
║  └───────────────────────────────┘                                   ║
║                                                                      ║
╚══════════════════════════╦═══════════════════════════════════════════╝
                           ║
            ═══════════════╩═══════════════
            ║  SQL reference (15 proc +   ║
            ║  2 trigera)                  ║
            ═══════════════╦═══════════════
                           ║
╔══════════════════════════╩═══════════════════════════════════════════╗
║                   opp7102025 (TRANSAKCIONA BAZA)                    ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  643 tabele organizovane po modulima:                               ║
║                                                                      ║
║  ┌────────────────────┬────────────────────┬──────────────────────┐  ║
║  │ ROBNO-MATERIJALNO  │ FINANSIJE          │ PLATE/KADROVI       │  ║
║  │ robno, trstanje    │ gk, gkstavke       │ zaposleni, ldstavke │  ║
║  │ artikli, fakture   │ fintrans, blagajna │ ldrekapitulacija    │  ║
║  │ kalkulacije...     │ frmgk_*...         │                     │  ║
║  ├────────────────────┼────────────────────┼──────────────────────┤  ║
║  │ KOMISIONA/AMBALAŽA │ OSNOVNA SREDSTVA   │ PROIZVODNJA         │  ║
║  │ tblkom*, tblamb*   │ ossredstva, osprom │ radnal, receptura   │  ║
║  │ nabambalaze        │ osamortizacija     │ tblrobtransf        │  ║
║  └────────────────────┴────────────────────┴──────────────────────┘  ║
║                                                                      ║
║  Zajedničke tabele (15): kontniplan, tabrac, operateri, sifobj,     ║
║  build, ld220, ldvp_opj1, mybsliveid, ld130, kporacuni, pk1racuni, ║
║  hot_tax, poljapozelji, puk_stepstrucnespreme, puk_strucnasprema   ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## 6. Ključni zaključci

### 6.1 Arhitekturni model
- **opp** = centralni šifarnik deljen između SVIH firmi/baza
- **opp7102025** = podaci jedne konkretne firme za jednu godinu
- Veza je **read-only** od opp7102025 ka opp (nikad obrnuto)

### 6.2 Najkritičnija zavisnost
**`opp.documents`** — 12 od 15 procedura koje referenciraju opp čitaju ovu tabelu. Ona definiše:
- Koji tip dokumenta (šifra AA-ZZ) mapira na koju fizičku tabelu
- Kakva je struktura ključa (`tipkljuca`)
- Da li je faktura, izlazni dokument, itd.

### 6.3 Real-time zavisnost
Trigeri `insstanje` i `updstanje` na tabeli `robno` čitaju **`opp.zirklista`** pri SVAKOM unosu/izmeni robnog knjiženja. Ako opp baza nije dostupna, robno knjiženje neće moći da izračuna kurseve.

### 6.4 Zajedničke tabele — sinhronizacija
Od 15 zajedničkih tabela:
- 5 su sinhronizovane (identične)
- 5 su prazne u opp7102025 (master kopija u opp)
- `kontniplan` divergira (opp7 ima 74 konta više — firmski specifično)
- `tabrac` divergira (opp7 ima 722 računa više — firmski specifično)

### 6.5 Implicitne zavisnosti (aplikativni nivo)
Delphi aplikacija verovatno čita ~30+ šifarničkih tabela iz opp za padajuće liste, validacije i autocomplete — ovo nije vidljivo iz SQL koda, ali je neophodno za funkcionisanje.
