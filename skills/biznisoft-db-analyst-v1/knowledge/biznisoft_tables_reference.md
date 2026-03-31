# Biznisoft OPP7102025 - Referenca transakcionih tabela

> Baza `opp7102025` sadrži podatke jedne firme - transakcije, partnere, artikle, dokumente.
> Generisano: 2025-03-29

---

# 1. OSNOVNI ENTITETI

## Tabela: kupci
Baza: opp7102025
**Opis:** Partneri (kupci, dobavljači, ostali). Centralna tabela za sve poslovne partnere.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | int(5) | NO | PRI |
| naziv | varchar(500) | YES | MUL |
| pbr | varchar(8) | YES |  |
| mesto | varchar(30) | YES |  |
| adresa | varchar(150) | YES |  |
| konosoba | varchar(255) | YES |  |
| telefoni | varchar(150) | YES |  |
| fax | varchar(20) | YES |  |
| drzava | varchar(30) | YES |  |
| pib | varchar(20) | YES | MUL |
| matbr | varchar(20) | YES |  |
| pdv | int(1) | NO |  |
| regbr | varchar(30) | YES |  |
| tip | int(1) | NO |  |
| kategorija | int(1) | YES |  |
| region | int(3) | YES |  |
| napomena | longtext | YES |  |
| prcrabat | double(5,2) | YES |  |
| kredlimit | double(15,2) | YES |  |
| rokpl | int(3) | YES |  |
| teren | int(4) | YES |  |
| pdvbroj | varchar(30) | YES |  |
| zavpl | int(1) | YES |  |
| povpl | int(1) | YES |  |
| boja | varchar(50) | YES |  |
| kamstopa | double(10,4) | YES |  |
| ts | timestamp | NO |  |
| operater | varchar(50) | YES |  |
| vpcenovnik | varchar(50) | YES |  |
| konto | varchar(20) | YES |  |
| komercijalista | varchar(50) | YES |  |
| pak | int(6) | YES |  |
| posotpremnica | int(1) | YES |  |
| sifraobveznika | varchar(20) | YES |  |
| blokiran | int(1) | YES |  |
| wsusername | varchar(10) | YES |  |
| wspassword | varchar(20) | YES |  |
| wsemail | varchar(90) | YES |  |
| kooperant | int(1) | YES |  |
| klauzula | int(3) | YES |  |
| tipkl | int(1) | YES |  |
| gln | varchar(30) | YES |  |
| licevanro | int(10) | YES |  |
| sortstampe | int(4) | YES |  |
| jbkjs | int(5) | YES |  |
| idpartnera | varchar(50) | YES |  |
| email | varchar(250) | YES |  |
| prijpadresa | varchar(500) | YES |  |
| prijppbrmesto | varchar(100) | YES |  |
| emailnarudzbine | varchar(255) | YES |  |
| emailios | varchar(255) | YES |  |
| bsstatus | int(1) | YES |  |
| drzavasifra | varchar(3) | YES |  |
| sifopstine | int(3) | YES |  |
| tipefakture | int(2) | YES |  |
| sef | int(1) | YES |  |
| poljoznaka | int(2) | YES |  |
| punnaziv | varchar(700) | YES |  |
| aktivan | int(1) | YES |  |
| posljedtip | int(1) | YES |  |
| posljeduplate | int(1) | YES |  |
| tipulaznogracuna | int(2) | YES |  |
| trebkomerc | int(1) | YES |  |
| valpl_obaveza | int(1) | YES |  |
| valpl_potrazivanja | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| operater | operateri | sifra | Operater |
| komercijalista | komercijalisti | sifra | Komercijalista |

---

## Tabela: artikli
Baza: opp7102025
**Opis:** Šifarnik artikala/robe/usluga sa cenama, PDV, barkodovima.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | int(6) | NO | PRI |
| grupa | int(4) | YES | MUL |
| barkod | varchar(30) | YES | MUL |
| naziv | varchar(1000) | YES |  |
| jedmere | char(3) | YES |  |
| tarbr | int(1) | NO |  |
| taksa | double(15,2) | NO |  |
| akciza | double(15,2) | NO |  |
| rokpl | int(3) | YES |  |
| datotv | datetime | YES |  |
| porez | varchar(2) | NO |  |
| sifobj | int(3) | YES |  |
| katbr | varchar(100) | YES | MUL |
| zamena | varchar(20) | YES |  |
| minzal | double(15,2) | YES |  |
| kasakoef | double(12,7) | YES |  |
| kasajmr | varchar(3) | YES |  |
| imaambalazu | tinyint(1) | YES |  |
| jeambalaza | tinyint(1) | YES |  |
| jesirovina | tinyint(1) | YES |  |
| jeproizvod | tinyint(1) | YES |  |
| jeusluga | tinyint(1) | YES |  |
| planskacena | double(15,2) | YES |  |
| vpcenasopst | double(15,2) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| prckala | double(15,5) | YES |  |
| proizvod9120 | tinyint(1) | YES |  |
| komision880 | tinyint(1) | YES |  |
| garancija | int(4) | YES |  |
| ambalaza | int(6) | YES |  |
| serbr | int(1) | YES |  |
| odeljenje | int(6) | YES |  |
| kpima | int(1) | YES |  |
| kpbarkod | varchar(15) | YES | MUL |
| kpkolicina | double(15,3) | YES |  |
| tpima | int(1) | YES |  |
| tpbarkod | varchar(15) | YES | MUL |
| tpkolicina | double(15,3) | YES |  |
| jegrupa | int(1) | YES |  |
| ts | timestamp | NO |  |
| operater | varchar(50) | YES |  |
| vaga | int(1) | NO |  |
| carst | double(10,2) | YES |  |
| jc_jedmere | char(3) | YES |  |
| jc_koef | double(12,7) | YES |  |
| akcrabat | double(5,2) | YES |  |
| faktorjm | double(15,7) | YES |  |
| faktoramb | double(15,4) | YES |  |
| zabranipos | int(1) | YES |  |
| tezina | double(15,7) | YES |  |
| dodaci | int(1) | YES |  |
| msort | int(1) | YES |  |
| ppima | int(1) | YES |  |
| ppbarkod | varchar(15) | YES | MUL |
| ppkolicina | double(15,3) | YES |  |
| serbrrok | int(1) | YES |  |
| imaplusifra | int(1) | YES |  |
| plusifra | int(5) | YES |  |
| ignminpos | int(1) | YES |  |
| webshoplink | varchar(500) | YES |  |
| wsstanje | int(5) | YES |  |
| kooperacija | int(1) | YES |  |
| obrnuto | int(1) | YES |  |
| adresaartikla | varchar(100) | YES |  |
| ssbrtip | int(1) | YES |  |
| sifakcize | int(2) | YES |  |
| turizam | int(1) | YES |  |
| zapremina | double(15,5) | YES |  |
| karaktertudja | int(2) | YES |  |
| ekotaksa | double(15,2) | YES |  |
| tezinski | int(1) | NO |  |
| stvarnack | int(1) | YES |  |
| nazivzafakturu | varchar(500) | YES |  |
| tezina_amb | double(15,2) | YES |  |
| polovnodobro | int(1) | YES |  |
| kp_tezina | double(15,2) | YES |  |
| tp_tezina | double(15,2) | YES |  |
| pp_tezina | double(15,2) | YES |  |
| invbroj | varchar(50) | YES |  |
| eotpremnice_akciza_tip | int(1) | YES |  |
| eotpremnice_akciza_vrednost | double(15,5) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| tarbr | tabrac | sifra | Tarifni broj |
| sifobj | objekti | sifra | Objekat/poslovnica |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |
| operater | operateri | sifra | Operater |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| updartikli | AFTER UPDATE | Sinhronizuje naziv/jedmere/porez/barkod sa trstanje |

---

## Tabela: artiklibarkod
Baza: opp7102025
**Opis:** Dodatni barkodovi za artikle (jedan artikal može imati više barkodova).

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | int(6) | NO |  |
| bc1 | varchar(30) | YES |  |

---

## Tabela: objekti
Baza: opp7102025
**Opis:** Objekti/poslovnice firme sa adresama i podešavanjima.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | int(3) | NO | PRI |
| naziv | varchar(120) | NO |  |
| konto | varchar(20) | YES |  |
| imeposl1 | varchar(30) | YES |  |
| imeposl2 | varchar(30) | YES |  |
| sifops | smallint(3) | YES |  |
| nazops | varchar(30) | YES |  |
| pbrmesto | varchar(40) | YES |  |
| adresa | varchar(40) | YES |  |
| ziroracun | varchar(20) | YES |  |
| telefoni | varchar(30) | YES |  |
| sifobj | int(3) | YES |  |
| datzakrobno | date | YES |  |
| datzaktrgk | date | YES |  |
| datzakfakt | date | YES |  |
| robno | int(1) | YES |  |
| cenovnici | int(1) | YES |  |
| tipkepu | int(1) | YES |  |
| proverastanja | int(1) | YES |  |
| refobj | int(3) | YES |  |
| plusifra | int(1) | YES |  |
| webshop | int(1) | YES |  |
| ugostitelj | int(1) | YES |  |
| nivulaz | int(1) | YES |  |
| nivizlaz | int(1) | YES |  |
| nivintrn | int(1) | YES |  |
| gln | varchar(30) | YES | MUL |
| teren | int(4) | YES |  |
| bkrobno | int(1) | YES |  |
| sortstampe | int(4) | YES |  |
| rezervacijeisticu | int(1) | YES |  |
| operater | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| myhotkey | int(2) | YES |  |
| aktivan | int(1) | YES |  |
| emailobj | varchar(255) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| operater | operateri | sifra | Operater |

---

## Tabela: operateri
Baza: opp7102025
**Opis:** Operateri sistema u okviru firme.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | varchar(10) | NO | PRI |
| naziv | varchar(50) | YES |  |
| ovlascenje | int(1) | YES |  |
| lozinka | varchar(20) | YES |  |
| posoperater | varchar(4) | YES |  |
| poslozinka | varchar(6) | YES |  |

---

## Tabela: kontniplan
Baza: opp7102025
**Opis:** Aktivni kontni plan firme (kopiran iz opp.kontniplan).

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| racun | varchar(20) | NO | PRI |
| naziv | varchar(255) | YES |  |
| analitika | varchar(50) | NO |  |
| knjizenje | varchar(20) | NO |  |
| valuta | int(1) | NO |  |
| zatvaranje | int(1) | NO |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| karakter | int(1) | YES |  |
| kursr | int(1) | YES |  |
| napomena | varchar(1000) | YES |  |
| starikonto | varchar(10) | YES |  |
| sifrakpl | varchar(10) | NO | PRI |
| vremeizmene | timestamp | NO |  |
| operater | varchar(20) | YES |  |
| ignmtnt | int(1) | YES |  |
| sifpopdv | int(4) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| racun | kontniplan | racun | Konto |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |
| operater | operateri | sifra | Operater |

---

## Tabela: tabrac
Baza: opp7102025
**Opis:** Tarifni brojevi u firmi.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | varchar(20) | NO | PRI |
| naziv | varchar(255) | YES |  |
| konto | varchar(20) | NO | MUL |
| sifrakpl | varchar(20) | NO | PRI |

---

## Tabela: sifobj
Baza: opp7102025
**Opis:** Šifarnik objekata u okviru firme.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | int(2) | NO | PRI |
| naziv | varchar(50) | YES |  |
| racun | varchar(20) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| racun | kontniplan | racun | Konto |

---

## Tabela: grupart
Baza: opp7102025
**Opis:** Grupe artikala - hijerarhijska klasifikacija.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | int(4) | NO | PRI |

---

## Tabela: dodaci
Baza: opp7102025
**Opis:** Dodaci - dodatne specifikacije za artikle.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | int(5) | NO | PRI |
| naziv | varchar(500) | YES |  |
| slika | blob | YES |  |

