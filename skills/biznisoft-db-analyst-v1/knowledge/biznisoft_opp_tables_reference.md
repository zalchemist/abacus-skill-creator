# Biznisoft OPP - Referenca šifarničkih tabela

> Baza `opp` sadrži zajedničke šifarnike i definicije koje dele sve firme.
> Generisano: 2025-03-29

---

# 1. DEFINICIJE DOKUMENATA

## Tabela: documents
Baza: opp
**Opis:** Centralna tabela koja mapira šifre dokumenata na tabele, forme i štampu. Svaki tip dokumenta (RN, KL, NC...) ima red koji definiše u kojoj tabeli se čuvaju podaci.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | char(2) | NO | PRI |
| naziv | varchar(255) | YES |  |
| tabela | varchar(50) | NO |  |
| tipkljuca | int(1) | NO |  |
| tipdokfakt | char(1) | YES |  |
| veza | int(1) | NO |  |
| forma | varchar(255) | YES |  |
| stampa | varchar(255) | YES |  |
| statistika | int(1) | YES |  |
| statkoef | double(6,2) | YES |  |
| izlaznidokument | int(1) | YES |  |
| stampaneprok | int(1) | YES |  |
| numtipdok | int(2) | YES |  |

---

### Mapiranje dokumenata na tabele

