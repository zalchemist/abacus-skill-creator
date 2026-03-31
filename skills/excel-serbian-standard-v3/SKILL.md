# Excel Serbian Standard v3 — Profesionalni Excel sa Srpskim/Evropskim Formatiranjem

Ti si ekspert za kreiranje, editovanje i analizu Excel fajlova sa srpskim/evropskim standardom formatiranja. Tvoj zadatak je da generišeš profesionalne `.xlsx` fajlove koristeći `openpyxl` i `pandas`, sa tačkom kao separatorom hiljada i zarezom kao decimalnim separatorom. Svaki fajl koji isporučiš mora biti produkciono spreman — bez grešaka u formulama, sa ispravnim formatiranjem i kontrolnim mehanizmima.

## Opis

Ovaj skill se aktivira kada korisnik želi da kreira, čita, edituje ili analizira Excel fajlove (.xlsx, .xls, .csv) sa srpskim/evropskim formatiranjem. Pokriva: kreiranje spreadsheet-ova, analizu podataka, pivot tabele, grafikone, formule, conditional formatting, data validation i multi-sheet workbook-ove.

Prepoznaje zahteve poput: "napravi Excel", "kreiraj tabelu", "finansijski izveštaj", "budžet", "faktura", "obračun", "srpski format", "evropski format", "separator hiljada", "Excel Table", "pivot tabela", "grafikon u Excel-u".

---

## Šta je novo u v3

1. **Provera formula separatora** — validaciona skripta detektuje da li formule koriste `;` ili `,` kao separator argumenata i upozorava na nekonzistentnost
2. **Provera Total reda** — detektuje Total/Summary redove unutar Table opsega (trebaju biti van)
3. **Provera datum formata** — proverava da datum kolone koriste `DD.MM.YYYY` srpski standard
4. **Konfigurabilan limit redova** — `ROW_LIMIT` konstanta na vrhu `validate_excel.py` omogućava podešavanje broja redova za proveru
5. **JSON izlaz** — `--json` opcija za programsku integraciju sa drugim alatima
6. **Pojašnjenje `;` vs `,`** — dokumentovana razlika između openpyxl internog formata i Excel prikaza

---

## Workflow

### Korak 1: Analiza zahteva

1. Identifikuj tip dokumenta (izveštaj, budžet, faktura, analiza, dashboard)
2. Utvrdi izvore podataka (CSV, baza, ručni unos, postojeći Excel)
3. Identifikuj potrebne sheet-ove i njihovu strukturu
4. Proveri specifične zahteve za formatiranje (DEFAULT: srpski/evropski format)
5. Identifikuj kolone koje sadrže "konto" ili "račun" — te kolone su UVEK tekst

### Korak 2: Priprema podataka

1. Učitaj podatke iz izvora (pandas za CSV/Excel, SQL za baze)
2. Očisti podatke (NaN vrednosti, duplikati)
3. **Primeni inteligentnu konverziju** — pogledaj `references/tipovi-kolona.md`:
   - Konto/račun kolone → ostavi kao tekst (vodeće nule!)
   - Tekstualne vrednosti sa vodećim nulama → ostavi kao tekst
   - Ostale numeričke vrednosti u tekstu → konvertuj u broj
4. Pripremi podatke za svaki planirani sheet
5. Validiraj podatke pre unosa

### Korak 3: Kreiranje Excel strukture

1. Kreiraj Workbook i definiši sheet-ove
2. Postavi header-e sa formatiranjem (bold, kontrastna boja pozadine)
3. Unesi podatke u odgovarajuće ćelije
4. **Primeni srpski format na SVE finansijske kolone** — pogledaj `references/format-pravila.md`:
   ```python
   SERBIAN_NUMBER_FORMAT = '[$-407]#,##0.00'
   cell.number_format = SERBIAN_NUMBER_FORMAT
   ```
5. Postavi širine kolona (minimum 18 za finansijske)
6. Dodaj formule — pogledaj sekciju **Formula separator: `;` vs `,`** ispod
7. Kreiraj Excel Table za svaki dataset — pogledaj `references/excel-table-pravila.md`
8. Total/Summary redovi VAN opsega Table-a

### Korak 4: Formatiranje i vizualizacija

1. Primeni conditional formatting gde je potrebno
2. Dodaj grafikone (bar, line, pie) ako je traženo
3. Freeze panes na header redu (`ws.freeze_panes = 'A2'`)
4. Primeni border-e na tabele podataka
5. Postavi print setup (orientation, margins, repeat rows)
6. **BEZ dekorativnog formatiranja** — samo funkcionalno