---

## Tabela: serbr
Baza: opp7102025
**Opis:** Serijski brojevi artikala.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| sifra | int(8) | NO | PRI |
| serbr | varchar(100) | NO | PRI |
| ulaz | double(15,4) | NO |  |
| izlaz | double(15,4) | NO |  |
| brnal | varchar(40) | NO | PRI |
| partner | int(5) | NO |  |
| datnal | date | NO |  |
| datdok | date | YES |  |
| brdok | varchar(50) | YES |  |
| rok | date | YES |  |
| vremeizmene | timestamp | NO |  |
| operater | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| partner | kupci | sifra | Partner/kupac |
| operater | operateri | sifra | Operater |

---

## Tabela: trstanje
Baza: opp7102025
**Opis:** Trenutno stanje zaliha po objektu i artiklu. Ažurira se trigerima.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| sifra | int(6) | NO | PRI |
| naziv | varchar(1000) | YES |  |
| jedmere | varchar(10) | YES |  |
| porez | varchar(2) | NO |  |
| tarbr | int(2) | YES |  |
| zadizm | varchar(255) | YES |  |
| faktcena | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| vpcena | double(15,2) | YES |  |
| mpcena | double(15,2) | YES |  |
| stanje | double(15,3) | YES |  |
| neprokkasa | double(15,3) | YES |  |
| rezervacije | double(15,3) | YES |  |
| barkod | varchar(20) | YES | MUL |
| kasakoef | double(17,7) | YES |  |
| taksa | double(15,2) | YES |  |
| akciza | double(15,2) | YES |  |
| eurcena | double(15,2) | YES |  |
| usdcena | double(15,2) | YES |  |
| chfcena | double(15,2) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| tarbr | tabrac | sifra | Tarifni broj |

---

## Tabela: zakljucano
Baza: opp7102025
**Opis:** Zaključani periodi - sprečava knjiženje u zaključan period.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| finansijsko | date | YES |  |
| kir | date | YES |  |
| kpr | date | YES |  |
| pk1 | date | YES |  |
| id | bigint(20) | NO | PRI |

---

## Tabela: poslovnagodina
Baza: opp7102025
**Opis:** Definicija poslovne godine.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| godina | int(4) | NO | PRI |

---

## Tabela: oznakadokumenta
Baza: opp7102025
**Opis:** Oznake/prefiksi dokumenata.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| brnal | varchar(50) | NO | PRI |

---

## Tabela: kuppobroj
Baza: opp7102025
**Opis:** Povezivanje kupaca po telefonskom broju.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | int(10) | NO | PRI |
| imeiprez | varchar(100) | YES |  |
| adresa | varchar(100) | YES |  |
| brtel | varchar(50) | YES |  |
| rabat | double(15,2) | YES |  |
| matbr | varchar(50) | YES |  |
| email | varchar(100) | YES |  |
| kod | varchar(50) | YES | MUL |
| nivo | int(3) | YES |  |
| operater | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| operater | operateri | sifra | Operater |

---

## Tabela: kupprom
Baza: opp7102025
**Opis:** Promet kupaca - agregirani podaci.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | int(5) | NO | PRI |
| datdok | date | YES |  |
| brdok | varchar(20) | YES |  |
| datval | date | NO | PRI |
| duguje | double(15,2) | YES |  |
| potrazuje | double(15,2) | YES |  |
| operater | varchar(10) | YES |  |
| brnal | varchar(20) | NO | PRI |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| operater | operateri | sifra | Operater |

---

## Tabela: defkontopart
Baza: opp7102025
**Opis:** Default konto za partnera.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifpart | int(5) | NO | PRI |
| oznnal | varchar(10) | NO | PRI |
| konto | varchar(20) | NO |  |
| sifobj | int(3) | NO | PRI |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |

---

# 2. ROBNO POSLOVANJE

## Tabela: robno
Baza: opp7102025
**Opis:** Glavni robni promet - sve ulazno/izlazne promene zaliha. Svaki red = jedna stavka prometa.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| sifra | int(6) | NO | PRI |
| datum | date | YES |  |
| brnal | varchar(50) | NO | PRI |
| ulaz | double | YES |  |
| izlaz | double | YES |  |
| duguje | double | YES |  |
| potrazuje | double | YES |  |
| rbr | int(4) | NO | PRI |
| cena | double(15,2) | YES |  |
| nabcena | double(15,4) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| prcruc | double | YES |  |
| ddatum | timestamp | NO |  |
| condatddat | varchar(50) | YES |  |
| subject | varchar(50) | YES | MUL |
| posljed | int(4) | YES |  |
| realizacija | double(15,2) | YES |  |
| rabat | double(15,2) | YES |  |
| komercijalista | varchar(50) | YES |  |
| operater | varchar(10) | YES | MUL |
| mestotr | int(6) | YES | MUL |
| nosioc | int(6) | YES | MUL |
| prernc | double(15,4) | NO |  |
| fid1 | double(15,2) | YES |  |
| fid2 | int(8) | YES |  |
| fid3 | int(8) | YES |  |
| fid4 | varchar(255) | YES |  |
| datorigdok | date | YES |  |
| brdok | varchar(50) | YES |  |
| stornirano | int(1) | YES |  |
| datumdokumenta | date | YES |  |
| originbrnal | varchar(30) | YES | MUL |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| subject | kupci | sifra | Partner |
| komercijalista | komercijalisti | sifra | Komercijalista |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| zak_ins_robno | BEFORE INSERT | Provera zaključanog robnog perioda |
| insstanje | AFTER INSERT | Ažurira trstanje (stanje zaliha) nakon unosa |
| zak_upd_robno | BEFORE UPDATE | Provera zaključanog robnog perioda |
| updstanje | AFTER UPDATE | Ažurira trstanje (stanje zaliha) nakon izmene |
| zak_del_robno | BEFORE DELETE | Provera zaključanog robnog perioda |
| delstanje | AFTER DELETE | Ažurira trstanje (stanje zaliha) nakon brisanja |

---

## Tabela: kalkulacije
Baza: opp7102025
**Opis:** Kalkulacije/prijemnice robe od dobavljača. Dokument tipa KL.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES | MUL |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_kalkulacije | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_kalkulacije | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_kalkulacije | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: nivelacije
Baza: opp7102025
**Opis:** Nivelacije cena. Dokument tipa NC.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brnivel | int(4) | NO | PRI |
| brdok | varchar(20) | YES | MUL |
| datum | date | YES |  |
| rbrst | int(5) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double | YES |  |
| novacena | double(15,6) | YES |  |
| staracena | double(15,6) | YES |  |
| vrednost | double(15,2) | YES |  |
| staripruc | double(15,2) | YES |  |
| novipruc | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| nabcena | double | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| stariporezpd | double(15,2) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_nivelacije | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_nivelacije | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_nivelacije | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: nivkalkulacije
Baza: opp7102025
**Opis:** Kalkulacije sa nivelacijom. Dokument tipa KI.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES | MUL |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_nivkalkulacije | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_nivkalkulacije | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_nivkalkulacije | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: intprijem
Baza: opp7102025
**Opis:** Interni prijem robe. Dokument tipa IP.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_intprijem | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_intprijem | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_intprijem | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: intracun
Baza: opp7102025
**Opis:** Interni prenos dobara. Dokument tipa IR.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| obj2 | int(3) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double | YES |  |
| cena | double(15,4) | YES |  |
| kolicina2 | double | YES |  |
| cena2 | double(15,4) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcruc | double | YES |  |
| iznruc | double | YES |  |
| datum | date | NO |  |
| tipobj1 | char(2) | YES |  |
| tipobj2 | char(2) | YES |  |
| porez | double(15,6) | YES |  |
| porez2 | double(15,6) | YES |  |
| prcruc2 | double | YES |  |
| iznruc2 | double | YES |  |
| taksa | double | YES |  |
| prenporez | double | YES |  |
| brdok | varchar(50) | YES | MUL |
| rezcena2 | double(15,4) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| konto2 | varchar(20) | YES |  |
| fid1 | double(15,2) | YES |  |
| fid2 | double(15,2) | YES |  |
| fid3 | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| dostava | int(2) | YES |  |
| wscheckirano | int(1) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| potvrdjeno | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_intracun | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_intracun | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_intracun | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: popis
Baza: opp7102025
**Opis:** Popis zaliha - višak/manjak. Dokument tipa PL.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| rbr | int(6) | NO | PRI |
| sifra | int(6) | NO |  |
| naziv | varchar(50) | YES |  |
| jm | char(3) | YES |  |
| cena | double(15,4) | YES |  |
| kolicina | double(25,10) | YES |  |
| vrednost | double(15,2) | YES |  |
| datum | date | NO |  |
| brpop | int(4) | NO | PRI |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| novakolicina | double(15,3) | YES |  |
| racun | varchar(20) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| barkod | varchar(15) | YES |  |
| opis | varchar(255) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| racun | kontniplan | racun | Konto |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_upd_popis | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_popis | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: proveraprijema
Baza: opp7102025
**Opis:** Provera prijema robe.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| brkl | int(6) | NO | PRI |
| datum | date | YES |  |
| brnal | varchar(50) | YES | MUL |
| datumnaloga | date | YES |  |
| sifobj | int(3) | YES |  |
| brdok | varchar(50) | YES |  |
| nazivpartnera | varchar(100) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| cena | double(15,2) | YES |  |
| kolicina | double(15,3) | YES |  |
| status | int(1) | YES |  |
| operater | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| serbr | varchar(100) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_proveraprijema | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_proveraprijema | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_proveraprijema | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: nabambalaze
Baza: opp7102025
**Opis:** Nabavka ambalaže. Dokument tipa NB.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_nabambalaze | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_nabambalaze | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_nabambalaze | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: komnivelacije
Baza: opp7102025
**Opis:** Nivelacija komisione robe. Dokument tipa KN.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brnivel | int(4) | NO | PRI |
| brdok | varchar(10) | YES | MUL |
| datum | date | YES |  |
| rbrst | int(5) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double | YES |  |
| novacena | double(15,6) | YES |  |
| staracena | double(15,6) | YES |  |
| vrednost | double(15,2) | YES |  |
| staripruc | double(15,2) | YES |  |
| novipruc | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| nabcena | double | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| staranabavna | double(15,6) | YES |  |
| novanabavna | double(15,6) | YES |  |
| partner | int(5) | NO |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| stariporezpd | double(15,2) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |
| partner | kupci | sifra | Partner/kupac |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_komnivelacije | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_komnivelacije | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_komnivelacije | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: cene
Baza: opp7102025
**Opis:** Cene artikala po objektima.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| tipobj | int(2) | NO | PRI |

---

## Tabela: cenovnik
Baza: opp7102025
**Opis:** Cenovnici - definicije cenovnika.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifra | int(6) | NO | PRI |
| objekat | int(3) | NO | PRI |
| mpcena | double(15,2) | YES |  |
| ts | timestamp | NO |  |
| operater | varchar(255) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| operater | operateri | sifra | Operater |

---

## Tabela: klista
Baza: opp7102025
**Opis:** Kursna lista u firmi.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| objekat | int(3) | NO | PRI |
| datum | date | NO | PRI |
| sifval | int(3) | NO | PRI |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifval | valuteplacanja | sifra | Valuta |

---

# 3. FAKTURE I PRODAJA

