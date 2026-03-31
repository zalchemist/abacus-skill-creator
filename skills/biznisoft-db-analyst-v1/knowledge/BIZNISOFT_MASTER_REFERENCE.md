# BIZNISOFT ERP — MASTER REFERENTNI DOKUMENT

**Verzija:** 1.0
**Datum:** 2026-03-29
**Izvor podataka:** opp (master baza, 195 tabela) + opp7102025 (transakciona baza firme 710, godina 2025, 643 tabele)
**Namena:** Kompletan pregled sistema za autonomnog agenta — čitanjem SAMO ovog fajla agent treba da razume celokupnu arhitekturu, podatke i poslovnu logiku.

---

## Sadržaj

1. [Uvod i arhitektura sistema](#1-uvod-i-arhitektura-sistema)
2. [Šifarnici (Master Data)](#2-šifarnici-master-data)
3. [Tipovi dokumenata](#3-tipovi-dokumenata)
4. [Stored Procedure — pregled](#4-stored-procedure--pregled)
5. [Trigeri — pregled](#5-trigeri--pregled)
6. [Implicitne relacije](#6-implicitne-relacije)
7. [Storno logika](#7-storno-logika)
8. [Zavisnosti opp ↔ oppXXXYYYY](#8-zavisnosti-opp--oppxxxyyy)
9. [Pravila integriteta](#9-pravila-integriteta)

---

## 1. Uvod i arhitektura sistema

### 1.1 Šta je BizniSoft

BizniSoft je sveobuhvatni ERP sistem za mala, srednja i velika preduzeća u Srbiji. Windows client/server arhitektura (Delphi klijent), MySQL/MariaDB baza. Optimizovan za visoke transakcione volumene — od POS sistema do računovodstvenih agencija sa stotinama firmi.

### 1.2 Glavni moduli

| Modul | Opis | Ključne tabele u transakcionoj bazi |
|-------|------|--------------------------------------|
| **Robno-trgovinsko** | Kalkulacije, fakture, nivelacije, popis, interni prenosi | `robno`, `fakture`, `kalkulacije`, `nivelacije`, `popis`, `kasa`, `trgovacka`, `trstanje` |
| **Finansijsko** | Glavna knjiga, nalozi, izvodi | `finprom`, `kontniplan`, `specifikacijanaloga`, `virmani` |
| **Finansijska operativa** | IOS, kompenzacije, kamate | `finprom` (analitika po partnerima) |
| **Proizvodnja** | Radni nalozi, recepture, cena koštanja | `radnal`, `tblrobtransf` |
| **Obračun zarada** | Plate, porezi, doprinosi | `ld110`, `ld120*`, `ldobracun`, `ldugozar`, `ldgknalog` |
| **Osnovna sredstva** | Evidencija, amortizacija | `osnsred_spec`, `osregos`, `osobracunpoa`, `osamvr`, `osnabvr` |
| **PDV evidencija** | EEOPDV, EEPPDV, POPDV | `popdv_promet`, `eeopdv_*`, `eeppdv_*` |
| **E-fakture (SEF)** | Elektronske fakture | `veznaefakture`, `logefakture`, `eracunprim`, `eracunposl` |
| **Kasa/POS** | Fiskalna kasa, pazari | `kasa`, `pospracuni`, `pazari` |
| **Kadrovi (HR)** | Evidencija zaposlenih | `puk_zaposleni`, `puk_orgjed`, `puk_radnamesta` |
| **Hotel** | Rezervacije, gosti, sobe | `hot_rezervacije`, `hot_gosti`, `hot_sifsoba` |

### 1.3 Multi-tenant model

```
opp                     → Master baza (šifarnici, konfiguracija, definicije)
                           195 tabela, 11 procedura, 0 trigera
                           Deljena između SVIH firmi/korisnika

opp{firma}{godina}      → Transakciona baza za jednu firmu i godinu
                           Primer: opp7102025 = firma 710, godina 2025
                           643 tabele, 105 procedura, 265 trigera
```

**Formula za ime baze:** `CONCAT(bsliveid, 'opp', sifrafirme, YEAR(NOW()))`
- `bsliveid` = identifikator instalacije (može biti prazan string)
- Primer: `'' + 'opp' + '710' + '2025'` = `opp7102025`

### 1.4 Uloge baza

| Aspekt | opp (Master) | oppXXXYYYY (Transakciona) |
|--------|-------------|---------------------------|
| **Sadržaj** | Šifarnici, konfiguracija, definicije dokumenata | Svi poslovni dokumenti i transakcije |
| **Ko piše** | Administratori, sistem | Operateri (dnevni rad) |
| **Ko čita** | Sve transakcione baze | Samo ta firma/godina |
| **Trigeri** | Nema (0) | 265 trigera |
| **Ažuriranje** | Retko (šifarničko) | Kontinualno (transakcije) |

### 1.5 Tip baze i ključne karakteristike

- **Engine:** MySQL/MariaDB, InnoDB
- **Foreign Keys:** **NEMA eksplicitnih FK constraints** — sve relacije su implicitne (aplikativni nivo)
- **Razlog:** Performanse, fleksibilnost, cross-database reference
- **Posledica:** Integritet se mora proveravati ručno ili kroz procedure

---

## 2. Šifarnici (Master Data)

### 2.1 Šifarnici u opp bazi (master — deljeni između svih firmi)

| Tabela | Redova | Uloga | Ključno polje |
|--------|--------|-------|---------------|
| **`documents`** | 95 | **CENTRALNA** — definicije svih tipova dokumenata → tabela → forma | `sifra` (2 char, npr. RN, KL) |
| **`matpod`** | 674 | Matični podaci svih firmi (naziv, PIB, matični broj, sedište) | `sifra` |
| **`operateri`** | 134 | Lista korisnika sistema, login, ovlašćenja | `korime` |
| **`tabrac`** | 426 | Kontni plan — tabela računa sa kontima i klasama | `sifra`, `konto` |
| **`kplvezna`** | 420 | Vezna tabela za automatsko knjiženje (konto → pravilo) | |
| **`pdvstope`** | 9 | PDV stope (opšta 20%, posebna 10%, oslobođen...) | `sifra` |
| **`pdvstopelabele`** | 6 | Labele PDV stopa za izveštavanje | |
| **`sifval`** | 37 | Valute (RSD, EUR, USD, CHF, GBP...) | `sifra` |
| **`drzave`** | 252 | Države (ISO kodovi) | |
| **`opstine`** | 207 | Opštine u Srbiji | |
| **`sifplac`** | 200 | Vrste plaćanja (gotovina, virman, kompenzacija, cesija...) | `sifra` |
| **`sifzanimanja`** | 2963 | Zanimanja (NKD klasifikacija) | |
| **`sifobj`** | 19 | Objekti — prodavnice, magacini, pogoni | `sifra` |
| **`propisani_parametri`** | 56 | Zakonski propisani parametri (minimalac, cenzusi, stope) | |
| **`cnfg_parametri`** | 1116 | Konfiguracioni parametri sistema | |
| **`datkl`** | 138,204 | Datumski kursevi valuta (velika tabela) | |
| **`zirklista`** | 10 | Kursna lista (EUR/USD/CHF) — čitana iz trigera! | |
| **`rnpartnkli`** | 167,690 | Registar partnera/klijenata (sve firme zajedno) | |
| **`kplprevod`** | 2,133 | Prevod kontnog plana | |
| **`oskateg`** | 15 | Kategorije osnovnih sredstava | |
| **`osporgrupe`** | 6 | Poreske grupe za amortizaciju OS | |
| **`osporpodgr`** | 92 | Poreske podgrupe za amortizaciju OS | |
| **`tr_pravila`** | 9 | Pravila za automatsko knjiženje troškova | |
| **`tr_pravila_stavke`** | 27 | Stavke pravila: artikal → konto → PDV oznaka | |
| **`propsifban`** | 20 | Šifre banaka u Srbiji | |
| **`ldkategugod`** | 79 | Kategorije ugovora o radu | |
| **`ldkategzap`** | 47 | Kategorije zaposlenih | |
| **`ovlpofirmama`** | 66,486 | Pristup firmama po operateru | |
| **`ovlpoizvest`** | 46,552 | Pristup izveštajima po operateru | |

### 2.2 Šifarnici u transakcionoj bazi (opp7102025 — firmski specifični)

| Tabela | Redova | Uloga | Ključno polje |
|--------|--------|-------|---------------|
| **`artikli`** | ~2,000+ | Šifarnik artikala (roba, usluge, proizvodi) | `sifra` |
| **`kupci`** | 2,324 | Šifarnik kupaca/partnera/dobavljača | `sifra` |
| **`objekti`** | var. | Objekti za ovu firmu | `objekat` |
| **`kontniplan`** | 17,077 | Kontni plan (kopija + 74 firmska konta) | `konto` |
| **`tarife`** | var. | Poreske tarife | `tarifa` |
| **`grupart`** | var. | Grupe artikala | |
| **`mestatr`** | var. | Mesta troškova | |
| **`komercijalisti`** | var. | Komercijalisti | |
| **`nosioci`** | var. | Nosioci troškova | |

### 2.3 Ključni podaci šifarnika artikala

- **Šifra artikla** — jedinstveni identifikator
- **Naziv**, Jedinica mere, Barkod, Kataloški broj
- **Poreska stopa:** S0=0%, S1=20%, S2=10%
- **Tarifa:** 0=bez PDV, 1=sa PDV, 9=usluge
- **Karakter artikla:** roba, usluga, proizvod, sirovina, ambalaža, komisiona roba
- **Grupa artikla** — hijerarhijsko grupisanje
- **Za proizvode:** planska cena, VP cena, receptura (normativ)

### 2.4 Ključni podaci šifarnika partnera (kupci)

- **Tipovi:** Pravno lice, Preduzetnik, Fizičko lice, Strano pravno lice, Poljoprivredni proizvođač
- **Podaci:** Šifra, naziv, adresa, PIB, matični broj, PDV obveznik (Da/Ne), tekući računi
- **NBS web servis:** Automatsko preuzimanje podataka partnera

### 2.5 Kontni plan

- **`tabrac`** u opp: 426 računa (master šablon)
- **`kontniplan`** u opp7102025: 17,077 konta (firmski specifično, divergira od mastera)
- **Atributi konta:** broj, naziv, analitika (partneri/objekti/zaposleni/bez), devizni, zatvaranje
- **Veza:** `kplvezna` definiše pravila automatskog knjiženja

---

## 3. Tipovi dokumenata

### 3.1 Tabela `opp.documents` — centralna definicija

Kolone:
- `sifra` — dvoslovni kod (AA-ZZ)
- `naziv` — pun naziv dokumenta
- `tabela` — fizička tabela u transakcionoj bazi
- `tipkljuca` — kategorija dokumenta (1-15)
- `tipdokfakt` — F=faktura, I=nalog za izdavanje, O=otpremnica, P=profaktura, A=avans, T=trošak
- `izlaznidokument` — 1=izlazni (smanjuje zalihe), 0=ulazni (povećava)
- `jefaktura` — 1=ulazi u PDV evidenciju
- `forma` — Delphi forma za unos

### 3.2 Klasifikacija po tipkljuca

| tipkljuca | Kategorija | Br. dok | Opis |
|-----------|-----------|---------|------|
| 1 | Ulazni robni | 21 | Kalkulacije, prijemnice, nabavke, trebovanja, otkupi |
| 2 | Izlazni robni / Fakture | 43 | Fakture, otpremnice, nalozi, povraćaji, izvoz, odobrenja |
| 3 | Interni prenosi | 7 | Interni prenosi, zaduženja, sitni inventar |
| 4 | Nivelacije | 3 | Nivelacije cena (redovna, komisiona, D.O.) |
| 5 | Popis | 1 | Višak/manjak po popisnoj listi |
| 6 | Kasa | 1 | Kasa u maloprodaji |
| 7 | Robno (cene/stanje) | 3 | Promena cene, početno stanje, dnevni pazari |
| 8 | Servis | 1 | Servisni nalog |
| 9 | Blagajna | 1 | Blagajničko poslovanje |
| 10 | Radni nalog | 2 | Radni nalog, grupni radni nalog |
| 11 | Isplata | 1 | Isplata poljoprivrednom proizvođaču |
| 13 | Finansijske transakcije | 8 | Prijem faktura, avansi, carina, troškovi, OS |
| 14 | Preknjižavanje | 2 | Preknjižavanje prometa, korekcija nabavne cene |
| 15 | Putni nalozi | 2 | Putni nalog zemlja/inostranstvo |

### 3.3 Kompletna lista — svih 95 tipova dokumenata

#### Ulazni robni dokumenti (tipkljuca=1)

| Šifra | Naziv | Tabela |
|-------|-------|--------|
| KL | Kalkulacija/prijemnica dobara | `kalkulacije` |
| KK | Kalkulacija komisione robe | `tblkomkalk` |
| KI | Kalkulacija sa nivelacijom | `nivkalkulacije` |
| DK | Kalkulacija iz D.O. | `prodkalkulacije` |
| UK | Uvozna kalkulacija | `tbluvoz` |
| IP | Interni prijem robe | `intprijem` |
| NB | Nabavka ambalaže | `nabambalaze` |
| SK | Nabavka sitnog inventara | `tblnabsitinv` |
| PD | Povraćaj robe dobavljaču | `tblpovracajdob` |
| KV | Vraćanje komisione robe | `tblkomvrac` |
| PP | Otkup poljopr. proizvoda | `tblpoljoprivreda` |
| TO | Prijem tuđe robe | `tblotkup` |
| TS | Otkup sekundarnih sirovina | `tblotkupss` |
| UP | Prijem sa tuđeg skladišta (revers) | `tblreversprijem` |
| MP | Prijem materijala sa obrade | `tblmatobrdorprij` |
| DP | Prijem robe sa obrade | `tblrobobrdorprij` |
| VP | Prijem proizvoda sa obrade | `tblproizvobrdorprij` |
| TB | Trebovanje robe | `tbltrebovanje` |
| ND | Narudžbine dobavljačima | `tblnardobavljacima` |
| OD | Prijem odobrenja/zaduženja dobavljača | `tblodobdob` |
| ZD | Odobrenje/zaduženje ino dobavljača | `tblodobinodob` |

#### Izlazni robni / Fakture (tipkljuca=2)

| Šifra | Naziv | Tabela | tipdokfakt | jefaktura |
|-------|-------|--------|------------|-----------|
| RN | Izlazna faktura / račun | `fakture` | F | 1 |
| NI | Nalog za izdavanje | `fakture` | I | 0 |
| OT | Otpremnica | `fakture` | O | 0 |
| PF | Profaktura/rezervacija | `fakture` | P | 0 |
| RA | Avansni račun | `fakture` | A | 0 |
| FA | Faktura sa akcijskim rabatom | `tblfaktakcrab` | F | 1 |
| NA | Nalog za izdavanje s akc.rab. | `tblfaktakcrab` | I | 0 |
| OA | Otpremnica s akc.rab. | `tblfaktakcrab` | O | 0 |
| RB | Fakturisanje bez obračuna nabavke | `tblfaktbezobr` | F | 1 |
| DF | Fakture iz D.O. | `tblprodfakture` | F | 1 |
| FS | Izlazna faktura za OS | `faktureos` | F | 1 |
| KF | Izdavanje fakture komisionaru | `tblkomfakture` | F | 1 |
| KO | Izdavanje repromaterijala kooperantu | `tblkooizdavanje` | F | 1 |
| ZZ | Izvoz robe i usluga | `tblizvoz` | F | 1 |
| ZA | Izvoz – avansni | `tblizvoz` | A | 0 |
| ZP | Izvoz – profaktura u EUR | `tblizvoz` | P | 0 |
| PK | Povraćaj robe od kupca | `tblpovracaj` | F | 0 |
| NO | Nalog za povraćaj kupca | `tblpovracaj` | O | 0 |
| NP | Povraćaj dobavljaču – novi promet | `tblpovracajdobnovi` | F | 1 |
| ZI | Povraćaj robe ino kupca | `tblpovracajinokup` | F | 0 |
| OK | Knjižno odobrenje | `tblodobkup` | F | 0 |
| ZO | Odobrenje/zaduženje ino kupca | `tblodobinokup` | F | 0 |
| NK | Narudžbine kupaca | `tblnarkupaca` | F | 0 |
| PO | Fakturisanje po POS otpremnicama | `tblposotpremnice` | F | 0 |
| GP | Prodaja gotovih proizvoda | `tblprodajagp` | F | 0 |
| FM | Prodaja repromaterijala | `tblprodmat` | F | 0 |
| RM | Prodaja ambalaže | `tblprodamb` | F | 0 |
| AM | Izdavanje ambalaže | `tblamizdkup` | F | 0 |
| AP | Povraćaj ambalaže od kupca | `tblampovkup` | F | 0 |
| AV | Povraćaj ambalaže dobavljaču | `tblampovdob` | F | 0 |
| AJ | Prijem ambalaže od dobavljača | `tblamprijdob` | F | 0 |
| TI | Izdavanje tuđe robe | `tblizdavanje` | F | 0 |
| UI | Izdavanje na tuđe skladište (revers) | `tblreversizdavanje` | F | 0 |
| MO | Slanje materijala na obradu | `tblmatobrdor` | F | 0 |
| RO | Slanje robe na obradu | `tblrobobrdor` | F | 0 |
| VO | Slanje proizvoda na obradu | `tblproizvobrdor` | F | 0 |
| ON | Otpis mimo zakonskih stopa | `tblotpisnz` | T | 0 |
| OZ | Otpis po zakonskim stopama | `tblotpisz` | T | 0 |
| SR | Rashodovanje sitnog inventara | `sitinvras` | T | 0 |
| RT | Račun sopstvenih troškova | `tblsopsttros` | T | 0 |
| DD | Povraćaj dobavljaču iz D.O. | `prodpovracajdob` | — | 0 |
| LL | Isplata poljopr. proizvođaču | `tblisplata` | — | 0 |

#### Interni prenosi (tipkljuca=3)

| Šifra | Naziv | Tabela |
|-------|-------|--------|
| IR | Interni prenos dobara | `intracun` |
| AA | Interni prenos ambalaže | `tblambintpr` |
| II | Interno izdavanje robe | `tblintizdavanje` |
| PI | Interni račun iz D.O. | `prodintracun` |
| SP | Povraćaj sitnog inventara | `sitinvpov` |
| SU | Izdavanje sitnog inventara | `tblsitanizd` |
| SZ | Zaduženje sitnog inventara | `sitinvzad` |

#### Nivelacije (tipkljuca=4)

| Šifra | Naziv | Tabela |
|-------|-------|--------|
| NC | Nivelacija cene | `nivelacije` |
| KN | Nivelacija komisione robe | `komnivelacije` |
| DN | Nivelacija iz D.O. | `prodnivelacije` |

#### Ostali tipovi

| Šifra | Naziv | Tabela | tipkljuca |
|-------|-------|--------|-----------|
| PL | Višak/manjak po popisnoj listi | `popis` | 5 |
| KA | Kasa u maloprodaji | `kasa` | 6 |
| PC | Promena cene | `robno` | 7 |
| PS | Početno stanje | `robno` | 7 |
| PZ | Dnevni pazari | `pazari` | 7 |
| SN | Servisni nalog | `dt_srv_rnpojed` | 8 |
| BL | Blagajničko poslovanje | `blgpromet` | 9 |
| RD | Radni nalog | `radnal` | 10 |
| GN | Grupni radni nalog | `radnal` | 10 |
| AR | Fin.trans. prijem avansnog računa | `frmgk_avans` | 13 |
| CR | Fin.trans. carina | `frmgk_carina` | 13 |
| ED | Fin.trans. elektronske dopune | `frmgk_ed` | 13 |
| FK | Fin.trans. izlazna faktura | `frmgk_faktura` | 13 |
| NR | Fin.trans. nefakturisana roba | `frmgk_nefak` | 13 |
| OS | Fin.trans. nabavka OS | `frmgk_osnsred` | 13 |
| RK | Prijem računa komitenta | `frmgk_prijemfakture` | 13 |
| TR | Fin.trans. troškovi | `frmgk_troskovi` | 13 |
| PR | Preknjižavanje prometa | **nema** (virtuelni) | 14 |
| RC | Korekcija nabavne cene | **nema** (virtuelni) | 14 |
| PN | Putni nalog u zemlji | `putninalog` | 15 |
| IN | Putni nalog u inostranstvu | `putninalog` | 15 |

### 3.4 Mapiranje — više tipova na istu tabelu

Više tipova dokumenata može koristiti istu fizičku tabelu (razlikuju se po `tipdokfakt` ili kontekstu):

| Fizička tabela | Tipovi dokumenata |
|---------------|-------------------|
| `fakture` | RN (faktura), NI (nalog za izdavanje), OT (otpremnica), PF (profaktura), RA (avansni račun) |
| `tblfaktakcrab` | FA (faktura), NA (nalog), OA (otpremnica) — sve sa akcijskim rabatom |
| `tblpovracaj` | PK (povraćaj od kupca), NO (nalog za povraćaj) |
| `tblizvoz` | ZZ (izvoz), ZA (avans), ZP (profaktura) |
| `putninalog` | PN (zemlja), IN (inostranstvo) |
| `radnal` | RD (radni nalog), GN (grupni radni nalog) |
| `robno` | PC (promena cene), PS (početno stanje) |

### 3.5 Veza dokument → knjiženje

| Dokument tabela | Gde se knjiži |
|-----------------|---------------|
| `fakture` | `finprom` + `robno` + `trgovacka` |
| `kalkulacije` | `robno` + `trgovacka` |
| `nivelacije` | `robno` + `trgovacka` |
| `intracun` | `robno` |
| `kasa` | `robno` + `trgovacka` (+ `finprom` za dnevni pazar) |
| `avracuni` | `finprom` (preko `frmgk_avans`) |
| `tbluvoz` | `robno` + `finprom` |
| `osnsred_spec` | `finprom` (amortizacija) |
| `ldugozar` + `ldobracun` | `finprom` (preko `ldgknalog`) |

---

## 4. Stored Procedure — pregled

### 4.1 Procedure u opp (master) — 11 procedura + 1 funkcija

| Procedura | Šta radi | Kada se poziva |
|-----------|---------|----------------|
| `AutCheckInt` | Iterira kroz sve firme u `defautint`, poziva `ProveraIntegriteta` u svakoj transakcionoj bazi, šalje notifikacije operaterima o greškama | Zakazano (scheduler), periodično |
| `bsnotif` | Kreira notifikaciju u `bsnotif` tabeli za konkretnog operatera | Pozivana iz drugih procedura |
| `bsnotiftoopers` | Šalje notifikaciju svim aktivnim operaterima (`notifikacije=1`) | Sistemska upozorenja |
| `CheckBsNotifForOper` | Proverava da li operater ima popunjenu sliku i ime — šalje podsetnik | Pri login-u operatera |
| `CheckBsNotification` | Proverava storno notifikacije iz `stornonotif` tabele | Sistemska |
| `checkistekugorad` | Proverava istek ugovora o radu, šalje upozorenja operaterima N dana pre isteka | Zakazano |
| `collect_ldstav_ugod` | Prikuplja stavke ličnih dohodaka iz ugovora iz SVIH transakcionih baza | Ad-hoc / izveštaji |
| `ExportAndDeleteProcedure` | Eksportuje `finprom` podatke iz više baza u CSV, zatim se briše | Maintenance |
| `fetch_finprom_data_new` | Dohvata `finprom` iz svih baza (2022/2023), kreira objedinjenu tabelu | Izveštaji |
| `fetch_finprom_data_new_z` | Isto, varijanta za 2023/2024 | Izveštaji |
| `popuniFirme` | Popunjava `arh_config` tabelu sa listom svih baza za backup | Administracija |
| `mod_97_10_check` (FUN) | Validacija mod 97-10 kontrolnog broja (IBAN) | Validacija podataka |

**Ključni obrazac:** Procedure koriste `PREPARE/EXECUTE` dinamički SQL za pristup transakcionim bazama čiji nazivi se formiraju kao `{bsliveid}opp{sifrafirme}{godina}`.

### 4.2 Procedure u opp7102025 (transakciona) — 105 procedura

#### Grupisane po funkcionalnosti:

**PDV evidencije (15 proc.):**
`eeopdvp`, `eeppdvp`, `creeeopdvp`, `creeeppdvp`, `formirajEEOPDVP`, `PrepareEEPPDVData`, `pr_doeeppdv`, `RekapitulacijaPDV`, `SrediTmpPopdvPromet`, `SrediTmp_eeopdv_*`, `SrediTmp_eeppdv_*`, `cre_pregled_eeppdv`, `dopuni_pregled_eeppdv`, `eeopdvspec`, `GetEEPAnalytics`

**FIFO kalkulacija nabavne cene (8 proc.):**
`fifo_calc`, `fifo_calc_prerNC`, `fifoPricePST`, `fifoPricePSTAll`, `PreracunajNC`, `NalogPrerNc`, `NalogPrerNcGK`, `NalogPrerNCRobno`
- FIFO metod za obračun nabavne cene — utiče na vrednost zaliha, razliku u ceni, finansijski promet

**Storniranje (5 proc.):**
`StornirajKnjizenja`, `StornirajKnjizenja3`, `StornirajKnjizenjaNaDan`, `getEvidencijaStorno`, `KreirajTabeleZaStorno`

**Prenos u novu godinu (3 proc.):**
`OtvaranjeNoveGodine`, `PrenosSifarnika`, `myprenos1`

**Statistike (8 proc.):**
`stats4art`, `stats4artgraph`, `stats4part`, `stats4partgraph`, `stats4kont`, `stats4kontgraph`, `statskart`, `GetEEPAnalytics`

**Cenovnici i akcije (6 proc.):**
`AktuelizujCenovnik`, `BojiAkcije`, `CheckAkcije`, `checkvpcenovnik`, `lastRabatI`, `lastRabatU`

**Provere i validacije (10 proc.):**
`ProveraIntegriteta`, `ProveraStatusa`, `checkForeignKeys`, `checkdokpary`, `CheckLDRN`, `CheckPrometPoSifri`, `CheckTabRnPog`, `CheckTabRnPogAMT`, `DaLiJeUAvansuOPP`, `AutCheckMinzal`

**Knjiženje (3 proc.):**
`sefknjizenjanew`, `sefknjizenjaold`, `oznakasef`

**Obračuni (4 proc.):**
`obracunPotvrdjeno`, `obracunRazlikeUCeni`, `racunajKolicine`, `RekapitulacijaPDV`

**Popis i zalihe (4 proc.):**
`kreirajPopis`, `starostzaliha`, `xtrstanje`, `xtrstanjesql`

**Pomoćne (14 proc.):**
`KreirajTmpTabele`, `pripremitabele`, `create_tmp_tmp_rek`, `CreTmpSerbr`, `cre_tmp_pojedinacna`, `eo_fix_auto_increment`, `PrepareZaSveArtikle`, `puniTmpZbirnu`, `punitmpzbirnusimulacija`, `SrediAmortizaciju`, `SrediSpecSerbr`, `SrediTmpFinprom`, `SrediTmpRobno`, `SrediTmpTrgovacka`

**Ostalo:**
`trigoperdoc`/`trigoperdocx` (upravljanje operdoc trigerima), `FormirajVeznu`, `GetNabCena`, `GetNextBrNal`, `ios` (izvod otvorenih stavki), `KnjiziTransformaciju`, `bsnotif`, `dajmidokumente`, `DeleteInvoiceRecords`, `prenesiSveArtikle`, `ProvRezervacije`, `RezNarTrb`, `automatskoHelper`, itd.

---

## 5. Trigeri — pregled

### 5.1 Statistika

- **opp:** 0 trigera
- **opp7102025:** 265 trigera na 91 tabeli

### 5.2 Operdoc sistem (231 od 265 trigera)

**Obrazac:** `operdoc_{ins|upd|del}_{tabela}`

Svaka transakciona tabela ima INSERT/UPDATE/DELETE trigere koji automatski upisuju/ažuriraju/brišu zapise u centralnu tabelu `operdoc` (operativni dokumenti). Ovo omogućava:
- **Jedinstven pregled** svih dokumenata u sistemu na jednom mestu
- **Praćenje statusa** dokumenata
- **Navigaciju** između povezanih dokumenata

**82 tabele** imaju operdoc trigere, uključujući sve ključne: `fakture`, `kalkulacije`, `nivelacije`, `blgpromet`, `finprom`, `intracun`, `kasa`, `popis`, `radnal`, `putninalog`, svi `tbl*` dokumenti, svi `frmgk_*` formulari.

### 5.3 Sistem zaključavanja — zak_* trigeri

Trigeri `zak_ins_*`, `zak_upd_*`, `zak_del_*` sprečavaju izmenu podataka u zaključanim periodima.

**Kontrolisane tabele:**

| Tabela | Šta štiti |
|--------|----------|
| `finprom` | Finansijski promet (glavna knjiga) |
| `robno` | Robno-materijalno knjiženje |
| `trgovacka` | Trgovačka knjiga |
| `popdv_promet` | PDV promet |
| `pk1` | PK-1 knjiga |

**Mehanizam:** Trigeri čitaju tabelu `zakljucano` i blokiraju INSERT/UPDATE/DELETE ako je period zaključan.

### 5.4 Specifični trigeri na transakcione tabele

| Tabela | Triger | Šta radi |
|--------|--------|----------|
| `artikli` | `updartikli` | AFTER UPDATE — propagira promene šifarnika |
| `fakture` | `updfakture` | AFTER UPDATE — ažurira vezane tabele |
| `kasa` | `delkasa`, `inskasa`, `updkasa` | Sinhronizacija kase sa robnim |
| `robno` | `insstanje`, `updstanje`, `delstanje` | **KRITIČNI** — čitaju `opp.zirklista` za preračun u strane valute! |
| `osamvr` | `delosamvr`, `insosamvr`, `updosamvr` | Osnovna sredstva - amortizacija |
| `osnabvr` | `delosnabvr`, `insosnabvr`, `updosnabvr` | OS - nabavna vrednost |
| `osotpis` | `delosotpis`, `insosotpis`, `updosotpis` | OS - otpis |

### 5.5 Real-time zavisnost trigera od opp baze

**KRITIČNO:** Trigeri `insstanje` i `updstanje` na tabeli `robno` čitaju `opp.zirklista` pri SVAKOM unosu/izmeni robnog knjiženja za preračun cena u EUR, USD, CHF. Ako opp baza nije dostupna, robno knjiženje neće moći da izračuna kurseve.

---

## 6. Implicitne relacije

### 6.1 Zašto nema FK

BizniSoft ne koristi eksplicitne foreign key constraints. Razlozi:
- Performanse (manje overhead pri INSERT/UPDATE/DELETE)
- Cross-database reference (opp ↔ oppXXXYYYY)
- Fleksibilnost za bulk operacije i migracije
- Legacy dizajn

### 6.2 Neuniformni nazivi kolona — KRITIČNO

Isti entitet se referencira **različitim imenima kolona** u različitim tabelama:

| Entitet | Mogući nazivi kolone | Master tabela.polje |
|---------|---------------------|---------------------|
| **Partner/kupac** | `sifkup`, `sifpar`, `partner`, `posp`, `kupac`, `sifra` | `kupci.sifra` |
| **Objekat/lokacija** | `sifobj`, `objekat`, `lokacija` | `objekti.sifra` / `sifobj.sifra` |
| **Artikal** | `sifra`, `sifart`, `artikal` | `artikli.sifra` |
| **Konto** | `racun`, `konto`, `kontod`, `kontop` | `kontniplan.konto` / `tabrac.konto` |
| **Dokument** | `brnal`, `brdok`, `brnalorig`, `biznisoftbrnal` | Interni sekvencijalni |
| **Operater** | `user`, `operater`, `korime` | `operateri.korime` |
| **Tarifa** | `tarifa` | `tarife.tarifa` |

### 6.3 Ključne implicitne relacije (potvrđene iz koda)

| Polje izvora | Koristi se u tabelama | Tip veze |
|-------------|----------------------|----------|
| `artikli.sifra` | `robno`, `trgovacka`, `kasa`, `fakture`, `kalkulacije`, `cenovnik`, `serbr`, `trstanje` | 1:N |
| `kupci.sifra` | `fakture`, `finprom`, `avracuni`, `tblodobkup`, narudžbine | 1:N |
| `objekti.objekat` | `robno`, `trgovacka`, `kasa`, `pazari`, `kalkulacije`, `nivelacije`, `trstanje` | 1:N |
| `kontniplan.konto` | `finprom`, `tr_finprom`, `specifikacijanaloga`, `defkontopart` | 1:N |
| `operateri.user` | Sve transakcije (audit trail) | 1:N |
| `tarife.tarifa` | `artikli`, `fakture`, `kalkulacije` | 1:N |

### 6.4 Konvencije imenovanja tabela

| Prefiks | Značenje | Primer |
|---------|----------|--------|
| `tbl*` | Transakcione tabele (dokumenti) | `tblfakture`, `tblpovracaj` |
| `frmgk_*` | Formulari za GK knjiženje | `frmgk_faktura`, `frmgk_avans` |
| `ld*` | Lični dohodak (obračun zarada) | `ld110`, `ldugozar` |
| `puk_*` | HR/kadrovska evidencija | `puk_zaposleni` |
| `hot_*` | Hotelski modul | `hot_rezervacije` |
| `os*` | Osnovna sredstva | `osregos`, `osamvr` |
| `sif*` | Šifarnici | `sifobj`, `sifodeljenja` |
| `pos*` / `kasa*` | POS/kasa operacije | `posakcije`, `kasaarhiva` |
| `blg*` | Blagajna | `blgpromet` |
| `cgf_*` | Računovodstveni okvir | `cgf_kupac` |
| `dt_*` | Duvanski promet / Servis | `dt_srv_rn` |
| `eo_*` | E-otpremnice | `eo_otpremnice` |
| `rfzo_*` | RFZO (zdravstveno) | `rfzo_fakture` |
| `my_*` | Custom/pomoćne tabele | `my_eeopdv` |
| `arh_*` | Arhiviranje | `arh_book` |
| `per_*` | Periodični obračuni | `per_stavke` |
| `jp_*` | JP obrasci (javna preduzeća) | `jp_ld110` |

### 6.5 Pravila za JOIN-ove

1. **Uvek proveri tip podatka** — `int` vs `varchar` (isti entitet, različit tip u raznim tabelama)
2. **Filtriraj NULL i prazne stringove** pre JOIN-a
3. **`0` vrednost** često znači "nije postavljeno", a ne FK ka zapisu sa ID=0
4. **Godina** je često deo kompozitnog ključa (`brnal` + `godina` + `objekat`)
5. **Verifikuj poklapanje:** >90% match = potvrđena veza, <50% = verovatno NIJE veza

---

## 7. Storno logika

### 7.1 Princip

Storniranje = **poništavanje dokumenta bez brisanja**. Kreira se novi zapis sa negativnim iznosima. Zakonski zahtev u računovodstvu — knjiženja se ne smeju brisati.

### 7.2 Obrazac sufiksa

```
KL003-00026      +1.809.068   Original
KL003-00026/1    -1.809.068   Storno (poništava original)
KL003-00026/2    +1.809.068   Re-knjiženje (ispravljen)
KL003-00026/3    -1.809.068   Storno re-knjiženja
KL003-00026/4    +1.809.068   Novo re-knjiženje
...
```

**Pravilo:** Neparni sufiksi (/1, /3, /5) = storno (negativni iznosi), Parni (/2, /4, /6) = re-knjiženje (pozitivni iznosi).

### 7.3 Mehanizam storno procedure

1. Kopira zapise iz originalne tabele u temp tabelu
2. Modifikuje kopije: dodaje sufiks, množi iznose sa -1, postavlja `stornirano=1`
3. Označava originale kao stornirane
4. Insertuje storno zapise nazad u originalnu tabelu
5. Beleži u `storniranja` tabelu (16,521 zapisa u opp7102025)

### 7.4 Propagacija storna kroz tabele

Storno pogađa **više tabela istovremeno:**
- `robno` — robno-materijalno knjiženje
- `finprom` — finansijske promene (glavna knjiga)
- `trgovacka` — trgovačka knjiga
- PDV evidencija
- Log knjiženja
- Serijski brojevi

### 7.5 Procedure za storniranje

| Procedura | Opis |
|-----------|------|
| `StornirajKnjizenja` | Osnovna storno procedura |
| `StornirajKnjizenja3` | Varijanta 3 (drugačije ponašanje) |
| `StornirajKnjizenjaNaDan` | Stornira na specifičan datum |
| `getEvidencijaStorno` | Vraća podatke za storno evidencije |
| `KreirajTabeleZaStorno` | Kreira pomoćne tabele za storno proces |

### 7.6 Distribucija storniranja (opp7102025)

| Broj storniranja | Broj naloga | Komentar |
|-----------------|-------------|----------|
| 1× | ~11,174 | Najčešći slučaj |
| 2× | ~1,748 | Storniran pa ponovo proknjižen pa opet |
| 3× | ~426 | Tri ciklusa ispravki |
| 4+ | ~48 | Retko (do 7× u praksi) |

### 7.7 Zamke

- Kolona `stornirano` **NIJE uvek pouzdana** — može imati različito značenje
- **Satelitski nalozi** (razlika u ceni, ispravke) mogu imati storno sufikse ali se NE loguju u `storniranja`
- Tabela `veze` čuva relacije između re-proknjiženih naloga
- Zbir originalnog + storno mora biti = 0 za proveru konzistentnosti

---

## 8. Zavisnosti opp ↔ oppXXXYYYY

### 8.1 Smer zavisnosti

**JEDNOSMERNO:** `opp7102025` → čita iz → `opp`
- Nema obrnutih referenci (opp NE referencira opp7102025)
- Nema foreign key-eva između baza (veze su na nivou koda)

### 8.2 Direktne reference iz PROCEDURA (15 procedura)

| opp tabela | Procedure koje je čitaju | Šta čitaju |
|------------|------------------------|------------|
| **`documents`** | `checkdokpary`, `checkForeignKeys`, `CheckPrometPoSifri`, `dajmidokumente`, `getEvidencijaStorno`, `GetNabCena`, `obracunPotvrdjeno`, `ProveraIntegriteta`, `sefknjizenjanew`, `sefknjizenjaold`, `trigoperdoc`, `trigoperdocx` (**12 proc**) | Tipove dok., mapiranje na tabele |
| **`rnpartnkli`** | `AzurRnPartKli` | Registar partnera |
| **`bsnotif`** | `bsnotif` | Notifikacije |
| **`datkl`** | `checkvpcenovnik` | Datumske kurseve |
| **`zirklista`** | `checkvpcenovnik` | Zvanične kurseve |
| **`tabakciza`** | `getakciza` | Akcizne stope |
| **`arh_locations`** | `GetArchiveParentUID` | Lokacije arhive |
| **`kplprevod`** | `GetKplPrevod`, `GetKplPrevodRacun` | Prevod kontnog plana |
| **`pdvstope`** | `getpdv` | PDV stope |
| **`sifobj`** | `obracunPotvrdjeno` | Šifarnik objekata |

### 8.3 Direktne reference iz TRIGERA (2 trigera)

| opp tabela | Triger | Na tabeli | Šta čita |
|------------|--------|-----------|----------|
| **`zirklista`** | `insstanje` | `robno` | EUR, USD, CHF kurs za datum transakcije |
| **`zirklista`** | `updstanje` | `robno` | EUR, USD, CHF kurs za datum transakcije |

⚠️ **Kritičan uvid:** Svaki INSERT/UPDATE na `robno` (188,619 redova) automatski čita kursnu listu iz opp baze!

### 8.4 TIER model zavisnosti

```
TIER 1: Kritične (SQL reference) — opp MORA biti dostupan
  documents (12 proc), zirklista (2 trig + 1 proc), rnpartnkli,
  datkl, pdvstope, kplprevod, sifobj

TIER 2: Aplikativne (Delphi klijent čita) — potrebne za UI
  operateri, ovlpofirmama, ovlpoizvest, drzave, opstine,
  sifval, sifplac, cnfg_*, pdvstopelabele...

TIER 3: Interne/log — nema direktnu vezu
  logfile, bcklog, arh_log, favorites, scheduler, fiz_*
```

### 8.5 Zajedničke tabele (15 tabela postoje u obe baze)

| Tabela | opp | opp7102025 | Status |
|--------|-----|-----------|--------|
| `build` | 1 | 1 | ✅ Sinhronizovano |
| `kontniplan` | 17,003 | 17,077 | ⚠️ opp7 ima +74 konta (firmski specifična) |
| `tabrac` | 426 | 1,148 | ⚠️ opp7 ima +722 (korisnički dodati) |
| `ld220` | 35 | 35 | ✅ Sinhronizovano |
| `ldvp_opj1` | 14 | 14 | ✅ Sinhronizovano |
| `mybsliveid` | 1 | 1 | ✅ Sinhronizovano |
| `operateri` | 134 | 0 | Master u opp |
| `sifobj` | 19 | 0 | Master u opp |

### 8.6 Šifarnici koji se čitaju SAMO na aplikativnom nivou

Ove tabele se ne vide u SQL kodu procedura/trigera, ali ih Delphi klijent verovatno čita:

`drzave` (252), `opstine` (207), `pbrmesto` (1,525), `ptt_brojevi` (1,994), `sifval` (37), `sifzanimanja` (2,963), `sifplac` (200), `oskateg`/`osamgzag`/`osamgdet`, `operateri` (134), `ovlpofirmama` (66,486), `ovlpoizvest` (46,552), `cnfg_*` (~3,476)

---

## 9. Pravila integriteta

### 9.1 Statusna polja dokumenata

| Vrednost | Status | Značenje |
|----------|--------|----------|
| 1 | U obradi | Dokument se može menjati |
| 2 | Potvrđen/Konfirmisan | Spreman za knjiženje, ne može se menjati |
| 9 | Proknjižen | Završen, utiče na izveštaje |
| stornirano=1 | Storniran | Poništen, ne utiče na izveštaje |

**Tok:** U obradi (1) → Potvrđen (2) → Proknjižen (9)
**Storno:** Proknjižen → Storniran (vraća u obradu sa negativnim iznosima)

### 9.2 Kritične provere integriteta

**Finansijsko:**
- Saldo naloga MORA biti 0 (duguje = potražuje za svaki nalog)
- `finprom`: proveriti `SUM(duguje) = SUM(potrazuje)` po nalogu

**Robno:**
- Ulaz − Izlaz = Stanje na kartici
- `robno`: proveriti konzistentnost sa `trstanje`
- Negativne zalihe — ne smeju postojati (osim specifičnih slučajeva)

**Kalkulacije:**
- Nabavna + Marža = Prodajna cena
- PDV obračun konzistentan sa `pdvstope`

**Popis:**
- Popisno stanje vs. knjigovodstveno stanje = Višak/Manjak

### 9.3 Provere za šifarnike

| Provera | SQL obrazac |
|---------|-------------|
| Orphan records | Stavke bez zaglavlja: `WHERE brnal NOT IN (SELECT brnal FROM zaglavlje)` |
| Duplikati | `GROUP BY sifra HAVING COUNT(*) > 1` |
| Neaktivni u transakcijama | Partneri/artikli koji se ne koriste |
| PIB validacija | Mod 97-10 (`mod_97_10_check` funkcija u opp) |
| Konzistentnost datuma | Faktura ne sme biti pre kalkulacije |

### 9.4 Ključna polja za povezivanje i validaciju

| Entitet | Polje | Povezuje | Tip |
|---------|-------|---------|-----|
| Partner | `sifra` u `kupci` | Fakture, kalkulacije, IOS, avansni | INT |
| Artikal | `sifra` u `artikli` | Stavke dokumenata, recepture, zalihe | INT/VARCHAR |
| Konto | `konto` u `kontniplan` | Nalozi za GK, specifikacije | VARCHAR |
| Objekat | `objekat`/`sifobj` | Robno, zalihe, kasa | INT |
| Radnik | Šifra radnika | Zarade, kadrovi | INT |
| Dokument | `brnal` + `godina` + `objekat` | Stavke, knjiženja | Kompozitni |

### 9.5 Zaključavanje perioda

Tabela `zakljucano` kontroliše koji periodi su zaključani. Trigeri (`zak_*`) blokiraju izmene u zaključanim periodima za:
- `finprom`, `robno`, `trgovacka`, `popdv_promet`, `pk1`

### 9.6 Procedura ProveraIntegriteta

Centralna procedura za proveru integriteta u transakcionoj bazi. Poziva se iz opp baze (`AutCheckInt`). Proverava:
- Saldo naloga u `finprom`
- Konzistentnost robnog i finansijskog
- Status dokumenata
- Šifarničke reference

### 9.7 Vremenske dimenzije — ključne za izveštaje

| Polje | Gde se koristi | Značenje |
|-------|---------------|----------|
| `godina` | Deo kompozitnog ključa | Poslovna godina |
| `period` | `finprom`, `robno` | Mesec za izveštaje (1-12) |
| `datum` | Svi dokumenti | Datum dokumenta |
| `datumknj` | `finprom`, `robno` | Datum knjiženja — kad stavka ulazi u izveštaje |

---

## Dodatak A: Top 30 tabela po broju redova (opp7102025)

| # | Tabela | Redova | Kategorija |
|---|--------|--------|------------|
| 1 | `finprom` | 197,012 | Finansije (dnevnik knjiženja) |
| 2 | `robno` | 188,619 | Robno poslovanje |
| 3 | `logknjizenja` | 125,600 | Log |
| 4 | `trgovacka` | 77,280 | Robno (trgovačka knjiga) |
| 5 | `logpotvrdi` | 47,634 | Log |
| 6 | `mylogpreuzmi` | 38,578 | Log |
| 7 | `logefakture` | 17,760 | E-fakture log |
| 8 | `intracun` | 17,715 | Interni prenosi |
| 9 | `kontniplan` | 16,711 | Kontni plan |
| 10 | `storniranja` | 16,521 | Storno evidencija |
| 11 | `popdv_promet` | 16,162 | PDV |
| 12 | `pospracuni` | 8,095 | POS |
| 13 | `fakture` | 5,644 | Fakturisanje |
| 14 | `radnal` | 5,290 | Radni nalozi |
| 15 | `kupci` | 2,324 | Šifarnik partnera |

## Dodatak B: Brza referenca — najčešći upiti

```sql
-- Svi aktivni dokumenti tipa faktura
SELECT * FROM fakture WHERE stornirano = 0;

-- Stanje artikla po objektima
SELECT sifra, objekat, SUM(kolicina) as stanje
FROM robno GROUP BY sifra, objekat;

-- Promet po partneru (finprom)
SELECT sifkup, SUM(duguje) as dug, SUM(potrazuje) as pot
FROM finprom GROUP BY sifkup;

-- Provera salda naloga
SELECT brnal, SUM(duguje) - SUM(potrazuje) as saldo
FROM finprom GROUP BY brnal HAVING ABS(saldo) > 0.01;

-- Tip dokumenta → fizička tabela
SELECT sifra, naziv, tabela, tipkljuca
FROM opp.documents ORDER BY tipkljuca, sifra;

-- Kursna lista za datum
SELECT * FROM opp.zirklista;
SELECT * FROM opp.datkl WHERE datum = CURDATE();

-- Storno parovi
SELECT brnalorig, brnalnovi FROM storniranja;
```

## Dodatak C: Dijagram arhitekture

```
╔══════════════════════════════════════════════════════════════╗
║                     opp (MASTER BAZA)                       ║
║  195 tabela │ 11 procedura │ 0 trigera                      ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  documents(95) ─── Definicije svih tipova dokumenata        ║
║  matpod(674) ───── Matični podaci firmi                     ║
║  operateri(134) ── Korisnici/login                          ║
║  tabrac/kplvezna ─ Kontni plan + auto-knjiženje             ║
║  pdvstope(9) ───── PDV stope                                ║
║  sifval/drzave ─── Geografija + valute                      ║
║  zirklista ──────── Kursna lista (REAL-TIME zavisnost!)     ║
║  datkl(138K) ───── Istorijski kursevi                       ║
║  rnpartnkli(167K)─ Registar partnera (sve firme)            ║
║  cnfg_*(3.4K) ──── Konfiguracija                            ║
║                                                              ║
╚═══════════════╦══════════════════════════════════════════════╝
                ║ 15 procedura + 2 trigera čitaju opp
                ▼
╔══════════════════════════════════════════════════════════════╗
║              opp7102025 (TRANSAKCIONA BAZA)                  ║
║  643 tabele │ 105 procedura │ 265 trigera                   ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  ┌─ ROBNO ──────────────── FINANSIJE ──────── PLATE ──────┐ ║
║  │ robno(188K)              finprom(197K)      ldobracun   │ ║
║  │ trgovacka(77K)           kontniplan(17K)    ldugozar    │ ║
║  │ fakture(5.6K)            tr_finprom         ld110-410   │ ║
║  │ kalkulacije              virmani            ldgknalog   │ ║
║  │ kasa(POS)                specifikacija                  │ ║
║  │ artikli, kupci           defkontopart                   │ ║
║  │ trstanje                 zakljucano                     │ ║
║  ├─ PDV ────────── OS ──────── HOTEL ──── PROIZVODNJA ────┤ ║
║  │ popdv_promet    osregos      hot_*       radnal         │ ║
║  │ eeopdv_*        osamvr       hot_gosti   receptura     │ ║
║  │ eeppdv_*        osnabvr                  tblrobtransf  │ ║
║  └─ OPERDOC (centralni registar svih dokumenata) ─────────┘ ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## Dodatak D: Parsiranje MySQL dump-ova

Za ekstrakciju strukture iz `.sql` dump fajlova:

- **Encoding:** Uvek `utf-8` sa `errors='replace'`
- **CREATE TABLE:** Regex `r"CREATE TABLE\s+\`(\w+)\`"`
- **Kolone:** `r'^`(\w+)`\s+(.+?)(?:,\s*)?$'`
- **PRIMARY KEY:** `r'^\s*PRIMARY KEY\s*\(([^)]+)\)'`
- **Kraj bloka:** Linija počinje sa `)` i sadrži `ENGINE` ili `;`
- **DELIMITER $$** menja separator za procedure/trigere
- Korisno: `grep -c 'CREATE TABLE' dump.sql` za brzi pregled

---

**Kraj dokumenta. Verzija 1.0 — 2026-03-29**
