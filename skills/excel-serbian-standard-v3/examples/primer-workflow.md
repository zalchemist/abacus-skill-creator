# Primer kompletnog workflow-a — Faktura iz CSV podataka

## Scenario

Korisnik uploaduje CSV fajl sa stavkama fakture i traži profesionalan Excel.

## Ulazni podaci (CSV)

```csv
Konto,Naziv stavke,Količina,Jedinična cena,Napomena
00410,Nematerijalna imovina,1,125000.50,Godišnja amortizacija
0200,Zemljište parcela 1,1,3500000.00,Procena 2026
1020,Sirovine - čelik,500,1250.75,Magacin A
1021,Sirovine - aluminijum,200,3420.00,Magacin B
4100,Troškovi materijala,1,890000.25,Q1 2026
```

## Korak 1: Analiza zahteva

- Tip: Faktura/finansijski pregled
- Izvor: CSV fajl
- Kolona "Konto" — sadrži vodeće nule → TEKST
- Kolone "Količina", "Jedinična cena" — numeričke → srpski format
- Potreban total red
- Geneza izmena → beleži se u `/home/ubuntu/geneza_izmena.md`

## Korak 2: Priprema podataka

```python
import pandas as pd

df = pd.read_csv('faktura.csv', dtype={'Konto': str})  # Konto kao string!
print(df.head())
print(df.dtypes)
```

**Važno:** `dtype={'Konto': str}` — sprečava pandas da konvertuje konto u broj.

## Korak 3: Kreiranje Excel strukture

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.table import Table, TableStyleInfo
from datetime import datetime

SERBIAN_NUMBER_FORMAT = '[$-407]#,##0.00'
MIN_FINANCIAL_WIDTH = 18

wb = Workbook()
ws = wb.active
ws.title = "Faktura"

# Header
headers = ['Konto', 'Naziv stavke', 'Količina', 'Jedinična cena', 'Ukupno', 'Napomena']
ws.append(headers)

# Stilovi
header_font = Font(name='Calibri', size=11, bold=True, color='FFFFFF')
header_fill = PatternFill(start_color='2c3e50', end_color='2c3e50', fill_type='solid')
header_align = Alignment(horizontal='center', vertical='center')

for cell in ws[1]:
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = header_align

# Podaci
for idx, row in df.iterrows():
    row_num = idx + 2
    # Konto — TEKST
    cell_konto = ws.cell(row=row_num, column=1, value=str(row['Konto']))
    cell_konto.number_format = '@'

    ws.cell(row=row_num, column=2, value=row['Naziv stavke'])

    # Količina — broj
    ws.cell(row=row_num, column=3, value=float(row['Količina']))
    ws.cell(row=row_num, column=3).number_format = SERBIAN_NUMBER_FORMAT

    # Jedinična cena — broj
    ws.cell(row=row_num, column=4, value=float(row['Jedinična cena']))
    ws.cell(row=row_num, column=4).number_format = SERBIAN_NUMBER_FORMAT

    # Ukupno — FORMULA
    ws.cell(row=row_num, column=5, value=f'=C{row_num}*D{row_num}')
    ws.cell(row=row_num, column=5).number_format = SERBIAN_NUMBER_FORMAT

    ws.cell(row=row_num, column=6, value=row['Napomena'])

last_data_row = len(df) + 1

# Excel Table — BEZ duplog AutoFiltera
table = Table(displayName="TabelaFaktura", ref=f"A1:F{last_data_row}")
table.tableStyleInfo = TableStyleInfo(
    name="TableStyleMedium9",
    showFirstColumn=False,
    showLastColumn=False,
    showRowStripes=True,
    showColumnStripes=False
)
ws.add_table(table)
# ⚠️ NEMA ws.auto_filter.ref!

# Total red VAN Table-a
total_row = last_data_row + 1
ws.cell(row=total_row, column=2, value='UKUPNO').font = Font(bold=True)
ws.cell(row=total_row, column=5, value=f'=SUM(E2:E{last_data_row})')
ws.cell(row=total_row, column=5).number_format = SERBIAN_NUMBER_FORMAT
ws.cell(row=total_row, column=5).font = Font(bold=True)
```

## Korak 4: Formatiranje

```python
# Širine kolona
ws.column_dimensions['A'].width = 12      # Konto
ws.column_dimensions['B'].width = 30      # Naziv
ws.column_dimensions['C'].width = MIN_FINANCIAL_WIDTH  # Količina
ws.column_dimensions['D'].width = MIN_FINANCIAL_WIDTH  # Jed. cena
ws.column_dimensions['E'].width = 20      # Ukupno
ws.column_dimensions['F'].width = 30      # Napomena

# Freeze
ws.freeze_panes = 'A2'
```

## Korak 5: Kontrolni mehanizmi

> **VAŽNO:** NE kreiraj kontrolne sheet-ove u Excel fajlu!
> Geneza izmena se beleži u poseban fajl.

```python
# Geneza izmena — beleži se u poseban fajl, NE u Excel
from datetime import datetime

geneza_entry = f"""
## {datetime.now().strftime("%d.%m.%Y")} — faktura_output.xlsx
- **Verzija:** 1.0
- **Izmena:** Inicijalna verzija fakture
- **Razlog:** Kreiranje novog dokumenta
- **Pogođeni sheet-ovi:** Faktura
"""

with open('/home/ubuntu/geneza_izmena.md', 'a', encoding='utf-8') as f:
    f.write(geneza_entry)
```

## Korak 6: Validacija i isporuka

```python
# Sačuvaj
wb.save('/home/ubuntu/faktura_output.xlsx')

# Validiraj
import subprocess
result = subprocess.run(
    ['python', 'scripts/validate_excel.py', '/home/ubuntu/faktura_output.xlsx'],
    capture_output=True, text=True
)
print(result.stdout)
```

## Očekivani rezultat validacije

```
=== VALIDACIJA EXCEL FAJLA ===
Fajl: /home/ubuntu/faktura_output.xlsx

[SHEET: Faktura]
  ✅ Excel Table pronađen: TabelaFaktura
  ✅ Nema duplog AutoFiltera
  ✅ Konto kolona je tekstualna
  ✅ Finansijske kolone imaju srpski format
  ✅ Minimalna širina kolona zadovoljena
  ✅ Nema formula grešaka

REZULTAT: ✅ SVE PROVERE PROŠLE
```