## Tabela: fakture
Baza: opp7102025
**Opis:** Izlazne fakture, otpremnice, profakture, nalog za izdavanje, avansni računi. Tipovi: F=faktura, I=nalog, O=otpremnica, P=profaktura, A=avans, X/B/Y/E/W=specijalni.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES | MUL |
| rbrst | int(7) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(5000) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(5) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_fakture | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_fakture | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| updfakture | AFTER UPDATE | Ažurira trstanje.rezervacije + refobjst nakon fakture |
| operdoc_del_fakture | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: faktureos
Baza: opp7102025
**Opis:** Izlazne fakture za osnovna sredstva. Dokument tipa FS.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES | MUL |
| rbrst | int(7) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(5000) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(5) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_faktureos | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_faktureos | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_faktureos | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: kasa
Baza: opp7102025
**Opis:** Kasa u maloprodaji - fiskalni računi. Dokument tipa KA.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(4) | NO | PRI |
| datum | date | NO | PRI |
| sifkup | int(4) | YES |  |
| brdok | varchar(20) | YES | MUL |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES | MUL |
| kolicina | double | YES |  |
| cena | double(15,2) | YES |  |
| prcrabat | double | YES |  |
| rabat | double | YES |  |
| prctran | double | YES |  |
| trantr | double | YES |  |
| prcruc | double | YES |  |
| iznruc | double | YES |  |
| status | int(2) | YES |  |
| operater | varchar(50) | NO | PRI |
| porezprom | double | YES |  |
| porezusl | double | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double | YES |  |
| taksa | double | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double | YES |  |
| tip | char(1) | YES |  |
| akcc | double | YES |  |
| prenporez | int(1) | YES |  |
| naziv | varchar(50) | YES |  |
| barkod | varchar(15) | YES |  |
| gotovina | double(15,2) | YES |  |
| bezgotovina | double(15,2) | YES |  |
| virman | double(15,2) | YES |  |
| kredit | double(15,2) | YES |  |
| novac | double(15,2) | YES |  |
| kusur | double(15,2) | YES |  |
| kupfiz | varchar(50) | YES | MUL |
| kupac | varchar(50) | YES | MUL |
| kartica | double(15,2) | YES |  |
| vreme | time | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(10) | YES |  |
| nazivkupca | varchar(50) | YES |  |
| fid1 | varchar(50) | YES |  |
| fid2 | varchar(50) | YES |  |
| fid3 | double(15,3) | YES |  |
| fid4 | double(15,3) | YES |  |
| idf | varchar(10) | YES |  |
| fid5 | varchar(50) | YES |  |
| fid6 | double(15,2) | YES |  |
| IKOF | varchar(50) | YES | MUL |
| vaucer | double(15,2) | YES |  |
| instantplacanje | double(15,2) | YES |  |
| tipracuna | int(1) | YES |  |
| izavansa | double(15,2) | YES |  |
| biznisoftbrnal | varchar(40) | YES | MUL |
| vrstaracuna | int(1) | YES |  |
| rucnacena | int(1) | YES |  |
| mfp1 | int(1) | YES |  |
| mfp2 | double(15,2) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| kupac | kupci | sifra | Partner/kupac |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| inskasa | AFTER INSERT | Ažurira trstanje (stanje zaliha) nakon unosa |
| updkasa | AFTER UPDATE | Ažurira trstanje (stanje zaliha) nakon izmene |
| delkasa | AFTER DELETE | Ažurira trstanje (stanje zaliha) nakon brisanja |

---

## Tabela: pazari
Baza: opp7102025
**Opis:** Dnevni pazari. Dokument tipa PZ.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| objekat | int(3) | NO | PRI |
| datum | date | NO | PRI |
| tstav | int(1) | NO | PRI |
| porstopa | double | NO | PRI |
| iznos | double | YES |  |
| datzr | date | YES |  |
| status | int(1) | YES |  |
| ts | timestamp | NO |  |
| operater | varchar(50) | YES |  |
| iznosporeza | double(15,2) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| rbrst | int(2) | NO | PRI |
| tipprom | int(2) | YES |  |
| popdvid | varchar(10) | YES |  |
| brdok | varchar(255) | YES |  |
| sifturusl | int(6) | YES |  |
| biznisoftbrnal | varchar(20) | NO |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| konto | varchar(10) | YES |  |
| iznrucpd | double(15,2) | YES |  |
| tiprefundacije | int(1) | YES |  |
| ikof | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_pazari | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_pazari | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_pazari | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: blgpromet
Baza: opp7102025
**Opis:** Blagajničko poslovanje - nalozi blagajne. Dokument tipa BL.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| datum | date | NO |  |
| brnal | int(8) | NO | PRI |
| brtran | int(6) | NO | PRI |
| transsr | int(5) | NO |  |
| sifra | int(5) | NO |  |
| analitika | varchar(10) | YES |  |
| uplata | double(15,2) | YES |  |
| isplata | double(15,2) | YES |  |
| vreme | timestamp | NO |  |
| operater | varchar(20) | NO |  |
| status | int(2) | NO |  |
| mestotr | int(6) | YES |  |
| nosioctr | int(6) | YES |  |
| dokumveza | varchar(50) | YES |  |
| opisprom | varchar(200) | YES |  |
| biznisoftbrnal | varchar(20) | NO |  |
| pocetno | int(1) | YES |  |
| potvrdjeno | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_upd_blgpromet | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_blgpromet | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

# 4. FINANSIJSKO POSLOVANJE

## Tabela: finprom
Baza: opp7102025
**Opis:** Finansijski promet - nalozi GK. Svaka stavka = jedno knjiženje duguje/potražuje.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| datnal | date | NO |  |
| brnal | varchar(50) | NO | PRI |
| datdok | date | YES |  |
| brdok | varchar(50) | YES |  |
| racun | varchar(20) | NO | MUL |
| datval | date | YES |  |
| izndug | decimal(15,2) | YES |  |
| iznpot | decimal(15,2) | YES |  |
| status | int(1) | NO | MUL |
| operater | varchar(50) | YES |  |
| rbrst | int(4) | NO | PRI |
| vd | char(2) | YES |  |
| dokumveza | varchar(50) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| opis | varchar(50) | YES |  |
| zatvoreno | char(1) | YES |  |
| sifval | int(3) | YES | MUL |
| izndugval | decimal(15,2) | YES |  |
| iznpotval | decimal(15,2) | YES |  |
| ts | timestamp | NO |  |
| kepuobj | int(3) | YES |  |
| externidokument | varchar(100) | YES | MUL |
| fid1 | varchar(50) | YES |  |
| fid2 | varchar(50) | YES |  |
| fid3 | varchar(50) | YES |  |
| valutaplacanja | date | YES |  |
| datpdv | date | YES |  |
| posljed | int(4) | YES |  |
| komercijalista | varchar(50) | YES |  |
| stornirano | int(1) | YES | MUL |
| biznisoftbrnal | varchar(50) | YES | MUL |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| racun | kontniplan | racun | Konto |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |
| sifval | valuteplacanja | sifra | Valuta |
| komercijalista | komercijalisti | sifra | Komercijalista |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| zak_ins_finprom | BEFORE INSERT | Provera zaključanog finansijskog perioda |
| operdoc_ins_finprom | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| zak_upd_finprom | BEFORE UPDATE | Provera zaključanog finansijskog perioda |
| operdoc_upd_finprom | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| zak_del_finprom | BEFORE DELETE | Provera zaključanog finansijskog perioda |
| operdoc_del_finprom | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: pk1
Baza: opp7102025
**Opis:** Poreska knjiga evidencije PDV-a.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| datknj | date | NO |  |
| sifobj | int(3) | YES |  |
| brnal | varchar(50) | NO | PRI |
| vrdok | char(2) | YES |  |
| opis | varchar(100) | NO |  |
| datdok | date | YES |  |
| ppspo | double(15,2) | YES |  |
| ppspn | double(15,2) | YES |  |
| ppbpdv | double(15,2) | YES |  |
| ppusp | double(15,2) | YES |  |
| ppubp | double(15,2) | YES |  |
| ppop6369 | double(15,2) | YES |  |
| svegapr | double(15,2) | YES |  |
| pdvobr | double(15,2) | YES |  |
| pdvpreth | double(15,2) | YES |  |
| pdvupl | double(15,2) | YES |  |
| nabvred | double(15,2) | YES |  |
| vredspr | double(15,2) | YES |  |
| razlucen | double(15,2) | YES |  |
| obrpdv | double(15,2) | YES |  |
| prodvr | double(15,2) | YES |  |
| trospr | double(15,2) | YES |  |
| doprinosi | double(15,2) | YES |  |
| finrash | double(15,2) | YES |  |
| rashodi | double(15,2) | YES |  |
| tekrnupl | double(15,2) | YES |  |
| tekrnisp | double(15,2) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| operater | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| rbrst | int(3) | NO | PRI |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| operater | operateri | sifra | Operater |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| zak_ins_pk1 | BEFORE INSERT | Provera zaključanog perioda |
| zak_upd_pk1 | BEFORE UPDATE | Provera zaključanog perioda |
| zak_del_pk1 | BEFORE DELETE | Provera zaključanog perioda |

---

## Tabela: popdv_promet
Baza: opp7102025
**Opis:** POPDV promet - evidencija za poresku prijavu PDV.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| brnal | varchar(50) | NO | PRI |
| rbrst | int(8) | NO | PRI |
| popdvid | varchar(10) | NO |  |
| sifpar | int(5) | NO |  |
| brrn | varchar(100) | NO |  |
| datnal | date | NO |  |
| datdok | date | NO |  |
| datpdv | date | NO |  |
| Ukupno | double(15,2) | NO |  |
| vrednost | double(15,2) | NO |  |
| osnovicaos | double(15,2) | NO |  |
| pdvos | double(15,2) | NO |  |
| osnovicaps | double(15,2) | NO |  |
| pdvps | double(15,2) | NO |  |
| operater | varchar(50) | NO |  |
| ts | timestamp | NO |  |
| rucni | int(1) | NO |  |
| opis | varchar(255) | YES |  |
| pib | varchar(20) | YES |  |
| osnovica0 | double(15,2) | YES |  |
| ostalipodaci | varchar(3000) | YES |  |
| sifobj | int(3) | YES |  |
| bezodbitka | double(15,2) | YES |  |
| posebnaid | varchar(10) | YES |  |
| srcpopdvid | varchar(10) | YES |  |
| eeopdv | int(2) | YES | MUL |
| sef | int(1) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| originalbrnal | varchar(50) | NO | MUL |
| eeopdv_def | int(1) | YES |  |
| eeopdv_pravac | int(1) | YES |  |
| eeopdv_inostrana | int(1) | YES |  |
| eeopdv_tipdok | int(1) | YES |  |
| eeopdv_brojpovdok | varchar(500) | YES |  |
| eeopdv_avansi | varchar(500) | YES |  |
| eeopdv_datplac | date | YES |  |
| eeopdv_tipprom | int(1) | YES |  |
| eeopdv_smanjenjepdv | double(15,2) | YES |  |
| eeopdv_uvecanjepdv | double(15,2) | YES |  |
| eeopdv_osnovodabira | int(1) | YES |  |
| eeopdv_opis | varchar(255) | YES |  |
| eeopdv_osnovavans | varchar(500) | YES |  |
| eeopdv_tipprometa | int(1) | YES |  |
| eeopdv_tipvzdokumenta | int(1) | YES |  |
| eeopdv_vezdokod | date | YES |  |
| eeopdv_vezdokdo | date | YES |  |
| eeopdv_avans | int(1) | YES |  |
| eeopdv_tipkorekcije | int(1) | YES |  |
| eeopdv_dokumentstorno | int(1) | YES |  |
| eeppdv_tipprometa | int(2) | YES |  |
| eeppdv_vrstaprometa | int(3) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| operater | operateri | sifra | Operater |
| sifobj | objekti | sifra | Objekat/poslovnica |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| zak_ins_popdv_promet | BEFORE INSERT | Provera zaključanog perioda |
| zak_upd_popdv_promet | BEFORE UPDATE | Provera zaključanog perioda |
| zak_del_popdv_promet | BEFORE DELETE | Provera zaključanog perioda |

