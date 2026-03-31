# Biznisoft - Funkcije u bazi `opp7102025` (klijentska baza)

> Generisano: 2026-03-29

## Pregled

Baza `opp7102025` sadrži **44 funkcije**. Organizovane su po poslovnim domenima.

---

## 1. OBRAČUN CENA I NABAVKE (Robno poslovanje)

### 1.1 `avgPrice(myprctype, so, sa, dt, qt)` → DOUBLE
**Prosečna nabavna cena artikla** po metodi ponderisanog proseka.
- **Parametri**: tip cene (NBC/VPC), šifra objekta, šifra artikla, datum, količina
- **Logika**:
  - Za NBC: računa prosek iz `duguje-potrazuje` ili `ulaz*nabcena - izlaz*nabcena`
  - Za VPC: koristi `nabcena` ili `prernc` (zavisno od parametra `@param10996`)
  - Ako nema zalihe, traži poslednju nabavnu cenu
  - Ako tražena količina > zaliha, kombinuje prosečnu i poslednju cenu (`lastPrice`)
- **Tabele**: `robno`
- **Poziva**: `lastPrice()`

### 1.2 `avgPricePrerNC(myprctype, so, sa, dt, qt, s_condatddat, s_mysifobj)` → DOUBLE
**Prosečna cena za preračunatu nabavnu cenu** (PrerNC).
- Ako je FIFO aktivan za tip objekta → delegira na `fifoPricePrerNC()`
- Inače računa prosek iz `my_prernc_robno` temp tabele
- **Tabele**: `my_prernc_robno`
- **Poziva**: `fifoPricePrerNC()`, `lastPricePrerNC()`, `lastPrice()`

### 1.3 `fifoPrice(so, sa, dt, qt)` → DOUBLE
**FIFO nabavna cena** - wrapper koji poziva proceduru `fifo_calc()`.
- **Poziva**: proceduru `fifo_calc()`

### 1.4 `fifoPricePrerNC(so, sa, dt, qt, s_condatddat)` → DOUBLE
**FIFO cena za preračunatu NC** - wrapper za `fifo_calc_prerNC()`.
- **Poziva**: proceduru `fifo_calc_prerNC()`

### 1.5 `lastPrice(so, sa, dt, qt)` → DOUBLE
**Poslednja nabavna cena** artikla na objektu.
- Traži poslednji ulaz pre datuma, pa bilo koji ulaz ako nema
- Koristi `prernc` ili `nabcena` zavisno od `@param10996`
- **Tabele**: `robno`

### 1.6 `lastPriceNCP(so, sa, dt, qt)` → DOUBLE
**Poslednja nabavna cena bez datumskog ograničenja** - traži poslednju cenu > 0.
- **Tabele**: `robno`

### 1.7 `lastPricePrerNC(so, sa, dt, qt)` → DOUBLE
**Poslednja preračunata NC** iz temp tabele `my_prernc_robno`.
- **Tabele**: `my_prernc_robno`

### 1.8 `obrNabavke(tipObjekta, sifraObjekta, sifraArtikla, kolicina, vrednost, datum, vrstaCene)` → DOUBLE
**Glavni dispatcher za obračun nabavne cene** po tipu objekta i metodi obračuna.
- Tip 01/02/03/10/08: FIFO (`@obrCen=1`) ili prosek (`@obrCen=2`)
- Tip 04/05: direktna vrednost
- Tip 10/18 sa `@obrCen=3`: planska cena iz `artikli`
- Tip 09/11: planska ili prosek
- Tip 06/07: poslednja cena
- Tip 21/22: prosečna cena
- **Tabele**: `artikli`, indirektno `robno`
- **Poziva**: `fifoPrice()`, `avgPrice()`, `lastPrice()`

### 1.9 `GetNovaPrerCena(s_brnal, s_sifra, s_nabcena)` → DOUBLE
**Nova preračunata cena** iz temp tabele za izlaze.
- **Tabele**: `my_prernc_robno_1`

### 1.10 `GetTransformacija(s_sifobj, s_sifra, s_brnal, defnabavnacena)` → DOUBLE
**Nabavna cena iz transformacije** (prerada/proizvodnja).
- **Tabele**: `my_prernc_robno_2`

### 1.11 `GetTransformacijaReceptura(s_brnal, s_sifra, s_kolicina, s_mysifobj, s_sifobj, s_datum, s_condatddat)` → DOUBLE
**Obračun cene po recepturi** - iterira kroz materijale iz recepture i sabira cene.
- Prvo traži u `transfmatreceptcuv`, pa u `receptura` ako nema
- **Tabele**: `transfmatreceptcuv`, `receptura`
- **Poziva**: `avgPricePrerNC()`

