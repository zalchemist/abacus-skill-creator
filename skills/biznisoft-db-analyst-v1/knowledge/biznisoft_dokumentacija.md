# BizniSoft ERP Dokumentacija

## Pregled

BizniSoft je sveobuhvatni ERP sistem namenjen malim, srednjim i velikim preduzećima u Srbiji. Aplikacija je Windows client/server arhitekture, optimizovana za visoke transakcione volumene - od POS sistema do velikih distribuiranih okruženja i računovodstvenih agencija.

---

## 1. Glavni Moduli Softvera

### 1.1 Robno-Trgovinsko Poslovanje
Modul obuhvata sva knjigovodstvena rešenja vezana za kretanje robe i usluga.

**Podržani poslovni objekti:**
- Maloprodaja
- Veleprodaja  
- Roba data/primljena u komision (maloprodaja i veleprodaja)
- Magacin robe po prosečnim cenama
- Magacin repromaterijala
- Magacin gotovih proizvoda i poluproizvoda
- Proizvodna jedinica

**Glavne funkcije:**
- Kalkulacije (trgovačka roba, komisiona roba, uvozna kalkulacija, otkup poljoprivrednih proizvoda)
- Izlazne fakture (domaće i devizne)
- Otpremnice
- Avansni računi i profakture
- Nivelacije cena
- Popis robe
- Povraćaj robe (kupcu i dobavljaču)
- Interni prenos robe između objekata

### 1.2 Finansijsko Poslovanje
Centralizuje unos, obradu i knjiženje svih računovodstvenih promena.

**Glavne funkcije:**
- Kontni plan firme (analitički i sintetički računi)
- Obrada naloga za glavnu knjigu
- Devizno poslovanje (izvodi, kursne razlike)
- Računi troškova
- Finansijski izveštaji (Bilans stanja, Bilans uspeha)
- PK-1 i KPO knjige

**Statusi dokumenata:**
1. **U obradi** - dokument se može menjati
2. **Konfirmisan/Potvrđen** - spreman za knjiženje
3. **Proknjižen** - završen, utiče na izveštaje

### 1.3 Finansijska Operativa
Prati detaljnu analitiku odnosa sa kupcima i dobavljačima.

**Funkcije:**
- Izvod otvorenih stavki (IOS)
- Obračun kamate
- Predlog za kompenzaciju
- Unos i štampa virmana
- Praćenje valuta plaćanja i dinamike

### 1.4 Proizvodnja
Upravlja proizvodnim procesima.

**Ključne funkcije:**
- Radni nalozi (pojedinačni i grupni)
- Recepture proizvoda (normativi)
- Izdatnica materijala
- Prijem proizvoda/poluproizvoda
- Obračun cene koštanja (stvarna ili planska)
- Unos obavljenog posla

**Tipovi proizvodnje:**
- Sa recepturom (predefinisane norme)
- Bez recepture (ad-hoc proizvodnja)

### 1.5 Obračun Zarada
Kompletan obračun plata, poreza i doprinosa.

**Komponente:**
- Matična knjiga radnika
- Stope poreza i doprinosa po kategorijama
- Vrste plaćanja (redovan rad, topli obrok, regres, bolovanje...)
- Obustave na procenat i rate
- Beneficirani radni staž
- Automatsko knjiženje u glavnu knjigu

### 1.6 Ostali Moduli
- **Stalna sredstva i inventar** - evidencija osnovnih sredstava
- **PDV evidencija** - ZPPPDV forma, usklađivanje PDV-a
- **eFakture i SEF** - elektronske fakture prema SEF sistemu
- **Upravljanje kadrovima** - HR modul
- **Administracija** - upravljanje godinama, licencama, arhiviranje
- **Integraciona rešenja** - WebService, mobilne aplikacije

---

## 2. Ključni Šifarnici

### 2.1 Šifarnik Artikala
Jedinstven na nivou cele firme. Omogućava pregled statusa, cena i rezervacija po svim objektima.