---

## Tabela: tr_finprom
Baza: opp7102025
**Opis:** Transfer finansijskih naloga (prelazna tabela).

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| brnal | varchar(50) | NO | PRI |
| racun | varchar(20) | NO |  |
| iznossapdv | double(15,2) | YES |  |
| osnovicaos | double(15,2) | YES |  |
| pdvos | double(15,2) | YES |  |
| osnovicans | double(15,2) | YES |  |
| pdvns | double(15,2) | YES |  |
| bezpdv | double(15,2) | YES |  |
| iznoszaknjizenje | double(15,2) | YES |  |
| oslobodjenopdv | double(15,2) | YES |  |
| stopa | char(2) | YES |  |
| mestotr | int(6) | YES |  |
| nosioctr | int(6) | YES |  |
| kljuc | int(6) | YES |  |
| tipanal | varchar(2) | YES |  |
| sifanal | int(5) | YES |  |
| rbrst | int(5) | NO | PRI |
| obrnuto | int(1) | YES |  |
| iznval | double(15,2) | YES |  |
| popdvid | varchar(10) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| racun | kontniplan | racun | Konto |
| mestotr | mestatr | sifra | Mesto troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tr_finprom | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tr_finprom | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tr_finprom | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: trgovacka
Baza: opp7102025
**Opis:** Trgovačka knjiga - evidencija prometa za TK.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| datum | date | YES |  |
| brdok | varchar(50) | NO | PRI |
| vd | char(2) | YES |  |
| posp | int(5) | YES |  |
| opis | varchar(255) | YES |  |
| duguje | double(15,2) | YES |  |
| potrazuje | double(15,2) | YES |  |
| datupl | date | YES |  |
| iznzr | double | YES |  |
| objekat | int(3) | NO | PRI |
| status | int(1) | NO | PRI |
| ts | timestamp | NO |  |
| operater | varchar(50) | YES |  |
| zaduzenjesapdv | double(15,2) | YES |  |
| razduzenjesapdv | double(15,2) | YES |  |
| brdokdob | varchar(255) | YES |  |
| sediste | varchar(255) | YES |  |
| rbrst | int(4) | NO | PRI |
| potvrdjeno | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| operater | operateri | sifra | Operater |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| zak_ins_trgovacka | BEFORE INSERT | Provera zaključanog perioda |
| zak_upd_trgovacka | BEFORE UPDATE | Provera zaključanog perioda |
| zak_del_trgovacka | BEFORE DELETE | Provera zaključanog perioda |

---

## Tabela: virmani
Baza: opp7102025
**Opis:** Virmanski nalozi za plaćanje.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| naziv | varchar(50) | NO | PRI |
| d1 | varchar(40) | YES |  |
| d2 | varchar(40) | YES |  |
| d3 | varchar(40) | YES |  |
| s1 | varchar(40) | YES |  |
| s2 | varchar(40) | YES |  |
| s3 | varchar(4) | YES |  |
| p1 | varchar(40) | YES |  |
| p2 | varchar(40) | YES |  |
| p3 | varchar(40) | YES |  |
| edit1 | varchar(30) | YES |  |
| edit2 | varchar(30) | YES |  |
| edit3 | varchar(30) | YES |  |
| edit4 | varchar(30) | YES |  |
| edit5 | varchar(30) | YES |  |
| edit6 | varchar(30) | YES |  |
| edit7 | varchar(30) | YES |  |
| edit8 | varchar(30) | YES |  |

---

# 5. FINANSIJSKE TRANSAKCIJE (frmgk_*)

> Tabele frmgk_* čuvaju dokumente kreirane kroz formu finansijskih transakcija.

## Tabela: frmgk_avans
Baza: opp7102025
**Opis:** Prijem avansnog računa. Dokument tipa AR.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| brnal | int(6) | NO | PRI |
| datnal | date | NO |  |
| brdok | varchar(50) | NO |  |
| datdok | date | NO |  |
| dobavljac | int(5) | NO |  |
| datval | date | NO |  |
| opis | varchar(255) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| prokav | int(1) | YES |  |
| datpdv | date | YES |  |
| biznisoftbrnal | varchar(20) | NO |  |
| klauzula | int(3) | YES |  |
| tipkl | int(1) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| sifval | int(3) | YES |  |
| datkurs | date | YES |  |
| kurs | double(15,6) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| ideFakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| dobavljac | kupci | sifra | Partner/kupac |
| operater | operateri | sifra | Operater |
| sifval | valuteplacanja | sifra | Valuta |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_upd_frmgk_avans | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_frmgk_avans | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: frmgk_carina
Baza: opp7102025
**Opis:** Prijem carinskog računa. Dokument tipa CR.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| brnal | int(6) | NO | PRI |
| datnal | date | NO |  |
| brdok | varchar(50) | NO |  |
| datdok | date | NO |  |
| dobavljac | int(5) | NO |  |
| konto_carine | varchar(20) | NO |  |
| sifobj | int(3) | NO |  |
| iznos_carine | double(15,2) | YES |  |
| osnovicaos | double(15,2) | YES |  |
| osnovicans | double(15,2) | YES |  |
| pdvos | double(15,2) | YES |  |
| pdvns | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(50) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| opis | varchar(255) | YES |  |
| datval | date | YES |  |
| datplac | date | YES |  |
| vremeizmene | timestamp | NO |  |
| datpdv | date | YES |  |
| knjiziosnovicu | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| ideFakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| dobavljac | kupci | sifra | Partner/kupac |
| sifobj | objekti | sifra | Objekat/poslovnica |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_upd_frmgk_carina | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_frmgk_carina | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: frmgk_ed
Baza: opp7102025
**Opis:** Elektronske dopune. Dokument tipa ED.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| brnal | int(6) | NO | PRI |
| datnal | date | NO |  |
| brdok | varchar(50) | NO |  |
| datdok | date | NO |  |
| dobavljac | int(5) | NO |  |
| datval | date | NO |  |
| opis | varchar(255) | YES |  |
| objekat | int(3) | NO |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| Iznossapdv | double(15,2) | YES |  |
| pdvos | double(15,2) | YES |  |
| provizija | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| datpdv | date | YES |  |
| posebnastopa | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| ideFakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| dobavljac | kupci | sifra | Partner/kupac |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |
| operater | operateri | sifra | Operater |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_upd_frmgk_ed | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_frmgk_ed | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: frmgk_faktura
Baza: opp7102025
**Opis:** Izlazna faktura iz fin.transakcija. Dokument tipa FK.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| brnal | int(6) | NO | PRI |
| datnal | date | NO |  |
| brdok | varchar(50) | NO |  |
| datdok | date | NO |  |
| kupac | int(5) | NO |  |
| datval | date | NO |  |
| opis | varchar(255) | YES |  |
| objekat | int(3) | NO |  |
| usluga | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| Iznossapdv | double(15,2) | YES |  |
| osnovicaos | double(15,2) | YES |  |
| osnovicans | double(15,2) | YES |  |
| osnovica0 | double(15,2) | YES |  |
| pdvos | double(15,2) | YES |  |
| pdvns | double(15,2) | YES |  |
| rabatos | double(15,2) | YES |  |
| rabatns | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| ekstdok | varchar(50) | YES |  |
| datpdv | date | YES |  |
| popdvid | varchar(10) | YES |  |
| biznisoftbrnal | varchar(20) | NO |  |
| klauzula | int(3) | YES |  |
| tipkl | int(1) | YES |  |
| nabvros | double(15,2) | YES |  |
| nabvrns | double(15,2) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| kupac | kupci | sifra | Partner/kupac |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |
| operater | operateri | sifra | Operater |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_upd_frmgk_faktura | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_frmgk_faktura | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: frmgk_nefak
Baza: opp7102025
**Opis:** Faktura nefakturisane robe. Dokument tipa NR.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| brnal | int(6) | NO | PRI |
| datnal | date | NO |  |
| brdok | varchar(50) | NO |  |
| datdok | date | NO |  |
| dobavljac | int(5) | NO |  |
| datval | date | NO |  |
| opis | varchar(255) | YES |  |
| objekat | int(3) | NO |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| Iznossapdv | double(15,2) | YES |  |
| pdvos | double(15,2) | YES |  |
| pdvns | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| ekstdok | varchar(50) | YES |  |
| obrnuto | int(1) | YES |  |
| datpdv | date | YES |  |
| osnovicaos | double(15,2) | YES |  |
| osnovicans | double(15,2) | YES |  |
| popdvid | varchar(10) | YES |  |
| biznisoftbrnal | varchar(20) | NO |  |
| klauzula | int(3) | YES |  |
| tipkl | int(1) | YES |  |
| placeno | int(1) | YES |  |
| racun | varchar(20) | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| ideFakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| dobavljac | kupci | sifra | Partner/kupac |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |
| operater | operateri | sifra | Operater |
| racun | kontniplan | racun | Konto |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_upd_frmgk_nefak | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_frmgk_nefak | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: frmgk_nefak_spec
Baza: opp7102025
**Opis:** Specifikacija stavki nefakturisane robe.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| brnal | varchar(50) | NO | PRI |
| rbrst | int(3) | NO | PRI |
| brnaldok | varchar(50) | YES |  |
| datnal | date | YES |  |
| datdok | date | YES |  |
| dokumveza | varchar(50) | YES |  |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_frmgk_nefak_spec | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_frmgk_nefak_spec | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_frmgk_nefak_spec | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: frmgk_osnsred
Baza: opp7102025
**Opis:** Nabavka osnovnog sredstva. Dokument tipa OS.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| brnal | int(6) | NO | PRI |
| datnal | date | NO |  |
| brdok | varchar(50) | NO |  |
| datdok | date | NO |  |
| dobavljac | int(5) | NO |  |
| datval | date | NO |  |
| opis | varchar(255) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| ekstdok | varchar(50) | YES |  |
| datpdv | date | YES |  |
| biznisoftbrnal | varchar(20) | NO |  |
| nefakturisano | int(1) | YES |  |
| klauzula | int(3) | YES |  |
| tipkl | int(1) | YES |  |
| sifval | int(3) | YES |  |
| datkurs | date | YES |  |
| kurs | double(15,6) | YES |  |
| placeno | int(1) | YES |  |
| racun | varchar(20) | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| ideFakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| dobavljac | kupci | sifra | Partner/kupac |
| operater | operateri | sifra | Operater |
| sifval | valuteplacanja | sifra | Valuta |
| racun | kontniplan | racun | Konto |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_upd_frmgk_osnsred | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_frmgk_osnsred | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: frmgk_prijemfakture
Baza: opp7102025
**Opis:** Prijem računa komitenta. Dokument tipa RK.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| brnal | int(6) | NO | PRI |
| datnal | date | NO |  |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| dobavljac | int(5) | NO |  |
| datval | date | NO |  |
| opis | varchar(255) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| datpdv | date | YES |  |
| biznisoftbrnal | varchar(20) | NO |  |
| klauzula | int(3) | YES |  |
| tipkl | int(1) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| sifval | int(3) | YES |  |
| datkurs | date | YES |  |
| kurs | double(15,6) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| dobavljac | kupci | sifra | Partner/kupac |
| operater | operateri | sifra | Operater |
| sifval | valuteplacanja | sifra | Valuta |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_upd_frmgk_prijemfakture | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_frmgk_prijemfakture | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: frmgk_troskovi
Baza: opp7102025
**Opis:** Račun troškova. Dokument tipa TR.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| brnal | int(6) | NO | PRI |
| datnal | date | NO |  |
| brdok | varchar(50) | NO |  |
| datdok | date | NO |  |
| dobavljac | int(5) | NO |  |
| datval | date | NO |  |
| ekstdok | varchar(50) | YES |  |
| opis | varchar(255) | YES |  |
| placeno | int(1) | YES |  |
| racun | varchar(20) | YES |  |
| analitika | varchar(20) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| sifval | int(3) | YES |  |
| datkurs | date | YES |  |
| kurs | double(15,6) | YES |  |
| datpdv | date | YES |  |
| biznisoftbrnal | varchar(20) | NO |  |
| nefakturisano | int(1) | YES |  |
| klauzula | int(3) | YES |  |
| tipkl | int(1) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| ideFakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| dobavljac | kupci | sifra | Partner/kupac |
| racun | kontniplan | racun | Konto |
| operater | operateri | sifra | Operater |
| sifval | valuteplacanja | sifra | Valuta |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_upd_frmgk_troskovi | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_frmgk_troskovi | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