### 1.12 `PrerNCPostojiTransformacija(s_brnal)` → BOOLEAN
**Proverava da li postoji transformacija** za dati broj naloga.
- **Tabele**: `my_prernc_robno_2`

### 1.13 `ZadNabPartner(psifobj, psifra, pdatum)` → DOUBLE
**Poslednja nabavna cena od partnera** (subject LIKE 'P-%').
- **Tabele**: `robno`

---

## 2. PDV I PORESKI OBRAČUN

### 2.1 `getpdv(mystopa, datum)` → DOUBLE(15,2)
**Vraća stopu PDV-a** za datu šifru stope i datum.
- **Tabele**: `opp.pdvstope` (iz šifarničke baze)

### 2.2 `getakciza(mystopa, datum)` → DOUBLE(15,6)
**Vraća iznos akcize** za datu šifru i datum.
- **Tabele**: `opp.tabakciza` (iz šifarničke baze)

### 2.3 `getizvor(brojevidencije, vrstadokumenta)` → VARCHAR(10)
**Generiše šifru izvora za PDV evidenciju** (POPDV obrazac).
- Mapira broj evidencije i vrstu dokumenta u format "X.Y.Z"
- Koristi se za popunjavanje POPDV obrasca

### 2.4 `getizvorbezodbitka(s)` → VARCHAR(10)
**Vraća šifru izvora za PDV bez prava odbitka** - dodaje ".x" sufiks.

### 2.5 `getizvoriname(izvor)` → VARCHAR(500)
**Vraća naziv izvora za PDV evidenciju** - mapira šifre u opise na srpskom.
- Pokriva sve kategorije POPDV obrasca (1.x, 2.x, 3.x, 4.x, 5.x)

### 2.6 `getUkupnoPrethodniPDV(mygodina, myperiod)` → DOUBLE
**Računa ukupan prethodni PDV** za godinu i period.
- Kompleksna kalkulacija koja sabira/oduzima PDV po svim izvorima
- **Tabele**: `eeppdv_promet`

### 2.7 `stornopopdvid(popdvid, ukupno, izvedeni)` → VARCHAR(10)
**Određuje POPDV kategoriju za storno dokument** - mapira originalni POPDV ID u odgovarajući storno ID.

### 2.8 `istiporpr(tromesecni, datpdv1, datpdv2)` → INT
**Proverava da li su dva datuma u istom poreskom periodu** (mesečnom ili tromesečnom).

### 2.9 `GetPeriod(porper, datum)` → INT
**Vraća poreski period** za datum (mesec ili kvartal 21-24).

---

## 3. FINANSIJSKO POSLOVANJE

### 3.1 `DaLiJeUAvansu(parkonto, parsifpar, nadan)` → INT
**Proverava da li partner ima avansno plaćanje** na datom kontu.
- Proverava operativne konte koji nisu avansi
- Gleda saldo u `finprom`
- **Tabele**: `tabrnoperative`, `tabrac`, `tabrnavansa`, `finprom`

### 3.2 `intufinansijskom(tipkljuca, statusdokumenta)` → BOOLEAN
**Da li je dokument proknjižen u finansijskom** - proverava bit 4 (vrednost 4) u statusu.

### 3.3 `intukep(tipkljuca, statusdokumenta)` → BOOLEAN
**Da li je dokument proknjižen u KEP knjizi** - proverava bit 8.

### 3.4 `intupdv(tipkljuca, statusdokumenta)` → BOOLEAN
**Da li je dokument proknjižen u PDV evidenciji** - proverava bitove 32 i 64.

### 3.5 `inturobnom(tipkljuca, statusdokumenta)` → BOOLEAN
**Da li je dokument proknjižen u robnom** - proverava bit 2.

### 3.6 `nadjiKonto(mysifra, pomPorez, jeProizvod, jeKomision, tipObjekta, datum)` → VARCHAR(20)
**Određuje konto za knjiženje** na osnovu tipa objekta, PDV stope, i da li je proizvod/komision.
- Kompleksna logika sa mnogo grana po tipu objekta (01-22)
- **Tabele**: `tabrac`, `artikli`
- **Poziva**: `getpdv()`

### 3.7 `getconvertvaluta(sifval1, sifval2, nadan)` → DOUBLE
**Konvertuje između valuta** koristeći srednji kurs.
- **Tabele**: `tmp_datkl`

---

## 4. KONTNI PLAN I PREVODI

### 4.1 `GetKplPrevod(racun, naziv)` → VARCHAR(255)
**Prevod naziva konta** u drugi kontni plan.
- **Tabele**: `opp.kplprevod`

### 4.2 `GetKplPrevodRacun(racun)` → VARCHAR(255)
**Prevod broja računa** u drugi kontni plan.
- **Tabele**: `opp.kplprevod`