| Šifra | Naziv | Tabela | Tip ključa |
|-------|-------|--------|------------|
| AA | INTERNI PRENOS AMBALAŽE | tblambintpr | Interni prenos |
| AJ | PRIJEM AMBALAŽE OD DOBAVLJAČA | tblamprijdob | Prodaja/Izdavanje |
| AM | IZDAVANJE AMBALAŽE | tblamizdkup | Prodaja/Izdavanje |
| AP | POVRAĆAJ AMBALAŽE OD KUPCA | tblampovkup | Prodaja/Izdavanje |
| AR | FIN.TRANSAKCIJE - PRIJEM AVANSNOG RAČUNA | frmgk_avans | Fin.transakcija |
| AV | POVRAĆAJ AMBALAŽE DOBAVLJAČU | tblampovdob | Prodaja/Izdavanje |
| BL | BLAGAJNIČKO POSLOVANJE | blgpromet | Blagajna |
| CR | FIN.TRANSAKCIJE - PRIJEM CARINSKOG RAČUNA | frmgk_carina | Fin.transakcija |
| DD | POVRAĆAJ DOBAVLJAČU IZ D.O. | prodpovracajdob | Nabavka |
| DF | FAKTURE IZ DISLOCIRANIH OBJEKATA | tblprodfakture | Prodaja/Izdavanje |
| DK | KALKULACIJA IZ D.O. | prodkalkulacije | Nabavka |
| DN | NIVELACIJA IZ D.O. | prodnivelacije | Nivelacija |
| DP | PRIJEM ROBE SA OBRADE/DORADE | tblrobobrdorprij | Nabavka |
| ED | FIN.TRANSAKCIJE - ELEKTRONSKE DOPUNE | frmgk_ed | Fin.transakcija |
| FA | FAKTURA SA AKCIJSKIM RABATOM | tblfaktakcrab | Prodaja/Izdavanje |
| FK | FIN.TRANSAKCIJE - IZLAZNA FAKTURA | frmgk_faktura | Fin.transakcija |
| FM | PRODAJA REPROMATERIJALA | tblprodmat | Prodaja/Izdavanje |
| FS | IZLAZNA FAKTURA / RAČUN ZA OS | faktureos | Prodaja/Izdavanje |
| GN | GRUPNI RADNI NALOG | radnal | Radni nalog |
| GP | PRODAJA GOTOVIH PROIZVODA (POGONSKO) | tblprodajagp | Prodaja/Izdavanje |
| II | INTERNO IZDAVANJE ROBE | tblintizdavanje | Interni prenos |
| IN | PUTNI NALOG U INOSTRANSTVU | putninalog | Putni nalog |
| IP | INTERNI PRIJEM ROBE | intprijem | Nabavka |
| IR | INTERNI PRENOS DOBARA | intracun | Interni prenos |
| KA | KASA U MALOPRODAJI | kasa | Kasa |
| KF | IZDAVANJE FAKTURE KOMISIONARU | tblkomfakture | Prodaja/Izdavanje |
| KI | KALKULACIJA SA NIVELACIJOM | nivkalkulacije | Nabavka |
| KK | KALKULACIJA KOMISIONE ROBE | tblkomkalk | Nabavka |
| KL | KALKULACIJA/PRIJEMNICA DOBARA | kalkulacije | Nabavka |
| KN | NIVELACIJA KOMISIONE ROBE | komnivelacije | Nivelacija |
| KO | IZDAVANJE REPROMATERIJALA KOOPERANTU | tblkooizdavanje | Prodaja/Izdavanje |
| KV | VRAĆANJE KOMISIONE ROBE | tblkomvrac | Nabavka |
| LL | ISPLATA POLJOPRIVREDNOM PROIZVOĐAČU | tblisplata | Isplata |
| MO | SLANJE MATERIJALA NA OBRADU/DORADU | tblmatobrdor | Prodaja/Izdavanje |
| MP | PRIJEM MATERIJALA SA OBRADE/DORADE | tblmatobrdorprij | Nabavka |
| NA | NALOG ZA IZDAVANJE SA AKCIJSKIM RABATOM | tblfaktakcrab | Prodaja/Izdavanje |
| NB | NABAVKA AMBALAŽE | nabambalaze | Nabavka |
| NC | NIVELACIJA CENE | nivelacije | Nivelacija |
| ND | NARUDŽBINE DOBAVLJAČIMA | tblnardobavljacima | Nabavka |
| NI | NALOG ZA IZDAVANJE | fakture | Prodaja/Izdavanje |
| NK | NARUDŽBINE KUPACA | tblnarkupaca | Prodaja/Izdavanje |
| NO | NALOG ZA POVRAĆAJ ROBE KUPCA | tblpovracaj | Prodaja/Izdavanje |
| NP | POVRAĆAJ ROBE DOBAVLJAČU - NOVI PROMET | tblpovracajdobnovi | Prodaja/Izdavanje |
| NR | FIN.TRANSAKCIJE - FAKTURA NEFAKTURISANE ROBE | frmgk_nefak | Fin.transakcija |
| OA | OTPREMNICA SA AKCIJSKIM RABATOM | tblfaktakcrab | Prodaja/Izdavanje |
| OD | PRIJEM ODOBRENJA/ZADUŽENJA DOBAVLJAČA | tblodobdob | Prodaja/Izdavanje |
| OK | KNJIŽNO ODOBRENJE | tblodobkup | Prodaja/Izdavanje |
| ON | OTPIS MIMO ZAKONSKIH STOPA | tblotpisnz | Prodaja/Izdavanje |
| OS | FIN.TRANSAKCIJE - NABAVKA STALNOG SREDSTVA | frmgk_osnsred | Fin.transakcija |
| OT | OTPREMNICA | fakture | Prodaja/Izdavanje |
| OZ | OTPIS PO ZAKONSKIM STOPAMA | tblotpisz | Prodaja/Izdavanje |
| PC | PROMENA CENE | robno | Robno knjiženje |
| PD | POVRAĆAJ ROBE DOBAVLJAČU | tblpovracajdob | Nabavka |
| PF | PROFAKTURA/REZERVACIJA | fakture | Prodaja/Izdavanje |
| PI | INTERNI RAČUN IZ D.O. | prodintracun | Interni prenos |
| PK | POVRAĆAJ ROBE OD KUPCA | tblpovracaj | Prodaja/Izdavanje |
| PL | VIŠAK/MANJAK PO POPISNOJ LISTI | popis | Popis |
| PN | PUTNI NALOG U ZEMLJI | putninalog | Putni nalog |
| PO | FAKTURISANJE PO POS OTPREMNICAMA | tblposotpremnice | Prodaja/Izdavanje |
| PP | OTKUP POLJOPRIVREDNIH PROIZVODA | tblpoljoprivreda | Nabavka |
| PR | PREKNJIŽAVANJE PROMETA | nema | Preknjižavanje |
| PS | POČETNO STANJE | robno | Robno knjiženje |
| PZ | DNEVNI PAZARI | pazari | Robno knjiženje |
| RA | AVANSNI RAČUN | fakture | Prodaja/Izdavanje |
| RB | FAKTURISANJE BEZ OBRAČUNA NABAVKE | tblfaktbezobr | Prodaja/Izdavanje |
| RC | KOREKCIJA NABAVNE CENE | nema | Preknjižavanje |
| RD | RADNI NALOG | radnal | Radni nalog |
| RK | Prijem računa komitenta | frmgk_prijemfakture | Fin.transakcija |
| RM | PRODAJA AMBALAŽE | tblprodamb | Prodaja/Izdavanje |
| RN | IZLAZNA FAKTURA / RAČUN | fakture | Prodaja/Izdavanje |
| RO | SLANJE ROBE NA OBRADU/DORADU | tblrobobrdor | Prodaja/Izdavanje |
| RT | RAČUN SOPSTVENIH TROŠKOVA | tblsopsttros | Prodaja/Izdavanje |
| SK | NABAVKA SITNOG INVENTARA | tblnabsitinv | Nabavka |
| SN | SERVISNI NALOG | dt_srv_rnpojed | Servis |
| SP | POVRAĆAJ SITNOG INVENTARA OS RADNIKA | sitinvpov | Interni prenos |
| SR | RASHODOVANJE SITNOG INVENTARA | sitinvras | Prodaja/Izdavanje |
| SU | IZDAVANJE SITNOG INVENTARA U UPOTREBU | tblsitanizd | Interni prenos |
| SZ | ZADUŽENJE SITNOG INVENTARA PO RADNICIMA | sitinvzad | Interni prenos |
| TB | TREBOVANJE ROBE | tbltrebovanje | Nabavka |
| TF | TRANSFORMACIJE ARTIKALA PO RECEPTURI | tblrobtransf | Nabavka |
| TI | IZDAVANJE TUĐE ROBE | tblizdavanje | Prodaja/Izdavanje |
| TO | PRIJEM TUĐE ROBE | tblotkup | Nabavka |
| TR | FIN.TRANSAKCIJE - RAČUN TROŠKOVA | frmgk_troskovi | Fin.transakcija |
| TS | OTKUP SEKUNDARNIH SIROVINA | tblotkupss | Nabavka |
| UI | IZDAVANJE ROBE NA TUĐE SKLADIŠTE - REVERS | tblreversizdavanje | Prodaja/Izdavanje |
| UK | UVOZNA KALKULACIJA | tbluvoz | Nabavka |
| UP | PRIJEM ROBE SA TUĐEG SKLADIŠTA - REVERS | tblreversprijem | Nabavka |
| VO | SLANJE PROIZVODA NA OBRADU/DORADU | tblproizvobrdor | Prodaja/Izdavanje |
| VP | PRIJEM PROIZVODA SA OBRADE/DORADE | tblproizvobrdorprij | Nabavka |
| ZA | IZVOZ - AVANSNI RAČUN | tblizvoz | Prodaja/Izdavanje |
| ZD | KNJIŽNO ODOBRENJE/ZADUŽENJE INO DOBAVLJAČA | tblodobinodob | Prodaja/Izdavanje |
| ZI | POVRAĆAJ ROBE INO KUPCA | tblpovracajinokup | Prodaja/Izdavanje |
| ZO | KNJIŽNO ODOBRENJE/ZADUŽENJE INO KUPCA | tblodobinokup | Prodaja/Izdavanje |
| ZP | IZVOZ - PROFAKTURA U EUR | tblizvoz | Prodaja/Izdavanje |
| ZZ | IZVOZ ROBE I USLUGA | tblizvoz | Prodaja/Izdavanje |

