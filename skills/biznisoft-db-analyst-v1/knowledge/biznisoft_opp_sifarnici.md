# Biznisoft OPP - Šifarnici i definicije

**Baza:** opp (globalna/master baza sa šifarnicima i definicijama)
**Datum ekstrakcije:** 2026-03-29

---

## Sadržaj

- [`sifostdokum`](#tabela-sifostdokum) - Šifarnik ostalih dokumenata
- [`documents`](#tabela-documents) - Definicije dokumenata
- [`pdvstope`](#tabela-pdvstope) - PDV stope
- [`pdvstopelabele`](#tabela-pdvstopelabele) - PDV stope - labele
- [`sifval`](#tabela-sifval) - Šifarnik valuta
- [`drzave`](#tabela-drzave) - Šifarnik država
- [`opstine`](#tabela-opstine) - Šifarnik opština
- [`cnfg_klasifikacija`](#tabela-cnfg_klasifikacija) - Konfiguracija - klasifikacija
- [`cnfg_vrste`](#tabela-cnfg_vrste) - Konfiguracija - vrste
- [`finiz_vp`](#tabela-finiz_vp) - Finansijski izveštaji - vrste
- [`fiz_vrste`](#tabela-fiz_vrste) - Finansijski izveštaji - vrste (2)
- [`fiz_celine`](#tabela-fiz_celine) - Finansijski izveštaji - celine
- [`sifobj`](#tabela-sifobj) - Šifarnik objekata
- [`sifplac`](#tabela-sifplac) - Šifarnik plaćanja
- [`sifpla2konta`](#tabela-sifpla2konta) - Veza plaćanja - konta
- [`arh_enttypes`](#tabela-arh_enttypes) - Arhiva - tipovi entiteta
- [`oskateg`](#tabela-oskateg) - Osnovna sredstva - kategorije
- [`osporgrupe`](#tabela-osporgrupe) - OS poreske grupe
- [`osporpodgr`](#tabela-osporpodgr) - OS poreske podgrupe
- [`tabrac`](#tabela-tabrac) - Tabela računa (kontni plan) - prvih 50
- [`kplvezna`](#tabela-kplvezna) - Kontni plan - vezna tabela - prvih 50
- [`matpod`](#tabela-matpod) - Matični podaci firmi (sifra, naziv, pib)
- [`matpodracuni`](#tabela-matpodracuni) - Matični podaci - računi
- [`nazmes`](#tabela-nazmes) - Nazivi meseci
- [`propisani_parametri`](#tabela-propisani_parametri) - Propisani parametri
- [`stope`](#tabela-stope) - Poreske stope
- [`propsifban`](#tabela-propsifban) - Propisane šifre banaka
- [`tr_pravila`](#tabela-tr_pravila) - Pravila za transakcije
- [`tr_pravila_stavke`](#tabela-tr_pravila_stavke) - Stavke pravila
- [`ldkategpok`](#tabela-ldkategpok) - LD kategorije pokrivanja
- [`ldkategzap`](#tabela-ldkategzap) - LD kategorije zaposlenih
- [`ldkategugod`](#tabela-ldkategugod) - LD kategorije ugovora
- [`cnfg_parametri`](#tabela-cnfg_parametri) - Konfiguracioni parametri - prvih 50

---

## Tabela: `sifostdokum`
**Opis:** Šifarnik ostalih dokumenata
**Redova:** 9

**Kolone:** `sifra`, `opis`

| sifra | opis |
| --- | --- |
| 1 | UGOVOR |
| 2 | ANEKS UGOVORA |
| 3 | FAKTURA |
| 4 | PONUDA |
| 5 | PROFAKTURA |
| 6 | REŠENJE |
| 7 | IZVOD BANKE |
| 8 | OSTALO |
| 10 | POTPISANA BS DOKUMENTA |

---

## Tabela: `documents`
**Opis:** Definicije dokumenata
**Redova:** 95

**Kolone:** `sifra`, `naziv`, `tabela`, `tipkljuca`, `tipdokfakt`, `veza`, `forma`, `stampa`, `statistika`, `statkoef`, `izlaznidokument`, `stampaneprok`, `numtipdok`, `jefaktura`

| sifra | naziv | tabela | tipkljuca | tipdokfakt | veza | forma | stampa | statistika | statkoef | izlaznidokument | stampaneprok | numtipdok | jefaktura |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AA | INTERNI PRENOS AMBALAŽE | tblambintpr | 3 | NULL | 1 | fambintpr | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| AJ | PRIJEM AMBALAŽE OD DOBAVLJAČA | tblamprijdob | 2 | F | 1 | famprijdob | button1click | 1 | 1.00 | 0 | 1 | 11 | 0 |
| AM | IZDAVANJE AMBALAŽE | tblamizdkup | 2 | F | 1 | famizdkup | button1click | 1 | 1.00 | 1 | 1 | 8 | 0 |
| AP | POVRAĆAJ AMBALAŽE OD KUPCA | tblampovkup | 2 | F | 1 | fampovkup | button1click | 1 | 1.00 | 0 | 1 | 10 | 0 |
| AR | FIN.TRANSAKCIJE - PRIJEM AVANSNOG RAČUNA | frmgk_avans | 13 | NULL | 1 | ffintrans | cxButton2Click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| AV | POVRAĆAJ AMBALAŽE DOBAVLJAČU | tblampovdob | 2 | F | 1 | fampovdob | button1click | 1 | 1.00 | 1 | 1 | 9 | 0 |
| BL | BLAGAJNIČKO POSLOVANJE | blgpromet | 9 | NULL | 1 | fblgpromet | cxbutton1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| CR | FIN.TRANSAKCIJE - PRIJEM CARINSKOG RAČUNA | frmgk_carina | 13 | NULL | 1 | ffintrans | cxButton2Click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| DD | POVRAĆAJ DOBAVLJAČU IZ D.O. | prodpovracajdob | 1 | NULL | 1 | fprodpovracajdob | button1click | 1 | 1.00 | 1 | 1 | 0 | 0 |
| DF | FAKTURE IZ DISLOCIRANIH OBJEKATA | tblprodfakture | 2 | F | 1 | fprodfaktura | button1click | 1 | 1.00 | 1 | 1 | 30 | 1 |
| DK | KALKULACIJA IZ D.O. | prodkalkulacije | 1 | NULL | 1 | fprodkalkulacije | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| DN | NIVELACIJA IZ D.O. | prodnivelacije | 4 | NULL | 1 | fprodniv | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| DP | PRIJEM ROBE SA OBRADE/DORADE | tblrobobrdorprij | 1 | NULL | 1 | frobobrdorprij | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| ED | FIN.TRANSAKCIJE - ELEKTRONSKE DOPUNE | frmgk_ed | 13 | NULL | 1 | ffintrans | cxButton2Click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| FA | FAKTURA SA AKCIJSKIM RABATOM | tblfaktakcrab | 2 | F | 1 | ffaktakcrab | button1click | 1 | 1.00 | 1 | 1 | 12 | 1 |
| FK | FIN.TRANSAKCIJE - IZLAZNA FAKTURA | frmgk_faktura | 13 | NULL | 1 | ffintrans | cxButton2Click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| FM | PRODAJA REPROMATERIJALA | tblprodmat | 2 | F | 1 | fprodmat | button1click | 1 | 1.00 | 1 | 1 | 31 | 0 |
| FS | IZLAZNA FAKTURA / RAČUN ZA OS | faktureos | 2 | F | 1 | ffakturaos | button1click | 1 | 1.00 | 1 | 1 | 44 | 1 |
| GN | GRUPNI RADNI NALOG | radnal | 10 | NULL | 1 | fnalrad | button1click | 0 | 1.00 | 0 | 1 | 0 | 0 |
| GP | PRODAJA GOTOVIH PROIZVODA (POGONSKO) | tblprodajagp | 2 | F | 1 | fprodajagp | button1click | 1 | 1.00 | 0 | 1 | 28 | 0 |
| II | INTERNO IZDAVANJE ROBE | tblintizdavanje | 3 | NULL | 1 | fintizdavanje | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| IN | PUTNI NALOG U INOSTRANSTVU | putninalog | 15 | NULL | 1 | fputninalog | OBRAUNPOIZVRENOMNALOGU1Click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| IP | INTERNI PRIJEM ROBE | intprijem | 1 | NULL | 1 | fintprijem | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| IR | INTERNI PRENOS DOBARA | intracun | 3 | NULL | 1 | fintracun | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| KA | KASA U MALOPRODAJI | kasa | 6 | NULL | 1 | fnakstrn | cxbutton1click | 0 | 1.00 | 0 | 1 | 7 | 1 |
| KF | IZDAVANJE FAKTURE KOMISIONARU | tblkomfakture | 2 | F | 1 | fkomfaktura | Button1Click | 1 | 1.00 | 0 | 1 | 42 | 1 |
| KI | KALKULACIJA SA NIVELACIJOM | nivkalkulacije | 1 | NULL | 1 | fnivkalkulacije | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| KK | KALKULACIJA KOMISIONE ROBE | tblkomkalk | 1 | NULL | 1 | fkomkalk | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| KL | KALKULACIJA/PRIJEMNICA DOBARA | kalkulacije | 1 | NULL | 1 | fkalkulacije | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| KN | NIVELACIJA KOMISIONE ROBE | komnivelacije | 4 | NULL | 1 | fkomnivelacije | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| KO | IZDAVANJE REPROMATERIJALA KOOPERANTU | tblkooizdavanje | 2 | F | 1 | fkooizdavanje | button1click | 1 | 1.00 | 1 | 1 | 18 | 1 |
| KV | VRAĆANJE KOMISIONE ROBE | tblkomvrac | 1 | NULL | 1 | fkomvrac | button1click | 1 | 1.00 | 1 | 1 | 0 | 0 |
| LL | ISPLATA POLJOPRIVREDNOM PROIZVOĐAČU | tblisplata | 11 | NULL | 1 | fisplata | cxbutton1click | 1 | 1.00 | 1 | 1 | 0 | 0 |
| MO | SLANJE MATERIJALA NA OBRADU/DORADU | tblmatobrdor | 2 | F | 1 | fmatobrdor | button1click | 1 | 1.00 | 1 | 1 | 19 | 0 |
| MP | PRIJEM MATERIJALA SA OBRADE/DORADE | tblmatobrdorprij | 1 | NULL | 1 | fmatobrdorprij | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| NA | NALOG ZA IZDAVANJE SA AKCIJSKIM RABATOM | tblfaktakcrab | 2 | I | 1 | FaktAkcRabNal | 1 | 1 | 1.00 | 1 | 1 | 13 | 0 |
| NB | NABAVKA AMBALAŽE | nabambalaze | 1 | NULL | 1 | fnabambalaze | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| NC | NIVELACIJA CENE | nivelacije | 4 | NULL | 1 | fnivelacije | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| ND | NARUDŽBINE DOBAVLJAČIMA | tblnardobavljacima | 1 | NULL | 1 | fnardobavljacima | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| NI | NALOG ZA IZDAVANJE | fakture | 2 | I | 1 | NalogZaIzdavanje | button1click | 1 | 1.00 | 0 | 1 | 3 | 0 |
| NK | NARUDŽBINE KUPACA | tblnarkupaca | 2 | F | 1 | fnarkupaca | button1click | 1 | 1.00 | 0 | 1 | 20 | 0 |
| NO | NALOG ZA POVRAĆAJ ROBE KUPCA | tblpovracaj | 2 | O | 1 | PovracajNalog | button1click | 1 | 1.00 | 0 | 1 | 26 | 0 |
| NP | POVRAĆAJ ROBE DOBAVLJAČU - NOVI PROMET | tblpovracajdobnovi | 2 | F | 1 | fpovracajdobnovi | button1click | 1 | 1.00 | 1 | 1 | 43 | 1 |
| NR | FIN.TRANSAKCIJE - FAKTURA NEFAKTURISANE ROBE | frmgk_nefak | 13 | NULL | 1 | ffintrans | cxButton2Click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| OA | OTPREMNICA SA AKCIJSKIM RABATOM | tblfaktakcrab | 2 | O | 1 | FaktAkcRabOtp | button1click | 1 | 1.00 | 1 | 1 | 34 | 0 |
| OD | PRIJEM ODOBRENJA/ZADUŽENJA DOBAVLJAČA | tblodobdob | 2 | F | 1 | fodobdob | button1click | 1 | 1.00 | 0 | 1 | 21 | 0 |
| OK | KNJIŽNO ODOBRENJE | tblodobkup | 2 | F | 1 | fodobkup | button1click | 1 | 1.00 | 1 | 1 | 22 | 0 |
| ON | OTPIS MIMO ZAKONSKIH STOPA | tblotpisnz | 2 | T | 1 | fotpisnz | button1click | 1 | 1.00 | 0 | 1 | 23 | 0 |
| OS | FIN.TRANSAKCIJE - NABAVKA STALNOG SREDSTVA | frmgk_osnsred | 13 | NULL | 1 | ffintrans | cxButton2Click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| OT | OTPREMNICA | fakture | 2 | O | 1 | Otpremnica | button1click | 1 | 1.00 | 0 | 1 | 4 | 0 |
| OZ | OTPIS PO ZAKONSKIM STOPAMA | tblotpisz | 2 | T | 1 | fotpisz | button1click | 1 | 1.00 | 0 | 1 | 24 | 0 |
| PC | PROMENA CENE | robno | 7 | NULL | 0 | NULL | NULL | 0 | 1.00 | 0 | 1 | 0 | 0 |
| PD | POVRAĆAJ ROBE DOBAVLJAČU | tblpovracajdob | 1 | NULL | 1 | fpovracajdob | button1click | 1 | 1.00 | 1 | 1 | 0 | 0 |
| PF | PROFAKTURA/REZERVACIJA | fakture | 2 | P | 1 | Profaktura | button1click | 1 | 1.00 | 0 | 1 | 5 | 0 |
| PI | INTERNI RAČUN IZ D.O. | prodintracun | 3 | NULL | 1 | fprodintrn | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| PK | POVRAĆAJ ROBE OD KUPCA | tblpovracaj | 2 | F | 1 | fpovracaj | button1click | 1 | 1.00 | 1 | 1 | 27 | 0 |
| PL | VIŠAK/MANJAK PO POPISNOJ LISTI | popis | 5 | NULL | 1 | fpopis | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| PN | PUTNI NALOG U ZEMLJI | putninalog | 15 | NULL | 1 | fputninalog_z | OBRAUNPOIZVRENOMNALOGU1Click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| PO | FAKTURISANJE PO POS OTPREMNICAMA | tblposotpremnice | 2 | F | 1 | fposotpremnice | button1click | 0 | 1.00 | 1 | 1 | 25 | 0 |
| PP | OTKUP POLJOPRIVREDNIH PROIZVODA | tblpoljoprivreda | 1 | NULL | 1 | fpoljoprivreda | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| PR | PREKNJIŽAVANJE PROMETA | nema | 14 | NULL | 0 | fprekprom | nema | 0 | 0.00 | 0 | 1 | 0 | 0 |
| PS | POČETNO STANJE | robno | 7 | NULL | 0 | NULL | NULL | 0 | 1.00 | 0 | 1 | 0 | 0 |
| PZ | DNEVNI PAZARI | pazari | 7 | NULL | 0 | NULL | NULL | 1 | 1.00 | 0 | 1 | 0 | 0 |
| RA | AVANSNI RAČUN | fakture | 2 | A | 1 | AvansniRacun | button1click | 1 | 1.00 | 0 | 1 | 1 | 0 |
| RB | FAKTURISANJE BEZ OBRAČUNA NABAVKE | tblfaktbezobr | 2 | F | 1 | ffaktbezobr | button1click | 1 | 1.00 | 1 | 1 | 14 | 1 |
| RC | KOREKCIJA NABAVNE CENE | nema | 14 | NULL | 0 | fprekprom | nema | 0 | 0.00 | 0 | 1 | 0 | 0 |
| RD | RADNI NALOG | radnal | 10 | NULL | 1 | fnalrad | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| RK | Prijem računa komitenta | frmgk_prijemfakture | 13 | NULL | 1 | ffintrans | cxButton2Click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| RM | PRODAJA AMBALAŽE | tblprodamb | 2 | F | 1 | fprodamb | button1click | 1 | 1.00 | 1 | 1 | 29 | 0 |
| RN | IZLAZNA FAKTURA / RAČUN | fakture | 2 | F | 1 | ffaktura | button1click | 1 | 1.00 | 1 | 1 | 2 | 1 |
| RO | SLANJE ROBE NA OBRADU/DORADU | tblrobobrdor | 2 | F | 1 | frobobrdor | button1click | 1 | 1.00 | 1 | 1 | 33 | 0 |
| RT | RAČUN SOPSTVENIH TROŠKOVA | tblsopsttros | 2 | T | 1 | fSopstveniTroskovi | button1click | 1 | 1.00 | 0 | 1 | 6 | 0 |
| SK | NABAVKA SITNOG INVENTARA | tblnabsitinv | 1 | NULL | 1 | fnabsitinv | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| SN | SERVISNI NALOG | dt_srv_rnpojed | 8 | NULL | 1 | dfsrvpreuzimanje | butprintclick | 0 | 1.00 | 0 | 1 | 0 | 0 |
| SP | POVRAĆAJ SITNOG INVENTARA OS RADNIKA | sitinvpov | 3 | NULL | 1 | fsitinvpov | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| SR | RASHODOVANJE SITNOG INVENTARA | sitinvras | 2 | T | 1 | fsitinvras | button1click | 1 | 1.00 | 0 | 1 | 37 | 0 |
| SU | IZDAVANJE SITNOG INVENTARA U UPOTREBU | tblsitanizd | 3 | NULL | 1 | fsitanizd | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| SZ | ZADUŽENJE SITNOG INVENTARA PO RADNICIMA | sitinvzad | 3 | NULL | 1 | fsitinvzad | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| TB | TREBOVANJE ROBE | tbltrebovanje | 1 | NULL | 1 | ftrebovanje | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| TF | TRANSFORMACIJE ARTIKALA PO RECEPTURI | tblrobtransf | 1 | NULL | 1 | frobtransf | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| TI | IZDAVANJE TUĐE ROBE | tblizdavanje | 2 | F | 1 | fizdavanje | button1click | 1 | 1.00 | 1 | 1 | 15 | 0 |
| TO | PRIJEM TUĐE ROBE | tblotkup | 1 | NULL | 1 | fotkup | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| TR | FIN.TRANSAKCIJE - RAČUN TROŠKOVA | frmgk_troskovi | 13 | NULL | 1 | ffintrans | cxButton2Click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| TS | OTKUP SEKUNDARNIH SIROVINA | tblotkupss | 1 | NULL | 1 | fotkupss | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| UI | IZDAVANJE ROBE NA TUĐE SKLADIŠTE - REVERS | tblreversizdavanje | 2 | F | 1 | freversizdavanje | Button1Click | 1 | 1.00 | 1 | 1 | 36 | 0 |
| UK | UVOZNA KALKULACIJA | tbluvoz | 1 | NULL | 1 | finhuvoz | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| UP | PRIJEM ROBE SA TUĐEG SKLADIŠTA - REVERS | tblreversprijem | 1 | NULL | 1 | freversprijem | Button1Click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| VO | SLANJE PROIZVODA NA OBRADU/DORADU | tblproizvobrdor | 2 | F | 1 | fproizvobrdor | button1click | 1 | 1.00 | 1 | 1 | 32 | 0 |
| VP | PRIJEM PROIZVODA SA OBRADE/DORADE | tblproizvobrdorprij | 1 | NULL | 1 | fproizvobrdorprij | button1click | 1 | 1.00 | 0 | 1 | 0 | 0 |
| ZA | IZVOZ - AVANSNI RAČUN | tblizvoz | 2 | A | 1 | izvAvans | button1click | 1 | 1.00 | 0 | 1 | 38 | 0 |
| ZD | KNJIŽNO ODOBRENJE/ZADUŽENJE INO DOBAVLJAČA | tblodobinodob | 2 | F | 1 | fodobinodob | Button1Click | 1 | 1.00 | 0 | 1 | 40 | 0 |
| ZI | POVRAĆAJ ROBE INO KUPCA | tblpovracajinokup | 2 | F | 1 | fpovracajinokup | Button1Click | 1 | 1.00 | 0 | 1 | 41 | 0 |
| ZO | KNJIŽNO ODOBRENJE/ZADUŽENJE INO KUPCA | tblodobinokup | 2 | F | 1 | fodobinokup | Button1Click | 1 | 1.00 | 1 | 1 | 39 | 0 |
| ZP | IZVOZ - PROFAKTURA U EUR | tblizvoz | 2 | P | 1 | IzvProfaktura | button1click | 1 | 1.00 | 1 | 1 | 16 | 0 |
| ZZ | IZVOZ ROBE I USLUGA | tblizvoz | 2 | F | 1 | fizvoz | button1click | 1 | 1.00 | 1 | 1 | 17 | 1 |

---

## Tabela: `pdvstope`
**Opis:** PDV stope
**Redova:** 9

**Kolone:** `stopa`, `datumod`, `datumdo`, `stopapdv`, `vremeizmene`, `operater`

| stopa | datumod | datumdo | stopapdv | vremeizmene | operater |
| --- | --- | --- | --- | --- | --- |
| B1 | 2014-01-01 | 2030-12-31 | 0.00 | 2023-10-11 06:04:56 | NULL |
| D1 | 2013-01-01 | 2030-12-31 | 15.00 | 2023-10-11 06:04:56 | NULL |
| P1 | 2005-01-01 | 2012-09-30 | 5.00 | 2023-10-11 06:04:56 | NULL |
| P1 | 2012-10-01 | 2030-12-31 | 8.00 | 2023-10-11 06:04:56 | NULL |
| S0 | 2005-01-01 | 2030-12-31 | 0.00 | 2023-10-11 06:04:56 | NULL |
| S1 | 2005-01-01 | 2012-09-30 | 18.00 | 2023-10-11 06:04:56 | NULL |
| S1 | 2012-10-01 | 2030-12-31 | 20.00 | 2023-10-11 06:04:56 | NULL |
| S2 | 2005-01-01 | 2013-12-31 | 8.00 | 2023-10-11 06:04:56 | NULL |
| S2 | 2014-01-01 | 2030-12-31 | 10.00 | 2023-10-11 06:04:56 | NULL |

---

## Tabela: `pdvstopelabele`
**Opis:** PDV stope - labele
**Redova:** 6

**Kolone:** `stopa`, `datumod`, `datumdo`, `labela`

| stopa | datumod | datumdo | labela |
| --- | --- | --- | --- |
| B1 | 2014-01-01 | 2030-12-31 | Г |
| S0 | 2005-01-01 | 2030-12-31 | А |
| S1 | 2005-01-01 | 2012-09-30 | Ђ |
| S1 | 2012-10-01 | 2030-12-31 | Ђ |
| S2 | 2005-01-01 | 2013-12-31 | Е |
| S2 | 2014-01-01 | 2030-12-31 | Е |

---

## Tabela: `sifval`
**Opis:** Šifarnik valuta
**Redova:** 37

**Kolone:** `sifval`, `oznval`, `nazval`, `nazzem`, `na_kl`, `datcre`, `operater`, `ts`

| sifval | oznval | nazval | nazzem | na_kl | datcre | operater | ts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 36 | AUD | AUSTRALIJSKI DOLAR | AUSTRALIJA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 40 | ATS | ŠILING | AUSTRIJA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 56 | BEF | BELGIJSKI FRANAK | BELGIJA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 124 | CAD | KANADSKI DOLAR | KANADA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 156 | CNY | JUAN | KINA | D | 2021-08-06 | BIZNISOFT | 2025-04-03 17:12:07 |
| 191 | HRK | HRVATSKA KUNA | HRVATSKA | D | 2021-08-06 | BIZNISOFT | 2025-04-03 17:12:07 |
| 203 | CZK | ČEŠKA KRUNA | ČEŠKA | D | 2021-08-06 | BIZNISOFT | 2025-04-03 17:12:07 |
| 208 | DKK | DANSKA KRUNA | DANSKA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 246 | FIM | FINSKA MARKA | FINSKA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 250 | FRF | FRANCUSKI FRANAK | FRANCUSKA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 280 | DEM | NEMAČKA MARKA | NEMAČKA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 300 | GRD | DRAHMA | GRČKA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 348 | HUF | FORINTA | MAĐARSKA | D | 2021-08-06 | BIZNISOFT | 2025-04-03 17:12:07 |
| 356 | INR | INDIJSKA RUPIJA | INDIJA | D | 2023-06-07 | BIZNISOFT | 2025-04-03 17:12:07 |
| 372 | IEP | IRSKA FUNTA | IRSKA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 380 | ITL | ITALIJANSKA LIRA | ITALIJA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 392 | JPY | JEN | JAPAN | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 414 | KWD | KUVAJTSKI DINAR | KUVAJT | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 442 | LUF | LUKSEMBURŠKI FRANAK | LUKSEMBURG | D | 2021-08-06 | BIZNISOFT | 2025-04-03 17:12:07 |
| 578 | NOK | NORVEŠKA KRUNA | NORVEŠKA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 620 | PTE | PORTUGALSKI ESKUDO | PORTUGALIJA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 643 | RUB | RUSKA RUBLJA | RUSKA FEDERACIJA | D | 2021-08-06 | BIZNISOFT | 2025-04-03 17:12:07 |
| 724 | ESP | ŠPANSKA PEZETA | ŠPANIJA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 752 | SEK | ŠVEDSKA KRUNA | ŠVEDSKA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 756 | CHF | ŠVAJCARSKI FRANAK | ŠVAJCARSKA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 784 | AED | UAE DIRHAM | UJEDINJENI ARAPSKI EMIRATI | D | 2023-06-07 | BIZNISOFT | 2025-04-03 17:12:07 |
| 807 | MKD | MAKEDONSKI DENAR | REPUBLIKA SEVERNA MAKEDONIJA | D | 2022-11-09 | BIZNISOFT | 2025-04-03 17:12:07 |
| 826 | GBP | FUNTA STERLINGA | VELIKA BRITANIJA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 840 | USD | AMERIČKI DOLAR | USA | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 933 | BYN | BELORUSKA RUBLJA | BELORUSIJA | D | 2021-08-06 | BIZNISOFT | 2025-04-03 17:12:07 |
| 941 | RSD | SRPSKI DINAR | SRBIJA | D | 2016-10-08 | BIZNISOFT | 2025-04-03 17:12:07 |
| 946 | RON | LEJ | RUMUNIJA | D | 2021-08-06 | BIZNISOFT | 2025-04-03 17:12:07 |
| 949 | TRY | TURSKA LIRA | TURSKA | D | 2021-08-06 | BIZNISOFT | 2025-04-03 17:12:07 |
| 975 | BGN | BUGARSKI LEV | BUGARSKA | D | 2021-08-06 | BIZNISOFT | 2025-04-03 17:12:07 |
| 977 | BAM | KONVERTIBILNA MARKA | BOSNA I HERCEGOVINA | D | 2021-08-06 | BIZNISOFT | 2025-04-03 17:12:07 |
| 978 | EUR | EVRO | EMU | D | 2005-05-18 | BIZNISOFT | 2025-04-03 17:12:07 |
| 985 | PLN | ZLOT | POLJSKA | D | 2021-08-06 | BIZNISOFT | 2025-04-03 17:12:07 |

---

## Tabela: `drzave`
**Opis:** Šifarnik država
**Redova:** 252

**Kolone:** `ID`, `DrzavaAlfa2Kod`, `DrzavaAlfa3Kod`, `DrzavaNumerikKod`, `DrzavaGeoKod`, `DrzavaNazivCir`, `DrzavaNazivLat`

| ID | DrzavaAlfa2Kod | DrzavaAlfa3Kod | DrzavaNumerikKod | DrzavaGeoKod | DrzavaNazivCir | DrzavaNazivLat |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | XS | XSS | 098 | 098 | СРБИЈА | SRBIJA |
| 10 | AM | ARM | 051 | 077 | ЈЕРМЕНИЈА | JERMENIJA |
| 100 | IN | IND | 356 | 664 | ИНДИЈА | INDIJA |
| 101 | IO | IOT | 86  | 357 | БРИТАНСКА ТЕРИТОРИЈА ИНДИЈСКОГ ОКЕАНА | BRITANSKA TERITORIJA INDIJSKOG OKEANA |
| 102 | IQ | IRQ | 368 | 612 | ИРАК | IRAK |
| 103 | IR | IRN | 364 | 616 | ИРАН, ИСЛАМСКА РЕПУБЛИКА | IRAN, ISLAMSKA REPUBLIKA |
| 104 | IS | ISL | 352 | 024 | ИСЛАНД | ISLAND |
| 105 | IT | ITA | 380 | 005 | ИТАЛИЈА | ITALIJA |
| 106 | JM | JAM | 388 | 464 | ЈАМАЈКА | JAMAJKA |
| 107 | JO | JOR | 400 | 628 | ЈОРДАН | JORDAN |
| 108 | JP | JPN | 392 | 732 | ЈАПАН | JAPAN |
| 109 | KE | KEN | 404 | 346 | КЕНИЈА | KENIJA |
| 11 | AN | ANT | 530 | 478 | ХОЛАНДСКИ АНТИЛИ | HOLANDSKI ANTILI |
| 110 | KG | KGZ | 417 | 083 | КИРГИСТАН | KIRGISTAN |
| 111 | KH | KHM | 116 | 696 | КАМБОЏА | KAMBOĐA |
| 112 | KI | KIR | 296 | 812 | КИРИБАТИ | KIRIBATI |
| 113 | KM | COM | 174 | 375 | КОМОРИ | KOMORI |
| 114 | KN | KNA | 659 | 449 | СЕНТ КИТС-НЕВИС | SENT KITS-NEVIS |
| 115 | KP | PRK | 408 | 724 | КОРЕЈА, ДНР | KOREJA, DNR  |
| 116 | KR | KOR | 410 | 728 | КОРЕЈА | KOREJA |
| 117 | KW | KWT | 414 | 636 | КУВАЈТ | KUVAJT |
| 118 | KY | CYM | 136 | 463 | КАЈМАНСКА ОСТРВА | KAJMANSKA OSTRVA |
| 119 | KZ | KAZ | 398 | 079 | КАЗАХСТАН | KAZAHSTAN |
| 12 | AO | AGO | 24  | 330 | АНГОЛА | ANGOLA |
| 120 | LA | LAO | 418 | 684 | ЛАОС, ДЕМОКРАТСКА НАРОДНА РЕПУБЛИКА | LAOS, DEMOKRATSKA NARODNA REPUBLIKA |
| 121 | LB | LBN | 422 | 604 | ЛИБАН | LIBAN |
| 122 | LC | LCA | 662 | 465 | СЕНТ ЛУСИЈА | SENT LUSIJA |
| 123 | LI | LIE | 438 | 037 | ЛИХТЕНШТАЈН | LIHTENŠTAJN |
| 124 | LK | LKA | 144 | 669 | ШРИ ЛАНКА | ŠRI LANKA |
| 125 | LR | LBR | 430 | 268 | ЛИБЕРИЈА | LIBERIJA |
| 126 | LS | LSO | 426 | 395 | ЛЕСОТО | LESOTO |
| 127 | LT | LTU | 440 | 055 | ЛИТВАНИЈА | LITVANIJA |
| 128 | LU | LUX | 442 | 018 | ЛУКСЕМБУРГ | LUKSEMBURG |
| 129 | LV | LVA | 428 | 054 | ЛЕТОНИЈА | LETONIJA |
| 13 | AQ | ATA | 10  | 891 | АНТАРКТИК | ANTARKTIK |
| 130 | LY | LBY | 434 | 216 | ЛИБИЈСКА АРАПСКА ЏАМАХИРИЈА | LIBIJSKA ARAPSKA ĐAMAHIRIJA |
| 131 | MA | MAR | 504 | 204 | МАРОКО | MAROKO |
| 132 | MD | MDA | 498 | 074 | МОЛДАВИЈА | MOLDAVIJA |
| 133 | MG | MDG | 450 | 370 | МАДАГАСКАР | MADAGASKAR |
| 134 | MH | MHL | 584 | 824 | МАРШАЛСКА ОСТРВА | MARŠALSKA OSTRVA  |
| 135 | MK | MKD | 807 | 096 | РЕПУБЛИКА МАКЕДОНИЈА | REPUBLIKA MAKEDONIJA |
| 136 | ML | MLI | 466 | 232 | МАЛИ | MALI |
| 137 | MM | MMR | 104 | 676 | МИЈАНМАР | MIJANMAR |
| 138 | MN | MNG | 496 | 716 | МОНГОЛИЈА | MONGOLIJA |
| 139 | MO | MAC | 446 | 743 | МАКАО | MAKAO |
| 14 | AR | ARG | 32  | 528 | АРГЕНТИНА | ARGENTINA |
| 140 | MP | MNP | 580 | 820 | СЕВЕРНО МАРИЈАНСКА ОСТРВА | SEVERNO MARIJANSKA OSTRVA  |
| 141 | MR | MRT | 478 | 228 | МАУРИТАНИЈА | MAURITANIJA |
| 142 | MS | MSR | 500 | 470 | МОНСЕРАТ | MONSERAT |
| 143 | MT | MLT | 470 | 046 | МАЛТА | MALTA |
| 144 | MU | MUS | 480 | 373 | МАУРИЦИЈУС | MAURICIJUS |
| 145 | MV | MDV | 462 | 667 | МАЛДИВИ | MALDIVI |
| 146 | MW | MWI | 454 | 386 | МАЛАВИ | MALAVI |
| 147 | MX | MEX | 484 | 412 | МЕКСИКО | MEKSIKO |
| 148 | MY | MYS | 458 | 701 | МАЛЕЗИЈА | MALEZIJA |
| 149 | MZ | MOZ | 508 | 366 | МОЗАМБИК | MOZAMBIK |
| 15 | AS | ASM | 16  | 830 | АМЕРИЧКА САМОА | AMERIČKA SAMOA |
| 150 | NA | NAM | 516 | 389 | НАМИБИЈА | NAMIBIJA |
| 151 | NC | NCL | 540 | 809 | НОВА КАЛЕДОНИЈА | NOVA KALEDONIJA |
| 152 | NE | NER | 562 | 240 | НИГЕР | NIGER |
| 153 | NF | NFK | 574 | 836 | НОРФОЛК ОСТРВО | NORFOLK OSTRVO |
| 154 | NG | NGA | 566 | 288 | НИГЕРИЈА | NIGERIJA |
| 155 | NI | NIC | 558 | 432 | НИКАРАГВА | NIKARAGVA |
| 156 | NL | NLD | 528 | 003 | ХОЛАНДИЈА | HOLANDIJA |
| 157 | NO | NOR | 578 | 028 | НОРВЕШКА | NORVEŠKA |
| 158 | NP | NPL | 524 | 672 | НЕПАЛ | NEPAL |
| 159 | NR | NRU | 520 | 803 | НАУРУ | NAURU |
| 16 | AT | AUT | 40  | 038 | АУСТРИЈА | AUSTRIJA |
| 160 | NU | NIU | 570 | 838 | НИУИ | NIUE |
| 161 | NZ | NZL | 554 | 804 | НОВИ ЗЕЛАНД | NOVI ZELAND |
| 162 | OM | OMN | 512 | 649 | ОМАН | OMAN |
| 163 | PA | PAN | 591 | 442 | ПАНАМА | PANAMA |
| 164 | PE | PER | 604 | 504 | ПЕРУ | PERU |
| 165 | PF | PYF | 258 | 822 | ФРАНЦУСКА ПОЛИНЕЗИЈА | FRANCUSKA POLINEZIJA |
| 166 | PG | PNG | 598 | 801 | ПАПУА НОВА ГВИНЕЈА | PAPUA NOVA GVINEJA |
| 167 | PH | PHL | 608 | 708 | ФИЛИПИНИ | FILIPINI |
| 168 | PK | PAK | 586 | 662 | ПАКИСТАН | PAKISTAN |
| 169 | PL | POL | 616 | 060 | ПОЉСКА | POLJSKA |
| 17 | AU | AUS | 36  | 800 | АУСТРАЛИЈА | AUSTRALIJA |
| 170 | PM | SPM | 666 | 408 | СЕН ПЈЕР И МИКЕЛОН | SEN PJER I MIKELON |
| 171 | PN | PCN | 612 | 813 | ПИТКЕРН | PITKERN |
| 172 | PS | PSE | 275 | 625 | ПАЛЕСТИНА | PALESTINA |
| 173 | PT | PRT | 620 | 010 | ПОРТУГАЛИЈА | PORTUGALIJA |
| 174 | PW | PLW | 585 | 825 | ПАЛАУ | PALAU |
| 175 | PY | PRY | 600 | 520 | ПАРАГВАЈ | PARAGVAJ |
| 176 | QA | QAT | 634 | 644 | КАТАР | KATAR |
| 177 | RO | ROM | 642 | 066 | РУМУНИЈА | RUMUNIJA |
| 178 | RU | RUS | 643 | 075 | РУСКА ФЕДЕРАЦИЈА | RUSKA FEDERACIJA |
| 179 | RW | RWA | 646 | 324 | РУАНДА | RUANDA |
| 18 | AW | ABW | 533 | 474 | АРУБА | ARUBA |
| 180 | SA | SAU | 682 | 632 | САУДИЈСКА АРАБИЈА | SAUDIJSKA ARABIJA |
| 181 | SB | SLB | 90  | 806 | СОЛОМОНСКА ОСТРВА | SOLOMONSKA OSTRVA |
| 182 | SC | SYC | 690 | 355 | СЕЈШЕЛСКА ОСТРВА | SEJŠELSKA OSTRVA |
| 183 | SD | SDN | 736 | 224 | СУДАН | SUDAN |
| 184 | SE | SWE | 752 | 030 | ШВЕДСКА | ŠVEDSKA |
| 185 | SG | SGP | 702 | 706 | СИНГАПУР | SINGAPUR |
| 186 | SH | SHN | 654 | 329 | СВЕТА ЈЕЛЕНА | SVETA JELENA |
| 187 | SI | SVN | 705 | 091 | СЛОВЕНИЈА | SLOVENIJA |
| 188 | SK | SVK | 703 | 063 | СЛОВАЧКА | SLOVAČKA |
| 189 | SL | SLE | 694 | 264 | СИЈЕРА ЛЕОНЕ | SIJERA LEONE |
| 19 | AZ | AZE | 31  | 078 | АЗЕРБЕЈЏАН | AZERBEJDŽAN |
| 190 | SM | SMR | 674 | 047 | САН МАРИНО | SAN MARINO |
| 191 | SN | SEN | 686 | 248 | СЕНЕГАЛ | SENEGAL |
| 192 | SO | SOM | 706 | 342 | СОМАЛИЈА | SOMALIJA |
| 193 | SR | SUR | 740 | 492 | СУРИНАМ | SURINAME |
| 194 | ST | STP | 678 | 311 | САО ТОМА И ПРИНЦИПЕ | SAO TOMA I PRINCIPE |
| 195 | SV | SLV | 222 | 428 | ЕЛ САЛВАДОР | EL SALVADOR |
| 196 | SY | SYR | 760 | 608 | СИРИЈСКА АРАПСКА РЕПУБЛИКА | SIRIJSKA ARAPSKA REPUBLIKA |
| 197 | SZ | SWZ | 748 | 393 | СВАЗИЛАНД | SVAZILAND |
| 198 | TC | TCA | 796 | 454 | ТУРКС И КАИКОС ОСТРВА | TURKS I KAIKOS OSTRVA |
| 199 | TD | TCD | 148 | 244 | ЧАД | ČAD |
| 2 | XM | XMM | 097 | 097 | ЦРНА ГОРА | CRNA GORA |
| 20 | BA | BIH | 70  | 093 | БОСНА И ХЕРЦЕГОВИНА | BOSNA I HERCEGOVINA |
| 200 | TF | ATF | 260 | 894 | ЈУЖНА ФРАНЦУСКА ТЕРИТОРИЈА | JUŽNA FRANCUSKA TERITORIJA  |
| 201 | TG | TGO | 768 | 280 | ТОГО | TOGO |
| 202 | TH | THA | 764 | 680 | ТАЈЛАНД | TAJLAND |
| 203 | TJ | TJK | 762 | 082 | ТАЏИКИСТАН | TADŽIKISTAN |
| 204 | TK | TKL | 772 | 839 | ТОКЕЛАУ | TOKELAU |
| 205 | TL | TLS | 628 | 626 | ТИМОР-ЛЕСТЕ | TIMOR-LESTE |
| 206 | TM | TKM | 795 | 080 | ТУРКМЕНИСТАН | TURKMENISTAN |
| 207 | TN | TUN | 788 | 212 | ТУНИС | TUNIS |
| 208 | TO | TON | 776 | 817 | ТОНГА | TONGA |
| 209 | TR | TUR | 792 | 052 | ТУРСКА | TURSKA |
| 21 | BB | BRB | 52  | 469 | БАРБАДОС | BARBADOS |
| 210 | TT | TTO | 780 | 472 | ТРИНИДАД И ТОБАГО | TRINIDAD I TOBAGO |
| 211 | TV | TUV | 798 | 807 | ТУВАЛУ | TUVALU |
| 212 | TW | TWN | 158 | 736 | ТАЈВАН | TAJVAN |
| 213 | TZ | TZA | 834 | 352 | ТАНЗАНИЈА, УЈЕДИЊЕНА РЕПУБЛИКА | TANZANIJA, UJEDINJENA REPUBLIKA |
| 214 | UA | UKR | 804 | 072 | УКРАЈИНА | UKRAJINA |
| 215 | UG | UGA | 800 | 350 | УГАНДА | UGANDA |
| 216 | UM | UMI | 581 | 832 | ДРЖАВА МАЊИХ УДАЉЕНИХ ОСТРВА | DRŽAVA MANJIH UDALJENIH OSZTRVA |
| 217 | US | USA | 840 | 400 | СЈЕДИЊЕНЕ АМЕРИЧКЕ ДРЖАВЕ | SAD |
| 218 | UY | URY | 858 | 524 | УРУГВАЈ | URUGVAJ |
| 219 | UZ | UZB | 860 | 081 | УЗБЕКИСТАН | UZBEKISTAN |
| 22 | BD | BGD | 50  | 666 | БАНГЛАДЕШ | BANGLADEŠ |
| 220 | VA | VAT | 336 | 045 | ВАТИКАН | VATIKAN  |
| 221 | VC | VCT | 670 | 467 | СЕНТ ВИНСЕНТ И ГРЕНАДИНИ | SENT VINSENT I GRENADINI |
| 222 | VE | VEN | 862 | 484 | ВЕНЕЦУЕЛА | VENECUELA |
| 223 | VG | VGB | 92  | 468 | ДЕВИЧАНСКА ОСТРВА (БРИТАНСКА) | DEVIČANSKA OSTRVA (BRITANSKA) |
| 224 | VI | VIR | 850 | 457 | ДЕВИЧАНСКА ОСТРВА (САД) | DEVIČANSKA OSTRVA (SAD) |
| 225 | VN | VNM | 704 | 690 | ВИЈЕТНАМ | VIJETNAM |
| 226 | VU | VUT | 548 | 816 | ВАНУАТА | VANUATA |
| 227 | WF | WLF | 876 | 811 | ВОЛИС И ФУТУНА ОСТРВА | VOLIS I FUTUNA OSTRVA |
| 228 | WS | WSM | 882 | 819 | САМОА | SAMOA |
| 229 | XC | 995 | 995 | 021 | КЕУТА | KEUTA |
| 23 | BE | BEL | 56  | 017 | БЕЛГИЈА | BELGIJA |
| 230 | XL | 994 | 994 | 023 | МЕЛИЛА | MELILA |
| 231 | YE | YEM | 887 | 653 | ЈЕМЕН | JEMEN |
| 232 | YT | MYT | 175 | 377 | МАЈОТЕ | MAJOTE |
| 233 | ZA | ZAF | 710 | 388 | ЈУЖНА АФРИКА | JUŽNA AFRIKA |
| 234 | ZM | ZMB | 894 | 378 | ЗАМБИЈА | ZAMBIJA |
| 235 | ZW | ZWE | 716 | 382 | ЗИМБАБВЕ | ZIMBABVE |
| 236 | IM | IMN | 833 | 998 | ОСТРВО МАН | OSTRVO MAN |
| 237 | EH | ESH | 732 |  | ЗАПАДНА САХАРА | ZAPADNA SAHARA |
| 238 | GF | GUF | 254 |  | ФРАНЦУСКА ГИЈАНА | FRANCUSKA GIJANA |
| 239 | GP | GLP | 312 |  | ГВАДАЛУПЕ | GVADALUPE |
| 24 | BF | BFA | 854 | 236 | БУРКИНА ФАСО | BURKINA FASO |
| 240 | JE | JEY | 832 |  | ЏЕРСИ | DŽERSI |
| 241 | MC | MCO | 492 |  | МОНАКО | MONAKO |
| 242 | MQ | MTQ | 474 |  | МАРТИНИК | MARTINIK |
| 243 | PR | PRI | 630 |  | ПОРТОРИКО | PORTORIKO |
| 244 | RE | REU | 638 |  | РЕЈУНИОН | REJUNION |
| 245 | SJ | SJM | 744 |  | СВАЛБАРД И ЈАН МАЈЕН ОСТРВА | SVALBARD I JAN MAJEN OSTRVA |
| 246 | TP | TMP | 626 |  | ИСТОЧНИ ТИМОР | ISTOČNI TIMOR |
| 247 | ZR | ZAR | 180 |  | ЗАИР | ZAIR |
| 248 | GG | GGY | 831 |  | ГЕРНЗИ | GERNZI |
| 249 | LY | LBY | 434 | 216 | ДРЖАВА ЛИБИЈА | DRŽAVA LIBIJA |
| 25 | BG | BGR | 100 | 068 | БУГАРСКА | BUGARSKA |
| 250 | MK | MKD | 807 | 096 | РЕПУБЛИКА СЕВЕРНА МАКЕДОНИЈА | REPUBLIKA SEVERNA MAKEDONIJA |
| 251 | CW | CUW | 531 |  | КУРАСАО | KURASAO |
| 26 | BH | BHR | 48  | 640 | БАХРЕИН | BAHREIN |
| 27 | BI | BDI | 108 | 328 | БУРУНДИЈА | BURUNDIJA |
| 28 | BJ | BEN | 204 | 284 | БЕНИН | BENIN |
| 29 | BM | BMU | 60  | 413 | БЕРМУДИ | BERMUDI |
| 3 | CS | SCG | 891 | 094 | СРБИЈА И ЦРНА ГОРА | SRBIJA I CRNA GORA |
| 30 | BN | BRN | 96  | 703 | БРУНЕЈ | BRUNEJ  |
| 31 | BO | BOL | 68  | 516 | БОЛИВИЈА | BOLIVIJA |
| 32 | BR | BRA | 76  | 508 | БРАЗИЛ | BRAZIL |
| 33 | BS | BHS | 44  | 453 | БАХАМИ | BAHAMI |
| 34 | BT | BTN | 64  | 675 | БУТАН | BUTAN |
| 35 | BV | BVT | 74  | 892 | БУВЕ | BUVE |
| 36 | BW | BWA | 72  | 391 | БОЦВАНА | BOCVANA |
| 37 | BY | BLR | 112 | 073 | БЕЛОРУСИЈА | BELORUSIJA |
| 38 | BZ | BLZ | 84  | 421 | БЕЛИЗЕ | BELIZE |
| 39 | CA | CAN | 124 | 404 | КАНАДА | KANADA |
| 4 | AD | AND | 020 | 043 | АНДОРА | ANDORA |
| 40 | CC | CCK | 166 | 833 | КОКОСОВА ОСТВРА | KOKOSOVA OSTRVA |
| 41 | CD | 996 | 996 | 322 | КОНГО, ДЕМОКРАТСКА РЕПУБЛИКА | KONGO, DEMOKRATSKA REPUBLIKA |
| 42 | CF | CAF | 140 | 306 | ЦЕНТРАЛНОАФРИЧКА РЕПУБЛИКА | CENTRALNOAFRIČKA REPUBLIKA |
| 43 | CG | COG | 178 | 318 | КОНГО | KONGO |
| 44 | CH | CHE | 756 | 039 | ШВАЈЦАРСКА | ŠVAJCARSKA |
| 45 | CI | CIV | 384 | 272 | ОБАЛА СЛОНОВАЧЕ | OBALA SLONOVAČE |
| 46 | CK | COK | 184 | 837 | КУКОВА ОСТРВА | KUKOVA OSTRVA |
| 47 | CL | CHL | 152 | 512 | ЧИЛЕ | ČILE |
| 48 | CM | CMR | 120 | 302 | КАМЕРУН | KAMERUN |
| 49 | CN | CHN | 156 | 720 | КИНА, НАРОДНА РЕПУБЛИКА | KINA, NARODNA REPUBLIKA |
| 5 | AE | ARE | 784 | 647 | УЈЕДИЊЕНИ АРАПСКИ ЕМИРАТИ | UJEDINJENI ARAPSKI EMIRATI |
| 50 | CO | COL | 170 | 480 | КОЛУМБИЈА | KOLUMBIJA |
| 51 | CR | CRI | 188 | 436 | КОСТАРИКА | KOSTARIKA |
| 52 | CU | CUB | 192 | 448 | КУБА | KUBA |
| 53 | CV | CPV | 132 | 247 | ЗЕЛЕНОРТСКА ОСТРВА | ZELENORTSKA OSTRVA |
| 54 | CX | CXR | 162 | 834 | БОЗИЋНО ОСТРВО | BOŽIČNO OSTRVO |
| 55 | CY | CYP | 196 | 600 | КИПАР | KIPAR |
| 56 | CZ | CZE | 203 | 061 | ЧЕШКА РЕПУБЛИКА | ČEŠKA REPUBLIKA |
| 57 | DE | DEU | 276 | 004 | НЕМАЧКА | NEMAČKA |
| 58 | DJ | DJI | 262 | 338 | ЏИБУТИ | ĐIBUTI |
| 59 | DK | DNK | 208 | 008 | ДАНСКА | DANSKA |
| 6 | AF | AFG | 000 | 660 | АВГАНИСТАН | AVGANISTAN |
| 60 | DM | DMA | 212 | 460 | ДОМИНИКА | DOMINIKA |
| 61 | DO | DOM | 214 | 456 | ДОМИНИКАНСКА РЕПУБЛИКА | DOMINIKANSKA REPUBLIKA |
| 62 | DZ | DZA | 12  | 208 | АЛЖИР | ALŽIR |
| 63 | EC | ECU | 218 | 500 | ЕКВАДОР | EKVADOR |
| 64 | EE | EST | 233 | 053 | ЕСТОНИЈА | ESTONIJA |
| 65 | EG | EGY | 818 | 220 | ЕГИПАТ | EGIPAT |
| 66 | ER | ERI | 232 | 336 | ЕРИТРЕЈА | ERITREJA |
| 67 | ES | ESP | 724 | 011 | ШПАНИЈА | ŠPANIJA |
| 68 | ET | ETH | 231 | 334 | ЕТИОПИЈА | ETIOPIJA |
| 69 | FI | FIN | 246 | 032 | ФИНСКА | FINSKA  |
| 7 | AG | ATG | 028 | 459 | АНТИГВА | ANTIGVA I BARBUDA |
| 70 | FJ | FJI | 242 | 815 | ФИЏИ | FIĐI |
| 71 | FK | FLK | 238 | 529 | ФОЛКЛАНДСКА ОСТРВА | FOLKLANDSKA OSTRVA |
| 72 | FM | FSM | 583 | 823 | МИКРОНЕЗИЈА, ФЕДЕРАЛНА ДРЖАВА | MIKRONEZIJA, FEDERALNA DRŽAVA |
| 73 | FO | FRO | 234 | 041 | ФАРСКА ОСТРВА | FARSKA OSTRVA |
| 74 | FR | FRA | 250 | 001 | ФРАНЦУСКА | FRANCUSKA |
| 75 | GA | GAB | 266 | 314 | ГАБОН | GABON |
| 76 | GB | GBR | 826 | 006 | ВЕЛИКА БРИТАНИЈА | VELIKA BRITANIJA |
| 77 | GD | GRD | 308 | 473 | ГРЕНАДА | GRENADA |
| 78 | GE | GEO | 268 | 076 | ГРУЗИЈА | GRUZIJA |
| 79 | GH | GHA | 288 | 276 | ГАНА | GANA |
| 8 | AI | AIA | 660 | 446 | АНГВИЛА | ANGVILA |
| 80 | GI | GIB | 292 | 044 | ГИБРАЛТАР | GIBRALTAR |
| 81 | GL | GRL | 304 | 406 | ГРЕНЛАНД | GRENLAND |
| 82 | GM | GMB | 270 | 252 | ГАМБИЈА | GAMBIJA |
| 83 | GN | GIN | 324 | 260 | ГВИНЕЈА | GVINEJA |
| 84 | GQ | GNQ | 226 | 310 | ЕКВАТОРИЈАЛНА ГВИНЕЈА | EKVATORIJALNA GVINEJA |
| 85 | GR | GRC | 300 | 009 | ГРЧКА | GRČKA |
| 86 | GS | SGS | 239 | 893 | ЈУЖНА ЏОРЏИЈА И СЕНДВИЧ ОСТВРА | JUŽNA ĐORĐIJA I SENDVIČ OSTRVA |
| 87 | GT | GTM | 320 | 416 | ГВАТЕМАЛА | GVATEMALA |
| 88 | GU | GUM | 316 | 831 | ГУАМ | GUAM |
| 89 | GW | GNB | 624 | 257 | ГВИНЕЈА БИСАО | GVINEJA BISAO |
| 9 | AL | ALB | 008 | 070 | АЛБАНИЈА | ALBANIJA |
| 90 | GY | GUY | 328 | 488 | ГВАЈАНА | GVAJANA |
| 91 | HK | HKG | 344 | 740 | ХОНГКОНГ | HONGKONG |
| 92 | HM | HMD | 334 | 835 | ХЕРД И МЕКДОНАЛД ОСТРВА | HERD I MEKDONALD OSTRVA  |
| 93 | HN | HND | 340 | 424 | ХОНДУРАС | HONDURAS |
| 94 | HR | HRV | 191 | 092 | ХРВАТСКА | HRVATSKA |
| 95 | HT | HTI | 332 | 452 | ХАИТИ | HAITI |
| 96 | HU | HUN | 348 | 064 | МАЂАРСКА | MAĐARSKA |
| 97 | ID | IDN | 360 | 700 | ИНДОНЕЗИЈА | INDONEZIJA |
| 98 | IE | IRL | 372 | 007 | ИРСКА | IRSKA |
| 99 | IL | ISR | 376 | 624 | ИЗРАЕЛ | IZRAEL |
| 978 | EU | EUR | 978 | 978 | ЕВРОПСКА УНИЈА | EVROPSKA UNIJA |

---

## Tabela: `opstine`
**Opis:** Šifarnik opština
**Redova:** 207

**Kolone:** `sifopst`, `nazivopst`, `datcre`, `operater`, `kontbr`, `ts`

| sifopst | nazivopst | datcre | operater | kontbr | ts |
| --- | --- | --- | --- | --- | --- |
| 1 | ALEKSANDROVAC | 2005-11-11 | BIZNISOFT | 95-001 | 2025-04-04 10:04:06 |
| 2 | ALEKSINAC | 2005-11-11 | BIZNISOFT | 92-002 | 2025-04-04 10:04:06 |
| 3 | ARANĐELOVAC | 2005-11-11 | BIZNISOFT | 89-003 | 2025-04-04 10:04:06 |
| 4 | ARILJE | 2005-11-11 | BIZNISOFT | 86-004 | 2025-04-04 10:04:06 |
| 6 | BABUŠNICA | 2005-11-11 | BIZNISOFT | 80-006 | 2025-04-04 10:04:06 |
| 7 | BAJINA BAŠTA | 2005-11-11 | BIZNISOFT | 77-007 | 2025-04-04 10:04:06 |
| 8 | BATOČINA | 2005-11-11 | BIZNISOFT | 74-008 | 2025-04-04 10:04:06 |
| 9 | BELA PALANKA | 2005-11-11 | BIZNISOFT | 71-009 | 2025-04-04 10:04:06 |
| 10 | BARAJEVO | 2005-11-11 | BIZNISOFT | 68-010 | 2025-04-04 10:04:06 |
| 11 | ČUKARICA | 2005-11-11 | BIZNISOFT | 65-011 | 2025-04-04 10:04:06 |
| 12 | GROCKA | 2005-11-11 | BIZNISOFT | 62-012 | 2025-04-04 10:04:06 |
| 13 | NOVI BEOGRAD | 2005-11-11 | BIZNISOFT | 59-013 | 2025-04-04 10:04:06 |
| 14 | OBRENOVAC | 2005-11-11 | BIZNISOFT | 56-014 | 2025-04-04 10:04:06 |
| 15 | PALILULA | 2005-11-11 | BIZNISOFT | 53-015 | 2025-04-04 10:04:06 |
| 16 | SAVSKI VENAC | 2005-11-11 | BIZNISOFT | 50-016 | 2025-04-04 10:04:06 |
| 17 | SOPOT | 2005-11-11 | BIZNISOFT | 47-017 | 2025-04-04 10:04:06 |
| 18 | STARI GRAD | 2005-11-11 | BIZNISOFT | 44-018 | 2025-04-04 10:04:06 |
| 19 | VOŽDOVAC | 2005-11-11 | BIZNISOFT | 41-019 | 2025-04-04 10:04:06 |
| 20 | VRAČAR | 2005-11-11 | BIZNISOFT | 38-020 | 2025-04-04 10:04:06 |
| 21 | ZEMUN | 2005-11-11 | BIZNISOFT | 35-021 | 2025-04-04 10:04:06 |
| 22 | ZVEZDARA | 2005-11-11 | BIZNISOFT | 32-022 | 2025-04-04 10:04:06 |
| 23 | BLACE | 2005-11-11 | BIZNISOFT | 29-023 | 2025-04-04 10:04:06 |
| 24 | BOGATIĆ | 2005-11-11 | BIZNISOFT | 26-024 | 2025-04-04 10:04:06 |
| 25 | BOJNIK | 2005-11-11 | BIZNISOFT | 23-025 | 2025-04-04 10:04:06 |
| 26 | BOLJEVAC | 2005-11-11 | BIZNISOFT | 20-026 | 2025-04-04 10:04:06 |
| 27 | BOR | 2005-11-11 | BIZNISOFT | 17-027 | 2025-04-04 10:04:06 |
| 28 | BOSILEGRAD | 2005-11-11 | BIZNISOFT | 14-028 | 2025-04-04 10:04:06 |
| 29 | BRUS | 2005-11-11 | BIZNISOFT | 11-029 | 2025-04-04 10:04:06 |
| 30 | BUJANOVAC | 2005-11-11 | BIZNISOFT | 08-030 | 2025-04-04 10:04:06 |
| 31 | CRNA TRAVA | 2005-11-11 | BIZNISOFT | 05-031 | 2025-04-04 10:04:06 |
| 32 | ĆIĆEVAC | 2005-11-11 | BIZNISOFT | 02-032 | 2025-04-04 10:04:06 |
| 33 | ĆUPRIJA | 2005-11-11 | BIZNISOFT | 96-033 | 2025-04-04 10:04:06 |
| 34 | ČAČAK | 2005-11-11 | BIZNISOFT | 93-034 | 2025-04-04 10:04:06 |
| 35 | ČAJETINA | 2005-11-11 | BIZNISOFT | 90-035 | 2025-04-04 10:04:06 |
| 36 | DESPOTOVAC | 2005-11-11 | BIZNISOFT | 87-036 | 2025-04-04 10:04:06 |
| 37 | DIMITROVGRAD | 2005-11-11 | BIZNISOFT | 84-037 | 2025-04-04 10:04:06 |
| 38 | DOLJEVAC | 2005-11-11 | BIZNISOFT | 81-038 | 2025-04-04 10:04:06 |
| 39 | GADŽIN HAN | 2005-11-11 | BIZNISOFT | 78-039 | 2025-04-04 10:04:06 |
| 40 | GOLUBAC | 2005-11-11 | BIZNISOFT | 75-040 | 2025-04-04 10:04:06 |
| 41 | GORNJI MILANOVAC | 2005-11-11 | BIZNISOFT | 72-041 | 2025-04-04 10:04:06 |
| 42 | IVANJICA | 2005-11-11 | BIZNISOFT | 69-042 | 2025-04-04 10:04:06 |
| 43 | KLADOVO | 2005-11-11 | BIZNISOFT | 66-043 | 2025-04-04 10:04:06 |
| 44 | KNIĆ | 2005-11-11 | BIZNISOFT | 63-044 | 2025-04-04 10:04:06 |
| 45 | KNJAŽEVAC | 2005-11-11 | BIZNISOFT | 60-045 | 2025-04-04 10:04:06 |
| 46 | KOCELJEVA | 2005-11-11 | BIZNISOFT | 57-046 | 2025-04-04 10:04:06 |
| 48 | KOSJERIĆ | 2005-11-11 | BIZNISOFT | 51-048 | 2025-04-04 10:04:06 |
| 49 | KRAGUJEVAC | 2005-11-11 | BIZNISOFT | 48-049 | 2025-04-04 10:04:06 |
| 50 | KRALJEVO | 2005-11-11 | BIZNISOFT | 45-050 | 2025-04-04 10:04:06 |
| 51 | KRUPANJ | 2005-11-11 | BIZNISOFT | 42-051 | 2025-04-04 10:04:06 |
| 52 | KRUŠEVAC | 2005-11-11 | BIZNISOFT | 39-052 | 2025-04-04 10:04:06 |
| 53 | KUČEVO | 2005-11-11 | BIZNISOFT | 36-053 | 2025-04-04 10:04:06 |
| 54 | KURŠUMLIJA | 2005-11-11 | BIZNISOFT | 33-054 | 2025-04-04 10:04:06 |
| 55 | LAJKOVAC | 2005-11-11 | BIZNISOFT | 30-055 | 2025-04-04 10:04:06 |
| 56 | LAZAREVAC | 2005-11-11 | BIZNISOFT | 27-056 | 2025-04-04 10:04:06 |
| 57 | LEBANE | 2005-11-11 | BIZNISOFT | 24-057 | 2025-04-04 10:04:06 |
| 58 | LESKOVAC | 2005-11-11 | BIZNISOFT | 21-058 | 2025-04-04 10:04:06 |
| 59 | LOZNICA | 2005-11-11 | BIZNISOFT | 18-059 | 2025-04-04 10:04:06 |
| 60 | LUČANI | 2005-11-11 | BIZNISOFT | 15-060 | 2025-04-04 10:04:06 |
| 61 | LJIG | 2005-11-11 | BIZNISOFT | 12-061 | 2025-04-04 10:04:06 |
| 62 | LJUBOVIJA | 2005-11-11 | BIZNISOFT | 09-062 | 2025-04-04 10:04:06 |
| 63 | DONJI MILANOVAC - MAJDANPEK | 2005-11-11 | BIZNISOFT | 06-063 | 2025-04-04 10:04:06 |
| 65 | MALI ZVORNIK | 2005-11-11 | BIZNISOFT | 97-065 | 2025-04-04 10:04:06 |
| 66 | MALO CRNIĆE | 2005-11-11 | BIZNISOFT | 94-066 | 2025-04-04 10:04:06 |
| 67 | MEDVEĐA | 2005-11-11 | BIZNISOFT | 91-067 | 2025-04-04 10:04:06 |
| 68 | MEROŠINA | 2005-11-11 | BIZNISOFT | 88-068 | 2025-04-04 10:04:06 |
| 69 | MIONICA | 2005-11-11 | BIZNISOFT | 85-069 | 2025-04-04 10:04:06 |
| 70 | MLADENOVAC | 2005-11-11 | BIZNISOFT | 82-070 | 2025-04-04 10:04:06 |
| 72 | NEGOTIN | 2005-11-11 | BIZNISOFT | 76-072 | 2025-04-04 10:04:06 |
| 74 | NOVA VAROŠ | 2005-11-11 | BIZNISOFT | 70-074 | 2025-04-04 10:04:06 |
| 75 | NOVI PAZAR | 2005-11-11 | BIZNISOFT | 67-075 | 2025-04-04 10:04:06 |
| 76 | OSEČINA | 2005-11-11 | BIZNISOFT | 64-076 | 2025-04-04 10:04:06 |
| 77 | PARAĆIN | 2005-11-11 | BIZNISOFT | 61-077 | 2025-04-04 10:04:06 |
| 78 | PETROVAC NA MLAVI | 2005-11-11 | BIZNISOFT | 58-078 | 2025-04-04 10:04:06 |
| 79 | PIROT | 2005-11-11 | BIZNISOFT | 55-079 | 2025-04-04 10:04:06 |
| 80 | POŽAREVAC | 2005-11-11 | BIZNISOFT | 52-080 | 2025-04-04 10:04:06 |
| 81 | POŽEGA | 2005-11-11 | BIZNISOFT | 49-081 | 2025-04-04 10:04:06 |
| 82 | PREŠEVO | 2005-11-11 | BIZNISOFT | 46-082 | 2025-04-04 10:04:06 |
| 83 | PRIBOJ | 2005-11-11 | BIZNISOFT | 43-083 | 2025-04-04 10:04:06 |
| 84 | PRIJEPOLJE | 2005-11-11 | BIZNISOFT | 40-084 | 2025-04-04 10:04:06 |
| 85 | PROKUPLJE | 2005-11-11 | BIZNISOFT | 37-085 | 2025-04-04 10:04:06 |
| 86 | RAČA | 2005-11-11 | BIZNISOFT | 34-086 | 2025-04-04 10:04:06 |
| 87 | RAŠKA | 2005-11-11 | BIZNISOFT | 31-087 | 2025-04-04 10:04:06 |
| 88 | RAŽANJ | 2005-11-11 | BIZNISOFT | 28-088 | 2025-04-04 10:04:06 |
| 89 | REKOVAC | 2005-11-11 | BIZNISOFT | 25-089 | 2025-04-04 10:04:06 |
| 91 | SJENICA | 2005-11-11 | BIZNISOFT | 19-091 | 2025-04-04 10:04:06 |
| 92 | SMEDEREVO | 2014-07-18 | BIZNISOFT | 16-092 | 2025-04-04 10:04:06 |
| 93 | SMEDEREVSKA PALANKA | 2005-11-11 | BIZNISOFT | 13-093 | 2025-04-04 10:04:06 |
| 94 | SOKOBANJA | 2005-11-11 | BIZNISOFT | 10-094 | 2025-04-04 10:04:06 |
| 95 | SURDULICA | 2005-11-11 | BIZNISOFT | 07-095 | 2025-04-04 10:04:06 |
| 96 | JAGODINA | 2005-11-11 | BIZNISOFT | 04-096 | 2025-04-04 10:04:06 |
| 97 | SVILAJNAC | 2005-11-11 | BIZNISOFT | 98-097 | 2025-04-04 10:04:06 |
| 98 | SVRLJIG | 2005-11-11 | BIZNISOFT | 95-098 | 2025-04-04 10:04:06 |
| 99 | ŠABAC | 2005-11-11 | BIZNISOFT | 92-099 | 2025-04-04 10:04:06 |
| 100 | UŽICE  | 2005-11-11 | BIZNISOFT | 89-100 | 2025-04-04 10:04:06 |
| 101 | TOPOLA | 2005-11-11 | BIZNISOFT | 86-101 | 2025-04-04 10:04:06 |
| 102 | TRGOVIŠTE | 2005-11-11 | BIZNISOFT | 83-102 | 2025-04-04 10:04:06 |
| 103 | TRSTENIK | 2005-11-11 | BIZNISOFT | 80-103 | 2025-04-04 10:04:06 |
| 104 | TUTIN | 2005-11-11 | BIZNISOFT | 77-104 | 2025-04-04 10:04:06 |
| 105 | UB | 2005-11-11 | BIZNISOFT | 74-105 | 2025-04-04 10:04:06 |
| 107 | VALJEVO | 2005-11-11 | BIZNISOFT | 68-107 | 2025-04-04 10:04:06 |
| 108 | VARVARIN | 2005-11-11 | BIZNISOFT | 65-108 | 2025-04-04 10:04:06 |
| 109 | VELIKA PLANA | 2005-11-11 | BIZNISOFT | 62-109 | 2025-04-04 10:04:06 |
| 110 | VELIKO GRADIŠTE | 2005-11-11 | BIZNISOFT | 59-110 | 2025-04-04 10:04:06 |
| 111 | VLADIČIN HAN | 2005-11-11 | BIZNISOFT | 56-111 | 2025-04-04 10:04:06 |
| 112 | VLADIMIRCI | 2005-11-11 | BIZNISOFT | 53-112 | 2025-04-04 10:04:06 |
| 113 | VLASOTINCE | 2005-11-11 | BIZNISOFT | 50-113 | 2025-04-04 10:04:06 |
| 114 | VRANJE | 2005-11-11 | BIZNISOFT | 47-114 | 2025-04-04 10:04:06 |
| 115 | VRNJAČKA BANJA | 2005-11-11 | BIZNISOFT | 44-115 | 2025-04-04 10:04:06 |
| 116 | ZAJEČAR | 2005-11-11 | BIZNISOFT | 41-116 | 2025-04-04 10:04:06 |
| 117 | ŽABARI | 2005-11-11 | BIZNISOFT | 38-117 | 2025-04-04 10:04:06 |
| 118 | ŽAGUBICA | 2005-11-11 | BIZNISOFT | 35-118 | 2025-04-04 10:04:06 |
| 119 | ŽITORAĐA | 2005-11-11 | BIZNISOFT | 32-119 | 2025-04-04 10:04:06 |
| 120 | RAKOVICA | 2005-11-11 | BIZNISOFT | 29-120 | 2025-04-04 10:04:06 |
| 121 | LAPOVO | 2005-11-11 | BIZNISOFT | 26-121 | 2025-04-04 10:04:06 |
| 122 | NIŠKA BANJA | 2005-11-11 | BIZNISOFT | 23-122 | 2025-04-04 10:04:06 |
| 123 | STRAGARI | 2005-11-11 | BIZNISOFT | 20-123 | 2025-04-04 10:04:06 |
| 124 | SURČIN | 2005-11-11 | BIZNISOFT | 17-124 | 2025-04-04 10:04:06 |
| 125 | PANTELEJ - NIŠ | 2005-11-11 | BIZNISOFT | 14-125 | 2025-04-04 10:04:06 |
| 126 | CRVENI KRST - NIŠ | 2005-11-11 | BIZNISOFT | 11-126 | 2025-04-04 10:04:06 |
| 127 | PALILULA - NIŠ | 2005-11-11 | BIZNISOFT | 08-127 | 2025-04-04 10:04:06 |
| 128 | MEDIJANA | 2005-11-11 | BIZNISOFT | 05-128 | 2025-04-04 10:04:06 |
| 129 | KOSTOLAC | 2019-12-10 | BIZNISOFT | 02-129 | 2025-04-04 10:04:06 |
| 130 | VRANJSKA BANJA | 2020-08-19 | BIZNISOFT | 96-130 | 2025-04-04 10:04:06 |
| 131 | SEVOJNO | 2020-08-19 | BIZNISOFT | 93-131 | 2025-04-04 10:04:06 |
| 201 | ADA | 2005-11-11 | BIZNISOFT | 77-201 | 2025-04-04 10:04:06 |
| 202 | ALIBUNAR | 2005-11-11 | BIZNISOFT | 74-202 | 2025-04-04 10:04:06 |
| 203 | APATIN | 2005-11-11 | BIZNISOFT | 71-203 | 2025-04-04 10:04:06 |
| 204 | BAČ | 2005-11-11 | BIZNISOFT | 68-204 | 2025-04-04 10:04:06 |
| 205 | BAČKA PALANKA | 2005-11-11 | BIZNISOFT | 65-205 | 2025-04-04 10:04:06 |
| 206 | BAČKA TOPOLA | 2005-11-11 | BIZNISOFT | 62-206 | 2025-04-04 10:04:06 |
| 207 | BAČKI PETROVAC | 2005-11-11 | BIZNISOFT | 59-207 | 2025-04-04 10:04:06 |
| 208 | BEČEJ | 2005-11-11 | BIZNISOFT | 56-208 | 2025-04-04 10:04:06 |
| 209 | BELA CRKVA | 2005-11-11 | BIZNISOFT | 53-209 | 2025-04-04 10:04:06 |
| 210 | BEOČIN | 2005-11-11 | BIZNISOFT | 50-210 | 2025-04-04 10:04:06 |
| 211 | ČOKA | 2005-11-11 | BIZNISOFT | 47-211 | 2025-04-04 10:04:06 |
| 212 | INĐIJA | 2005-11-11 | BIZNISOFT | 44-212 | 2025-04-04 10:04:06 |
| 213 | IRIG | 2005-11-11 | BIZNISOFT | 41-213 | 2025-04-04 10:04:06 |
| 214 | KANJIŽA | 2005-11-11 | BIZNISOFT | 38-214 | 2025-04-04 10:04:06 |
| 215 | KIKINDA | 2018-06-27 | BIZNISOFT | 35-215 | 2025-04-04 10:04:06 |
| 216 | KOVAČICA | 2005-11-11 | BIZNISOFT | 32-216 | 2025-04-04 10:04:06 |
| 217 | KOVIN | 2005-11-11 | BIZNISOFT | 29-217 | 2025-04-04 10:04:06 |
| 218 | KULA | 2005-11-11 | BIZNISOFT | 26-218 | 2025-04-04 10:04:06 |
| 219 | MALI IĐOŠ | 2005-11-11 | BIZNISOFT | 23-219 | 2025-04-04 10:04:06 |
| 220 | NOVA CRNJA | 2005-11-11 | BIZNISOFT | 20-220 | 2025-04-04 10:04:06 |
| 221 | NOVI BEČEJ | 2005-11-11 | BIZNISOFT | 17-221 | 2025-04-04 10:04:06 |
| 222 | NOVI KNEŽEVAC | 2005-11-11 | BIZNISOFT | 14-222 | 2025-04-04 10:04:06 |
| 223 | NOVI SAD | 2005-11-11 | BIZNISOFT | 11-223 | 2025-04-04 10:04:06 |
| 224 | ODŽACI | 2005-11-11 | BIZNISOFT | 08-224 | 2025-04-04 10:04:06 |
| 225 | OPOVO | 2005-11-11 | BIZNISOFT | 05-225 | 2025-04-04 10:04:06 |
| 226 | PANČEVO | 2005-11-11 | BIZNISOFT | 02-226 | 2025-04-04 10:04:06 |
| 227 | PEĆINCI | 2005-11-11 | BIZNISOFT | 96-227 | 2025-04-04 10:04:06 |
| 228 | PLANDIŠTE | 2005-11-11 | BIZNISOFT | 93-228 | 2025-04-04 10:04:06 |
| 229 | RUMA | 2005-11-11 | BIZNISOFT | 90-229 | 2025-04-04 10:04:06 |
| 230 | SEČANJ | 2005-11-11 | BIZNISOFT | 87-230 | 2025-04-04 10:04:06 |
| 231 | SENTA | 2005-11-11 | BIZNISOFT | 84-231 | 2025-04-04 10:04:06 |
| 232 | SOMBOR | 2005-11-11 | BIZNISOFT | 81-232 | 2025-04-04 10:04:06 |
| 233 | SRBOBRAN | 2005-11-11 | BIZNISOFT | 78-233 | 2025-04-04 10:04:06 |
| 234 | SREMSKA MITROVICA | 2005-11-11 | BIZNISOFT | 75-234 | 2025-04-04 10:04:06 |
| 235 | STARA PAZOVA | 2005-11-11 | BIZNISOFT | 72-235 | 2025-04-04 10:04:06 |
| 236 | SUBOTICA | 2005-11-11 | BIZNISOFT | 69-236 | 2025-04-04 10:04:06 |
| 237 | ŠID | 2005-11-11 | BIZNISOFT | 66-237 | 2025-04-04 10:04:06 |
| 238 | TEMERIN | 2005-11-11 | BIZNISOFT | 63-238 | 2025-04-04 10:04:06 |
| 239 | TITEL | 2005-11-11 | BIZNISOFT | 60-239 | 2025-04-04 10:04:06 |
| 240 | VRBAS | 2005-11-11 | BIZNISOFT | 57-240 | 2025-04-04 10:04:06 |
| 241 | VRŠAC | 2005-11-11 | BIZNISOFT | 54-241 | 2025-04-04 10:04:06 |
| 242 | ZRENJANIN | 2005-11-11 | BIZNISOFT | 51-242 | 2025-04-04 10:04:06 |
| 243 | ŽABALJ | 2005-11-11 | BIZNISOFT | 48-243 | 2025-04-04 10:04:06 |
| 244 | ŽITIŠTE | 2005-11-11 | BIZNISOFT | 45-244 | 2025-04-04 10:04:06 |
| 247 | PETROVARADIN | 2005-11-11 | BIZNISOFT | 36-247 | 2025-04-04 10:04:06 |
| 250 | SREMSKI KARLOVCI | 2005-11-11 | BIZNISOFT | 27-250 | 2025-04-04 10:04:06 |
| 301 | DEČANI | 2005-11-11 | BIZNISOFT | 68-301 | 2025-04-04 10:04:06 |
| 303 | ĐAKOVICA | 2005-11-11 | BIZNISOFT | 62-303 | 2025-04-04 10:04:06 |
| 304 | GLOGOVAC | 2005-11-11 | BIZNISOFT | 59-304 | 2025-04-04 10:04:06 |
| 305 | GNJILANE | 2019-12-10 | BIZNISOFT | 56-305 | 2025-04-04 10:04:06 |
| 306 | ISTOK | 2005-11-11 | BIZNISOFT | 53-306 | 2025-04-04 10:04:06 |
| 307 | KAČANIK | 2005-11-11 | BIZNISOFT | 50-307 | 2025-04-04 10:04:06 |
| 308 | KLINA | 2005-11-11 | BIZNISOFT | 47-308 | 2025-04-04 10:04:06 |
| 309 | KOSOVSKA KAMENICA | 2005-11-11 | BIZNISOFT | 44-309 | 2025-04-04 10:04:06 |
| 310 | KOSOVSKA MITROVICA | 2005-11-11 | BIZNISOFT | 41-310 | 2025-04-04 10:04:06 |
| 311 | LEPOSAVIĆ | 2005-11-11 | BIZNISOFT | 38-311 | 2025-04-04 10:04:06 |
| 312 | LIPLJAN | 2005-11-11 | BIZNISOFT | 35-312 | 2025-04-04 10:04:06 |
| 313 | ORAHOVAC | 2005-11-11 | BIZNISOFT | 32-313 | 2025-04-04 10:04:06 |
| 314 | PEĆ | 2005-11-11 | BIZNISOFT | 29-314 | 2025-04-04 10:04:06 |
| 315 | PODUJEVO | 2005-11-11 | BIZNISOFT | 26-315 | 2025-04-04 10:04:06 |
| 316 | PRIŠTINA | 2005-11-11 | BIZNISOFT | 23-316 | 2025-04-04 10:04:06 |
| 317 | PRIZREN | 2005-11-11 | BIZNISOFT | 20-317 | 2025-04-04 10:04:06 |
| 318 | SRBICA | 2005-11-11 | BIZNISOFT | 17-318 | 2025-04-04 10:04:06 |
| 319 | SUVA REKA | 2005-11-11 | BIZNISOFT | 14-319 | 2025-04-04 10:04:06 |
| 320 | UROŠEVAC | 2005-11-11 | BIZNISOFT | 11-320 | 2025-04-04 10:04:06 |
| 321 | VITINA | 2005-11-11 | BIZNISOFT | 08-321 | 2025-04-04 10:04:06 |
| 322 | VUČITRN | 2005-11-11 | BIZNISOFT | 05-322 | 2025-04-04 10:04:06 |
| 324 | ZUBIN POTOK | 2005-11-11 | BIZNISOFT | 96-324 | 2025-04-04 10:04:06 |
| 325 | ŠTIMLJE | 2005-11-11 | BIZNISOFT | 93-325 | 2025-04-04 10:04:06 |
| 326 | ŠTRPCE | 2005-11-11 | BIZNISOFT | 90-326 | 2025-04-04 10:04:06 |
| 327 | OBILIĆ | 2005-11-11 | BIZNISOFT | 87-327 | 2025-04-04 10:04:06 |
| 328 | KOSOVO POLJE | 2005-11-11 | BIZNISOFT | 84-328 | 2025-04-04 10:04:06 |
| 329 | NOVO BRDO | 2005-11-11 | BIZNISOFT | 81-329 | 2025-04-04 10:04:06 |
| 330 | ZVEČAN | 2005-11-11 | BIZNISOFT | 78-330 | 2025-04-04 10:04:06 |
| 331 | DRAGAŠ (GORA) | 2005-11-11 | BIZNISOFT | 75-331 | 2025-04-04 10:04:06 |
| 501 | GRAD BEOGRAD | 2005-11-11 | BIZNISOFT | 50-501 | 2025-04-04 10:04:06 |
| 511 | GRAD NOVI SAD | 2005-11-11 | BIZNISOFT | 20-511 | 2025-04-04 10:04:06 |
| 521 | GRAD NIŠ | 2005-11-11 | BIZNISOFT | 87-521 | 2025-04-04 10:04:06 |
| 531 | GRAD KRAGUJEVAC | 2005-11-11 | BIZNISOFT | 57-531 | 2025-04-04 10:04:06 |
| 541 | GRAD PRIŠTINA | 2005-11-11 | BIZNISOFT | 27-541 | 2025-04-04 10:04:06 |
| 581 | AP VOJVODINA | 2005-11-11 | BIZNISOFT | 04-581 | 2025-04-04 10:04:06 |
| 591 | AP KOSOVO I METOHIJA | 2005-11-11 | BIZNISOFT | 71-591 | 2025-04-04 10:04:06 |
| 601 | REPUBLIKA SRBIJA | 2005-11-11 | BIZNISOFT | 41-601 | 2025-04-04 10:04:06 |

---

## Tabela: `cnfg_klasifikacija`
**Opis:** Konfiguracija - klasifikacija
**Redova:** 15

**Kolone:** `sifra`, `naziv`

| sifra | naziv |
| --- | --- |
| 101 | Osnovna podešavanja |
| 102 | Knjigovodstveni podaci |
| 103 | BizniSoft POS - osnovno |
| 104 | BizniSoft POS - dozvole |
| 105 | BizniSoft POS - fiskalni uređaj |
| 106 | Podešavanje dokumenta |
| 107 | Dislocirani objekti |
| 108 | Specifični podsistemi i ostale funkcije |
| 109 | BizniSoft Assistant |
| 130 | Elektronska fiskalizacija - Crna Gora |
| 201 | Specifična ovlašćenja |
| 202 | Provera kompleksnosti lozinke |
| 301 | Postavke fontova |
| 311 | BizniSoft dnevnik |
| 401 | Definisanje knjigovodstvenih računa |

---

## Tabela: `cnfg_vrste`
**Opis:** Konfiguracija - vrste
**Redova:** 4

**Kolone:** `sifra`, `naziv`

| sifra | naziv |
| --- | --- |
| 1 | Konfiguracija |
| 2 | Ovlašćenje |
| 3 | Status |
| 4 | Specifikacija knjigovodstvenih računa |

---

## Tabela: `finiz_vp`
**Opis:** Finansijski izveštaji - vrste
**Redova:** 7

**Kolone:** `finizvp`, `opis`, `srtpol`

| finizvp | opis | srtpol |
| --- | --- | --- |
| 300 | Sindikalne organizacije | 4 |
| 570 | Banke i druge finansijske organizacije | 6 |
| 580 | Davaoci finansijskog lizinga | 7 |
| 750 | Privredna društva (preduzeća) i zadruge | 1 |
| 751 | Druga pravna lica | 2 |
| 753 | Ogranci i drugi delovi stranih pravnih lica | 5 |
| 755 | Preduzetnici | 3 |

---

## Tabela: `fiz_vrste`
**Opis:** Finansijski izveštaji - vrste (2)
**Redova:** 40

**Kolone:** `siffinizv`, `naziv`, `tip`, `kontniplan`, `aoptip`, `setparametra`

| siffinizv | naziv | tip | kontniplan | aoptip | setparametra |
| --- | --- | --- | --- | --- | --- |
| 1 | BILANS STANJA - MIKRO | 1 | KPL2014PDP | 1 | 1 |
| 2 | BILANS USPEHA - MIKRO | 1 | KPL2014PDP | 2 | 1 |
| 3 | STATISTIČKI IZVEŠTAJ | 3 | KPL2014PDP | 3 | 1 |
| 4 | BILANS STANJA | 2 | KPL2014PDP | 1 | 1 |
| 5 | BILANS USPEHA | 2 | KPL2014PDP | 2 | 1 |
| 6 | IZVEŠTAJ O OSTALOM REZULTATU | 2 | KPL2014PDP | 4 | 1 |
| 7 | IZVEŠTAJ O TOKOVIMA GOTOVINE | 2 | KPL2014PDP | 5 | 1 |
| 8 | IZVEŠTAJ O PROMENAMA NA KAPITALU | 2 | KPL2014PDP | 6 | 1 |
| 9 | BILANS STANJA DRUGA PRAVNA LICA | 1 | KPL2014DPL | 1 | 1 |
| 10 | BILANS USPEHA DRUGA PRAVNA LICA | 1 | KPL2014DPL | 2 | 1 |
| 11 | STATISTIČKI IZVEŠTAJ DRUGA PRAVNA LICA | 1 | KPL2014DPL | 3 | 1 |
| 12 | BILANS STANJA OLD | 1 | KPL2013OLD | 1 | 1 |
| 13 | BILANS USPEHA OLD | 1 | KPL2013OLD | 2 | 1 |
| 14 | STATISTIČKI ANEKS | 1 | KPL2013OLD | 3 | 1 |
| 15 | BILANS STANJA CG | 1 | KPL2013OLD | 1 | 1 |
| 16 | BILANS USPJEHA CG | 1 | KPL2013OLD | 2 | 1 |
| 17 | BILANS STANJA DRUŠTVA ZA UPRAVLJANJE INVESTICIONIM FONDOVIMA | 2 | KPL2014IFN | 1 | 1 |
| 18 | BILANS USPEHA DRUŠTVA ZA UPRAVLJANJE INVESTICIONIM FONDOVIMA | 2 | KPL2014IFN | 2 | 1 |
| 19 | IZVEŠTAJ O OSTALOM REZULTATU DRUŠTVA ZA UPRAVLJANJE INVESTICIONIM FONDOVIMA | 2 | KPL2014IFN | 4 | 1 |
| 20 | STATISTIČKI IZVEŠTAJ DRUŠTVA ZA UPRAVLJANJE INVESTICIONIM FONDOVIMA | 2 | KPL2014IFN | 3 | 1 |
| 21 | IZVEŠTAJ O TOKOVIMA GOTOVINE DRUŠTVA ZA UPRAVLJANJE INVESTICIONIM FONDOVIMA | 2 | KPL2014IFN | 5 | 1 |
| 22 | IZVEŠTAJ O PROMENAMA NA KAPITALU DRUŠTVA ZA UPRAVLJANJE INVESTICIONIM FONDOVIMA | 2 | KPL2014IFN | 6 | 1 |
| 31 | BILANS STANJA - MIKRO | 1 | KPL2021PDP | 1 | 1 |
| 32 | BILANS USPEHA - MIKRO | 1 | KPL2021PDP | 2 | 1 |
| 33 | STATISTIČKI IZVEŠTAJ | 3 | KPL2021PDP | 3 | 1 |
| 34 | BILANS STANJA | 2 | KPL2021PDP | 1 | 1 |
| 35 | BILANS USPEHA | 2 | KPL2021PDP | 2 | 1 |
| 36 | IZVEŠTAJ O OSTALOM REZULTATU | 2 | KPL2021PDP | 4 | 1 |
| 37 | IZVEŠTAJ O TOKOVIMA GOTOVINE | 2 | KPL2021PDP | 5 | 1 |
| 38 | IZVEŠTAJ O PROMENAMA NA KAPITALU | 2 | KPL2021PDP | 6 | 1 |
| 39 | BILANS STANJA DRUGA PRAVNA LICA | 1 | KPL2021DPL | 1 | 1 |
| 40 | BILANS USPEHA DRUGA PRAVNA LICA | 1 | KPL2021DPL | 2 | 1 |
| 41 | STATISTIČKI IZVEŠTAJ DRUGA PRAVNA LICA | 1 | KPL2021DPL | 3 | 1 |
| 42 | NAPOMENE UZ FINANSIJSKE IZVEŠTAJE | 1 | KPL2021PDP | 7 | 1 |
| 43 | NAPOMENE UZ FINANSIJSKE IZVEŠTAJE | 2 | KPL2021PDP | 7 | 1 |
| 44 | BILANS STANJA DRUGA PRAVNA LICA | 2 | KPL2021DPL | 1 | 1 |
| 45 | BILANS USPEHA DRUGA PRAVNA LICA | 2 | KPL2021DPL | 2 | 1 |
| 46 | STATISTIČKI IZVEŠTAJ DRUGA PRAVNA LICA | 2 | KPL2021DPL | 3 | 1 |
| 50 | ISKAZ O FINANSIJSKOJ POZICIJI /BILANS STANJA/ | 1 | KPL2013OLD | 1 | 1 |
| 51 | ISKAZ O UKUPNOM REZULTATU /BILANS USPJEHA/ | 1 | KPL2013OLD | 2 | 1 |

---

## Tabela: `fiz_celine`
**Opis:** Finansijski izveštaji - celine
**Redova:** 142

**Kolone:** `siffinizv`, `sifceline`, `naziv`

| siffinizv | sifceline | naziv |
| --- | --- | --- |
| 1 | 1 | AKTIVA |
| 1 | 2 | PASIVA |
| 2 | 1 | PRIHODI IZ REDOVNOG POSLOVANJA |
| 2 | 2 | RASHODI IZ REDOVNOG POSLOVANJA |
| 3 | 1 | I. OPŠTI PODACI O PRAVNOM LICU I PREDUZETNIKU |
| 3 | 2 | II. BRUTO PROMENE NEMATERIJALNE IMOVINE I NEKRETNINA, POSTROJENJA, OPREME I BIOLOŠKIH SREDSTAVA |
| 3 | 3 | III. STRUKTURA OSNOVNOG KAPITALA |
| 3 | 4 | IV. STRUKTURA AKCIJSKOG KAPITALA |
| 3 | 5 | V. STRUKTURA ISPLAĆENIH DIVIDENDI I UČEŠĆA U DOBITKU, PO SEKTORIMA |
| 3 | 6 | VI. POTRAŽIVANJA I OBAVEZE |
| 3 | 7 | VII. DRUGI TROŠKOVI I RASHODI |
| 3 | 8 | VIII. DRUGI PRIHODI |
| 3 | 9 | IX. OSTALI PODACI |
| 3 | 10 | RAZGRANIČENI NEGATIVNI NETO EFEKTI UGOVORENE VALUTNE KLAUZULE I KURSNIH RAZLIKA |
| 3 | 11 | XI. RAZGRANIČENI POZITIVNI NETO EFEKTI UGOVORENE VALUTNE KLAUZULE I KURSNIH RAZLIKA |
| 3 | 12 | XII. BRUTO POTRAŽIVANJA ZA DATE KREDITE I ZAJMOVE, PRODATE PROIZVODE, ROBU I USLUGE I DATE AVANSE U  |
| 4 | 1 | AKTIVA |
| 4 | 2 | PASIVA |
| 5 | 1 | PRIHODI IZ REDOVNOG POSLOVANJA |
| 5 | 2 | RASHODI IZ REDOVNOG POSLOVANJA |
| 6 | 1 | IZVEŠTAJ O OSTALOM REZULTATU |
| 7 | 1 | IZVEŠTAJ O TOKOVIMA GOTOVINE |
| 8 | 3 | Osnovni kapital |
| 8 | 4 | Upisani a neuplaćeni kapital |
| 8 | 5 | Rezerve |
| 8 | 6 | Gubitak |
| 8 | 7 | Otkupljene sopstvene akcije |
| 8 | 8 | Neraspoređeni dobitak |
| 8 | 9 | Revalorizacione rezerve |
| 8 | 10 | Aktuarski dobici ili gubici |
| 8 | 11 | Dobici ili gubici po osnovu ulaganja u vlasničke isntrumente kapitala |
| 8 | 12 | Dobici ili gubici na osnovu udela u ostalom dobitku ili gubitku pridruženih društava |
| 8 | 13 | Dobici ili gubici po osnovu iostranog poslovanja i preračuna finansijkih izveštaja |
| 8 | 14 | Dobici ili gubici po osnovu hrdžinga novčanog toka |
| 8 | 15 | Dobici ili gubici po osnovu hov raspoloživih za prodaju |
| 8 | 16 | Ukupan kapital [Ʃ(red 1b kol 3 do kol 15)- Ʃ(red 1a kol 3 do kol 15) ]≥0 |
| 8 | 17 | Gubitak iznad kapitala [Ʃ(red 1a kol 3 do kol 15)- Ʃ(red 1b kol 3 do kol 15) ]≥0 |
| 9 | 1 | AKTIVA |
| 9 | 2 | PASIVA |
| 10 | 1 | POSLOVNI PRIHODI |
| 10 | 2 | POSLOVNI RASHODI |
| 11 | 1 | I. OPŠTI PODACI O DRUGOM PRAVNOM LICU |
| 11 | 2 | II. POTRAŽIVANJA I OBAVEZE |
| 11 | 3 | III. DRUGI TROŠKOVI I RASHODI |
| 11 | 4 | IV. DRUGI PRIHODI |
| 11 | 5 | V. OSTALI PODACI |
| 11 | 6 | VI. RAZGRANIČENI NEGATIVNI NETO EFEKTI UGOVORENE VALUTNE KLAUZULE I KURSNIH RAZLIKA |
| 11 | 7 | VII. RAZGRANIČENI POZITIVNI NETO EFEKTI UGOVORENE VALUTNE KLAUZULE I KURSNIH RAZLIKA |
| 12 | 1 | AKTIVA |
| 12 | 2 | PASIVA |
| 13 | 1 | A. PRIHODI I RASHODI IZ REDOVNOG POSLOVANJA I. POSLOVNI PRIHODI |
| 14 | 1 | I. OPŠTI PODACI O PRAVNOM LICU, ODNOSNO PREDUZETNIKU |
| 14 | 2 | II. BRUTO PROMENE NEMATERIJALNIH ULAGANJA I NEKRETNINA, POSTROJENJA, OPREME I BIOLOŠKIH SREDSTAVA |
| 14 | 3 | III. STRUKTURA ZALIHA |
| 14 | 4 | IV. STRUKTURA OSNOVNOG KAPITALA |
| 14 | 5 | IV. STRUKTURA AKCIJSKOG KAPITALA |
| 14 | 6 | VI. POTRAŽIVANJA I OBAVEZE |
| 14 | 7 | VII. DRUGI TROŠKOVI I RASHODI |
| 14 | 8 | VIII. DRUGI PRIHODI |
| 14 | 9 | IX. OSTALI PODACI |
| 14 | 10 | RAZGRANIČENI NEGATIVNI NETO EFEKTI UGOVORENE VALUTNE KLAUZULE I KURSNIH RAZLIKA |
| 14 | 11 | XI. RAZGRANIČENI POZITIVNI NETO EFEKTI UGOVORENE VALUTNE KLAUZULE I KURSNIH RAZLIKA |
| 15 | 1 | AKTIVA |
| 15 | 2 | PASIVA |
| 16 | 1 | I. POSLOVNI PRIHODI (202 do 206) |
| 17 | 1 | АКТИВА |
| 17 | 2 | ПАСИВА |
| 18 | 1 | А.ПОСЛОВНИ ПРИХОДИ И РАСХОДИ |
| 18 | 2 | Б.ФИНАНСИЈСКИ ПРИХОДИ И РАСХОДИ |
| 19 | 1 | ИЗВЕШТАЈ О ОСТАЛОМ РЕЗУЛТАТУ ДРУШТВА ЗА УПРАВЉАЊЕ ИНВЕСТИЦИОНИМ ФОНДОВИМА |
| 20 | 1 | ОПШТИ ПОДАЦИ О ОБВЕЗНИКУ |
| 20 | 2 | ПРОМЕНЕ НЕМАТЕРИЈАЛНЕ И МАТЕРЈАЛНЕ ИМОВИНЕ |
| 20 | 3 | СТРУКТУРА ОСНОВНОГ КАПИТАЛА |
| 20 | 4 | СТРУКТУРА АКЦИЈСКОГ КАПИТАЛА |
| 20 | 5 | ПОТРАЖИВАЊА И ОБАВЕЗЕ |
| 20 | 6 | ДРУГИ ТРОШКОВИ И РАСХОДИ |
| 20 | 7 | ДРУГИ ПРИХОДИ |
| 21 | 1 | ИЗВЕШТАЈ О ТОКОВИМА ГОТОВИНЕ ДРУШТВА ЗА УПРАВЉАЊЕ ИНВЕСТИЦИОНИМ ФОНДОВИМА |
| 22 | 3 | 30 Основни капитал |
| 22 | 4 | 31 Уписани а неуплаћени капитал |
| 22 | 5 | 32 и 33 Резерве |
| 22 | 6 | 36 Губитак |
| 22 | 7 | 032 и 232 Откупљење сопствене акције |
| 22 | 8 | 35 Нераспоређени добитак |
| 22 | 9 | 340 ревалор. резерве |
| 22 | 10 | 341, 343 нереализовани добици по основу ХОВ |
| 22 | 11 | 342, 344 нереализовани губици по основу ХОВ |
| 22 | 12 | Укупан (ред б кол 3 до кол 11) - (ред а кол 3 до кол 11) >/0 |
| 22 | 13 | Губитак изнад висине капитала (ред а кол 3 до кол 11) -(ред б кол 3 до 11)>0/ |
| 31 | 1 | AKTIVA |
| 31 | 2 | PASIVA |
| 32 | 1 | PRIHODI IZ REDOVNOG POSLOVANJA |
| 32 | 2 | RASHODI IZ REDOVNOG POSLOVANJA |
| 33 | 1 | I. OPŠTI PODACI O PRAVNOM LICU I PREDUZETNIKU |
| 33 | 2 | II. BRUTO PROMENE NEMATERIJALNE IMOVINE I NEKRETNINA, POSTROJENJA, OPREME I BIOLOŠKIH SREDSTAVA |
| 33 | 3 | III. STRUKTURA ZALIHA |
| 33 | 4 | IV. STRUKTURA OSNOVNOG KAPITALA |
| 33 | 5 | V. STRUKTURA AKCIJSKOG KAPITALA |
| 33 | 6 | VI. STRUKTURA ISPLAĆENIH DIVIDENDI I UČEŠĆA U DOBITKU, PO SEKTORIMA |
| 33 | 7 | VII. POTRAŽIVANJA I OBAVEZE |
| 33 | 8 | VIII. DRUGI TROŠKOVI I RASHODI |
| 33 | 9 | IX. RASHODI KAMATA |
| 33 | 10 | X. DRUGI PRIHODI |
| 33 | 11 | XI. PRIHODI OD KAMATA |
| 33 | 12 | XII. OSTALI PODACI |
| 33 | 13 | XIII. BRUTO POTRAŽIVANJA ZA DATE KREDITE I ZAJMOVE, PRODATE PROIZVODE, ROBU I USLUGE I DATE AVANSE I |
| 34 | 1 | AKTIVA |
| 34 | 2 | PASIVA |
| 35 | 1 | POSLOVNI PRIHODI |
| 35 | 2 | POSLOVNI RASHODI |
| 36 | 1 | IZVEŠTAJ O OSTALOM REZULTATU |
| 37 | 1 | IZVEŠTAJ O TOKOVIMA GOTOVINE |
| 38 | 1 | Osnovni kapital |
| 39 | 1 | AKTIVA |
| 39 | 2 | PASIVA |
| 40 | 1 | POSLOVNI PRIHODI |
| 40 | 2 | POSLOVNI RASHODI |
| 41 | 1 | I. OPŠTI PODACI O DRUGOM PRAVNOM LICU |
| 41 | 2 | II. BRUTO PROMENE NEMATERIJALNE IMOVINE, NEKRETNINA, POSTROJENJA, OPREME I BIOLOŠKIH SREDSTAVA |
| 41 | 3 | III. STRUKTURA ZALIHA |
| 41 | 4 | IV. OBAVEZE |
| 41 | 5 | V. DRUGI TROŠKOVI I RASHODI |
| 41 | 6 | VI. RASHODI KAMATA |
| 41 | 7 | VII. DRUGI PRIHODI |
| 41 | 8 | VIII. PRIHODI OD KAMATA |
| 41 | 9 | XII. OSTALI PODACI |
| 44 | 1 | AKTIVA |
| 44 | 2 | PASIVA |
| 45 | 1 | POSLOVNI PRIHODI |
| 45 | 2 | POSLOVNI RASHODI |
| 46 | 1 | I. OPŠTI PODACI O DRUGOM PRAVNOM LICU |
| 46 | 2 | II. BRUTO PROMENE NEMATERIJALNE IMOVINE, NEKRETNINA, POSTROJENJA, OPREME I BIOLOŠKIH SREDSTAVA |
| 46 | 3 | III. STRUKTURA ZALIHA |
| 46 | 4 | IV. OBAVEZE |
| 46 | 5 | V. DRUGI TROŠKOVI I RASHODI |
| 46 | 6 | VI. RASHODI KAMATA |
| 46 | 7 | VII. DRUGI PRIHODI |
| 46 | 8 | VIII. PRIHODI OD KAMATA |
| 46 | 9 | XII. OSTALI PODACI |
| 50 | 1 | AKTIVA |
| 50 | 2 | PASIVA |
| 51 | 1 | BILANS USPJEHA |

---

## Tabela: `sifobj`
**Opis:** Šifarnik objekata
**Redova:** 19

**Kolone:** `sifra`, `naziv`, `racun`, `sifcene`

| sifra | naziv | racun | sifcene |
| --- | --- | --- | --- |
| 1 | M A L O P R O D A J A | BSRN0017 | mpc |
| 2 | MAGACIN ROBE - PO VP CENAMA | BSRN0011 | vpc |
| 3 | ROBA U CARINSKOM SKLADIŠTU | BSRN0185 | nbc |
| 4 | ROBA DATA U KOMISION - MALOPRODAJA | BSRN0013 | mpc |
| 5 | ROBA DATA U KOMISION - VELEPRODAJA | BSRN0014 | vpc |
| 6 | PRIMLJENA KOMISIONA ROBA - MALOPRODAJE | BSRN0116 | mpc |
| 7 | PRIMLJENA KOMISIONA ROBA - VELEPRODAJA | BSRN0115 | vpc |
| 8 | MAGACIN ROBE - PO NABAVNIM CENAMA | BSRN0009 | nbc |
| 9 | MAGACIN GOTOVIH PROIZVODA | BSRN0131 | nbc |
| 10 | MAGACIN REPROMATERIJALA | BSRN0002 | nbc |
| 11 | MAGACIN POLUPROIZVODA | BSRN0130 | nbc |
| 12 | ROBA U TRANZITU | BSRN0193 | nbc |
| 18 | PROIZVODNA JEDINICA | BSRN0124 | nbc |
| 20 | PROIZVODNJA I MALOPRODAJA PROIZVODA | BSRN0002 | mpc |
| 21 | SITAN INVENTAR NA ZALIHAMA | BSRN0005 | nbc |
| 22 | SITAN INVENTAR U UPOTREBI | BSRN0142 | nbc |
| 23 | SITAN INVENTAR ZADUŽEN PO RADNICIMA | BSRN0142 | nbc |
| 98 | B L A G A J N E |  | xxx |
| 99 | OSTALO - OBJEKAT BEZ ROBE |  | xxx |

---

## Tabela: `sifplac`
**Opis:** Šifarnik plaćanja
**Redova:** 200

**Kolone:** `sifra`, `naziv`

| sifra | naziv |
| --- | --- |
| 120 | PROMET ROBE I USLUGA - MEĐUFAZNA POTROŠNJA |
| 121 | PROMET ROBE I USLUGA -  FINALNA POTROŠNJA |
| 122 | USLUGE JAVNIH PREDUZEĆA |
| 123 | INVESTICIJE U OBJEKTE I OPREMU |
| 124 | INVESTICIJE - OSTALO |
| 125 | ZAKUPNINE |
| 126 | ZAKUPNINE |
| 127 | SUBVENCIJE, REGRESI I PREMIJE S POSEBNIH RAČUNA |
| 128 | SUBVENCIJE, REGRESI I PREMIJE SA OSTALIH RAČUNA |
| 131 | CARINE I DRUGE UVOZNE DAŽBINE |
| 140 | ZARADE I DRUGA PRIMANJA ZAPOSLENIH |
| 141 | NEOPOREZIVA PRIMANJA ZAPOSLENIH I OBUSTAVE OD ZARA |
| 142 | NAKNADE ZARADA NA TERET POSLODAVCA |
| 144 | ISPLATE PREKO OMLADINSKIH I STUDENTSKIH ZADRUGA |
| 145 | PENZIJE |
| 146 | OBUSTAVE OD PENZIJA |
| 147 | NAKNADE ZARADA NA TERET DRUGIH ISPLATILACA |
| 148 | PRIHODI FIZIČKIH LICA OD KAPITALA I DRUGIH IMOVINS |
| 149 | OSTALI PRIHODI FIZIČKIH LICA |
| 153 | UPLATA JAVNIH PRIHODA IZUZEV POREZA I DOPRINOSA PO |
| 154 | UPLATA POREZA I DOPRINOSA PO ODBITKU |
| 157 | POVRAĆAJ VIŠE NAPLAĆENIH ILI POGREŠNO NAPLAĆENIH T |
| 158 | PREKNJIŽAVANJE VIŠE UPLAĆENIH ILI POGREŠNO UPLAĆEN |
| 160 | PREMIJE OSIGURANJA I NADOKNADA ŠTETE |
| 161 | RASPORED TEKUĆIH PRIHODA |
| 162 | TRANSFERI U OKVIRU DRŽAVNIH ORGANA |
| 163 | OSTALI TRANSFERI |
| 164 | PRENOS SREDSTAVA IZ BUDŽETA ZA OBEZBEĐENJE POVRAĆA |
| 165 | UPLATA PAZARA |
| 166 | ISPLATA GOTOVINE |
| 170 | KRATKOROČNI KREDITI |
| 171 | DUGOROČNI KREDITI |
| 172 | AKTIVNA KAMATA |
| 173 | POLAGANJE OROČENIH DEPOZITA |
| 175 | OSTALI PLASMANI |
| 176 | OTPLATA KRATKOROČNIH KREDITA |
| 177 | OTPLATA DUGOROČNIH KREDITA |
| 178 | POVRAĆAJ OROČENIH DEPOZITA |
| 179 | PASIVNA KAMATA |
| 180 | ESKONT HARTIJA OD VREDNOSTI |
| 181 | POZAJMICE OSNIVAČA ZA LIKVIDNOST |
| 182 | POVRAĆAJ POZAJMICE ZA LIKVIDNOST OSNIVAČU |
| 183 | NAPLATA ČEKOVA GRAĐANA |
| 184 | PLATNE KARTICE |
| 185 | MENJAČKI POSLOVI |
| 186 | KUPOPRODAJA DEVIZA |
| 187 | DONACIJE I SPONZORSTVA |
| 188 | DONACIJE |
| 189 | TRANSAKCIJE PO NALOGU GRAĐANA |
| 190 | DRUGE TRANSAKCIJE |
| 220 | PROMET ROBE I USLUGA - MEĐUFAZNA POTROŠNJA |
| 221 | PROMET ROBE I USLUGA -  FINALNA POTROŠNJA |
| 222 | USLUGE JAVNIH PREDUZEĆA |
| 223 | INVESTICIJE U OBJEKTE I OPREMU |
| 224 | INVESTICIJE - OSTALO |
| 225 | ZAKUPNINE |
| 226 | ZAKUPNINE |
| 227 | SUBVENCIJE, REGRESI I PREMIJE S POSEBNIH RAČUNA |
| 228 | SUBVENCIJE, REGRESI I PREMIJE SA OSTALIH RAČUNA |
| 231 | CARINE I DRUGE UVOZNE DAŽBINE |
| 240 | ZARADE I DRUGA PRIMANJA ZAPOSLENIH |
| 241 | NEOPOREZIVA PRIMANJA ZAPOSLENIH I OBUSTAVE OD ZARA |
| 242 | NAKNADE ZARADA NA TERET POSLODAVCA |
| 244 | ISPLATE PREKO OMLADINSKIH I STUDENTSKIH ZADRUGA |
| 245 | PENZIJE |
| 246 | OBUSTAVE OD PENZIJA |
| 247 | NAKNADE ZARADA NA TERET DRUGIH ISPLATILACA |
| 248 | PRIHODI FIZIČKIH LICA OD KAPITALA I DRUGIH IMOVINS |
| 249 | OSTALI PRIHODI FIZIČKIH LICA |
| 253 | UPLATA JAVNIH PRIHODA IZUZEV POREZA I DOPRINOSA PO |
| 254 | UPLATA POREZA I DOPRINOSA PO ODBITKU |
| 257 | POVRAĆAJ VIŠE NAPLAĆENIH ILI POGREŠNO NAPLAĆENIH T |
| 258 | PREKNJIŽAVANJE VIŠE UPLAĆENIH ILI POGREŠNO UPLAĆEN |
| 260 | PREMIJE OSIGURANJA I NADOKNADA ŠTETE |
| 261 | RASPORED TEKUĆIH PRIHODA |
| 262 | TRANSFERI U OKVIRU DRŽAVNIH ORGANA |
| 263 | OSTALI TRANSFERI |
| 264 | PRENOS SREDSTAVA IZ BUDŽETA ZA OBEZBEĐENJE POVRAĆA |
| 265 | UPLATA PAZARA |
| 266 | ISPLATA GOTOVINE |
| 270 | KRATKOROČNI KREDITI |
| 271 | DUGOROČNI KREDITI |
| 272 | AKTIVNA KAMATA |
| 273 | POLAGANJE OROČENIH DEPOZITA |
| 275 | OSTALI PLASMANI |
| 276 | OTPLATA KRATKOROČNIH KREDITA |
| 277 | OTPLATA DUGOROČNIH KREDITA |
| 278 | POVRAĆAJ OROČENIH DEPOZITA |
| 279 | PASIVNA KAMATA |
| 280 | ESKONT HARTIJA OD VREDNOSTI |
| 281 | POZAJMICE OSNIVAČA ZA LIKVIDNOST |
| 282 | POVRAĆAJ POZAJMICE ZA LIKVIDNOST OSNIVAČU |
| 283 | NAPLATA ČEKOVA GRAĐANA |
| 284 | PLATNE KARTICE |
| 285 | MENJAČKI POSLOVI |
| 286 | KUPOPRODAJA DEVIZA |
| 287 | DONACIJE I SPONZORSTVA |
| 288 | DONACIJE |
| 289 | TRANSAKCIJE PO NALOGU GRAĐANA |
| 290 | DRUGE TRANSAKCIJE |
| 320 | PROMET ROBE I USLUGA - MEĐUFAZNA POTROŠNJA |
| 321 | PROMET ROBE I USLUGA -  FINALNA POTROŠNJA |
| 322 | USLUGE JAVNIH PREDUZEĆA |
| 323 | INVESTICIJE U OBJEKTE I OPREMU |
| 324 | INVESTICIJE - OSTALO |
| 325 | ZAKUPNINE |
| 326 | ZAKUPNINE |
| 327 | SUBVENCIJE, REGRESI I PREMIJE S POSEBNIH RAČUNA |
| 328 | SUBVENCIJE, REGRESI I PREMIJE SA OSTALIH RAČUNA |
| 331 | CARINE I DRUGE UVOZNE DAŽBINE |
| 340 | ZARADE I DRUGA PRIMANJA ZAPOSLENIH |
| 341 | NEOPOREZIVA PRIMANJA ZAPOSLENIH I OBUSTAVE OD ZARA |
| 342 | NAKNADE ZARADA NA TERET POSLODAVCA |
| 344 | ISPLATE PREKO OMLADINSKIH I STUDENTSKIH ZADRUGA |
| 345 | PENZIJE |
| 346 | OBUSTAVE OD PENZIJA |
| 347 | NAKNADE ZARADA NA TERET DRUGIH ISPLATILACA |
| 348 | PRIHODI FIZIČKIH LICA OD KAPITALA I DRUGIH IMOVINS |
| 349 | OSTALI PRIHODI FIZIČKIH LICA |
| 353 | UPLATA JAVNIH PRIHODA IZUZEV POREZA I DOPRINOSA PO |
| 354 | UPLATA POREZA I DOPRINOSA PO ODBITKU |
| 357 | POVRAĆAJ VIŠE NAPLAĆENIH ILI POGREŠNO NAPLAĆENIH T |
| 358 | PREKNJIŽAVANJE VIŠE UPLAĆENIH ILI POGREŠNO UPLAĆEN |
| 360 | PREMIJE OSIGURANJA I NADOKNADA ŠTETE |
| 361 | RASPORED TEKUĆIH PRIHODA |
| 362 | TRANSFERI U OKVIRU DRŽAVNIH ORGANA |
| 363 | OSTALI TRANSFERI |
| 364 | PRENOS SREDSTAVA IZ BUDŽETA ZA OBEZBEĐENJE POVRAĆA |
| 365 | UPLATA PAZARA |
| 366 | ISPLATA GOTOVINE |
| 370 | KRATKOROČNI KREDITI |
| 371 | DUGOROČNI KREDITI |
| 372 | AKTIVNA KAMATA |
| 373 | POLAGANJE OROČENIH DEPOZITA |
| 375 | OSTALI PLASMANI |
| 376 | OTPLATA KRATKOROČNIH KREDITA |
| 377 | OTPLATA DUGOROČNIH KREDITA |
| 378 | POVRAĆAJ OROČENIH DEPOZITA |
| 379 | PASIVNA KAMATA |
| 380 | ESKONT HARTIJA OD VREDNOSTI |
| 381 | POZAJMICE OSNIVAČA ZA LIKVIDNOST |
| 382 | POVRAĆAJ POZAJMICE ZA LIKVIDNOST OSNIVAČU |
| 383 | NAPLATA ČEKOVA GRAĐANA |
| 384 | PLATNE KARTICE |
| 385 | MENJAČKI POSLOVI |
| 386 | KUPOPRODAJA DEVIZA |
| 387 | DONACIJE I SPONZORSTVA |
| 388 | DONACIJE |
| 389 | TRANSAKCIJE PO NALOGU GRAĐANA |
| 390 | DRUGE TRANSAKCIJE |
| 920 | PROMET ROBE I USLUGA - MEĐUFAZNA POTROŠNJA |
| 921 | PROMET ROBE I USLUGA -  FINALNA POTROŠNJA |
| 922 | USLUGE JAVNIH PREDUZEĆA |
| 923 | INVESTICIJE U OBJEKTE I OPREMU |
| 924 | INVESTICIJE - OSTALO |
| 925 | ZAKUPNINE |
| 926 | ZAKUPNINE |
| 927 | SUBVENCIJE, REGRESI I PREMIJE S POSEBNIH RAČUNA |
| 928 | SUBVENCIJE, REGRESI I PREMIJE SA OSTALIH RAČUNA |
| 931 | CARINE I DRUGE UVOZNE DAŽBINE |
| 940 | ZARADE I DRUGA PRIMANJA ZAPOSLENIH |
| 941 | NEOPOREZIVA PRIMANJA ZAPOSLENIH I OBUSTAVE OD ZARA |
| 942 | NAKNADE ZARADA NA TERET POSLODAVCA |
| 944 | ISPLATE PREKO OMLADINSKIH I STUDENTSKIH ZADRUGA |
| 945 | PENZIJE |
| 946 | OBUSTAVE OD PENZIJA |
| 947 | NAKNADE ZARADA NA TERET DRUGIH ISPLATILACA |
| 948 | PRIHODI FIZIČKIH LICA OD KAPITALA I DRUGIH IMOVINS |
| 949 | OSTALI PRIHODI FIZIČKIH LICA |
| 953 | UPLATA JAVNIH PRIHODA IZUZEV POREZA I DOPRINOSA PO |
| 954 | UPLATA POREZA I DOPRINOSA PO ODBITKU |
| 957 | POVRAĆAJ VIŠE NAPLAĆENIH ILI POGREŠNO NAPLAĆENIH T |
| 958 | PREKNJIŽAVANJE VIŠE UPLAĆENIH ILI POGREŠNO UPLAĆEN |
| 960 | PREMIJE OSIGURANJA I NADOKNADA ŠTETE |
| 961 | RASPORED TEKUĆIH PRIHODA |
| 962 | TRANSFERI U OKVIRU DRŽAVNIH ORGANA |
| 963 | OSTALI TRANSFERI |
| 964 | PRENOS SREDSTAVA IZ BUDŽETA ZA OBEZBEĐENJE POVRAĆA |
| 965 | UPLATA PAZARA |
| 966 | ISPLATA GOTOVINE |
| 970 | KRATKOROČNI KREDITI |
| 971 | DUGOROČNI KREDITI |
| 972 | AKTIVNA KAMATA |
| 973 | POLAGANJE OROČENIH DEPOZITA |
| 975 | OSTALI PLASMANI |
| 976 | OTPLATA KRATKOROČNIH KREDITA |
| 977 | OTPLATA DUGOROČNIH KREDITA |
| 978 | POVRAĆAJ OROČENIH DEPOZITA |
| 979 | PASIVNA KAMATA |
| 980 | ESKONT HARTIJA OD VREDNOSTI |
| 981 | POZAJMICE OSNIVAČA ZA LIKVIDNOST |
| 982 | POVRAĆAJ POZAJMICE ZA LIKVIDNOST OSNIVAČU |
| 983 | NAPLATA ČEKOVA GRAĐANA |
| 984 | PLATNE KARTICE |
| 985 | MENJAČKI POSLOVI |
| 986 | KUPOPRODAJA DEVIZA |
| 987 | DONACIJE I SPONZORSTVA |
| 988 | DONACIJE |
| 989 | TRANSAKCIJE PO NALOGU GRAĐANA |
| 990 | DRUGE TRANSAKCIJE |

---

## Tabela: `sifpla2konta`
**Opis:** Veza plaćanja - konta
**Redova:** 21

**Kolone:** `sifpla`, `tipdok`, `opisdok`, `rnodob`, `rnzadu`, `datcre`, `datizm`, `operater`, `racun`, `polje`, `tipoperacije`, `analitika`, `mestotr`, `nosioc`, `sifrakpl`, `firma`

| sifpla | tipdok | opisdok | rnodob | rnzadu | datcre | datizm | operater | racun | polje | tipoperacije | analitika | mestotr | nosioc | sifrakpl | firma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 - Opšti slučaj | 24191 | 24191 | 2025-10-17 | 2025-10-17 14:02:20 | 13 | Card: | 1 | 2 |  | NULL | NULL | KPL2021PDP | 0 |
| 0 | 0 | 0 - Opšti slučaj | 5530 | 5530 | 2025-10-17 | 2025-10-17 14:02:24 | 13 | Mob: | 1 | 2 |  | NULL | NULL | KPL2021PDP | 0 |
| 0 | 0 | 0 - Opšti slučaj | NULL | 24191 | 2025-04-23 | 2025-04-23 16:19:01 | 13 | card | 2 | 1 |  | NULL | NULL | KPL2021PDP | 0 |
| 0 | 0 | 0 - Opšti slučaj |  | 5530 | 2025-04-23 | 2025-04-23 16:19:37 | 13 | interni | 2 | 1 |  | NULL | NULL | KPL2021PDP | 0 |
| 121 | 0 | 0 - Opšti slučaj | 2040 | 4350 | 2012-07-07 | 2023-01-18 10:45:40 | 9 |  | 0 | 0 |  | NULL | NULL | KPL2021PDP | 0 |
| 165 | 0 | 0 - Opšti slučaj | 2419 | NULL | 2012-07-07 | 2023-01-18 10:45:40 | 9 |  | 0 | 0 |  | NULL | NULL | KPL2021PDP | 0 |
| 166 | 0 | 0 - Opšti slučaj | NULL | 24190 | 2012-07-07 | 2023-01-18 10:45:40 | 9 |  | 0 | 0 |  | NULL | NULL | KPL2021PDP | 0 |
| 189 | 0 | 0 - Opšti slučaj | 2040 | 4350 | 2012-07-07 | 2023-01-18 10:45:40 | 9 |  | 0 | 0 |  | NULL | NULL | KPL2021PDP | 0 |
| 220 | 0 | 0 - Opšti slučaj | 2040 | 4350 | 2011-09-05 | 2023-01-18 10:45:40 | 9 |  | 0 | 0 |  | NULL | NULL | KPL2021PDP | 0 |
| 221 | 0 | 0 - Opšti slučaj | 2040 | 4350 | 2012-07-04 | 2025-10-22 15:07:23 | 13 |  | 0 | 0 |  | NULL | NULL | KPL2021PDP | 0 |
| 221 | 0 | 0 - Opšti slučaj | 6620 | 5620 | 2023-01-25 | 2023-01-25 00:21:47 | 1 | Kamat | 2 | 1 |  | NULL | NULL | KPL2021PDP | 0 |
| 221 | 0 | 0 - Opšti slučaj | NULL | 5530 | 2024-10-22 | 2024-10-22 14:23:02 | 9 | naknad | 2 | 1 |  | NULL | NULL | KPL2021PDP | 0 |
| 221 | 0 | 0 - Opšti slučaj | NULL | 5530 | 2023-01-25 | 2023-01-25 00:18:12 | 1 | proviz | 2 | 1 |  | NULL | NULL | KPL2021PDP | 0 |
| 221 | 1 | 1 - Avansni račun | 1500 | 4300 | 2012-07-07 | 2023-01-18 10:45:40 | 9 |  | 0 | 0 |  | NULL | NULL | KPL2021PDP | 0 |
| 222 | 0 | 0 - Opšti slučaj | 2040 | 4350 | 2012-07-07 | 2023-01-18 10:45:40 | 9 |  | 0 | 0 |  | NULL | NULL | KPL2021PDP | 0 |
| 240 | 0 | 0 - Opšti slučaj | NULL | 4500 | 2012-07-07 | 2023-01-18 10:45:40 | 9 |  | 0 | 0 |  | NULL | NULL | KPL2021PDP | 0 |
| 248 | 0 | 0 - Opšti slučaj | NULL | 4654 | 2025-04-22 | 2025-04-22 10:46:29 | 13 |  | 0 | 0 |  | NULL | NULL | KPL2021PDP | 0 |
| 253 | 0 | 0 - Opšti slučaj | 2790 | 4790 | 2024-10-22 | 2024-10-22 14:22:00 | 9 | 840000071411284310 | 0 | 0 |  | NULL | NULL | KPL2021PDP | 0 |
| 254 | 0 | 0 - Opšti slučaj | NULL | 4590 | 2023-01-25 | 2023-01-25 00:16:01 | 1 | 840000000000484837 | 0 | 0 |  | NULL | NULL | KPL2021PDP | 0 |
| 284 | 0 | 0 - Opšti slučaj | 2281 | 24191 | 2023-01-25 | 2023-01-25 00:18:58 | 1 |  | 0 | 0 |  | NULL | NULL | KPL2021PDP | 0 |
| 290 | 0 | 0 - Opšti slučaj | 42291 | 2324 | 2025-04-22 | 2025-04-22 10:37:00 | 13 |  | 0 | 0 |  | NULL | NULL | KPL2021PDP | 0 |

---

## Tabela: `arh_enttypes`
**Opis:** Arhiva - tipovi entiteta
**Redova:** 3

**Kolone:** `entId`, `entname`, `image`

| entId | entname | image |
| --- | --- | --- |
| 1 | REGISTRATOR | 0 |
| 2 | FASCIKLA | 1 |
| 3 | KUTIJA | 2 |

---

## Tabela: `oskateg`
**Opis:** Osnovna sredstva - kategorije
**Redova:** 15

**Kolone:** `sifkat`, `oznkat`, `opis`

| sifkat | oznkat | opis |
| --- | --- | --- |
| 0 | Z. | SOPSTVENI ŠIFARNIK |
| 1 | I. | GRAÐEVINSKI OBJEKTI\n |
| 2 | II. | OPREMA ZA VRŠENJE DELATNOSTI RUDNIKA I ZA\nISTRAŽIVANJE,PROIZVODNJU I PRENOS NAFTE I GASA\n |
| 3 | III. | OPREMA VODOPRIVREDE, ELEKTROPRIVREDE \nVODOVODA I KANALIZACIJE |
| 4 | IV. | OPREMA ZA VRŠENJE DELATNOSTI INDUSTRIJE\n |
| 5 | V. | OPREMA ZA VRŠENJE DELATNOSTI IZ OBLASTI\nPOLJOPRIVREDE, RIBARSTVA I ŠUMARSTVA |
| 6 | VI. | OPREMA ZA VRŠENJE DELATNOSTI GRAÐEVINARSTVA\n(GRAÐEVINSKA MEHANIZACIJA) |
| 7 | VII. | OPREMA ZA TRGOVINU,UGOSTITELJSTVO I TURIZAM I\nOPREMA ZA ZANATSTVO I KOMUNALNE USLUGE |
| 8 | VIII. | OPREMA ZA OBAVLJANJE DRUŠTVENIH DELATNOSTI |
| 9 | IX. | OPREMA ZA SAOBRAÆAJ I VEZE I UTOVARINO-ISTOVARNA\nI TRANSPORTNA MEHANIZACIJA |
| 10 | X. | SPECIJALNI I UNIVERZALNI ALAT,OPREMA ZA \nUPRAVLJANJE PROCESIMA RADA I OPREMA ZA\nODRŽAVANJE I OPR |
| 11 | XI. | OPREMA ZA UREÐENJE I ODRŽAVANJE KANCELARIJSKIH\nI DRUGIH PROSTORIJA, ZA OBAVLJANJE KANCELARIJSKUH\ |
| 12 | XII. | VOÆNJACI, VINOGRADI I HMELJNICI |
| 13 | XIII. | RADNA I PRIPLODNA STOKA |
| 14 | XIV. | OSTALA ULAGANJA |

---

## Tabela: `osporgrupe`
**Opis:** OS poreske grupe
**Redova:** 6

**Kolone:** `porgrupa`, `proc`

| porgrupa | proc |
| --- | --- |
| 1 | 2.5000 |
| 2 | 10.0000 |
| 3 | 15.0000 |
| 4 | 20.0000 |
| 5 | 30.0000 |
| 99 | 0.0000 |

---

## Tabela: `osporpodgr`
**Opis:** OS poreske podgrupe
**Redova:** 92

**Kolone:** `porgrupa`, `podgrupa`, `opis`, `datcre`, `datizm`, `operater`

| porgrupa | podgrupa | opis | datcre | datizm | operater |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | Asfaltne Površine | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 2 | Avionske piste | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 3 | Brane za akumulaciju vode | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 4 | Cevi za gasovod | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 5 | Dokovi za vezivanje brodova | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 6 | Elektrane | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 7 | Električni dalekovodi | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 8 | Eskalatori - pokretne stepenice | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 9 | Hangari | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 10 | Lukobrani | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 11 | Marine | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 12 | Mostovi | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 13 | Nadvožnjaci i vijadukti | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 14 | Naftovodi | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 15 | Odvodni i dovodni kanali | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 16 | Parking površine | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 17 | Putevi i auto-putevi | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 18 | Ribnjaci | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 19 | Skladišta i rezervoari | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 20 | Sportski objekti (stadioni, bazeni, sportske hale i dr.) | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 21 | Silosi na poljoprivrednim dobrima | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 22 | Tuneli | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 23 | Vodovodi i cevovodi | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 24 | Železnička infrastruktura | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 25 | Zgrade | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 1 | 26 | Sve ostale nepomenute nepokretnosti | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 2 | 1 | Avioni | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 2 | 2 | Brodovi i ostali plovni objekti | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 2 | 3 | Klima uređaji i sva ostala oprema za hlađenje, grejanje i protok vazdu | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 2 | 4 | Liftovi | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 2 | 5 | Bojleri | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 2 | 6 | Nameštaj u brodovima | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 2 | 7 | Medicinska oprema | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 2 | 8 | Ograde | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 2 | 9 | Nameštaj za poslovni prostor (stolovi, stolice, fotelje, komode, orman | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 2 | 10 | Oprema za proizvodnju i distribuciju solarne energije | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 2 | 11 | Oprema za proizvodnju i distribuciju električne energije, gasa, toplot | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 2 | 12 | Vagoni | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 2 | 13 | Vinogradi | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 2 | 14 | Voćnjaci | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 2 | 15 | Nepokretnosti koje imaju upotrebni vek kraći od 40 godina | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 1 | Alat i inventar | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 2 | Autobusi | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 3 | Automobili | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 4 | Oprema za termoelektrane | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 5 | Oprema za proizvodnju mleka i mlečnih proizvoda | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 6 | Fiskalne kase | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 7 | Fliperi | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 8 | Hladnjače za povrće | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 9 | Kalkulatori | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 10 | Kamioni i prikolice | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 11 | Laboratorijska oprema | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 12 | Mašine za čišćenje žitarica | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 13 | Oprema za fotokopiranje | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 14 | Ulaganje u tuđa osnovna sredstva | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 15 | Oprema za istraživanje | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 16 | Postrojenja za pravljenje betona | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 17 | Pokretna oprema za proizvodnju električne energije (agregati i sl.) | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 18 | Radari | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 20 | Televizijske antene | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 3 | 21 | Sva ostala stalna sredstva (osim nepokretnosti) | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 4 | 1 | Nameštaj u avionima | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 4 | 2 | Oprema za kontrolu zagađenja vazduha i vode - nelicencirana | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 4 | 3 | Oprema za emitovanje radio i TV programa | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 4 | 4 | Oprema za naftne bušotine | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 4 | 5 | Oprema za obradu rude | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 4 | 6 | Rezervni delovi za avione | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 4 | 7 | Fiksna i mobilna telefonska oprema i aparati, faks-aparati i telegrafs | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 4 | 8 | Povratna ambalaža koja se daje kupcima pri prodaji proizvoda sa obavez | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 1 | Automobili za iznajmljivanje ili lizing i taksi vozila  | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 2 | Bilbordi | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 3 | Branici za puteve i pruge | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 4 | Električne reklame | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 5 | Elektronska i IT oprema za procesiranje podataka | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 6 | Opema za informatičku infrastrukturu (Yupak, Interner) | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 7 | Filmovi | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 8 | Televizijske reklame i spotovi | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 9 | Građevinska pokretna oprema | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 10 | Kalupi za livenje | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 11 | Knjige u biblioteci koje se iznajmljuju | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 12 | Industrijski noževi | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 13 | Oprema za seču drveća | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 14 | Platno (tepisi, zastori ,zavese, itisoni i sl.) | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 15 | Pokretna oprema koja koristi el. energiju (bušilice, brusilice i sl.) | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 16 | Pokretni kampovi | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 17 | Skeneri za bar-kod | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 18 | Traktori | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 19 | Uniforme | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 20 | Video igre - na novčić | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 21 | Video trake, CD, DVD i sl. | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 5 | 22 | Osnovno stado | 2006-05-06 | 2006-05-06 13:23:14 | BizniSoft |
| 99 | 99 | Ne podleže obračunu poreske amortizacije | 2006-06-09 | 2006-06-09 13:34:44 | ZIKA |

---

## Tabela: `tabrac`
**Opis:** Tabela računa (kontni plan) - prvih 50
**Redova:** 426

**Kolone:** `sifra`, `naziv`, `konto`, `sifrakpl`, `PoStopama`

| sifra | naziv | konto | sifrakpl | PoStopama |
| --- | --- | --- | --- | --- |
| BSRN0001 | AVANSI ZA POSTROJENJA I OPREMU | 0281 | KPL2013OLD | 0 |
| BSRN0002 | ZALIHE ROBE U MAGACINU REPROMATERIJALA (TIP OBJEKTA 10) | 1010 | KPL2013OLD | 1 |
| BSRN0003 | MATERIJAL U OBRADI/DORADI | 1014 | KPL2013OLD | 1 |
| BSRN0004 | ISPRAVKA VREDNOSTI MATERIJALA ZBOG ZAOKRUZENJA | 1019 | KPL2013OLD | 0 |
| BSRN0005 | ALAT I INVENTAR NA ZALIHAMA | 1030 | KPL2013OLD | 0 |
| BSRN0006 | POVRATNA AMBALAŽA | 1031 | KPL2013OLD | 0 |
| BSRN0007 | ODSTUPANJE OD PLANSKE CENE AMBALAŽE | 1039 | KPL2013OLD | 0 |
| BSRN0008 | ISPRAVKA VREDNOSTI ZALIHA MATERIJALA | 1099 | KPL2013OLD | 0 |
| BSRN0009 | ZALIHE ROBE U MAGACINU ROBE (TIP OBJEKTA 08) | 1310 | KPL2013OLD | 1 |
| BSRN0010 | RAZLIKA U CENI U MAGACINU ROBE (TIP OBJEKTA 08) | 1319 | KPL2013OLD | 0 |
| BSRN0011 | ZALIHE ROBE U VELEPRODAJI (TIP OBJEKTA 02) | 1320 | KPL2013OLD | 1 |
| BSRN0012 | UKALKULISANA RAZLIKA U CENI U VELEPRODAJI (TIP OBJEKTA 02) | 1329 | KPL2013OLD | 0 |
| BSRN0013 | ROBA DATA U KOMISION MALOPRODAJE (TIP OBJEKTA 04) | 1334 | KPL2013OLD | 1 |
| BSRN0014 | ROBA DATA U KOMISION VELEPRODAJE (TIP OBJEKTA 05) | 1336 | KPL2013OLD | 1 |
| BSRN0015 | UKALKULISANI POREZ KOMISIONE ROBE | 1337 | KPL2013OLD | 1 |
| BSRN0016 | RAZLIKA U CENI ROBE DATE U KOMISION VELEPROD.AJE (TIP OBJEKTA 05) | 1339 | KPL2013OLD | 0 |
| BSRN0017 | ZALIHE ROBE U MALORPODAJI (TIP OBJEKTA 01) | 1340 | KPL2013OLD | 1 |
| BSRN0018 | UKALKULISANA POREZA U MALOPRODAJI (TIP OBJEKTA 01) | 1344 | KPL2013OLD | 1 |
| BSRN0019 | RAZLIKA U CENI U MALOPRODAJI (TIP OBJEKTA 01) | 1349 | KPL2013OLD | 0 |
| BSRN0020 | ROBA NA DORADI/OBRADI | 1350 | KPL2013OLD | 0 |
| BSRN0021 | ISPRAVKA VREDNOSTI ROBE ZBOG ZAOKRUZENJA | 1399 | KPL2013OLD | 0 |
| BSRN0022 | DATI AVANSI ZA ZALIHE | 1500 | KPL2013OLD | 0 |
| BSRN0023 | KUPCI-MATIČNA I ZAVISNA PRAVNA LICA | 2000 | KPL2013OLD | 0 |
| BSRN0024 | KUPCI-OSTALA POVEZANA PRAVNA LICA | 2010 | KPL2013OLD | 0 |
| BSRN0025 | KUPCI U ZEMLJI | 2020 | KPL2013OLD | 0 |
| BSRN0026 | KUPCI U INOSTRANSTVU | 2030 | KPL2013OLD | 0 |
| BSRN0027 | POTRAŽIVANJA IZ KOMISIONE PRODAJE (TIP OBJEKTA 05) | 2123 | KPL2013OLD | 0 |
| BSRN0028 | POTRAŽIVANJA PLATNIH KARTICA | 2280 | KPL2013OLD | 0 |
| BSRN0029 | ČEKOVI GRAÐANA | 2400 | KPL2013OLD | 0 |
| BSRN0030 | PRELAZNI RAČUN PAZARA | 2419 | KPL2013OLD | 0 |
| BSRN0031 | GOTOVINSKI RAČUNI KOJI ČEKAJU NA ISPLATU | 24190 | KPL2013OLD | 0 |
| BSRN0032 | PRELAZNI RAČUN ZA ISPLATU POLJOPRIVREDNIKU | 24191 | KPL2013OLD | 0 |
| BSRN0033 | PRIMLJENI PDV PO OPŠTOJ STOPI | 2700 | KPL2013OLD | 0 |
| BSRN0034 | PRIMLJENI PDV PO NIŽOJ STOPI | 2710 | KPL2013OLD | 0 |
| BSRN0035 | PRIMLJENI PDV PO OPŠTOJ STOPI PO AVANSNIM RAČUNIMA | 2720 | KPL2013OLD | 0 |
| BSRN0036 | PRIMLJENI PDV PO NIŽOJ STOPI PO AVANSNIM RAČUNIMA | 2730 | KPL2013OLD | 0 |
| BSRN0037 | PRIMLJEN PDV KOD UVOZA PO OPŠTOJ STOPI | 2740 | KPL2013OLD | 0 |
| BSRN0038 | PRIMLJEN PDV KOD UVOZA PO NIŽOJ STOPI | 2750 | KPL2013OLD | 0 |
| BSRN0039 | PRIMLJEN PDV OD POLJOPRIVREDNIKA PO POSEBNOJ STOPI | 2780 | KPL2013OLD | 0 |
| BSRN0040 | POTRAŽIVANJA ZA VIŠE PLAĆENI PDV | 2790 | KPL2013OLD | 0 |
| BSRN0041 | NEFAKTURISAN PRETHODNI PDV PO OPŠTOJ STOPI | 28201 | KPL2013OLD | 0 |
| BSRN0042 | NEFAKTURISAN PRETHODNI PDV PO NIŽOJ STOPI | 28202 | KPL2013OLD | 0 |
| BSRN0043 | RAZGRANIČENI PRETHODNI PDV PO OPŠTOJ STOPI | 287270 | KPL2013OLD | 0 |
| BSRN0044 | RAZGRANIČENI PRETHODNI PDV PO NIŽOJ STOPI | 287271 | KPL2013OLD | 0 |
| BSRN0045 | ODLOŽENA PORESKA SREDSTVA ZA OTKUP POLJ.PROIZVODA | 2885 | KPL2013OLD | 0 |
| BSRN0046 | AKTIVNA VREMENSKA RAZGRANIČENJA - AVANSI PO OPŠTO STOPI | 28901 | KPL2013OLD | 0 |
| BSRN0047 | AKTIVNA VREMENSKA RAZGRANIČENJA - AVANSI PO NIŽOJ STOPI | 28902 | KPL2013OLD | 0 |
| BSRN0048 | NERASPOREÐENA DOBIT TEKUĆE GODINE | 3410 | KPL2013OLD | 0 |
| BSRN0049 | GUBITAK TEKUĆE GODINE | 3510 | KPL2013OLD | 0 |
| BSRN0050 | PRIMLJENI AVANSI | 4300 | KPL2013OLD | 0 |

---

## Tabela: `kplvezna`
**Opis:** Kontni plan - vezna tabela - prvih 50
**Redova:** 420

**Kolone:** `kpl2013old`, `kpl2014pdp`, `kpl2014dpl`, `kpl2014ifl`, `kpl2016bst`, `kpl2021pdp`, `kpl2021dpl`, `kpl2021bdd`

| kpl2013old | kpl2014pdp | kpl2014dpl | kpl2014ifl | kpl2016bst | kpl2021pdp | kpl2021dpl | kpl2021bdd |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0190 | NULL | NULL | NULL | 0108 | NULL | NULL |
|  | 0191 | NULL | NULL | NULL | 0109 | NULL | NULL |
|  | 0192 | NULL | NULL | NULL | 0118 | NULL | NULL |
|  | 0193 | NULL | NULL | NULL | 0119 | NULL | NULL |
|  | 0194 | NULL | NULL | NULL | 0128 | NULL | NULL |
|  | 0195 | NULL | NULL | NULL | 0129 | NULL | NULL |
|  | 0196 | NULL | NULL | NULL | 0139 | NULL | NULL |
|  | 0198 | NULL | NULL | NULL | 0148 | NULL | NULL |
|  | 0199 | NULL | NULL | NULL | 0149 | NULL | NULL |
|  | 0150 | NULL | NULL | NULL | 0160 | NULL | NULL |
|  | 0151 | NULL | NULL | NULL | 0161 | NULL | NULL |
|  | 0152 | NULL | NULL | NULL | 0162 | NULL | NULL |
|  | 0153 | NULL | NULL | NULL | 0163 | NULL | NULL |
|  | 0155 | NULL | NULL | NULL | 0165 | NULL | NULL |
|  | 0197 | NULL | NULL | NULL | 0169 | NULL | NULL |
|  | 0160 | NULL | NULL | NULL | 0170 | NULL | NULL |
|  | 0161 | NULL | NULL | NULL | 0171 | NULL | NULL |
|  | 0162 | NULL | NULL | NULL | 0172 | NULL | NULL |
|  | 0290 | NULL | NULL | NULL | 0209 | NULL | NULL |
|  | 0291 | NULL | NULL | NULL | 0219 | NULL | NULL |
|  | 0292 | NULL | NULL | NULL | 0228 | NULL | NULL |
|  | 0293 | NULL | NULL | NULL | 0229 | NULL | NULL |
|  | 0294 | NULL | NULL | NULL | 0238 | NULL | NULL |
|  | 0295 | NULL | NULL | NULL | 0239 | NULL | NULL |
|  | 0296 | NULL | NULL | NULL | 0248 | NULL | NULL |
|  | 0297 | NULL | NULL | NULL | 0249 | NULL | NULL |
|  | 0250 | NULL | NULL | NULL | 0260 | NULL | NULL |
|  | 0251 | NULL | NULL | NULL | 0261 | NULL | NULL |
|  | 0252 | NULL | NULL | NULL | 0262 | NULL | NULL |
|  | 0253 | NULL | NULL | NULL | 0263 | NULL | NULL |
|  | 0250 | NULL | NULL | NULL | 0264 | NULL | NULL |
|  | 0255 | NULL | NULL | NULL | 0265 | NULL | NULL |
|  | 0256 | NULL | NULL | NULL | 0266 | NULL | NULL |
|  | 0298 | NULL | NULL | NULL | 0268 | NULL | NULL |
|  | 0299 | NULL | NULL | NULL | 0269 | NULL | NULL |
|  | 0260 | NULL | NULL | NULL | 0270 | NULL | NULL |
|  | 0261 | NULL | NULL | NULL | 0271 | NULL | NULL |
|  | 0265 | NULL | NULL | NULL | 0275 | NULL | NULL |
|  | 02910 | NULL | NULL | NULL | 0279 | NULL | NULL |
|  | 0270 | NULL | NULL | NULL | 0280 | NULL | NULL |
|  | 0271 | NULL | NULL | NULL | 0281 | NULL | NULL |
|  | 0272 | NULL | NULL | NULL | 0282 | NULL | NULL |
|  | 02911 | NULL | NULL | NULL | 0288 | NULL | NULL |
|  | 02912 | NULL | NULL | NULL | 0289 | NULL | NULL |
|  | 0280 | NULL | NULL | NULL | 0290 | NULL | NULL |
|  | 0281 | NULL | NULL | NULL | 0291 | NULL | NULL |
|  | 0282 | NULL | NULL | NULL | 0292 | NULL | NULL |
|  | 02913 | NULL | NULL | NULL | 0299 | NULL | NULL |
|  | 0313 | NULL | NULL | NULL | 0321 | NULL | NULL |
|  | 0314 | NULL | NULL | NULL | 0322 | NULL | NULL |

---

## Tabela: `matpod`
**Opis:** Matični podaci firmi (sifra, naziv, pib)
**Redova:** 674

**Kolone:** `sifra`, `naziv`, `vlasnik`, `adresa`, `telefoni`, `mesto`, `pib`, `zr1`, `zr2`, `zr3`, `matbr`, `sifdel`, `regbr`, `zadnja`, `prb`, `web`, `email`, `skin`, `zadnjiobj`, `barkod`, `npp`, `pdv`, `cenovnik`, `dvojno`, `robno`, `napomena`, `boja`, `tip`, `porper`, `pdvbroj`, `naplacenpdv`, `sifops`, `ovllice`, `sifrakpl`, `externidokument`, `gln`, `aktivna`, `vpnadresa`, `vpnport`, `operater`, `velicina`, `korjav`, `jbkjs`, `ts`, `operater2`

*Tabela je prazna.*

---

## Tabela: `matpodracuni`
**Opis:** Matični podaci - računi
**Redova:** 9

**Kolone:** `sifra`, `brtekrn`, `status`, `opis`, `sef`

| sifra | brtekrn | status | opis | sef |
| --- | --- | --- | --- | --- |
| 2 | 205-14814-72 | 1 | NULL | 0 |
| 2 | 265-1750310000541-26 | 1 | NULL | 0 |
| 2 | 325-9500500003066-19 | 1 | NULL | 0 |
| 2 | 325-9500500484422-87 | 1 | NULL | 0 |
| 2 | 340-11013722-68 | 1 | NULL | 0 |
| 4 | 840-54216763-21 | 1 | NULL | 0 |
| 50 | 205-225341-58 | 1 | racun bolovanja | 0 |
| 71 | 160-6000001800610-52 | 1 | banca intesa | 0 |
| 614 | 325950050017240879 | 1 | OTP  | 0 |

---

## Tabela: `nazmes`
**Opis:** Nazivi meseci
**Redova:** 12

**Kolone:** `mesec`, `naziv_meseca`

| mesec | naziv_meseca |
| --- | --- |
| 1 | JANUAR |
| 2 | FEBRUAR |
| 3 | MART |
| 4 | APRIL |
| 5 | MAJ |
| 6 | JUNI |
| 7 | JULI |
| 8 | AVGUST |
| 9 | SEPTEMBAR |
| 10 | OKTOBAR |
| 11 | NOVEMBAR |
| 12 | DECEMBAR |

---

## Tabela: `propisani_parametri`
**Opis:** Propisani parametri
**Redova:** 56

**Kolone:** `id`, `tip`, `opis`, `uhiljadama`, `pisinule`, `tipvrednost`, `vrednost`, `myblob`

| id | tip | opis | uhiljadama | pisinule | tipvrednost | vrednost | myblob |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7 | Šablon Napomena uz finansijske izveštaje | 0 | 0 | NULL |  | PK\0\0\0\0�AV7g��<\0\0�\0\0\0\0\0word/header1.xml��]k� ��J�\\�Ք�iZ\n���`��Z����h�_?�נ�1荚�� |
| 2 | 7 | Šablon Napomena uz finansijske izveštaje - MSFI za MSP | 0 | 0 | NULL |  | PK\0\0\0\0�q�X7g��<\0\0�\0\0\0\0\0word/header1.xml��]k� ��J�\\�Ք�iZ\n���`��Z����h�_?�נ�1荚�� |
| 91 | 4 | Pravilnik o kontnom okviru | 0 | 0 | NULL | PRAVILNIK O KONTNOM OKVIRU I SADRŽINI RAČUNA U KONTNOM OKVIRU ZA PRIVREDNA DRUŠTVA, ZADRUGE I PREDUZ | NULL |
| 92 | 4 | Računovodstvena regulativa | 0 | 0 | NULL | PRAVILNIK O NAČINU PRIZNAVANJA, VREDNOVANJA, PREZENTACIJE I OBELODANJIVANJA POZICIJA U POJEDINAČNIM  | NULL |
| 100 | 4 | Mesto sedišta firme | 0 | 0 | NULL | NOVI BEOGRAD | NULL |
| 101 | 4 | Naziv firme | 0 | 0 | NULL | FUTURAMA CENTAR DELTA DOO | NULL |
| 102 | 1 | Poslovna godina | 0 | 0 | NULL | 2025 | NULL |
| 103 | 4 | Matični broj firme | 0 | 0 | NULL | 21409375 | NULL |
| 104 | 4 | PIB firme | 0 | 0 | NULL | 110979442 | NULL |
| 105 | 4 | Adresa sedišta firme | 0 | 0 | NULL | JURIJA GAGARINA 16 LOKAL 315 | NULL |
| 106 | 4 | Šifra delatnosti | 0 | 0 | NULL | 9329 | NULL |
| 107 | 4 | Osnivač/vlasnik firme | 0 | 0 | NULL | BORVERK DOO | NULL |
| 108 | 4 | Odgovorno lice | 0 | 0 | NULL | ZORAN KARAMARKOVIĆ | NULL |
| 109 | 1 | Prosečan broj zaposlenih | 0 | 1 | NULL | 6 | NULL |
| 110 | 3 | Finansijski izveštaji za period OD | 0 | 0 | NULL | 2025-01-01 | NULL |
| 111 | 3 | Finansijski izveštaji za period DO | 0 | 0 | NULL | 2025-12-31 | NULL |
| 112 | 1 | Prethodna poslovna godina | 0 | 0 | NULL | 2024 | NULL |
| 113 | 1 | Prosečan broj zaposlenih - prethodna godina | 0 | 1 | NULL | 6 | NULL |
| 117 | 4 | Lice odgovorno za sastavljanje izveštaja | 0 | 1 | NULL | NULL | NULL |
| 118 | 4 | Datum odobravanja finansijskih izveštaja | 0 | 1 | NULL | NULL | NULL |
| 119 | 1 | Godina osnivanja društva | 0 | 1 | NULL | NULL | NULL |
| 120 | 4 | Razvrstavanje za FI | 0 | 0 | NULL | Mikro pravno lice | NULL |
| 301 | 1 | Upisane a neuplaćene akcije - tekuća godina godina | 1 | 1 | NULL | NULL | NULL |
| 302 | 1 | Upisani a neuplaćeni udeli i ulozi - tekuća godina godina | 1 | 1 | NULL | NULL | NULL |
| 303 | 1 | Upisane a neuplaćene akcije - prethodna godina godina | 1 | 1 | NULL | NULL | NULL |
| 304 | 1 | Upisani a neuplaćeni udeli i ulozi - prethodna godina godina | 1 | 1 | NULL | NULL | NULL |
| 310 | 1 | Iznos neusaglašenih potraživanja u 000 RSD - TG | 1 | 1 | NULL | NULL | NULL |
| 311 | 1 | Ukupan iznos potraživanja u 000 RSD - TG | 1 | 1 | NULL | NULL | NULL |
| 312 | 4 | % iznosa neusaglašenih u ukupnom iznosu potraživanja - TG | 0 | 1 | NULL | NULL | NULL |
| 313 | 1 | Broj neusaglašenih potraživanja - TG | 0 | 1 | NULL | NULL | NULL |
| 314 | 1 | Ukupan broj potraživanja - TG | 0 | 1 | NULL | NULL | NULL |
| 315 | 4 | % broja neusaglašenih u ukupnom broju potraživanja - TG | 0 | 1 | NULL | NULL | NULL |
| 320 | 1 | Iznos neusaglašenih obaveza u 000 RSD - TG | 1 | 1 | NULL | NULL | NULL |
| 321 | 1 | Ukupan iznos obaveza u 000 RSD - TG | 1 | 1 | NULL | NULL | NULL |
| 322 | 4 | % iznosa obaveza u ukupnom iznosu obaveza - TG | 0 | 1 | NULL | NULL | NULL |
| 323 | 1 | Broj neusaglašenih obaveza - TG | 0 | 1 | NULL | NULL | NULL |
| 324 | 1 | Ukupan broj obaveza - TG | 0 | 1 | NULL | NULL | NULL |
| 325 | 4 | % broja neusaglašenih u ukupnom broju obaveza - TG | 0 | 1 | NULL | NULL | NULL |
| 410 | 1 | Iznos neusaglašenih potraživanja u 000 RSD - PG | 1 | 1 | NULL | NULL | NULL |
| 411 | 1 | Ukupan iznos potraživanja u 000 RSD - PG | 1 | 1 | NULL | NULL | NULL |
| 412 | 4 | % iznosa neusaglašenih u ukupnom iznosu potraživanja - PG | 0 | 1 | NULL | NULL | NULL |
| 413 | 1 | Broj neusaglašenih potraživanja - PG | 0 | 1 | NULL | NULL | NULL |
| 414 | 1 | Ukupan broj potraživanja - PG | 0 | 1 | NULL | NULL | NULL |
| 415 | 4 | % broja neusaglašenih u ukupnom broju potraživanja - PG | 0 | 1 | NULL | NULL | NULL |
| 420 | 1 | Iznos neusaglašenih obaveza u 000 RSD - PG | 1 | 1 | NULL | NULL | NULL |
| 421 | 1 | Ukupan iznos obaveza u 000 RSD - PG | 1 | 1 | NULL | NULL | NULL |
| 422 | 4 | % iznosa obaveza u ukupnom iznosu obaveza - PG | 0 | 1 | NULL | NULL | NULL |
| 423 | 1 | Broj neusaglašenih obaveza - PG | 0 | 1 | NULL | NULL | NULL |
| 424 | 1 | Ukupan broj obaveza - PG | 0 | 1 | NULL | NULL | NULL |
| 425 | 4 | % broja neusaglašenih u ukupnom broju obaveza - PG | 0 | 1 | NULL | NULL | NULL |
| 901 | 8 | Tabela srednjih kurseva | 0 | 0 | NULL | NULL | NULL |
| 902 | 8 | Koeficijenti rasta potrošačkih cena | 0 | 0 | NULL | NULL | NULL |
| 903 | 8 | Specifikacija potraživanja po osnovu prodaje | 0 | 0 | NULL | NULL | NULL |
| 904 | 8 | Specifikacija primljenih avansa, depozita i kaucija | 0 | 0 | NULL | NULL | NULL |
| 905 | 8 | Specifikacija obaveza iz poslovanja | 0 | 0 | NULL | NULL | NULL |
| 906 | 8 | Starosna struktura potraživanja po osnovu prodaje | 0 | 0 | NULL | NULL | NULL |

---

## Tabela: `stope`
**Opis:** Poreske stope
**Redova:** 1

**Kolone:** `ppproi`, `ppusl`, `ppruc`, `matricni`

| ppproi | ppusl | ppruc | matricni |
| --- | --- | --- | --- |
| 18 | 18 | 18 | 0 |

---

## Tabela: `propsifban`
**Opis:** Propisane šifre banaka
**Redova:** 20

**Kolone:** `sifra`, `naziv`, `mesto`, `datcre`, `datizm`, `operater`, `tekrn`, `ulibr`

| sifra | naziv | mesto | datcre | datizm | operater | tekrn | ulibr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 105 | AGROINDUSTRIJSKA KOMERCIJALNA BANKA AIK BANKA AD | NOVI BEOGRAD | 1993-06-28 | 2024-11-19 08:00:00 | BIZNISOFT | 908-10501-97 | BULEVAR MIHAILA PUPINA 115Đ |
| 115 | YETTEL BANKA AD | NOVI BEOGRAD | 2024-05-25 | 2024-11-19 08:00:00 | BIZNISOFT | 908-11501-07 | OMLADINSKIH BRIGADA 88 |
| 145 | ADRIATIC BANK AD | BEOGRAD | 2023-08-31 | 2024-11-19 08:00:00 | BIZNISOFT | 908-14501-28 | DALMATINSKA 22 |
| 150 | EUROBANK DIREKTNA AD | BEOGRAD | 2021-12-11 | 2024-11-19 08:00:00 | BIZNISOFT | 908-15001-80 | VUKA KARADŽIĆA 10 |
| 155 | HALKBANK AD | NOVI BEOGRAD | 2015-10-22 | 2024-11-19 08:00:00 | BIZNISOFT | 908-15501-35 | MILUTINA MILANKOVIĆA 9E |
| 160 | BANCA INTESA AD | NOVI BEOGRAD | 1991-09-19 | 2024-11-19 08:00:00 | BIZNISOFT | 908-16001-87 | MILENTIJA POPOVIĆA 7B |
| 165 | ADDIKO BANK AD | NOVI BEOGRAD | 2016-07-08 | 2024-11-19 08:00:00 | BIZNISOFT | 908-16501-42 | MILUTINA MILANKOVIĆA 7V |
| 170 | UNICREDIT BANK SRBIJA AD | BEOGRAD - STARI GRAD | 2001-07-02 | 2024-11-19 08:00:00 | BIZNISOFT | 908-17001-94 | RAJIĆEVA 27-29 |
| 190 | ALTA BANKA AD | NOVI BEOGRAD | 2020-03-27 | 2024-11-19 08:00:00 | BIZNISOFT | 908-19001-11 | BULEVAR ZORANA ĐINĐIĆA 121 |
| 200 | BANKA POŠTANSKA ŠTEDIONICA AD | BEOGRAD - PALILULA | 2002-11-21 | 2024-11-19 08:00:00 | BIZNISOFT | 908-20001-18 | KRALJICE MARIJE 3 |
| 205 | NLB KOMERCIJALNA BANKA AD | NOVI BEOGRAD | 2022-04-30 | 2024-11-19 08:00:00 | BIZNISOFT | 908-20501-70 | BULEVAR MIHAILA PUPINA 165B |
| 220 | PROCREDIT BANK AD | NOVI BEOGRAD | 2001-04-05 | 2024-11-19 08:00:00 | BIZNISOFT | 908-22001-32 | MILUTINA MILANKOVIĆA 17 |
| 265 | RAIFFEISEN BANKA AD | NOVI BEOGRAD | 2001-03-09 | 2024-11-19 08:00:00 | BIZNISOFT | 908-26501-15 | ĐORĐA STANOJEVIĆA 16 |
| 295 | SRPSKA BANKA AD | BEOGRAD - SAVSKI VENAC | 1996-11-04 | 2024-11-19 08:00:00 | BIZNISOFT | 908-29501-36 | SAVSKA 25 |
| 325 | OTP BANKA SRBIJA AD | NOVI SAD | 2021-04-30 | 2024-11-19 08:00:00 | BIZNISOFT | 908-32501-57 | TRG SLOBODE 5 |
| 340 | ERSTE BANK AD | NOVI SAD | 1989-12-20 | 2024-11-19 08:00:00 | BIZNISOFT | 908-34001-19 | BULEVAR OSLOBOĐENJA 5 |
| 370 | 3 BANKA AD | NOVI SAD | 2021-11-22 | 2024-11-19 08:00:00 | BIZNISOFT | 908-37001-40 | BULEVAR OSLOBOĐENJA 2A |
| 375 | API BANK AD | BEOGRAD | 2018-10-18 | 2024-11-19 08:00:00 | BIZNISOFT | 908-37501-92 | BULEVAR VOJVODE BOJOVIĆA 6-8 |
| 380 | MIRABANK AD | NOVI BEOGRAD | 2015-02-05 | 2024-11-19 08:00:00 | BIZNISOFT | 908-38001-47 | ŠPANSKIH BORACA 1 |
| 385 | BANK OF CHINA SRBIJA AD | NOVI BEOGRAD | 2016-12-20 | 2024-11-19 08:00:00 | BIZNISOFT | 908-38501-02 | BULEVAR ZORANA ĐINĐIĆA 2A |

---

## Tabela: `tr_pravila`
**Opis:** Pravila za transakcije
**Redova:** 9

**Kolone:** `idpravila`, `naziv`, `zafirmu`, `idfirme`, `nazivfirme`, `zadob`, `pib`, `nazdob`, `mysort`, `placeno`, `racun`, `analitika`

| idpravila | naziv | zafirmu | idfirme | nazivfirme | zadob | pib | nazdob | mysort | placeno | racun | analitika |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | YETTEL | 1 | NULL |  | 1 | 104318304 | YETTEL TELENOR D.O.O. | 0 | 0 | NULL | NULL |
| 5 | OPŠTE PRAVILO ZA TROŠKOVE | 0 | NULL |  | 0 | NULL |  | 0 | 0 | NULL | NULL |
| 6 | OPŠTE PRAVILO ZA TROŠKOVE NISU U PDV | 0 | NULL |  | 0 | NULL |  | 0 | 0 | NULL | NULL |
| 7 | ŽIVANOVIĆ | 1 | 367 | PEJKOM DOO BEOGRAD | 1 | 113371356 | ŽIVANOVIĆ 2011 DOO KOVAČEVAC | 0 | 0 | NULL | NULL |
| 8 | 5300 | 1 | NULL |  | 0 | NULL |  | 0 | 0 | NULL | NULL |
| 9 | KALKULACIJE | 0 | NULL |  | 0 | NULL |  | 0 | 0 | NULL | NULL |
| 10 | POVRAĆAJ ROBE | 0 | NULL |  | 0 | NULL |  | 0 | 0 | NULL | NULL |
| 11 | BROKERI-PROVIZIJA BANKE | 1 | 728 | BDD TRADEWIN 24 AD BEOGRAD-STARI GRAD | 0 | NULL |  | 0 | 0 | NULL | NULL |
| 12 | BROKERI-TROŠAK  | 1 | 728 | BDD TRADEWIN 24 AD BEOGRAD-STARI GRAD | 0 | NULL |  | 0 | 0 | NULL | NULL |

---

## Tabela: `tr_pravila_stavke`
**Opis:** Stavke pravila
**Redova:** 27

**Kolone:** `idpravila`, `rbr`, `tipart`, `nazart`, `konto`, `tipanal`, `analitika`, `popdvid`, `internipdv`, `mestotr`, `nosioctr`

| idpravila | rbr | tipart | nazart | konto | tipanal | analitika | popdvid | internipdv | mestotr | nosioctr |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 1 | 0 | NULL | 55091 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 4 | 2 | 1 | NULL | 55091 | 0 | NULL | 8v.2 | 0 | NULL | NULL |
| 4 | 3 | 1 | VIRTUALNA KANCELARIJA | 5334 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 5 | 1 | 0 | NULL | 5509 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 5 | 2 | 1 | 163  PRINTER MODEL:TRADER BT-306 | 5123 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 5 | 3 | 1 | KNJIŽENJE NAKNADE PO ZAHTEVIMA ZA REGISTRACIJU/IZMENU/BRISANJE MENICA/OVLAŠĆENJA | 5530 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 5 | 4 | 1 | OBRACUN PROVIZIJE ZA ELEKTRONSKE NALOGE ZA RACUN 265163031001029867 | 5530 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 5 | 5 | 1 | VIRTUALNA KANCELARIJA | 5334 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 5 | 6 | 1 | NULL | 5129 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 5 | 7 | 1 |  | 5110 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 5 | 8 | 1 | KAMATA NA NEPLAĆENE RAČUNE | 5624 | 0 | NULL | 8v.2 | 0 | NULL | NULL |
| 5 | 10 | 1 | UTROŠENA EL. ENERGIJA SA PRIPADAJUĆIM TROŠKOVIMA | 5130 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 5 | 11 | 1 | TAKSA ZA JAVNI MEDIJSKI SERVIS | 5130 | 0 | NULL | 11.8 | 0 | NULL | NULL |
| 5 | 12 | 1 | ODRŽAVANJE OSNOVNIH SREDSTAVA | 5320 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 5 | 13 | 1 | TROŠKOVI TRANSPORTA | 5310 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 6 | 1 | 1 | AVANS | 1500 | 0 | NULL | 8a.7 | 0 | NULL | NULL |
| 7 | 2 | 1 | USLUGA PRESOVANJA GUMENIH PLOČA | 5300 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 7 | 3 | 1 | INFO BOARD | 5300 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 7 | 4 | 1 | USLUGA PREVOZA | 5300 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 7 | 5 | 1 | MONTAZA MOBILIJARA | 5300 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 7 | 6 | 1 | USLUGA PRESOVANJA GUMENIH PLOČA ODBOJNICI | 5300 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 8 | 1 | 0 | NULL | 5300 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 9 | 1 | 0 | NULL | 1340 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 10 | 1 | 0 | NULL | 5123 | 0 | NULL | 8a.2 | 0 | NULL | NULL |
| 11 | 1 | 0 | NULL | 6630 | 0 | NULL | 8v.2 | 0 | NULL | NULL |
| 11 | 2 | 2 | KONSULTANT | 6697 | 0 | NULL | 9.01 | 0 | NULL | NULL |
| 12 | 1 | 0 | NULL | 6799 | 0 | NULL | 9.01 | 0 | NULL | NULL |

---

## Tabela: `ldkategpok`
**Opis:** LD kategorije pokrivanja
**Redova:** 6

**Kolone:** `tipug`, `sifkat`, `opis`, `porez_proc`, `porez_procum`, `pio_proc`, `zdro_proc`, `nzp_proc`, `nortros_proc`, `porez_uplrac`, `pio_uplrac`, `zdro_uplrac`, `nzp_uplrac`, `proc_pioi`, `proc_zdroi`, `datcre`, `datizm`, `operater`, `konto_duguje`, `konto_neto`, `konto_porez`, `konto_pio`, `konto_zdrav`, `konto_pioi`

| tipug | sifkat | opis | porez_proc | porez_procum | pio_proc | zdro_proc | nzp_proc | nortros_proc | porez_uplrac | pio_uplrac | zdro_uplrac | nzp_uplrac | proc_pioi | proc_zdroi | datcre | datizm | operater | konto_duguje | konto_neto | konto_porez | konto_pio | konto_zdrav | konto_pioi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 1 | DIVIDENDE I UDELI U DOBITI | 15.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 840-711141843-68 | NULL | NULL | NULL | 0.0000 | 0.0000 | 2007-01-01 | 2015-12-14 07:35:06 | 1 | 3400 | 4610 | 4890 | NULL | NULL | NULL |
| I | 2 | PRIMANJA ZAPOSLENIH I ČLANOVA UPRAVE PRIVREDNOG DRUŠTVA PO OSNOVU UČEŠĆA U DOBITI | 10.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 840-711141843-68 | NULL | NULL | NULL | 0.0000 | 0.0000 | 2007-01-01 | NULL | BizniSOFT | 340 | 4610 | 4890 | NULL | NULL | NULL |
| I | 3 | UZIMANJE IZ IMOVINE PRIVREDNOG DRUŠTVA OD STARNE VLASNIKA U SKLADU SA ZAKONOM | 10.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 840-711141843-68 | NULL | NULL | NULL | 0.0000 | 0.0000 | 2007-01-01 | NULL | BizniSOFT | 7230 | 2210 | 4890 | NULL | NULL | NULL |
| I | 4 | IZDAVANJE SOPSTVENIH NEPOKRETNOSTI | 20.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 25.0000 | 840-711149843-27 |  |  |  | 0.0000 | 0.0000 | 2013-07-19 | 2014-01-29 13:23:06 | 1 | 5250 | 4654 | 4890 |  |  |  |
| I | 5 | IZNAJMLJIVANJE STANOVA, SOBA... | 20.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 50.0000 | 840-711143843-82 |  |  |  | 0.0000 | 0.0000 | 2013-07-19 | 2013-07-19 00:00:00 | DEMO | 5250 | 4654 | 4890 |  |  |  |
| I | 6 | PRIHODI OD KAPITALA KAMATA | 15.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 840-711143843-75 |  |  |  | 0.0000 | 0.0000 | 2013-07-19 | 2013-07-19 00:00:00 | DEMO |  |  | 4890 |  |  |  |

---

## Tabela: `ldkategzap`
**Opis:** LD kategorije zaposlenih
**Redova:** 47

**Kolone:** `sifkat`, `opis`, `porez_proc`, `oslob_poreza`, `pior_proc`, `zdror_proc`, `nzpr_proc`, `piop_proc`, `zdrop_proc`, `nzpp_proc`, `datcre`, `datizm`, `operater`, `sub_porez_proc`, `sub_pior_proc`, `sub_piop_proc`, `sub_zdrr_proc`, `sub_zdrp_proc`, `sub_nzpr_proc`, `sub_nzpp_proc`

| sifkat | opis | porez_proc | oslob_poreza | pior_proc | zdror_proc | nzpr_proc | piop_proc | zdrop_proc | nzpp_proc | datcre | datizm | operater | sub_porez_proc | sub_pior_proc | sub_piop_proc | sub_zdrr_proc | sub_zdrp_proc | sub_nzpr_proc | sub_nzpp_proc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | OPŠTA KATEGORIJA | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2006-01-25 | 2023-11-16 09:21:32 | 13 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 2 | Novozaposleni /1.9.04 - 1.1.05/  preko 50 godina starosti | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 0.0000 | 0.0000 | 0.0000 | 2006-01-25 | 2014-07-31 13:46:43 | 1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 3 | Novozaposleni /1.9.04 - 1.1.04/  preko 45 godina starosti | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 2.4000 | 1.0300 | 0.0000 | 2006-01-25 | 2020-01-30 11:39:13 | 14 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 4 | Novozaposleni od 1.1.05 stariji od 50 godona | 10.0000 | D | 14.0000 | 5.1500 | 0.7500 | 0.0000 | 0.0000 | 0.0000 | 2006-01-25 | 2014-07-31 13:46:43 | 1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 5 | Novozaposleni od 1.1.05 stariji od 45 godina | 10.0000 | D | 14.0000 | 5.1500 | 0.7500 | 2.4000 | 1.0300 | 0.0000 | 2006-01-25 | 2020-01-30 11:39:15 | 14 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 6 | Ostali novozaposleni od 1.1.2005 | 10.0000 | D | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2006-01-25 | 2023-01-03 08:22:27 | 13 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 7 | Invalidna lica u preduzecima za radno osposobljavanje | 0.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2006-01-25 | 2023-01-03 08:22:30 | 13 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 8 | Novozaposleni pripravnici mladji od 30 god. (21v - 45a/1) | 10.0000 | D | 14.0000 | 5.1500 | 0.7500 | 0.0000 | 0.0000 | 0.0000 | 2006-10-13 | 2014-07-31 13:46:45 | 1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 9 | Ostali novozaposleni mladji od 30 god. (21g - 45a/2) | 10.0000 | D | 14.0000 | 5.1500 | 0.7500 | 0.0000 | 0.0000 | 0.0000 | 2006-10-13 | 2014-07-31 13:46:46 | 1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 10 | Novozaposlena invalidna lica (21d - 45a-3) | 0.0000 | D | 14.0000 | 5.1500 | 0.7500 | 0.0000 | 0.0000 | 0.0000 | 2006-10-13 | 2019-10-01 13:19:21 | 10 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 11 | Lica starosti od 30 do 45 god. (čl.2.st.1. Uredbe) | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2011-07-12 | 2023-01-03 08:22:33 | 13 | 30.0000 | 100.0000 | 100.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 12 | Lica mlađa od 30 ili starija od 45 god. (čl.2.st.1. Uredbe) | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2011-07-12 | 2023-01-03 08:22:34 | 13 | 100.0000 | 100.0000 | 100.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 13 | Penzioner zasnovao radni odnos | 10.0000 | N | 14.0000 | 5.1500 | 0.0000 | 10.0000 | 5.1500 | 0.0000 | 2014-02-27 | 2023-01-31 09:33:51 | ANA | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 14 | Lična zarada preduzetnika koji je osiguran po drugom osnovu | 10.0000 | N | 24.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2016-02-29 | 2023-01-31 09:34:09 | ANA | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 15 | Lična zarada preduzetnika koji nije osiguran po drugom osnovu | 10.0000 | N | 24.0000 | 10.3000 | 0.7500 | 0.0000 | 0.0000 | 0.0000 | 2014-02-27 | 2024-11-22 10:26:54 | 13 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 16 | Vlasnik koji nije u radnom odnosu | 0.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2013-08-14 | 2023-01-03 08:22:36 | 13 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 17 | Opšta - penzioner | 10.0000 | N | 14.0000 | 5.1500 | 0.0000 | 10.0000 | 5.1500 | 0.0000 | 2015-09-15 | 2023-03-25 19:37:22 | 13 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 18 | Osnivač koji nije zaposlen u svom preduzeću i jeste osiguran po drugom osnovu | 0.0000 | N | 14.0000 | 0.0000 | 0.0000 | 10.0000 | 0.0000 | 0.0000 | 2020-01-31 | 2023-02-03 13:07:11 | 13 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 19 | Lična zarada preduzetnika poljoprivrednika (čl 32 stav 3 Zakona) | 10.0000 | N | 24.0000 | 10.3000 | 0.7500 | 0.0000 | 0.0000 | 0.0000 | 2020-11-25 | 2023-01-31 09:34:12 | ANA | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 20 | Novozaposleni od 01.07.2014. refundacija 65% | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2014-10-08 | 2023-01-03 08:22:56 | 13 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 21 | Novozaposleni od 01.07.2014. refundacija 70% | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2014-10-08 | 2023-01-03 08:22:57 | 13 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 22 | Novozaposleni od 01.07.2014. refundacija 75% | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2014-10-08 | 2023-01-03 08:22:58 | 13 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 23 | Novozaposleni u mikro i malom pravnom licu refundacija 75% doprinosa | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2016-02-29 | 2023-01-31 09:33:54 | ANA | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 24 | Zarada osnivača sa olakšicom od 01.10.2018. (21đ - 45g) bez plaćanja PIO | 0.0000 | N | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2018-10-17 | 2019-01-03 10:36:23 | ANA | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 25 | Zarada osnivača sa olakšicom od 01.10.2018. (21đ - 45g) sa plaćanjem PIO | 0.0000 | N | 14.0000 | 0.0000 | 0.0000 | 10.0000 | 0.0000 | 0.0000 | 2018-10-17 | 2023-01-31 09:33:55 | ANA | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 26 | Lična zarada preduzetnika od 01.10.2018. (21đ - 45g) bez plaćanja PIO | 0.0000 | N | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2018-10-17 | 2018-12-25 08:49:37 | IVANA | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 27 | Lična zarada preduzetnika od 01.10.2018. (21đ - 45g) sa plaćanjem PIO | 0.0000 | N | 24.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2018-10-17 | 2023-01-31 09:34:14 | ANA | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 28 | Osnivači- subvencije po članu 21đ Zakona i članu 45g Zakona o doprinosima | 0.0000 | N | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2020-01-28 | 2020-01-28 13:01:17 | ANA | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 29 | Preduzetnici - subvencije po članu 21đ Zakona i članu 45g Zakona o doprinosima | 0.0000 | N | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2020-01-28 | 2020-01-28 13:01:25 | ANA | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 30 | Novozaposleni od 01.01.2020. (21ž - 45đ) oslobođen PIO 100% i porez 70% | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2020-01-30 | 2023-01-03 08:22:59 | 13 | 70.0000 | 100.0000 | 100.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 31 | Novozaposleni od 01.01.2020. (21ž - 45đ) oslobođen PIO 95% i porez 65% | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2020-01-30 | 2023-01-03 08:22:59 | 13 | 65.0000 | 95.0000 | 95.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 32 | Novozaposleni od 01.01.2020. (21ž - 45đ) oslobođen PIO 85% i porez 60% | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2020-01-30 | 2023-01-03 08:23:01 | 13 | 60.0000 | 85.0000 | 85.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 33 | Zarada novonastanjenog obveznika, umanjenje za 70% (15v-15a) | 3.0000 | N | 4.2000 | 1.5450 | 0.2250 | 3.0000 | 1.5450 | 0.0000 | 2020-12-08 | 2023-08-23 11:34:39 | 22 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 34 | Novozaposleni od 01.01.2020. (21ž - 45đ) oslobođen PIO 85% i porez 60% (2023-2025) | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2022-01-31 | 2023-01-31 09:33:59 | ANA | 60.0000 | 85.0000 | 85.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 35 | novozaposleni 2023 | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2023-01-06 | 2023-01-06 13:03:46 | 13 | 50.0000 | 75.0000 | 75.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 36 | novozaposleni 2024 | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2023-01-06 | 2023-01-06 13:16:24 | 13 | 40.0000 | 65.0000 | 65.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 37 | novozaposleni 2025 | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2023-01-06 | 2023-01-06 13:16:59 | 13 | 30.0000 | 55.0000 | 55.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 38 | Novozaposleni od 01.01.2022. (21ž - 45đ) oslobođen PIO 82% i porez 57% (2022-2025) | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2022-02-24 | 2023-01-31 09:34:01 | ANA | 57.0000 | 82.0000 | 82.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 39 | Novozaposleni od 01.01.2022. (21ž - 45đ) oslobođen PIO 72% i porez 47% (2022-2025) | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2022-02-24 | 2023-01-31 09:34:02 | ANA | 47.0000 | 72.0000 | 72.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 40 | Novozaposleni od 01.01.2022. (21ž - 45đ) oslobođen PIO 62% i porez 37% (2022-2025) | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2022-02-24 | 2023-01-31 09:34:03 | ANA | 37.0000 | 62.0000 | 62.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 41 | Novozaposleni od 01.01.2022. (21ž - 45đ) oslobođen PIO 52% i porez 27% (2022-2025) | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2022-02-24 | 2023-01-31 09:34:03 | ANA | 27.0000 | 52.0000 | 52.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 42 | Novozaposleni od 01.03.2022. (21z - 45ž) oslobođen PIO 100% i porez 70% (2022-2024) | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2022-02-24 | 2023-01-31 09:34:04 | ANA | 70.0000 | 100.0000 | 100.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 43 | Novozaposleni od 01.03.2022. (21i - 45z) oslobođen PIO 100% i porez 70%  | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2022-02-24 | 2023-01-31 09:34:04 | ANA | 70.0000 | 100.0000 | 100.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 49 | Zdravsteno - posebna nega deteta | 0.0000 | N | 0.0000 | 5.1500 | 0.0000 | 0.0000 | 5.1500 | 0.0000 | 2021-02-26 | 2021-02-26 14:25:39 | 10 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 51 | Privremeni poslovi - nemaju drugo osiguranje | 10.0000 | N | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2006-11-08 | 2023-01-03 08:23:02 | 13 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 52 | Privremeni poslovi - imaju drugo osiguranje (penzioneri) | 10.0000 | N | 14.0000 | 0.0000 | 0.0000 | 10.0000 | 0.0000 | 0.0000 | 2006-11-08 | 2023-01-03 08:23:04 | 13 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 101 | Z | 10.0000 | D | 14.0000 | 5.1500 | 0.7500 | 10.0000 | 5.1500 | 0.0000 | 2023-01-06 | 2023-01-06 12:29:17 | 1 | 50.0000 | 75.0000 | 75.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

---

## Tabela: `ldkategugod`
**Opis:** LD kategorije ugovora
**Redova:** 79

**Kolone:** `tipug`, `starasifra`, `sifkat`, `opis`, `porez_proc`, `porez_procum`, `pio_proc`, `zdro_proc`, `nortros_proc`, `proc_pioi`, `proc_zdroi`, `konto_duguje`, `konto_neto`, `konto_porez`, `konto_pio`, `konto_zdrav`, `konto_pioi`, `popdvid`, `sifravrsteplacanja`

| tipug | starasifra | sifkat | opis | porez_proc | porez_procum | pio_proc | zdro_proc | nortros_proc | proc_pioi | proc_zdroi | konto_duguje | konto_neto | konto_porez | konto_pio | konto_zdrav | konto_pioi | popdvid | sifravrsteplacanja |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | 1 | 301 | Prihod autora osiguran po drugom osnovu (50%NorTroš) | 20 | 0 | 24 | 0 | 50 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 2 | 302 | Prihod autora nije osiguran po drugom osnovu (50%NT) | 20 | 0 | 24 | 10.3 | 50 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 1 | 303 | Prihod autora osiguran po drugom osnovu (43%NT) | 20 | 0 | 24 | 0 | 43 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 2 | 304 | Prihod autora nije osiguran po drugom osnovu (43%NT) | 20 | 0 | 24 | 10.3 | 43 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 1 | 305 | Prihod autora osiguran po drugom osnovu (34%NT) | 20 | 0 | 24 | 0 | 34 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 2 | 306 | Prihod autora nije osiguran po drugom osnovu (34%NT) | 20 | 0 | 24 | 10.3 | 34 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 1 | 307 | Prihod autora osiguran po drugom osnovu (50%NT+naknada) | 20 | 0 | 24 | 0 | 50 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 2 | 308 | Prihod autora nije osiguran po drugom osnovu (50%NT+naknada) | 20 | 0 | 24 | 10.3 | 50 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 1 | 309 | Prihod autora osiguran po drugom osnovu (43%NT+naknada) | 20 | 0 | 24 | 0 | 43 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 2 | 310 | Prihod autora nije osiguran po drugom osnovu (43%NT+naknada) | 20 | 0 | 24 | 10.3 | 43 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 1 | 311 | Prihod autora osiguran po drugom osnovu (34%NT+naknada) | 20 | 0 | 24 | 0 | 34 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 2 | 312 | Prihod autora nije osiguran po drugom osnovu (34%NT+naknada) | 20 | 0 | 24 | 10.3 | 34 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 1 | 313 | Prihod autora osiguran po drugom osnovu (stvarni troškovi) | 20 | 0 | 24 | 0 | 0 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 2 | 314 | Prihod autora nije osiguran po drugom osnovu (stvarni troškovi) | 20 | 0 | 24 | 10.3 | 0 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 3 | 315 | Prihod autora bez plaćanja doprinosa (50%NT) | 20 | 0 | 0 | 0 | 50 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 3 | 316 | Prihod autora bez plaćanja doprinosa (43%NT) | 20 | 0 | 0 | 0 | 43 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 3 | 317 | Prihod autora bez plaćanja doprinosa (34%NT) | 20 | 0 | 0 | 0 | 34 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 3 | 318 | Prihod autora bez plaćanja doprinosa (50%NT+naknada) | 20 | 0 | 0 | 0 | 50 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 3 | 319 | Prihod autora bez plaćanja doprinosa (43%NT+naknada) | 20 | 0 | 0 | 0 | 43 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 3 | 320 | Prihod autora bez plaćanja doprinosa (34%NT+naknada) | 20 | 0 | 0 | 0 | 34 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 3 | 321 | Prihod autora bez plaćanja doprinosa (stvarni troškovi) | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 3 | 322 | Prihod vlasnika prava industrijske svojine (stvarni troškovi) | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| A | 3 | 323 | Prihod naslednika autorskog prava uz priznavanje troškova na ime naknade | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 5230 | 4650 | 4891 | 4891 | 4891 |  | NULL | 249 |
| I | 1 | 401 | Kamate po osnovu zajma, štednih i drugih depozita i hartija od vrednosti | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 5629 | 4609 | 4899 | 4899 | 4899 |  | NULL | 248 |
| I | 1 | 402 | Dividende i učešće u dobiti | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 3400 | 4620 | 4899 | 4899 | 4899 |  | NULL | 248 |
| I | 1 | 403 | Dividende i učešće u dobiti kod kupovine društvenog kapitala | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 3400 | 4620 | 4899 | 4899 | 4899 |  | NULL | 248 |
| I | 1 | 404 | Prinos od investicione jedinice otvorenog investicionog fonda | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 3400 | 4620 | 4899 | 4899 | 4899 |  | NULL | 248 |
| I | 4 | 405 | Prihod od izdavanja nepokretnosti (25% normiranih troškova) | 20 | 0 | 0 | 0 | 25 | 0 | 0 | 5250 | 4654 | 4890 | 4890 | 4890 |  | NULL | 248 |
| I | 5 | 406 | Prihod od iznajmljivanja stanova, soba i postelja (50%NT) | 20 | 0 | 0 | 0 | 50 | 0 | 0 | 5250 | 4654 | 4892 | 4892 | 4892 |  | NULL | 248 |
| I | 5 | 407 | Prihod od izdavanja nepokretnosti, stanova,soba i postelja (stvarni troškovi) | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 5250 | 4654 | 4892 | 4892 | 4892 |  | NULL | 248 |
| I | 2 | 408 | Primanja zaposlenih i članova uprave privrednog društva po osnovu učešća i dobiti | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 3400 | 4620 | 4899 | 4899 | 4899 |  | NULL | 248 |
| I | 3 | 409 | Uzimanje iz imovine i korišćenje usluga privrednog društva zaključno sa 23.05.13 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 3400 | 4620 | 4899 | 4899 | 4899 |  | NULL | 248 |
| I | 3 | 410 | Uzimanje iz imovine i korišćenje usluga privrednog društva od 01.01.16 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 3400 | 4620 | 4899 | 4899 | 4899 |  | NULL | 248 |
| Z | 12 | 501 | Zakup pokretnih stvari uz normirane troškove 20% | 20 | 0 | 0 | 0 | 20 | 0 | 0 | 5250 | 4654 | 4890 | 4890 | 4890 |  | NULL | 248 |
| Z | 12 | 502 | Zakup pokretnih stvari uz priznavanje stvarnih troškova | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 5250 | 4654 | 4892 | 4892 | 4892 |  | NULL | 248 |
| Z | 12 | 503 | Dobici od igara na sreću | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 5250 | 4654 | 4892 | 4892 | 4892 |  | NULL | 249 |
| Z | 12 | 504 | Prihodi od osiguranja lica | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 5250 | 4654 | 4892 | 4892 | 4892 |  | NULL | 249 |
| Z | 12 | 505 | Prihod profesionalnih sportista, amatera, sportskih stručnjaka osiguran (50%NT) | 20 | 0 | 24 | 0 | 50 | 0 | 0 | 5250 | 4654 | 4892 | 4892 | 4892 |  | NULL | 249 |
| Z | 12 | 506 | Prihod profesionalnih sportista, amatera, sportskih stručnjaka nije osiguran (50%NT) | 20 | 0 | 24 | 10.3 | 50 | 0 | 0 | 5250 | 4654 | 4892 | 4892 | 4892 |  | NULL | 249 |
| Z | 12 | 507 | Prihod profesionalnih sportista, amatera, sportskih stručnjaka (50%NT) | 20 | 0 | 0 | 0 | 50 | 0 | 0 | 5250 | 4654 | 4892 | 4892 | 4892 |  | NULL | 249 |
| Z | 12 | 508 | Prihod profesionalnih sportista, amatera, sportskih stručnjaka bez doprinosa (50%NT) | 20 | 0 | 0 | 0 | 50 | 0 | 0 | 5250 | 4654 | 4892 | 4892 | 4892 |  | NULL | 249 |
| D | 1 | 601 | UGOVOR O DELU, NAKNADE ZA ZASTUPANJE-OSIGURANO LIC | 20 | 0 | 24 | 0 | 20 | 0 | 0 | 5220 | 4650 | 4890 | 4890 | 4890 |  | NULL | 249 |
| D | 2 | 602 | Ugovor o delu, nije osiguran po drugom osnovu (20% normiranih troškova) | 20 | 0 | 24 | 10.3 | 20 | 0 | 0 | 5220 | 4650 | 4890 | 4890 | 4890 |  | NULL | 249 |
| D | 4 | 603 | Ugovor o delu, bez doprinosa (20% normiranih troškova) | 20 | 0 | 0 | 0 | 20 | 0 | 0 | 5220 | 4650 | 4890 | 4890 | 4890 |  | NULL | 249 |
| C | 1 | 604 | Privremeni i povremeni poslovi preko zadruge lica do 26 godina | 20 | 40 | 0 | 0 | 20 | 4 | 2 | 5240 | 4650 | 4890 | 4890 | 4890 | 4890 | NULL | 249 |
| D | 1 | 605 | Prihodi po osnovu dopunskog rada | 20 | 0 | 24 | 0 | 20 | 0 | 0 | 5250 | 4653 | 4899 | 4899 | 4899 |  | NULL | 249 |
| D | 4 | 606 | Prihodi po osnovu dopunskog rada bez plaćanja doprinosa | 20 | 0 | 0 | 0 | 20 | 0 | 0 | 5250 | 4653 | 4899 | 4899 | 4899 |  | NULL | 249 |
| S | 3 | 607 | Prihodi od prikupljanja i prodaje sekundarnih sirovina (20%NT) | 20 | 40 | 0 | 0 | 20 | 0 | 0 | 5559 | 5559 | 48901 | 48901 | 48901 |  | NULL | 249 |
| S | 1 | 608 | Prihodi od prikupljanja i prodaje šumskih plodova i lekovitog bilja osiguran po drugom osnovu (20%NT | 20 | 40 | 24 | 0 | 20 | 0 | 0 | 5250 | 4654 | 4899 | 4899 | 4899 |  | NULL | 249 |
| S | 2 | 609 | Prihodi od prikupljanja i prodaje šumskih plodova i lekovitog bilja nije osiguran po drugom osnovu ( | 20 | 40 | 24 | 10.3 | 20 | 0 | 0 | 5250 | 4654 | 4899 | 4899 | 4899 |  | NULL | 249 |

---

## Tabela: `cnfg_parametri`
**Opis:** Konfiguracioni parametri - prvih 50
**Redova:** 1116

**Kolone:** `id`, `vrsta`, `klasifikacija`, `naziv`, `tip`, `tipvrednost`, `vrednost`

| id | vrsta | klasifikacija | naziv | tip | tipvrednost | vrednost |
| --- | --- | --- | --- | --- | --- | --- |
| 10001 | 1 | 101 | Klijent koristi internet VPN konekciju | 1 | NULL | 0 |
| 10002 | 1 | 101 | Podrazumevana godina | 2 | NULL | 2026 |
| 10005 | 1 | 101 | Radno vreme od | 3 | NULL | 06:00:00 |
| 10006 | 1 | 101 | Data terminal - tip | 4 | CIPHERLAB 800x,UNITECH HT630,DATALOGIC,BIZNISOFT ASSISTANT,NEWLAND N2S000 | 2 |
| 10007 | 1 | 101 | Data terminal - port | 2 | NULL | 2 |
| 10008 | 1 | 101 | Data terminal - separator | 5 | NULL | , |
| 10009 | 1 | 101 | Koristi se samo obračun LD-a | 1 | NULL | 0 |
| 10011 | 1 | 101 | Vrsta štampe | 4 | Tektualna,Grafička | 1 |
| 10012 | 1 | 101 | Podrazumevani DOC/XLS program | 4 | Microsoft Excel/Word,OpenOffice Calc/Writer | 0 |
| 10013 | 1 | 101 | Standardni tip dostave | 2 | Lično preuzimanje,Naš prevoz,Pošta - pretplata,Pošta - pouzećem,Kurirska služba - pretplata, Kurirsk | 2 |
| 10014 | 1 | 101 | Prikaz količina na 3 decimale | 1 | NULL | 0 |
| 10015 | 1 | 101 | Zaokruženje na 2 decimale kod nabavke | 1 | NULL | 0 |
| 10016 | 1 | 101 | Knjiženje naloga sa detektovanim minusnim stanjem | 1 | NULL | 1 |
| 10017 | 1 | 102 | Obračun nabavke - Maloprodaja - Tip 01 | 4 | FIFO,Prosečna nabavna cena,Prodajna cena (VPC) | 2 |
| 10018 | 1 | 102 | Obračun nabavke - Veleprodaja - Tip 02 | 4 | FIFO,Prosečna nabavna cena,Prodajna cena (VPC) | 2 |
| 10019 | 1 | 102 | Obračun nabavke - Veleprodaja - Tip 08 | 4 | FIFO,Prosečna nabavna cena | 1 |
| 10020 | 1 | 102 | Obračun nabavke - Magacin repromaterijala - Tip 10 | 4 | FIFO,Prosečna nabavna cena,Planska nabavna cena | 1 |
| 10021 | 1 | 102 | Obračun nabavke - Gotovi proizvodi - Tip 09 | 4 | Planska cena koštanja,Stvarna cena koštanja | 0 |
| 10022 | 1 | 102 | Obračun nabavke - Poluproizvodi - Tip 11 | 4 | Planska cena koštanja,Stvarna cena koštanja | 0 |
| 10023 | 1 | 102 | Knjiži dokument vezu u polje "Eksterni dokument" prilikom knjiženja izlaznih dokumenta | 1 | NULL | 1 |
| 10024 | 1 | 103 | Ignoriši minusno stanje | 1 | NULL | 0 |
| 10025 | 1 | 103 | Dodatna F9 potvrda pogrešne šifre | 1 | NULL | 1 |
| 10026 | 1 | 103 | Podaci iz kase se ne knjiže | 1 | NULL | 0 |
| 10027 | 1 | 103 | Šifra je sastavni deo naziva | 1 | NULL | 1 |
| 10028 | 1 | 103 | Ignoriši greške kod izdavanja fiskalnog isečka | 1 | NULL | 0 |
| 10029 | 1 | 103 | Ignoriši pogrešne količine | 1 | NULL | 1 |
| 10030 | 1 | 103 | Barkod čitač je podrazumevan | 1 | NULL | 0 |
| 10031 | 1 | 103 | Prikaži grešku ukoliko artikal nema cenu | 1 | NULL | 1 |
| 10032 | 1 | 103 | Specifičnost zaokruženja GP550 | 1 | NULL | 0 |
| 10033 | 1 | 103 | Ne prikazuj rabate u POS-u | 1 | NULL | 0 |
| 10034 | 1 | 103 | Bizerba BC2 dužina naziva 283 | 1 | NULL | 0 |
| 10036 | 1 | 103 | Omogući unos dodatnih podataka | 1 | NULL | 0 |
| 10037 | 1 | 103 | Naziv dodatnih podataka | 6 | NULL | REGISTARSKI BROJ: |
| 10038 | 1 | 104 | Omogući brisanje računa | 1 | NULL | 0 |
| 10040 | 1 | 104 | Omogući unos/ažuriranje artikla | 1 | NULL | 1 |
| 10046 | 1 | 106 | Omogući promenu cene u objektu iz koga se prenosi roba u internim računima | 1 | NULL | 0 |
| 10047 | 1 | 106 | Omogući promenu cene u objektu u kome se prenosi roba u internim računima i za objekte koji se vode  | 1 | NULL | 0 |
| 10048 | 1 | 106 | Prikaži dugovanje partnera kod fakturisanja | 1 | NULL | 1 |
| 10049 | 1 | 106 | Prikaži zadnju fakturnu cenu prilikom obrade prijemnih dokumenata | 1 | NULL | 1 |
| 10050 | 1 | 106 | Omogući menjanje broja fakture/naloga | 1 | NULL | 1 |
| 10052 | 1 | 106 | Postoji cenovnik u bodovima | 1 | NULL | 0 |
| 10053 | 1 | 101 | Ne prikazuj crveni font u izveštajima | 1 | NULL | 0 |
| 10054 | 1 | 106 | PDV po otpisu iznad zakonskih limita knjiži na BSRN0060/BSRN0061 | 1 | NULL | 0 |
| 10055 | 1 | 106 | Formiraj izdatnicu ambalaže prilikom štampe naloga za izdavanje | 1 | NULL | 0 |
| 10056 | 1 | 106 | Onemogući unos istog artikla u dokumentima izlaza | 1 | NULL | 0 |
| 10057 | 1 | 106 | Omogući unos istog barkoda na više artikla u šifarniku | 1 | NULL | 0 |
| 10058 | 1 | 106 | Ne prikazuj datum štampe u izveštajima | 1 | NULL | 0 |
| 10059 | 1 | 106 | Štampaj ambalažu sa tekućeg dokumenta | 1 | NULL | 1 |
| 10060 | 1 | 106 | Narudžbine kupaca - Ignoriši raspoložive količine prilikom rezervisanja | 1 | NULL | 0 |
| 10061 | 1 | 106 | Narudžbine kupaca - Potvrda kontrolne liste sa količinskim razlikama | 1 | NULL | 1 |

---