# 6. DISLOCIRANI OBJEKTI (prod*)

## Tabela: prodkalkulacije
Baza: opp7102025
**Opis:** Kalkulacija iz dislociranog objekta. Dokument tipa DK.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES | MUL |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_prodkalkulacije | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_prodkalkulacije | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_prodkalkulacije | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: prodnivelacije
Baza: opp7102025
**Opis:** Nivelacija iz dislociranog objekta. Dokument tipa DN.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brnivel | int(4) | NO | PRI |
| brdok | varchar(20) | YES | MUL |
| datum | date | YES |  |
| rbrst | int(5) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double | YES |  |
| novacena | double(15,2) | YES |  |
| staracena | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| staripruc | double(15,2) | YES |  |
| novipruc | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| nabcena | double | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| stariporezpd | double(15,2) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_prodnivelacije | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_prodnivelacije | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_prodnivelacije | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: prodintracun
Baza: opp7102025
**Opis:** Interni račun iz dislociranog objekta. Dokument tipa PI.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| obj2 | int(3) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double | YES |  |
| cena | double(15,4) | YES |  |
| kolicina2 | double | YES |  |
| cena2 | double(15,4) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcruc | double | YES |  |
| iznruc | double | YES |  |
| datum | date | NO |  |
| tipobj1 | char(2) | YES |  |
| tipobj2 | char(2) | YES |  |
| porez | double(15,6) | YES |  |
| porez2 | double(15,6) | YES |  |
| prcruc2 | double | YES |  |
| iznruc2 | double | YES |  |
| taksa | double | YES |  |
| prenporez | double | YES |  |
| brdok | varchar(20) | YES | MUL |
| rezcena2 | double(15,4) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| konto2 | varchar(20) | YES |  |
| fid1 | double(15,2) | YES |  |
| fid2 | double(15,2) | YES |  |
| fid3 | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| dostava | int(2) | YES |  |
| wscheckirano | int(1) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| potvrdjeno | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_prodintracun | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_prodintracun | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_prodintracun | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: prodpovracajdob
Baza: opp7102025
**Opis:** Povraćaj dobavljaču iz D.O. Dokument tipa DD.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| novpromet | int(1) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_prodpovracajdob | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_prodpovracajdob | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_prodpovracajdob | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

# 7. ROBNO-TRGOVAČKE OPERACIJE (tbl*)

> Tabele tbl* čuvaju specifične tipove robnih dokumenata.