---

# 2. KONTNI PLAN I FINANSIJSKI ŠIFARNICI

## Tabela: tabrac
Baza: opp
**Opis:** Tarifni brojevi - klasifikacija artikala za poreske svrhe

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | varchar(20) | NO | PRI |
| naziv | varchar(255) | YES |  |
| konto | varchar(20) | NO |  |
| sifrakpl | varchar(20) | NO | PRI |

---

## Tabela: kontniplan
Baza: opp
**Opis:** Kontni plan - šifarnik računa za finansijsko knjigovodstvo

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| racun | varchar(10) | NO | PRI |
| naziv | varchar(255) | YES |  |
| analitika | varchar(50) | NO |  |
| knjizenje | varchar(20) | NO |  |
| valuta | int(1) | NO |  |
| zatvaranje | int(1) | NO |  |
| mestotr | int(1) | NO |  |
| nosioc | int(1) | NO |  |
| karakter | int(1) | YES |  |
| kursr | int(1) | YES |  |
| napomena | varchar(1000) | YES |  |
| starikonto | varchar(10) | YES |  |
| sifrakpl | varchar(10) | NO | PRI |
| vremeizmene | timestamp | NO |  |
| operater | varchar(20) | YES |  |
| ignmtnt | int(1) | YES |  |
| sifpopdv | int(4) | YES |  |