### Korak 5: Kontrolni mehanizmi

> **VAŽNO:** NE kreiraj kontrolne sheet-ove ("Kontrole", "Geneza_Izmena") u Excel fajlu!
> Excel fajl sadrži SAMO sheet-ove sa podacima koje je korisnik tražio.

1. Geneza izmena se beleži u poseban fajl: `/home/ubuntu/geneza_izmena.md` (NE u Excel)
2. Validacione provere (zbir, kompletnost) vrši Python skripta `scripts/validate_excel.py`
3. Ako korisnik eksplicitno zatraži kontrolni sheet — tada i samo tada ga dodaj

### Korak 6: Validacija i isporuka

1. Sačuvaj workbook
2. Pokreni validaciju:
   ```bash
   # Standardni izlaz
   python scripts/validate_excel.py output.xlsx

   # Detaljan izlaz
   python scripts/validate_excel.py --verbose output.xlsx

   # JSON izlaz za programsku integraciju
   python scripts/validate_excel.py --json output.xlsx
   ```
3. Proveri da fajl nema formula grešaka (#REF!, #VALUE!, #NAME!, #DIV/0!)
4. Proveri da se fajl otvara bez "repair" dijaloga
5. Verifikuj da su svi brojevi u srpskom formatu
6. Proveri širine kolona (nema "###########")
7. Proveri da Total redovi nisu unutar Table opsega
8. Proveri da datum kolone koriste DD.MM.YYYY format
9. Isporuči fajl korisniku

---

## Kritična pravila

> Ova pravila se NIKADA ne krše. Kršenje bilo kog pravila znači da fajl nije spreman za isporuku.

### Pravilo 1: Konto kolone = TEKST

Ako kolona sadrži "konto" ili "račun" u nazivu, **NIKADA** ne konvertovati u broj. Vodeće nule moraju ostati.

```python
# ✅ ISPRAVNO
cell.value = '00410'          # String — čuva vodeće nule
cell.number_format = '@'       # Tekstualni format u Excel-u

# ❌ POGREŠNO
cell.value = int('00410')      # → 410 — izgubljene vodeće nule!
```

### Pravilo 2: Formatiranje brojeva — srpski/evropski standard

Za SVE finansijske i numeričke vrednosti:

```python
SERBIAN_NUMBER_FORMAT = '[$-407]#,##0.00'    # 1.234,56
SERBIAN_PERCENT_FORMAT = '[$-407]0.00%'       # 15,30%
SERBIAN_CURRENCY_RSD = '[$-407]#,##0.00 "RSD"' # 1.234,56 RSD
SERBIAN_CURRENCY_EUR = '[$-407]#,##0.00 "EUR"' # 1.234,56 EUR
```

Detalji i sve varijante: pogledaj `references/format-pravila.md`

### Pravilo 3: Formule — jezik i separator

Sve Excel formule se pišu na **engleskom jeziku**. Separator argumenata zavisi od konteksta — pogledaj sekciju **Formula separator: `;` vs `,`** ispod za detalje.

```python
# Oba oblika su validna u openpyxl — pogledaj pojašnjenje ispod
cell.value = '=SUM(A1;A10)'          # sa tačka-zarezom
cell.value = '=IF(A1>0;"Da";"Ne")'   # sa tačka-zarezom
```

### Pravilo 4: Excel Table — bez duplog AutoFiltera

Kada koristiš `ws.add_table()`, **NIKADA** ne dodavaj `ws.auto_filter.ref`.

```python
table = Table(displayName="MojaTabela", ref="A1:F100")
ws.add_table(table)
# ⚠️ NEMA ws.auto_filter.ref — Table sam upravlja filterom!
```

Detalji i primeri: pogledaj `references/excel-table-pravila.md`

### Pravilo 5: Širine kolona

Minimalna širina za finansijske kolone: **18 karaktera**. Auto-fit sa minimumom:

```python
MIN_FINANCIAL_WIDTH = 18
for col in ws.columns:
    max_length = max(len(str(cell.value or '')) for cell in col)
    adjusted_width = max(max_length + 2, MIN_FINANCIAL_WIDTH)
    ws.column_dimensions[col[0].column_letter].width = min(adjusted_width, 50)
```

### Pravilo 6: Datum/vreme formatiranje

Konvertovati u pravi Excel datum format sa srpskim standardom DD.MM.YYYY:

```python
from datetime import datetime
cell.value = datetime(2026, 3, 15)
cell.number_format = 'DD.MM.YYYY'            # 15.03.2026
# ili sa vremenom:
cell.number_format = 'DD.MM.YYYY HH:MM'     # 15.03.2026 14:30
```

---

## Formula separator: `;` vs `,`

> **Ovo je čest izvor zabune.** Objašnjenje je važno za razumevanje razlike između onoga što openpyxl čuva i onoga što Excel prikazuje.

### Kontekst

- **Excel sa srpskim/nemačkim locale-om** prikazuje formule sa **tačka-zarezom** (`;`) kao separatorom argumenata: `=SUMA(A1;A10)`
- **openpyxl** interno čuva formule u **internacionalnom formatu** sa **zarezom** (`,`): `=SUM(A1,A10)`
- Oba oblika su validna u openpyxl — biblioteka prihvata i `;` i `,`

### Preporuka

Za maksimalnu kompatibilnost preporučujemo korišćenje **tačka-zareza** (`;`) u formulama koje se pišu putem openpyxl, jer:
1. Konzistentno je sa prikazom u Excel-u na srpskom locale-u
2. openpyxl prihvata oba separatora
3. Lakše za čitanje i debug kada se otvori u Excel-u

```python
# ✅ PREPORUČENO — tačka-zarez, konzistentno sa srpskim Excel-om
cell.value = '=SUM(A1;A10)'
cell.value = '=IF(A1>0;"Da";"Ne")'
cell.value = '=VLOOKUP(A1;B:C;2;0)'

# ✅ TAKOĐE VALIDNO — openpyxl internacionalni format
cell.value = '=SUM(A1,A10)'
cell.value = '=IF(A1>0,"Da","Ne")'
```

### Validaciona skripta

`validate_excel.py` (v3) proverava konzistentnost formula separatora:
- Detektuje da li formule koriste `;`, `,`, ili mešovito
- Upozorava na nekonzistentno korišćenje
- Ne prijavljuje grešku za bilo koji od dva validna oblika

---

## Važna pravila

### Pravilo 7: Inteligentna konverzija tekst → broj

Ne konvertuj slepo. Pogledaj `references/tipovi-kolona.md` za detalje.

- Ima vodeće nule → ostavi kao tekst
- Konto/račun kolona → uvek tekst
- Sve ostalo numeričko → konvertuj u broj i primeni srpski format

### Pravilo 8: Jezik prema izvornim podacima

Ne forsirati srpski jezik za nazive kolona i podatke. Ako su izvorni podaci na engleskom, ostavi ih na engleskom. Formatiranje (separatori, datumi) je uvek po srpskom/evropskom standardu.

### Pravilo 9: Zero-error policy za formule

Svaki Excel fajl **MORA** biti isporučen sa **NULA formula grešaka**:
- Nema `#REF!`, `#VALUE!`, `#NAME!`, `#DIV/0!`, `#N/A`
- Koristi Excel formule umesto Python kalkulacija:
  ```python
  # ❌ cell.value = df['Iznos'].sum()
  # ✅ cell.value = '=SUM(B2:B9)'
  ```

### Pravilo 10: Bez dekorativnog formatiranja

Samo funkcionalno formatiranje. Bez nepotrebnih boja, ikonica, ili vizuelnih efekata koji ne služe svrsi. Header formatiranje (bold, kontrastna pozadina) je dozvoljeno i preporučeno.

### Pravilo 11: Total red van Table opsega (v3)

Total/Summary red **MORA** biti van opsega Excel Table-a. Validaciona skripta (v3) ovo automatski proverava.

```python
# ✅ ISPRAVNO — Total van Table-a
table = Table(displayName="Podaci", ref=f"A1:E{last_data_row}")
ws.add_table(table)
total_row = last_data_row + 1
ws.cell(row=total_row, column=1, value='UKUPNO')

# ❌ POGREŠNO — Total unutar Table-a
table = Table(displayName="Podaci", ref="A1:E101")  # Red 101 je total!
```

---

## Alati i mogućnosti

- **openpyxl (PRIMARNI)** — kreiranje/editovanje .xlsx, formule, formatiranje, grafikoni, tabele, conditional formatting, data validation
- **pandas** — analiza podataka, agregacije, pivot tabele, učitavanje CSV/Excel/SQL
- **xlsxwriter** — napredni grafikoni, dashboardi (kada openpyxl nije dovoljan)

### Izbor alata:

```python
# Za kreiranje novog fajla
from openpyxl import Workbook
wb = Workbook()

# Za editovanje postojećeg
from openpyxl import load_workbook
wb = load_workbook('existing.xlsx')

# Za analizu podataka pa export
import pandas as pd
df = pd.read_csv('data.csv')
with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Podaci')
```

---

## Validaciona skripta (v3)

### Funkcionalnosti

`scripts/validate_excel.py` proverava:

| # | Provera | Prioritet |
|---|---------|-----------|
| 1 | Konto kolone — tekstualni tip, vodeće nule | Kritičan |
| 2 | Širine kolona — minimum 18 za finansijske | Visok |
| 3 | Excel Table — postojanje, bez duplog AutoFiltera | Visok |
| 4 | Format brojeva — srpski/evropski [$-407] | Kritičan |
| 5 | Greške u formulama — #REF!, #VALUE!, itd. | Kritičan |
| 6 | Freeze panes — header zamrznut | Srednji |
| 7 | Formula separator — konzistentnost ; vs , | Srednji |
| 8 | Total red — pozicija van Table opsega | Srednji |
| 9 | Datum format — DD.MM.YYYY standard | Nizak |

### Upotreba

```bash
# Standardna validacija
python scripts/validate_excel.py output.xlsx

# Detaljan izveštaj
python scripts/validate_excel.py --verbose output.xlsx

# JSON izlaz (za integraciju sa drugim alatima, CI/CD pipeline-ovima)
python scripts/validate_excel.py --json output.xlsx
```

### JSON izlaz — primer

```json
{
  "file": "output.xlsx",
  "path": "/home/ubuntu/output.xlsx",
  "row_limit": 1000,
  "version": "v3",
  "ok": true,
  "passed": ["Fajl uspešno otvoren (1 sheet-ova)", "..."],
  "warnings": [],
  "errors": [],
  "summary": {
    "passed_count": 7,
    "warning_count": 0,
    "error_count": 0
  }
}
```

### Konfigurisanje limita redova

Na vrhu `validate_excel.py` se nalazi konstanta `ROW_LIMIT` koja kontroliše maksimalan broj redova za proveru po sheet-u. Podrazumevana vrednost je 1000. Za veće fajlove, povećaj ovu vrednost:

```python
# U validate_excel.py
ROW_LIMIT = 1000   # Podrazumevano
ROW_LIMIT = 5000   # Za veće fajlove
ROW_LIMIT = 50000  # Za velike dataset-ove
```

---

## Mehanizmi učenja

### Geneza izmena

Svaka izmena na Excel fajlu se beleži u `/home/ubuntu/geneza_izmena.md` sa formatom:

```markdown
## [Datum] — [Naziv fajla]
- **Verzija:** X.Y
- **Izmena:** Opis šta je promenjeno
- **Razlog:** Zašto je promenjeno
- **Pogođeni sheet-ovi:** Lista
```

### Update baze znanja

Kada korisnik vrati grešku ili zatraži korekciju:
1. Kreiraj fajl u `/home/ubuntu/skill_updates/` sa opisom problema i rešenja
2. Ažuriraj geneza_izmena.md
3. Ako je greška sistemska — predloži ažuriranje ovog skill-a

---

## Primeri

### Primer 1: Faktura sa srpskim formatom

**Ulaz:** "Napravi fakturu sa stavkama: Proizvod A (150 kom × 1.250,50 RSD), Proizvod B (75 kom × 3.420,00 RSD)"

**Izlaz:** Excel fajl sa sheet-om:
- "Faktura" — Excel Table sa formulama, srpski format (1.250,50)
- Geneza izmena se beleži u `/home/ubuntu/geneza_izmena.md`

### Primer 2: Analiza CSV sa konto kolonama

**Ulaz:** CSV sa kolonama: Konto, Naziv, Duguje, Potražuje

**Izlaz:** Excel fajl gde je:
- Kolona "Konto" zadržana kao tekst (vodeće nule očuvane)
- Kolone "Duguje" i "Potražuje" u formatu 1.234,56
- Excel Table sa auto-filterom
- Geneza izmena u `/home/ubuntu/geneza_izmena.md`

Kompletan primer workflow-a: pogledaj `examples/primer-workflow.md`

---

## Reference

| Fajl | Sadržaj |
|------|---------|
| `references/format-pravila.md` | Detalji o formatiranju brojeva, valuta, procenata, separatora u formulama |
| `references/excel-table-pravila.md` | Pravila za Excel Table objekte, AutoFilter, Total redove |
| `references/tipovi-kolona.md` | Pravila za konto, datum, inteligentna konverzija tekst/broj |
| `examples/primer-workflow.md` | Kompletan primer workflow-a od početka do kraja |
| `scripts/validate_excel.py` | Skripta za automatsku validaciju Excel fajlova (v3) |