**Osnovni podaci artikla:**
- Šifra artikla
- Naziv
- Jedinica mere
- Poreska stopa (S0-0%, S1-20%, S2-10%)
- Tarifa (0-bez PDV, 1-sa PDV, 9-usluge)
- Barkod, kataloški broj
- Grupa artikla
- Karakter artikla (roba, usluga, proizvod, sirovina, ambalaža, komisiona roba)

**Za proizvode:**
- Planska cena
- VP cena (veleprodajna)
- Receptura (normativ materijala)

### 2.2 Šifarnik Poslovnih Partnera
Upravlja kupcima i dobavljačima.

**Tipovi:**
- Pravno lice
- Preduzetnik
- Fizičko lice
- Strano pravno lice
- Poljoprivredni proizvođač

**Podaci:**
- Šifra, naziv, adresa
- PIB, matični broj
- PDV obveznik (Da/Ne)
- Tekući računi
- Povezivanje sa NBS web servisom za automatsko preuzimanje podataka

### 2.3 Kontni Plan
Definiše računovodstvenu strukturu.

**Karakteristike računa:**
- Broj konta i naziv
- Analitika (partneri, objekti, zaposleni, bez analitike)
- Devizni račun (DEV oznaka)
- Mesto troška i nosioci troškova
- Zatvaranje (za konta koja se zatvaraju)

### 2.4 Ostali Šifarnici
- **Tabela poreskih stopa** - usklađena sa ESIR zahtevima
- **Kursna lista** - preuzimanje sa NBS-a
- **Šifarnik banaka-kreditora** - za obračun zarada
- **Šifarnik radnih operacija** - za proizvodnju
- **Tabela kamatnih stopa** - za finansijsku operativu
- **Fond časova po mesecima** - za obračun zarada

---

## 3. Tokovi Dokumenata

### 3.1 Kalkulacija Trgovačke Robe
**Tok:** Kreiranje (F5) → Unos zaglavlja (datum, dobavljač, dokument) → Unos stavki (artikal, količina, cena, rabat, marža) → Štampa → Knjiženje (F3)

**Automatska knjiženja:**
- Finansijsko (glavna knjiga)
- Robno (kartice robe)
- KEP knjiga
- PDV evidencija

### 3.2 Izlazna Faktura
**Tok:** Kreiranje → Unos kupca → Stavke → Potvrđivanje (F11) → Knjiženje (F3)

**V12 novine:**
- Potvrđivanje dokumenta (F11) pre knjiženja
- Storniranje knjiženja vraća dokument u obradu
- Simulacija knjiženja (Shift+F3)

### 3.3 Radni Nalog (Proizvodnja)
**Tok:** Kreiranje RN → Izdatnica materijala → Unos obavljenog posla → Prijem proizvoda → Obračun cene koštanja → Knjiženje

**Automatsko formiranje:**
- Može se generisati iz izlazne fakture za dopunu zaliha

### 3.4 Obračun Zarade
**Tok:** Ažuriranje minulog rada → Formiranje naloga → Unos časova/vrsta primanja → Obračun → Štampa → Knjiženje → PPP-PO prijava

### 3.5 Obrada Izvoda
**Tok:** Import XML/TXT iz e-bankinga → Automatsko knjiženje na osnovu pravila → Potvrđivanje → Proknjižavanje

---

## 4. Povezivanje Podataka Između Modula

### 4.1 Robno ↔ Finansijsko
- Kalkulacije, fakture i nivelacije automatski generišu naloge za glavnu knjigu
- Koriste se definisana konta iz kontnog plana
- Partner iz šifarnika se koristi za analitiku

### 4.2 Proizvodnja ↔ Robno
- Receptura koristi artikle iz šifarnika
- Izdatnica materijala umanjuje zalihe u magacinu sirovina
- Prijem proizvoda povećava zalihe u magacinu gotovih proizvoda
- Cena koštanja se prenosi u robno poslovanje

### 4.3 Zarade ↔ Finansijsko
- Obračun zarada automatski kreira nalog za glavnu knjigu
- Koriste se konta definisana u specifikaciji računa za GL
- Obustave se povezuju sa šifarnikom banaka-kreditora