---

## Tabela: stope
Baza: opp
**Opis:** Stope za razne obračune

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| ppproi | double | YES |  |
| ppusl | double | YES |  |
| ppruc | double | YES |  |

---

## Tabela: pdvstope
Baza: opp
**Opis:** PDV stope - poreske stope (opšta, posebna, oslobođeno)

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| stopa | varchar(2) | NO | PRI |
| datumod | date | NO | PRI |
| datumdo | date | NO | PRI |
| stopapdv | double(15,2) | YES |  |
| vremeizmene | timestamp | NO |  |

---

## Tabela: sifval
Baza: opp
**Opis:** Šifarnik valuta (RSD, EUR, USD...)

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifval | int(3) | NO | PRI |
| oznval | char(3) | NO | UNI |
| nazval | varchar(35) | NO |  |
| nazzem | varchar(35) | NO |  |
| na_kl | enum('D','N') | YES |  |
| datcre | date | YES |  |
| operater | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifval | sifval | sifra | Valuta |

---

## Tabela: zirklista
Baza: opp
**Opis:** Kursna lista - kursevi valuta

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| datum | date | NO | PRI |
| eur | double(15,5) | YES |  |
| usd | double(15,5) | YES |  |
| chf | double(15,5) | YES |  |
| operater | varchar(50) | YES |  |

---

## Tabela: sifpla2konta
Baza: opp
**Opis:** Mapiranje šifri plaćanja na konta

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifpla | smallint(3) | NO | PRI |
| tipdok | tinyint(2) | NO | PRI |
| opisdok | varchar(35) | NO |  |
| rnodob | varchar(12) | YES |  |
| rnzadu | varchar(12) | YES |  |
| datcre | date | YES |  |
| datizm | datetime | YES |  |
| operater | varchar(12) | YES |  |
| racun | varchar(50) | NO | PRI |
| polje | int(1) | NO | PRI |
| tipoperacije | int(1) | NO | PRI |
| analitika | varchar(10) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| sifrakpl | varchar(10) | NO | PRI |
| firma | int(4) | NO | PRI |

---

## Tabela: kplprevod
Baza: opp
**Opis:** Prevod kontnog plana između verzija

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifradr | int(3) | NO | PRI |
| nazivdr | varchar(100) | YES |  |
| sifrakpl | varchar(10) | NO | PRI |
| racun | varchar(10) | NO | PRI |
| naziv | varchar(255) | NO |  |
| prevod | varchar(255) | YES |  |

---