## Tabela: tblizdavanje
Baza: opp7102025
**Opis:** Izdavanje tuđe robe. Dokument tipa TI.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblizdavanje | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblizdavanje | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblizdavanje | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblotkup
Baza: opp7102025
**Opis:** Prijem tuđe robe. Dokument tipa TO.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES | MUL |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblotkup | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblotkup | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblotkup | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblotkupss
Baza: opp7102025
**Opis:** Otkup sekundarnih sirovina. Dokument tipa TS.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES | MUL |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblotkupss | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblotkupss | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblotkupss | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblpovracaj
Baza: opp7102025
**Opis:** Povraćaj robe kupca + nalog za povraćaj. Dok: PK/NO.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES | MUL |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| knjizenourobnom | int(1) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| novpromet | int(1) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| prcakcrab | double(15,2) | YES |  |
| iznakcrab | double(15,2) | YES |  |
| ukupnorabat | double(15,2) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |
| tipdokefakt | int(1) | YES |  |
| vrdokizvor | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| idefakture | int(10) | YES |  |
| iskazandatum | date | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblpovracaj | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblpovracaj | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblpovracaj | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblpovracajdob
Baza: opp7102025
**Opis:** Povraćaj robe dobavljaču. Dokument tipa PD.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| novpromet | int(1) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblpovracajdob | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblpovracajdob | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblpovracajdob | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblpovracajdobnovi
Baza: opp7102025
**Opis:** Povraćaj dobavljaču - novi promet. Dokument tipa NP.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES | MUL |
| rbrst | int(7) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(5000) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| nabavnacenadob | double(15,4) | YES |  |
| cenazaobjekat | double(15,4) | YES |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblpovracajdobnovi | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblpovracajdobnovi | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblpovracajdobnovi | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblpovracajinokup
Baza: opp7102025
**Opis:** Povraćaj robe ino kupca. Dokument tipa ZI.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(5000) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| sifval | int(3) | YES |  |
| oznval | char(3) | YES |  |
| kurs | double(15,4) | YES |  |
| cenaval | double(15,6) | YES |  |
| iznosval | double(15,2) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| novpromet | int(1) | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |
| datumvazenja | date | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |
| sifval | valuteplacanja | sifra | Valuta |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblpovracajinokup | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblpovracajinokup | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblpovracajinokup | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblprodfakture
Baza: opp7102025
**Opis:** Fakture iz dislociranih objekata. Dokument tipa DF.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(5000) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblprodfakture | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblprodfakture | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblprodfakture | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblkomfakture
Baza: opp7102025
**Opis:** Izdavanje fakture komisionaru. Dokument tipa KF.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES | MUL |
| rbrst | int(7) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(5000) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| sifkomobj | int(3) | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblkomfakture | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblkomfakture | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblkomfakture | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblkomkalk
Baza: opp7102025
**Opis:** Kalkulacija komisione robe. Dokument tipa KK.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblkomkalk | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblkomkalk | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblkomkalk | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblkomvrac
Baza: opp7102025
**Opis:** Vraćanje komisione robe. Dokument tipa KV.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblkomvrac | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblkomvrac | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblkomvrac | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblrobobrdor
Baza: opp7102025
**Opis:** Slanje robe na obradu/doradu. Dokument tipa RO.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblrobobrdor | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblrobobrdor | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblrobobrdor | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblrobobrdorprij
Baza: opp7102025
**Opis:** Prijem robe sa obrade/dorade. Dokument tipa DP.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblrobobrdorprij | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblrobobrdorprij | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblrobobrdorprij | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblrobtransf
Baza: opp7102025
**Opis:** Transformacije artikala po recepturi. Dokument tipa TF.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| receptura | int(1) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblrobtransf | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblrobtransf | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblrobtransf | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblmatobrdor
Baza: opp7102025
**Opis:** Slanje materijala na obradu/doradu. Dokument tipa MO.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblmatobrdor | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblmatobrdor | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblmatobrdor | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblmatobrdorprij
Baza: opp7102025
**Opis:** Prijem materijala sa obrade/dorade. Dokument tipa MP.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblmatobrdorprij | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblmatobrdorprij | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblmatobrdorprij | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblproizvobrdor
Baza: opp7102025
**Opis:** Slanje proizvoda na obradu/doradu. Dokument tipa VO.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblproizvobrdor | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblproizvobrdor | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblproizvobrdor | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblproizvobrdorprij
Baza: opp7102025
**Opis:** Prijem proizvoda sa obrade/dorade. Dokument tipa VP.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblproizvobrdorprij | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblproizvobrdorprij | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblproizvobrdorprij | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tbltrebovanje
Baza: opp7102025
**Opis:** Trebovanje robe. Dokument tipa TB.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(6) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| tipdob | int(1) | NO |  |
| rezervisano | double(15,3) | NO |  |
| naruceno | double(15,3) | NO |  |
| realizovano | double(15,3) | NO |  |
| statuszat | int(1) | NO |  |
| zalihe | double(15,3) | NO |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| grupno | int(1) | YES |  |
| grpobj | int(3) | YES |  |
| preracun | int(1) | YES |  |
| grprez | double(15,3) | YES |  |
| grpfor | double(15,3) | YES |  |
| datisteka | date | YES |  |
| zatvoreno | int(1) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |
| posljed | int(4) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tbltrebovanje | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tbltrebovanje | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tbltrebovanje | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tbluvoz
Baza: opp7102025
**Opis:** Uvozna kalkulacija. Dokument tipa UK.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES | MUL |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| brjci | varchar(100) | YES |  |
| datjci | date | YES |  |
| sifval | int(3) | YES |  |
| oznval | varchar(3) | YES |  |
| kurs | double(12,6) | YES |  |
| cenaval | double(15,6) | YES |  |
| carst | double(10,2) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| objcar | int(3) | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |
| sifval | valuteplacanja | sifra | Valuta |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tbluvoz | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tbluvoz | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tbluvoz | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblizvoz
Baza: opp7102025
**Opis:** Izvoz robe - faktura, profaktura, avans. Dok: ZZ/ZP/ZA.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(5000) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| sifval | int(3) | YES |  |
| oznval | char(3) | YES |  |
| kurs | double(15,4) | YES |  |
| cenaval | double(15,6) | YES |  |
| iznosval | double(15,6) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |
| datumvazenja | date | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |
| sifval | valuteplacanja | sifra | Valuta |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblizvoz | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblizvoz | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblizvoz | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblfaktakcrab
Baza: opp7102025
**Opis:** Faktura sa akcijskim rabatom. Dok: FA/NA/OA.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES | MUL |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(5000) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| prcakcrab | double(15,2) | YES |  |
| iznakcrab | double(15,2) | YES |  |
| ukupnorabat | double(15,2) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(5) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblfaktakcrab | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblfaktakcrab | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblfaktakcrab | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblfaktbezobr
Baza: opp7102025
**Opis:** Fakturisanje bez obračuna nabavke. Dokument tipa RB.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(5) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblfaktbezobr | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblfaktbezobr | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblfaktbezobr | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblintizdavanje
Baza: opp7102025
**Opis:** Interno izdavanje robe. Dokument tipa II.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| obj2 | int(3) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double | YES |  |
| cena | double(15,4) | YES |  |
| kolicina2 | double | YES |  |
| cena2 | double(15,4) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcruc | double | YES |  |
| iznruc | double | YES |  |
| datum | date | NO |  |
| tipobj1 | char(2) | YES |  |
| tipobj2 | char(2) | YES |  |
| porez | double(15,6) | YES |  |
| porez2 | double(15,6) | YES |  |
| prcruc2 | double | YES |  |
| iznruc2 | double | YES |  |
| taksa | double | YES |  |
| prenporez | double | YES |  |
| brdok | varchar(20) | YES |  |
| rezcena2 | double(15,4) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| konto2 | varchar(20) | YES |  |
| zadnjanabavna | double(15,2) | YES |  |
| fid1 | double(15,2) | YES |  |
| fid2 | double(15,2) | YES |  |
| fid3 | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| dostava | int(2) | YES |  |
| wscheckirano | int(1) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| potvrdjeno | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblintizdavanje | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblintizdavanje | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblintizdavanje | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblisplata
Baza: opp7102025
**Opis:** Isplata poljoprivrednom proizvođaču. Dokument tipa LL.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(5) | NO | PRI |
| brpl | int(3) | NO | PRI |
| datum | date | YES |  |
| brdok | varchar(100) | YES |  |
| opis | varchar(255) | YES |  |
| iznos | double(15,2) | YES |  |
| operater | varchar(100) | YES |  |
| status | int(2) | YES |  |
| godina | int(2) | NO |  |
| brnal | varchar(30) | NO |  |
| konto | varchar(20) | NO |  |
| datpdv | date | NO |  |
| popdvid | varchar(10) | YES |  |
| samoupdv | int(1) | YES |  |
| sifpolj | int(5) | NO |  |
| biznisoftbrnal | varchar(20) | NO |  |
| kompenzacija | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| dokumveza2 | varchar(200) | YES |  |
| isplatazaobracun | int(1) | YES |  |
| potvrdjeno | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_upd_tblisplata | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblisplata | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblkooizdavanje
Baza: opp7102025
**Opis:** Izdavanje repromaterijala kooperantu. Dokument tipa KO.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| obj2 | int(3) | YES |  |
| kultura | int(6) | YES |  |
| paritet | double(15,6) | YES |  |
| eur | double(15,4) | YES |  |
| nazivkul | varchar(255) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblkooizdavanje | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblkooizdavanje | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblkooizdavanje | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblnabsitinv
Baza: opp7102025
**Opis:** Nabavka sitnog inventara. Dokument tipa SK.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblnabsitinv | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblnabsitinv | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblnabsitinv | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblsitanizd
Baza: opp7102025
**Opis:** Izdavanje sitnog inventara u upotrebu. Dokument tipa SU.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| obj2 | int(3) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double | YES |  |
| cena | double(15,4) | YES |  |
| kolicina2 | double | YES |  |
| cena2 | double(15,4) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcruc | double | YES |  |
| iznruc | double | YES |  |
| datum | date | NO |  |
| tipobj1 | char(2) | YES |  |
| tipobj2 | char(2) | YES |  |
| porez | double(15,6) | YES |  |
| porez2 | double(15,6) | YES |  |
| prcruc2 | double | YES |  |
| iznruc2 | double | YES |  |
| taksa | double | YES |  |
| prenporez | double | YES |  |
| brdok | varchar(50) | YES | MUL |
| rezcena2 | double(15,4) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| konto2 | varchar(20) | YES |  |
| fid1 | double(15,2) | YES |  |
| fid2 | double(15,2) | YES |  |
| fid3 | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| dostava | int(2) | YES |  |
| wscheckirano | int(1) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| potvrdjeno | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblsitanizd | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblsitanizd | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblsitanizd | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblreversizdavanje
Baza: opp7102025
**Opis:** Izdavanje robe na tuđe skladište - revers. Dok: UI.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| stalnosredstvo | int(1) | YES |  |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblreversizdavanje | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblreversizdavanje | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblreversizdavanje | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblreversprijem
Baza: opp7102025
**Opis:** Prijem robe sa tuđeg skladišta - revers. Dok: UP.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| stalnosredstvo | int(1) | YES |  |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblreversprijem | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblreversprijem | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblreversprijem | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblpoljoprivreda
Baza: opp7102025
**Opis:** Otkup poljoprivrednih proizvoda. Dokument tipa PP.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES | MUL |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| eur | double(15,4) | YES |  |
| nacisplate | varchar(255) | YES |  |
| kvalitet | varchar(255) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| tudjaroba | int(1) | YES |  |
| objekattudjerobe | int(3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| wscheckirano | int(1) | YES |  |
| bruto | double(15,2) | YES |  |
| brgajb | double(15,2) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| ambalaza | int(6) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblpoljoprivreda | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblpoljoprivreda | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblpoljoprivreda | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblotpisnz
Baza: opp7102025
**Opis:** Otpis mimo zakonskih stopa. Dokument tipa ON.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(10) | NO | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| racuntroska | varchar(20) | NO |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblotpisnz | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblotpisnz | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblotpisnz | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblotpisz
Baza: opp7102025
**Opis:** Otpis po zakonskim stopama. Dokument tipa OZ.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(10) | NO | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| racuntroska | varchar(20) | NO |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblotpisz | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblotpisz | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblotpisz | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblprodamb
Baza: opp7102025
**Opis:** Prodaja ambalaže. Dokument tipa RM.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblprodamb | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblprodamb | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblprodamb | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblprodmat
Baza: opp7102025
**Opis:** Prodaja repromaterijala. Dokument tipa FM.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(5) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblprodmat | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblprodmat | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblprodmat | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblsopsttros
Baza: opp7102025
**Opis:** Račun sopstvenih troškova. Dokument tipa RT.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES | MUL |
| rbrst | int(7) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(5000) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| racuntroska | varchar(20) | NO |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblsopsttros | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblsopsttros | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblsopsttros | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblnarkupaca
Baza: opp7102025
**Opis:** Narudžbine kupaca. Dokument tipa NK.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES | MUL |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| rezervisano | double(15,3) | NO |  |
| realizovano | double(15,3) | NO |  |
| statuszat | int(1) | YES |  |
| trebovano | double(15,3) | NO |  |
| vremeizmene | timestamp | NO |  |
| formirano | int(1) | YES |  |
| prcakcrab | double(15,2) | YES |  |
| iznakcrab | double(15,2) | YES |  |
| ukupnorabat | double(15,2) | YES |  |
| serija | varchar(1000) | YES |  |
| rezervisi | double(15,3) | YES |  |
| kontlista | int(1) | YES |  |
| tipdok | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| zatvoreno | int(1) | YES |  |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |
| sifval | int(3) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |
| sifval | valuteplacanja | sifra | Valuta |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblnarkupaca | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblnarkupaca | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblnarkupaca | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblnardobavljacima
Baza: opp7102025
**Opis:** Narudžbine dobavljačima. Dokument tipa ND.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brkalk | int(4) | NO | PRI |
| datum | date | YES |  |
| dobavljac | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| datdok | date | NO |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| rabat | double(15,2) | YES |  |
| exttr | double(15,2) | YES |  |
| inttr | double(15,2) | YES |  |
| nabcena | double(15,2) | YES |  |
| nabvrednost | double(15,2) | YES |  |
| ruc | double(15,2) | YES |  |
| cenabezpp | double(15,2) | YES |  |
| vredbezpp | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| obrpp | double(15,2) | YES |  |
| prenetpp | double(15,2) | YES |  |
| cenasapp | double(15,2) | YES |  |
| vrednostsapp | double(15,2) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcrabat | double | YES |  |
| prcexttr | double | YES |  |
| prcinttr | double | YES |  |
| prctaksa | double | YES |  |
| prcruc | double | YES |  |
| vrednost | double(15,2) | YES |  |
| izntaksa | double(15,2) | YES |  |
| nc | int(1) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| realizovano | double(15,3) | NO |  |
| statuszat | int(1) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| racunjeplacen | int(1) | YES |  |
| kontrastav | varchar(20) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| internipdv | int(1) | YES |  |
| zatvoreno | int(1) | YES |  |
| datisteka | date | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| objekat2 | int(3) | YES |  |
| datumvalute | date | YES |  |
| analitika | varchar(20) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| sifval | int(3) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| dobavljac | kupci | sifra | Partner/kupac |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |
| sifval | valuteplacanja | sifra | Valuta |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblnardobavljacima | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblnardobavljacima | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblnardobavljacima | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblodobdob
Baza: opp7102025
**Opis:** Prijem odobrenja/zaduženja dobavljača. Dokument tipa OD.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumrobno | date | YES |  |
| datumvalute | date | YES |  |
| nefakturisano | int(1) | YES |  |
| korekcija | double(15,2) | YES |  |
| korekcijakolicina | double(15,2) | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |
| datprometa | date | YES |  |
| datprih | date | YES |  |
| iskazandatum | date | YES |  |
| idefakture | int(10) | YES |  |
| vrdokizvor | int(1) | YES |  |
| odobrenjezaavans | int(1) | YES |  |
| tipdokefakt | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblodobdob | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblodobdob | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblodobdob | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblodobkup
Baza: opp7102025
**Opis:** Knjižno odobrenje kupcu. Dokument tipa OK.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(5) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblodobkup | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblodobkup | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblodobkup | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblodobinodob
Baza: opp7102025
**Opis:** Knjižno odobrenje/zaduženje ino dobavljača. Dok: ZD.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(5000) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| sifval | int(3) | YES |  |
| oznval | char(3) | YES |  |
| kurs | double(15,4) | YES |  |
| cenaval | double(15,6) | YES |  |
| iznosval | double(15,2) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| datumrobno | date | YES |  |
| nefakturisano | int(1) | YES |  |
| korekcija | double(15,2) | YES |  |
| korekcijakolicina | double(15,2) | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |
| tipdokefakt | int(1) | YES |  |
| datumvazenja | date | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |
| sifval | valuteplacanja | sifra | Valuta |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblodobinodob | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblodobinodob | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblodobinodob | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblodobinokup
Baza: opp7102025
**Opis:** Knjižno odobrenje/zaduženje ino kupca. Dok: ZO.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(5000) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| sifval | int(3) | YES |  |
| oznval | char(3) | YES |  |
| kurs | double(15,4) | YES |  |
| cenaval | double(15,6) | YES |  |
| iznosval | double(15,2) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |
| datumvazenja | date | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |
| sifval | valuteplacanja | sifra | Valuta |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblodobinokup | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblodobinokup | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblodobinokup | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblprodajagp
Baza: opp7102025
**Opis:** Prodaja gotovih proizvoda (pogonsko). Dokument tipa GP.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblprodajagp | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblprodajagp | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblprodajagp | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblposotpremnice
Baza: opp7102025
**Opis:** Fakturisanje po POS otpremnicama. Dokument tipa PO.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| datumod | date | NO |  |
| datumdo | date | NO |  |
| posbrdok | varchar(50) | YES |  |
| posdatumdok | date | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblposotpremnice | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblposotpremnice | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblposotpremnice | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblamprijdob
Baza: opp7102025
**Opis:** Prijem ambalaže od dobavljača. Dokument tipa AJ.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblamprijdob | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblamprijdob | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblamprijdob | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblamizdkup
Baza: opp7102025
**Opis:** Izdavanje ambalaže kupcu. Dokument tipa AM.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblamizdkup | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblamizdkup | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblamizdkup | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblambintpr
Baza: opp7102025
**Opis:** Interni prenos ambalaže. Dokument tipa AA.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| obj2 | int(3) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double | YES |  |
| cena | double(15,4) | YES |  |
| kolicina2 | double | YES |  |
| cena2 | double(15,4) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcruc | double | YES |  |
| iznruc | double | YES |  |
| datum | date | NO |  |
| tipobj1 | char(2) | YES |  |
| tipobj2 | char(2) | YES |  |
| porez | double(15,6) | YES |  |
| porez2 | double(15,6) | YES |  |
| prcruc2 | double | YES |  |
| iznruc2 | double | YES |  |
| taksa | double | YES |  |
| prenporez | double | YES |  |
| brdok | varchar(20) | YES | MUL |
| rezcena2 | double(15,4) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| konto2 | varchar(20) | YES |  |
| fid1 | double(15,2) | YES |  |
| fid2 | double(15,2) | YES |  |
| fid3 | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| dostava | int(2) | YES |  |
| wscheckirano | int(1) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| potvrdjeno | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblambintpr | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblambintpr | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblambintpr | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblampovdob
Baza: opp7102025
**Opis:** Povraćaj ambalaže dobavljaču. Dokument tipa AV.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblampovdob | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblampovdob | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblampovdob | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblampovkup
Baza: opp7102025
**Opis:** Povraćaj ambalaže od kupca. Dokument tipa AP.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(255) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| sifra | artikli | sifra | Artikal |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_tblampovkup | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_tblampovkup | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_tblampovkup | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: tblpodosp
Baza: opp7102025
**Opis:** Pregled dospelih obaveza.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| kolona | int(1) | NO | PRI |
| od | int(5) | NO |  |

---

## Tabela: tblpodospnedosp
Baza: opp7102025
**Opis:** Pregled nedospelih obaveza.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| kolona | int(1) | NO | PRI |
| od | int(5) | NO |  |

---

## Tabela: tblcennivel1
Baza: opp7102025
**Opis:** Cenovna nivelacija tip 1.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |

---

## Tabela: tblcennivel2
Baza: opp7102025
**Opis:** Cenovna nivelacija tip 2.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| operater | varchar(12) | NO | PRI |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| operater | operateri | sifra | Operater |

---

# 8. SITNI INVENTAR

## Tabela: sitinvpov
Baza: opp7102025
**Opis:** Povraćaj sitnog inventara od radnika. Dokument tipa SP.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| obj2 | int(3) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double | YES |  |
| cena | double(15,4) | YES |  |
| kolicina2 | double | YES |  |
| cena2 | double(15,4) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcruc | double | YES |  |
| iznruc | double | YES |  |
| datum | date | NO |  |
| tipobj1 | char(2) | YES |  |
| tipobj2 | char(2) | YES |  |
| porez | double(15,6) | YES |  |
| porez2 | double(15,6) | YES |  |
| prcruc2 | double | YES |  |
| iznruc2 | double | YES |  |
| taksa | double | YES |  |
| prenporez | double | YES |  |
| brdok | varchar(50) | YES | MUL |
| rezcena2 | double(15,4) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| konto2 | varchar(20) | YES |  |
| fid1 | double(15,2) | YES |  |
| fid2 | double(15,2) | YES |  |
| fid3 | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| radnik | int(6) | NO |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| dostava | int(2) | YES |  |
| wscheckirano | int(1) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| potvrdjeno | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_sitinvpov | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_sitinvpov | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_sitinvpov | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: sitinvras
Baza: opp7102025
**Opis:** Rashodovanje sitnog inventara. Dokument tipa SR.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| datum | date | NO |  |
| sifkup | int(5) | YES | MUL |
| brdok | varchar(50) | YES |  |
| rbrst | int(7) | NO | PRI |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | YES |  |
| cena | double(20,6) | YES |  |
| prcrabat | double(15,6) | YES |  |
| rabat | double(15,2) | YES |  |
| prctran | double(15,2) | YES |  |
| trantr | double(15,2) | YES |  |
| prcruc | double(15,2) | YES |  |
| iznruc | double(15,2) | YES |  |
| status | int(5) | YES |  |
| operater | varchar(10) | YES |  |
| porezprom | double(15,2) | YES |  |
| porezusl | double(15,2) | YES |  |
| cenakupac | double(15,2) | YES |  |
| vredkupac | double(15,2) | YES |  |
| razluceni | double(15,2) | YES |  |
| taksa | double(15,2) | YES |  |
| vrednost | double(15,2) | YES |  |
| prcporpr | double(15,2) | YES |  |
| tip | char(1) | NO | PRI |
| akcc | int(1) | YES |  |
| prenporez | int(1) | YES |  |
| datprom | date | NO |  |
| napomena | varchar(5000) | YES |  |
| avracuni | varchar(255) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| dostava | int(2) | YES |  |
| nivcena | double(15,6) | YES |  |
| racuntroska | varchar(20) | NO |  |
| datpdv | date | YES |  |
| defpopdvid | varchar(10) | YES |  |
| popdvid | varchar(10) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| idf | varchar(10) | YES |  |
| wscheckirano | int(1) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| datumvalute | date | YES |  |
| IKOF | varchar(50) | YES |  |
| potvrdjeno | int(1) | YES |  |
| stornirano | int(1) | YES |  |
| efaktpdvoznaka | varchar(2) | YES |  |
| datumslanja | date | NO |  |
| postkom | varchar(50) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_sitinvras | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_sitinvras | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_sitinvras | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: sitinvzad
Baza: opp7102025
**Opis:** Zaduženje sitnog inventara po radnicima. Dokument tipa SZ.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brrn | int(6) | NO | PRI |
| obj2 | int(3) | YES |  |
| rbrst | int(3) | NO | PRI |
| sifra | int(6) | YES |  |
| kolicina | double | YES |  |
| cena | double(15,4) | YES |  |
| kolicina2 | double | YES |  |
| cena2 | double(15,4) | YES |  |
| status | int(2) | YES |  |
| operater | varchar(10) | YES |  |
| prcruc | double | YES |  |
| iznruc | double | YES |  |
| datum | date | NO |  |
| tipobj1 | char(2) | YES |  |
| tipobj2 | char(2) | YES |  |
| porez | double(15,6) | YES |  |
| porez2 | double(15,6) | YES |  |
| prcruc2 | double | YES |  |
| iznruc2 | double | YES |  |
| taksa | double | YES |  |
| prenporez | double | YES |  |
| brdok | varchar(50) | YES | MUL |
| rezcena2 | double(15,4) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| konto | varchar(20) | YES |  |
| konto2 | varchar(20) | YES |  |
| fid1 | double(15,2) | YES |  |
| fid2 | double(15,2) | YES |  |
| fid3 | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| kontlista | int(1) | YES |  |
| radnik | int(6) | NO |  |
| nivcena | double(15,2) | YES |  |
| nivkolicina | double(15,3) | YES |  |
| dostava | int(2) | YES |  |
| wscheckirano | int(1) | YES |  |
| iznosakcize | double(15,6) | YES |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| potvrdjeno | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_ins_sitinvzad | BEFORE INSERT | Provera vlasništva operatera i statusa dokumenta |
| operdoc_upd_sitinvzad | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_sitinvzad | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

# 9. OSNOVNA SREDSTVA

## Tabela: osamvr
Baza: opp7102025
**Opis:** Amortizacija osnovnih sredstava. Ima AFTER trigere za ažuriranje vrednosti.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| osoznaka | varchar(6) | NO | PRI |
| invbroj | int(8) | NO | PRI |
| datam | date | NO | PRI |
| rbr | tinyint(2) | NO | PRI |
| opis | varchar(70) | YES |  |
| datumod | date | YES |  |
| metoda | char(1) | YES |  |
| nabvr | double(15,2) | YES |  |
| amvrpreth | double(15,2) | YES |  |
| osnovica | double(15,2) | YES |  |
| godstopa | float(7,4) | YES |  |
| brmes | int(4) | YES |  |
| procfam | float(9,6) | YES |  |
| amvr | double(15,2) | YES |  |
| rn_amvr | varchar(10) | YES |  |
| rn_trosam | varchar(10) | YES |  |
| tipam | enum('K','P','S') | YES |  |
| datcre | date | YES |  |
| datizm | datetime | YES |  |
| operater | varchar(12) | YES |  |
| komada | int(11) | YES |  |
| rbramort | int(3) | NO | PRI |
| datnab | date | YES |  |
| rbrnab | int(3) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| insosamvr | AFTER INSERT | Ažurira vrednost OS nakon promene |
| updosamvr | AFTER UPDATE | Ažurira vrednost OS nakon promene |
| delosamvr | AFTER DELETE | Ažurira vrednost OS nakon promene |

---

## Tabela: osnabvr
Baza: opp7102025
**Opis:** Nabavna vrednost OS. Ima AFTER trigere.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| osoznaka | varchar(6) | NO | PRI |
| invbroj | int(8) | NO | PRI |
| datnab | date | NO | PRI |
| rbr | tinyint(2) | NO | PRI |
| opis | varchar(255) | YES |  |
| cena | double(15,2) | YES |  |
| nabvr | double(15,2) | YES |  |
| amvr | double(15,2) | YES |  |
| rzdvr | double(15,2) | YES |  |
| sifdob | int(8) | YES |  |
| nazdob | varchar(70) | YES |  |
| brdok | varchar(20) | YES |  |
| fabbr | varchar(35) | YES |  |
| datproizvodnje | date | YES |  |
| datsadvr | date | YES |  |
| datsadvra | date | YES |  |
| cuvdatsvr | date | YES |  |
| tipnab | enum('0','1','2','3') | YES |  |
| datcre | date | YES |  |
| datizm | datetime | YES |  |
| operater | varchar(12) | YES |  |
| komada | double(15,2) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| operater | operateri | sifra | Operater |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| insosnabvr | AFTER INSERT | Ažurira vrednost OS nakon promene |
| updosnabvr | AFTER UPDATE | Ažurira vrednost OS nakon promene |
| delosnabvr | AFTER DELETE | Ažurira vrednost OS nakon promene |

---

## Tabela: osotpis
Baza: opp7102025
**Opis:** Otpis OS. Ima AFTER trigere za ažuriranje vrednosti.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| osoznaka | varchar(6) | NO | PRI |
| invbroj | int(8) | NO | PRI |
| datotp | date | NO | MUL |
| tipotp | enum('1','2','3','4') | YES |  |
| opis | varchar(70) | YES |  |
| nabvr | double(15,2) | YES |  |
| amvr | double(15,2) | YES |  |
| iznotp | double(15,6) | YES |  |
| prodcena | double(15,2) | YES |  |
| rn_nabvr | varchar(10) | YES |  |
| rn_amvr | varchar(10) | YES |  |
| rn_kontra | varchar(10) | YES |  |
| datcre | date | YES |  |
| datizm | datetime | YES |  |
| operater | varchar(12) | YES |  |
| komada | double(15,2) | YES |  |
| rbr | smallint(6) | NO | PRI |
| neotporvr | double(15,2) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| operater | operateri | sifra | Operater |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| insosotpis | AFTER INSERT | Ažurira vrednost OS nakon promene |
| updosotpis | AFTER UPDATE | Ažurira vrednost OS nakon promene |
| delosotpis | AFTER DELETE | Ažurira vrednost OS nakon promene |

---

# 10. OSTALI DOKUMENTI

## Tabela: radnal
Baza: opp7102025
**Opis:** Radni nalog / grupni radni nalog. Dok: RD/GN.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| sifobj | int(3) | NO | PRI |
| brnal | int(5) | NO | PRI |
| datnal | date | NO |  |
| sifobjmrm | int(2) | NO |  |
| nazobjmrm | varchar(100) | NO |  |
| sifobjmgp | int(2) | NO |  |
| nazobjmgp | varchar(100) | NO |  |
| sifra | int(6) | NO |  |
| kolicina | double(15,3) | NO |  |
| status | int(3) | YES |  |
| operater | varchar(100) | YES |  |
| brdok | varchar(20) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| nadbrnal | varchar(20) | YES |  |
| poctermin | datetime | YES |  |
| krtermin | datetime | YES |  |
| narucilac | int(5) | YES |  |
| primalac | int(5) | YES |  |
| napomena | longtext | YES |  |
| xxbrnal | varchar(20) | YES | MUL |
| gnbrnal | varchar(20) | YES | MUL |
| oznaka | varchar(255) | YES |  |
| biznisoftbrnal | varchar(20) | NO |  |
| receptura_broj | int(4) | YES |  |
| receptura_vrsta | int(1) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_upd_radnal | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_radnal | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

## Tabela: putninalog
Baza: opp7102025
**Opis:** Putni nalog u zemlji/inostranstvu. Dok: PN/IN.

### Struktura
| Kolona | Tip | Null | Ključ |
|--------|-----|------|-------|
| tip | int(1) | NO | PRI |
| broj | int(6) | NO | PRI |
| datnal | date | NO |  |
| radnik | int(6) | NO |  |
| datpolaska | date | NO |  |
| planpovratka | date | NO |  |
| vozilo | int(4) | NO |  |
| drzava | int(3) | NO |  |
| mesto | varchar(255) | NO |  |
| zadatak | varchar(500) | YES |  |
| sifobj | int(3) | NO |  |
| tipmesto | int(1) | NO |  |
| akontacijaRSD | double(15,2) | YES |  |
| akontsifval | int(3) | NO |  |
| akontacijaval | double(15,2) | YES |  |
| vremeprelgro | datetime | YES |  |
| vremeprelgrd | datetime | YES |  |
| datobracuna | date | YES |  |
| status | int(1) | NO |  |
| operater | varchar(50) | YES |  |
| vremeizmene | timestamp | NO |  |
| biznisoftbrnal | varchar(20) | NO | MUL |
| vremepocetka | datetime | YES |  |
| vremekraja | datetime | YES |  |
| cena1lg | double(15,2) | YES |  |
| mestotr | int(6) | YES |  |
| nosioc | int(6) | YES |  |
| potvrdjeno | int(1) | YES |  |
| bop | varchar(19) | YES |  |

### Relacije
| Kolona | → Tabela | → Kolona | Tip |
|--------|----------|----------|-----|
| sifobj | objekti | sifra | Objekat/poslovnica |
| operater | operateri | sifra | Operater |
| mestotr | mestatr | sifra | Mesto troška |
| nosioc | nosioci | sifra | Nosilac troška |

### Trigeri
| Triger | Događaj | Šta radi |
|--------|---------|----------|
| operdoc_upd_putninalog | BEFORE UPDATE | Provera vlasništva operatera i statusa dokumenta |
| operdoc_del_putninalog | BEFORE DELETE | Provera vlasništva operatera i statusa dokumenta |

---

# 11. PROCEDURE I FUNKCIJE

### Ključne procedure

| Procedura/Funkcija | Tip | Opis |
|-------------------|-----|------|
| AktuelizujCenovnik | PROCEDURE | Aktuelizuje cenovnik za objekte |
| AutCheckMinzal | PROCEDURE |  |
| automatskoHelper | PROCEDURE |  |
| avgPrice | FUNCTION | Prosečna nabavna cena (FUNCTION) |
| avgPricePrerNC | FUNCTION |  |
| AzurRnPartKli | PROCEDURE |  |
| BojiAkcije | PROCEDURE |  |
| bsnotif | PROCEDURE |  |
| CheckAkcije | PROCEDURE | Proverava aktivne akcije za artikle |
| checkdokpary | PROCEDURE |  |
| checkForeignKeys | PROCEDURE |  |
| CheckLDRN | PROCEDURE |  |
| CheckPrometPoSifri | PROCEDURE |  |
| CheckTabRnPog | PROCEDURE |  |
| CheckTabRnPogAMT | PROCEDURE |  |
| checkvpcenovnik | PROCEDURE |  |
| create_tmp_tmp_rek | PROCEDURE |  |
| creeeopdvp | PROCEDURE |  |
| creeeopdv_pz | PROCEDURE |  |
| creeeppdvp | PROCEDURE |  |
| CreTmpSerbr | PROCEDURE |  |
| cre_pregled_eeppdv | PROCEDURE |  |
| cre_tmp_pojedinacna | PROCEDURE |  |
| dajmidokumente | PROCEDURE |  |
| DaLiJeUAvansu | FUNCTION | Provera da li je dokument avansan (FUNCTION) |
| DaLiJeUAvansuOPP | PROCEDURE |  |
| DeleteInvoiceRecords | PROCEDURE |  |
| dododatrsub | PROCEDURE |  |
| dopuni_pregled_eeppdv | PROCEDURE |  |
| DoWriteLocation | PROCEDURE |  |
| eeopdvp | PROCEDURE | Evidencija ePDV - obrada |
| eeopdvspec | PROCEDURE |  |
| eeppdvp | PROCEDURE | Evidencija ePDV - prijem |
| eo_fix_auto_increment | PROCEDURE |  |
| eo_get_max_document_id | FUNCTION |  |
| fifoPrice | FUNCTION | FIFO nabavna cena (FUNCTION) |
| fifoPricePrerNC | FUNCTION |  |
| fifoPricePST | PROCEDURE |  |
| fifoPricePSTAll | PROCEDURE | FIFO preračun cena - svi artikli |
| fifo_calc | PROCEDURE |  |
| fifo_calc_prerNC | PROCEDURE |  |
| formirajEEOPDVP | PROCEDURE |  |
| FormirajVeznu | PROCEDURE | Formira veznu tabelu kontnog plana |
| getakciza | FUNCTION | Vraća akcizu za artikal (FUNCTION) |
| GetArchiveParentUID | FUNCTION |  |
| getconvertvaluta | FUNCTION |  |
| GetEEPAnalytics | PROCEDURE |  |
| getEvidencijaStorno | PROCEDURE |  |
| getizvor | FUNCTION |  |
| getizvorbezodbitka | FUNCTION |  |
| getizvoriname | FUNCTION |  |
| GetKplPrevod | FUNCTION |  |
| GetKplPrevodRacun | FUNCTION |  |
| getlokacija | FUNCTION |  |
| GetNabCena | PROCEDURE |  |
| GetNextBrNal | PROCEDURE | Daje sledeći broj naloga |
| GetNovaPrerCena | FUNCTION |  |
| GetOsnovniBrnal | FUNCTION |  |
| getosrn | FUNCTION |  |
| getpdv | FUNCTION | Vraća PDV stopu za artikal (FUNCTION) |
| GetPeriod | FUNCTION |  |
| getPrevodArtikla | FUNCTION |  |
| GetSrbDayOfWeek | FUNCTION |  |
| GetSrbMonth | FUNCTION |  |
| GetSrbQuarter | FUNCTION |  |
| GetTransformacija | FUNCTION |  |
| GetTransformacijaReceptura | FUNCTION |  |
| getUkupnoPrethodniPDV | FUNCTION |  |
| GetYM | FUNCTION |  |
| intufinansijskom | FUNCTION | Da li je nalog u finansijskom (FUNCTION) |
| intukep | FUNCTION |  |
| intupdv | FUNCTION | Da li je nalog u PDV evidenciji (FUNCTION) |
| inturobnom | FUNCTION | Da li je nalog u robnom prometu (FUNCTION) |
| ios | PROCEDURE | IOS - Izvod otvorenih stavki |
| istiporpr | FUNCTION |  |
| KnjiziTransformaciju | PROCEDURE | Knjiženje transformacija po recepturi |
| kreirajPopis | PROCEDURE | Kreira popis na osnovu stanja |
| KreirajTabeleZaStorno | PROCEDURE |  |
| KreirajTmpTabele | PROCEDURE |  |
| labelsInsert | PROCEDURE |  |
| lastPrice | FUNCTION | Poslednja nabavna cena (FUNCTION) |
| lastPriceNCP | FUNCTION |  |
| lastPricePrerNC | FUNCTION |  |
| lastRabatI | PROCEDURE |  |
| lastRabatU | PROCEDURE |  |
| MyDayOfWeek | FUNCTION |  |
| myprenos1 | PROCEDURE |  |
| nadjiKonto | FUNCTION | Nalazi odgovarajući konto (FUNCTION) |
| NalogPrerNc | PROCEDURE |  |
| NalogPrerNcGK | PROCEDURE |  |
| NalogPrerNCRobno | PROCEDURE |  |
| nazivppz | FUNCTION |  |
| obojiavanse | PROCEDURE |  |
| obracunPotvrdjeno | PROCEDURE |  |
| obracunRazlikeUCeni | PROCEDURE |  |
| obrNabavke | FUNCTION |  |
| OtvaranjeNoveGodine | PROCEDURE | Procedura za otvaranje nove poslovne godine |
| oznakasef | PROCEDURE |  |
| prenesiSveArtikle | PROCEDURE |  |
| PrenosSifarnika | PROCEDURE |  |
| PrepareEEPPDVData | PROCEDURE |  |
| PrepareZaSveArtikle | PROCEDURE |  |
| PreracunajNC | PROCEDURE | Preračunava nabavne cene |
| PrerNCPostojiTransformacija | FUNCTION |  |
| pripremitabele | PROCEDURE |  |
| ProveraIntegriteta | PROCEDURE | Proverava integritet podataka |
| ProveraStatusa | PROCEDURE |  |
| ProvRezervacije | PROCEDURE |  |
| pr_doeeppdv | PROCEDURE |  |
| punitabelu | PROCEDURE |  |
| puniTmpZbirnu | PROCEDURE |  |
| punitmpzbirnusimulacija | PROCEDURE |  |
| racunajKolicine | PROCEDURE |  |
| RekapitulacijaPDV | PROCEDURE | Rekapitulacija PDV-a |
| RezNarTrb | PROCEDURE |  |
| sefknjizenjanew | PROCEDURE | SEF knjiženja - nova verzija |
| sefknjizenjaold | PROCEDURE |  |
| SpremiZaSimulaciju1 | PROCEDURE |  |
| SpremiZaSimulaciju2 | PROCEDURE |  |
| SpremiZaSimulaciju3 | PROCEDURE |  |
| SrediAmortizaciju | PROCEDURE |  |
| SrediSpecSerbr | PROCEDURE |  |
| SrediTmpFinprom | PROCEDURE |  |
| SrediTmpPopdvPromet | PROCEDURE |  |
| SrediTmpRobno | PROCEDURE |  |
| SrediTmpTrgovacka | PROCEDURE |  |
| SrediTmp_eeopdv_pojedinacna | PROCEDURE |  |
| SrediTmp_eeopdv_zbirna | PROCEDURE |  |
| SrediTmp_eeppdv_promet | PROCEDURE |  |
| starostzaliha | PROCEDURE |  |
| stats4art | PROCEDURE |  |
| stats4artgraph | PROCEDURE |  |
| stats4kont | PROCEDURE |  |
| stats4kontgraph | PROCEDURE |  |
| stats4part | PROCEDURE |  |
| stats4partgraph | PROCEDURE |  |
| statskart | PROCEDURE |  |
| StornirajKnjizenja | PROCEDURE | Storniranje knjiženja |
| StornirajKnjizenja3 | PROCEDURE |  |
| StornirajKnjizenjaNaDan | PROCEDURE |  |
| stornopopdvid | FUNCTION |  |
| TrebStanje | FUNCTION |  |
| trigoperdoc | PROCEDURE | Kreira operdoc trigere na tabelama |
| trigoperdocx | PROCEDURE |  |
| WriteLocation | PROCEDURE |  |
| xtrstanje | PROCEDURE | Rekalkulacija stanja zaliha (trstanje) |
| xtrstanjesql | PROCEDURE |  |
| ZadNabPartner | FUNCTION |  |
| ZbirnoPoDokumentu | PROCEDURE |  |

# 12. PREGLED TRIGERA PO TABELAMA

> Većina tabela ima `operdoc_*` trigere (provera operatera/statusa) i `zak_*` trigere (zaključan period).

### Tabele sa specijalnim trigerima (ne samo operdoc/zak)

| Tabela | Triger | Tip | Šta radi |
|--------|--------|-----|----------|
| artikli | updartikli | AFTER UPDATE | Sinhronizuje naziv/jedmere/porez/barkod u trstanje |
| fakture | updfakture | AFTER UPDATE | Ažurira trstanje.rezervacije i refobjst |
| robno | insstanje | AFTER INSERT | Ažurira trstanje nakon unosa robnog prometa |
| robno | updstanje | AFTER UPDATE | Ažurira trstanje nakon izmene robnog prometa |
| robno | delstanje | AFTER DELETE | Ažurira trstanje nakon brisanja robnog prometa |
| kasa | inskasa | AFTER INSERT | Ažurira trstanje nakon unosa kase |
| kasa | updkasa | AFTER UPDATE | Ažurira trstanje nakon izmene kase |
| kasa | delkasa | AFTER DELETE | Ažurira trstanje nakon brisanja kase |
| osamvr | ins/upd/del | AFTER * | Ažurira vrednost OS amortizacije |
| osnabvr | ins/upd/del | AFTER * | Ažurira nabavnu vrednost OS |
| osotpis | ins/upd/del | AFTER * | Ažurira vrednost otpisa OS |