### 4.4 Zarade ↔ Kadrovi
- Matična knjiga radnika može se importovati u HR modul
- Podaci se sinhronizuju između modula

### 4.5 Finansijska Operativa ↔ Finansijsko
- IOS koristi stavke iz glavne knjige po partnerima
- Kompenzacije zatvaraju stavke u finansijskom
- Virmani se formiraju na osnovu obaveza

---

## 5. Struktura Baze i Logika Podataka

### 5.1 Opšte Karakteristike
- **Tip baze:** Operativno-transakciona (OLTP)
- **Broj tabela:** 644 (u konkretnoj bazi opp7102025)
- **Foreign Keys:** Nema eksplicitnih FK veza - relacije su implicitne

### 5.2 Ključna Polja za Povezivanje
Na osnovu logike aplikacije, pretpostavljene veze:

| Entitet | Verovatno polje | Povezuje sa |
|---------|-----------------|-------------|
| Partner | Šifra partnera | Fakture, Kalkulacije, IOS |
| Artikal | Šifra artikla | Stavke dokumenata, Recepture |
| Konto | Broj konta | Nalozi za GK, Specifikacije |
| Objekat | Šifra objekta | Robno poslovanje, Zalihe |
| Radnik | Šifra radnika | Zarade, Kadrovi |
| Dokument | Broj dokumenta, Tip, Godina | Stavke, Knjiženja |

### 5.3 Statusna Polja
Dokumenti imaju status polja:
- **1** - U obradi
- **2** - Potvrđen/Konfirmisan
- **9** - Proknjižen
- **Storniran** - posebna oznaka za poništene

### 5.4 Vremenske Dimenzije
- **Godina** - često deo kompozitnog ključa
- **Period** - mesec za izveštaje
- **Datum knjiženja** - određuje kada stavka ulazi u izveštaje

### 5.5 Implikacije za Integritet
Bez eksplicitnih FK veza potrebno je proveriti:
- Šifre partnera u transakcijama vs. šifarnik
- Šifre artikala u stavkama vs. šifarnik
- Konta u knjiženjima vs. kontni plan
- Konzistentnost statusa između zaglavlja i stavki
- Numeričku konzistentnost (saldo = promet duguje - promet potražuje)

---

## 6. Napomene za Analizu Baze

### 6.1 Prioritetni Šifarnici za Pregled
1. Artikli (status, klasifikacija)
2. Partneri (validnost PIB, adresa)
3. Kontni plan (struktura, analitika)
4. Objekti (tipovi, aktivnost)

### 6.2 Kritične Tabele za Integritet
1. Glavni nalozi (saldo mora biti 0)
2. Robne kartice (ulaz - izlaz = stanje)
3. Kalkulacije (nabavna + marža = prodajna)
4. Zalihe (popisna vs. knjigovodstvena)

### 6.3 Tipične Provere
- Orphan records (stavke bez zaglavlja)
- Duplikati u šifarnicima
- Neaktivni entiteti u transakcijama
- Neusklađenost datuma (faktura pre kalkulacije)
- Negativne zalihe

---

## Izvori

- https://www.biznisoft.com/podrska
- https://www.biznisoft.com/wp-content/uploads/2024/10/uputstvo-BS-uvod.pdf
- https://www.biznisoft.com/wp-content/uploads/2024/10/uputstvo-BS-robno.pdf
- https://www.biznisoft.com/wp-content/uploads/2024/10/uputstvo-BS-finan.pdf
- https://www.biznisoft.com/wp-content/uploads/2024/10/uputstvo-BS-finop.pdf
- https://www.biznisoft.com/wp-content/uploads/2024/10/uputstvo-BS-obracun-zarada.pdf
- https://www.biznisoft.com/wp-content/uploads/2024/10/BIZNISOFT-PROIZVODNJA-PO-CENI-KOSTANJA.pdf
- https://www.biznisoft.com/biznisoft-novosti/biznisoft-v12