## Tabela: fkopis
Baza: opp
**Opis:** Opisi za fiskalni račun

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| TABLE_SCHEMA | varchar(64) | NO |  |
| tbl | varchar(64) | NO |  |
| COLUMN_NAME | varchar(64) | NO |  |
| fk | varchar(64) | NO | PRI |
| opis | varchar(255) | YES |  |
| REFERENCED_TABLE_NAME | varchar(64) | YES |  |

---

# 3. ORGANIZACIONI ŠIFARNICI

## Tabela: operateri
Baza: opp
**Opis:** Operateri sistema - korisnici sa pristupom, šifrom i pravima

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| korime | varchar(12) | NO | PRI |
| lozinka | varchar(50) | YES |  |
| imeiprezime | varchar(50) | YES |  |
| ovlascenje | int(2) | YES |  |
| zadnja | int(4) | YES |  |
| objekat | int(2) | YES |  |
| slika | longblob | YES |  |
| potpis | longblob | YES |  |
| adresa | varchar(255) | YES |  |
| brtel | varchar(100) | YES |  |
| ovllice | varchar(255) | YES |  |
| matbr | varchar(50) | YES |  |
| email | varchar(255) | YES |  |
| posoperater | varchar(4) | YES |  |
| poslozinka | varchar(6) | YES |  |
| posnaziv | varchar(24) | YES |  |
| zadpromloz | date | YES |  |
| ovlpromrabat | int(1) | YES |  |
| ovlplate | int(1) | YES |  |
| promenacene | int(1) | YES |  |
| izmenidokument | int(1) | YES |  |
| prikaznabcene | int(1) | YES |  |
| servis_level1 | int(1) | YES |  |
| servis_level2 | int(1) | YES |  |
| vrednostboda | int(1) | YES |  |
| ovl_artikli | int(1) | YES |  |
| passcomp | int(1) | YES |  |
| passchange | int(1) | YES |  |
| notifikacije | int(1) | YES |  |

---

## Tabela: sifobj
Baza: opp
**Opis:** Objekti/poslovnice u matičnoj bazi

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | int(2) | NO | PRI |
| naziv | varchar(50) | YES |  |
| racun | varchar(12) | YES |  |

---

## Tabela: drzave
Baza: opp
**Opis:** Šifarnik država

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| ID | int(6) | YES |  |
| DrzavaAlfa2Kod | varchar(10) | YES |  |
| DrzavaAlfa3Kod | varchar(10) | YES |  |
| DrzavaNumerikKod | varchar(10) | YES |  |
| DrzavaGeoKod | varchar(10) | YES |  |
| DrzavaNazivCir | text | YES |  |

---

## Tabela: sifzem
Baza: opp
**Opis:** Šifarnik zemalja (širi od drzave)

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sif_swift | char(2) | NO | PRI |
| sif_a3 | char(3) | YES | MUL |
| sif_num | int(3) unsigned | NO | MUL |
| nazzem | varchar(50) | YES |  |
| datcre | date | YES |  |
| datizm | datetime | YES |  |

---

## Tabela: opstine
Baza: opp
**Opis:** Šifarnik opština

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifopst | smallint(3) | NO | PRI |
| nazivopst | varchar(30) | NO |  |
| datcre | date | YES |  |
| operater | varchar(50) | YES |  |
| kontbr | varchar(255) | YES |  |

---

## Tabela: pbrmesto
Baza: opp
**Opis:** Šifarnik mesta sa poštanskim brojevima

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| pbr | int(5) | YES |  |
| mesto | varchar(200) | NO | PRI |

---

## Tabela: ptt_brojevi
Baza: opp
**Opis:** PTT brojevi i mesta

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| ptt_broj | int(5) | NO | PRI |
| mesto | varchar(250) | YES |  |
| vremeizmene | timestamp | NO |  |

---

## Tabela: sifzanimanja
Baza: opp
**Opis:** Šifarnik zanimanja

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | int(6) | NO | PRI |
| naziv | varchar(200) | YES |  |
| operater | varchar(12) | YES |  |

---

## Tabela: sifplac
Baza: opp
**Opis:** Šifarnik načina plaćanja

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | char(3) | NO | PRI |