---

## 5. LOKACIJE I MAGACIN

### 5.1 `getlokacija(so, sa)` → VARCHAR(50)
**Vraća lokaciju artikla** u objektu na osnovu poslednjeg prometa.
- Kreira temp tabelu, analizira poslednje transakcije
- **Tabele**: `lokpromet`, temp `tmp_lok_1`

### 5.2 `TrebStanje(so, sa, BrojTrebovanja, sifdob, redbr, maxrbrst)` → DOUBLE
**Raspoloživo stanje za trebovanje** = stanje - rezervacije - neprokkasa - refobjst - druga trebovanja.
- **Tabele**: `trstanje`, `tbltrebovanje`

---

## 6. POMOĆNE / UTILITY FUNKCIJE

### 6.1 `GetSrbDayOfWeek(dt)` → VARCHAR(255)
**Srpski naziv dana u nedelji** (Ponedeljak, Utorak...).

### 6.2 `GetSrbMonth(dt)` → VARCHAR(255)
**Srpski naziv meseca** (Januar, Februar...).

### 6.3 `GetSrbQuarter(dt)` → VARCHAR(255)
**Srpski kvartal** u formatu "2025 I kv.".

### 6.4 `GetYM(dt)` → VARCHAR(255)
**Mesec.Godina** u formatu "03.26".

### 6.5 `MyDayOfWeek(dt)` → INT
**Dan u nedelji** (1=Ponedeljak, 7=Nedelja) - ISO format.

### 6.6 `GetOsnovniBrnal(mybrnal)` → VARCHAR(50)
**Osnovni broj naloga** - uklanja sufiks posle "/" (npr. "KR-001/1" → "KR-001").

### 6.7 `getosrn(rnnabvr, osstatus)` → VARCHAR(10)
**Vraća radni nalog za osnovna sredstva** - mapira nabavni RN u RN pripreme.
- **Tabele**: `ostabrn`

### 6.8 `nazivppz(tip, vrednost, tipvrednost)` → VARCHAR(255)
**Formatira vrednost po tipu polja** - tekst, broj, datum, DA/NE, lista.

---

## 7. E-OTPREMNICE / E-DOKUMENTI

### 7.1 `eo_get_max_document_id(doc_type)` → BIGINT
**Maksimalni ID dokumenta** za e-otpremnice ili e-prijemnice.
- Proverava sve povezane tabele (stavke, atributi, prevoznici, prilozi)
- **Tabele**: `eo_otpremnice*`, `eo_prijemnice*`

---

## 8. ARHIVIRANJE

### 8.1 `GetArchiveParentUID(in_UID)` → VARCHAR(100)
**Traži roditeljski UUID arhivske lokacije** sa AK=1 (arhivska kutija).
- Rekurzivno prati ParentUUID do kutije
- **Tabele**: `opp.arh_locations`

---

## 9. ARTIKLI I PREVODI

### 9.1 `getPrevodArtikla(SifraArtikla, SifraDrzave)` → VARCHAR(255)
**Prevod naziva artikla** za stranu državu.
- **Tabele**: `artikliprevod`, `artikli`

---

## Sumarni pregled korišćenih tabela

| Tabela | Koristi je funkcija |
|--------|-------------------|
| `robno` | avgPrice, lastPrice, lastPriceNCP, ZadNabPartner |
| `my_prernc_robno` | avgPricePrerNC, lastPricePrerNC |
| `my_prernc_robno_1` | GetNovaPrerCena |
| `my_prernc_robno_2` | GetTransformacija, PrerNCPostojiTransformacija |
| `finprom` | DaLiJeUAvansu |
| `tabrac` | DaLiJeUAvansu, nadjiKonto |
| `tabrnoperative` | DaLiJeUAvansu |
| `tabrnavansa` | DaLiJeUAvansu |
| `artikli` | obrNabavke, nadjiKonto, getPrevodArtikla |
| `artikliprevod` | getPrevodArtikla |
| `trstanje` | TrebStanje |
| `tbltrebovanje` | TrebStanje |
| `lokpromet` | getlokacija |
| `eeppdv_promet` | getUkupnoPrethodniPDV |
| `transfmatreceptcuv` | GetTransformacijaReceptura |
| `receptura` | GetTransformacijaReceptura |
| `ostabrn` | getosrn |
| `tmp_datkl` | getconvertvaluta |
| `opp.pdvstope` | getpdv |
| `opp.tabakciza` | getakciza |
| `opp.kplprevod` | GetKplPrevod, GetKplPrevodRacun |
| `opp.arh_locations` | GetArchiveParentUID |
| `eo_otpremnice*` | eo_get_max_document_id |
| `eo_prijemnice*` | eo_get_max_document_id |