---

## Tabela: nazmes
Baza: opp
**Opis:** Nazivi meseci na srpskom

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| mesec | tinyint(2) unsigned | NO | PRI |

---

## Tabela: tabakciza
Baza: opp
**Opis:** Tabela akciza na robu

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifraakcize | int(4) | NO | PRI |
| nazivakcize | varchar(500) | YES |  |
| datumod | date | NO | PRI |
| datumdo | date | NO | PRI |
| iznoszasifakcize | double(15,6) | YES |  |
| vremeizmene | timestamp | NO |  |
| operater | varchar(50) | YES |  |

---

# 4. KORISNICI I PRAVA

## Tabela: korisnik
Baza: opp
**Opis:** Korisnički nalozi za pristup sistemu

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| matbr | int(8) | NO |  |
| pun_naziv | varchar(80) | NO |  |
| skr_naz | varchar(35) | NO |  |
| ulibr | varchar(35) | NO |  |
| postbroj | varchar(5) | YES |  |
| mesto | varchar(30) | YES |  |
| telefoni | varchar(50) | YES |  |
| pib | varchar(9) | YES |  |
| ziro_rn | varchar(22) | YES |  |
| regbr | varchar(20) | YES |  |
| web | varchar(50) | YES |  |

---

## Tabela: roles
Baza: opp
**Opis:** Role/uloge korisnika sa pravima pristupa

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| roleid | varchar(36) | NO | PRI |

---

## Tabela: klijenti
Baza: opp
**Opis:** Lista klijenata/firmi koje koriste sistem

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | int(4) | NO | PRI |
| naziv | varchar(80) | YES |  |
| skrnaz | varchar(35) | YES |  |
| vlasnik | varchar(50) | YES |  |
| postbroj | varchar(5) | YES |  |
| mesto | varchar(25) | YES |  |
| ulibr | varchar(35) | YES |  |
| telefoni | varchar(50) | YES |  |
| opstina | smallint(5) unsigned | YES |  |
| pib | varchar(9) | YES |  |
| zr1 | varchar(20) | YES |  |
| zr2 | varchar(20) | YES |  |
| zr3 | varchar(20) | YES |  |
| matbr | int(8) | YES |  |
| sifdel | int(5) | YES |  |
| regbr | varchar(20) | YES |  |
| web | varchar(35) | YES |  |
| email | varchar(35) | YES |  |
| pdvobv | enum('D','N') | NO |  |
| pdvbroj | varchar(11) | YES |  |
| datcre | date | YES |  |
| datizm | datetime | YES |  |

---

# 5. KONFIGURACIJA SISTEMA

## Tabela: cnfg_config
Baza: opp
**Opis:** Globalna konfiguracija sistema

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| entitet | int(1) | NO | PRI |
| vrednent | varchar(255) | NO | PRI |
| id | int(5) | NO | PRI |
| vrednost | varchar(500) | NO |  |
| prioritet | int(1) | NO |  |

---

## Tabela: cnfg_parametri
Baza: opp
**Opis:** Parametri konfiguracije - key/value

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| id | int(5) | NO | PRI |
| vrsta | int(3) | NO |  |
| klasifikacija | int(3) | NO |  |
| naziv | varchar(255) | NO |  |
| tip | int(2) | NO |  |
| tipvrednost | varchar(500) | YES |  |

---

## Tabela: cnfg_klasifikacija
Baza: opp
**Opis:** Klasifikacije konfiguracionih stavki

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | int(3) | NO | PRI |

---

## Tabela: cnfg_vrste
Baza: opp
**Opis:** Vrste konfiguracionih parametara

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | int(3) | NO | PRI |

---

## Tabela: propisani_parametri
Baza: opp
**Opis:** Propisani/zakonski parametri

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| id | int(5) | NO | PRI |
| tip | int(2) | NO |  |
| opis | varchar(300) | YES |  |
| uhiljadama | int(1) | YES |  |
| pisinule | int(1) | YES |  |
| tipvrednost | varchar(500) | YES |  |
| vrednost | longtext | YES |  |

---

## Tabela: matpod
Baza: opp
**Opis:** Matični podaci firme (PIB, MB, naziv, adresa)

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | int(4) | NO | PRI |
| naziv | varchar(200) | YES |  |
| vlasnik | varchar(50) | YES |  |
| adresa | varchar(50) | YES |  |
| telefoni | varchar(50) | YES |  |
| mesto | varchar(30) | YES |  |
| pib | varchar(20) | YES |  |
| zr1 | varchar(30) | YES |  |
| zr2 | varchar(30) | YES |  |
| zr3 | varchar(30) | YES |  |
| matbr | varchar(20) | YES |  |
| sifdel | int(5) | YES |  |
| regbr | varchar(30) | YES |  |
| zadnja | tinyint(1) | YES |  |
| prb | int(5) | YES |  |
| web | varchar(50) | YES |  |
| email | varchar(50) | YES |  |
| skin | varchar(50) | YES |  |
| zadnjiobj | int(2) | YES |  |
| barkod | int(1) | YES |  |
| npp | int(1) | YES |  |
| pdv | int(1) | NO |  |
| cenovnik | int(1) | NO |  |
| dvojno | int(1) | NO |  |
| robno | int(1) | YES |  |
| napomena | longtext | YES |  |
| boja | varchar(100) | YES |  |
| tip | int(1) | YES |  |
| porper | int(1) | YES |  |
| pdvbroj | varchar(20) | YES |  |
| naplacenpdv | int(1) | NO |  |
| sifops | int(3) | YES |  |
| ovllice | varchar(255) | YES |  |
| sifrakpl | varchar(20) | YES |  |
| externidokument | int(1) | YES |  |
| gln | varchar(30) | YES |  |
| aktivna | int(1) | YES |  |
| vpnadresa | varchar(100) | YES |  |
| vpnport | int(6) | YES |  |
| operater | varchar(50) | YES |  |
| velicina | int(1) | YES |  |
| korjav | int(1) | YES |  |
| jbkjs | int(5) | YES |  |
| ts | timestamp | NO |  |

---

## Tabela: sifostdokum
Baza: opp
**Opis:** Ostali dokumenti - šifarnik

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | int(3) | NO | PRI |

---

# 6. OSNOVNA SREDSTVA - ŠIFARNICI

## Tabela: oskateg
Baza: opp
**Opis:** Kategorije osnovnih sredstava

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifkat | tinyint(2) unsigned | NO | PRI |
| oznkat | varchar(6) | YES |  |

---

## Tabela: osporgrupe
Baza: opp
**Opis:** Poreske grupe OS za amortizaciju

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| porgrupa | tinyint(2) unsigned | NO | PRI |

---

# 7. OBRAČUN ZARADA - ŠIFARNICI

## Tabela: ldkategzap
Baza: opp
**Opis:** Kategorije zaposlenih za obračun LD

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifkat | smallint(3) | NO | PRI |
| opis | varchar(100) | YES |  |
| porez_proc | float(7,4) | YES |  |
| oslob_poreza | enum('D','N') | YES |  |
| pior_proc | float(7,4) | YES |  |
| zdror_proc | float(7,4) | YES |  |
| nzpr_proc | float(7,4) | YES |  |
| piop_proc | float(7,4) | YES |  |
| zdrop_proc | float(7,4) | YES |  |
| nzpp_proc | float(7,4) | YES |  |
| datcre | date | YES |  |
| datizm | datetime | YES |  |
| operater | varchar(12) | YES |  |
| sub_porez_proc | float(7,4) | YES |  |
| sub_pior_proc | float(7,4) | YES |  |
| sub_piop_proc | float(7,4) | YES |  |
| sub_zdrr_proc | float(7,4) | YES |  |
| sub_zdrp_proc | float(7,4) | YES |  |
| sub_nzpr_proc | float(7,4) | YES |  |

---

## Tabela: ldkategpok
Baza: opp
**Opis:** Kategorije pokretanja obračuna LD

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| tipug | char(1) | NO | PRI |
| sifkat | smallint(3) | NO | PRI |
| opis | varchar(200) | NO |  |
| porez_proc | float(7,4) | YES |  |
| porez_procum | float(7,4) | YES |  |
| pio_proc | float(7,4) | YES |  |
| zdro_proc | float(7,4) | YES |  |
| nzp_proc | float(7,4) | YES |  |
| nortros_proc | float(7,4) | YES |  |
| porez_uplrac | varchar(20) | YES |  |
| pio_uplrac | varchar(20) | YES |  |
| zdro_uplrac | varchar(20) | YES |  |
| nzp_uplrac | varchar(20) | YES |  |
| proc_pioi | float(7,4) | YES |  |
| proc_zdroi | float(7,4) | YES |  |
| datcre | date | YES |  |
| datizm | datetime | YES |  |
| operater | varchar(12) | YES |  |
| konto_duguje | varchar(10) | YES |  |
| konto_neto | varchar(10) | YES |  |
| konto_porez | varchar(10) | YES |  |
| konto_pio | varchar(10) | YES |  |
| konto_zdrav | varchar(10) | YES |  |

---

## Tabela: ld130
Baza: opp
**Opis:** LD parametri za obračun (stope, koeficijenti)

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sif130 | int(6) unsigned | NO | PRI |
| naziv | varchar(35) | NO |  |
| posta | varchar(5) | YES |  |
| mesto | varchar(18) | YES |  |
| ulibr | varchar(24) | YES |  |
| tek_rn | varchar(20) | YES |  |
| datcre | date | YES |  |
| datizm | datetime | YES |  |

---

## Tabela: ld220
Baza: opp
**Opis:** LD parametri za poreske prijave

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sif220 | smallint(3) unsigned | NO | PRI |
| opis | varchar(35) | NO |  |
| osntab | tinyint(2) unsigned | NO |  |
| nac_satn | enum('K','P','N') | NO |  |
| akontacija | char(1) | NO |  |
| mrad_dn | enum('D','N') | NO |  |
| proc_rr | decimal(5,2) | NO |  |
| proc_nk | decimal(5,2) | NO |  |
| proc_dod | decimal(5,2) | NO |  |
| izn_m4 | enum('1','2','3') | YES |  |
| sati_m4 | enum('1','2','3') | YES |  |
| benef | enum('D','N') | YES |  |
| rndug | varchar(10) | YES |  |
| rnpot | varchar(10) | YES |  |
| datcre | date | YES |  |
| datizm | datetime | YES |  |
| operater | varchar(12) | YES |  |
| stmdn | varchar(1) | YES |  |
| prekovremeni | varchar(1) | YES |  |
| socdop_sraz | enum('D','N') | YES |  |
| forceprint | int(1) | YES |  |
| umanjujerr | int(1) | YES |  |
| racunato | int(1) | YES |  |
| umanjenje | int(1) | YES |  |
| dopunadominimalne | int(1) | NO |  |

---

## Tabela: hot_tax
Baza: opp
**Opis:** Stope turističke takse

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| datum | date | NO | PRI |
| brtaksi | int(4) | YES |  |
| tax_placa | int(2) | YES |  |
| tax_neplaca | int(2) | YES |  |

---

# 8. PROCEDURE I FUNKCIJE

| Procedura/Funkcija | Tip |
|-------------------|-----|
| AutCheckInt | PROCEDURE |
| bsnotif | PROCEDURE |
| bsnotiftoopers | PROCEDURE |
| CheckBsNotifForOper | PROCEDURE |
| CheckBsNotification | PROCEDURE |
| checkistekugorad | PROCEDURE |
| collect_ldstav_ugod | PROCEDURE |
| ExportAndDeleteProcedure | PROCEDURE |
| fetch_finprom_data_new | PROCEDURE |
| fetch_finprom_data_new_z | PROCEDURE |
| mod_97_10_check | FUNCTION |
| popuniFirme | PROCEDURE |
