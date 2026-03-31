# Pravila za formatiranje brojeva — Srpski/Evropski standard

## Osnovno pravilo

Svi finansijski i numerički podaci u Excel-u koriste locale format `[$-407]` koji forsira evropski prikaz:
- **Tačka (`.`)** kao separator hiljada
- **Zarez (`,`)** kao decimalni separator

## Format kodovi

### Konstante za Python kod

```python
# Definisati na početku svake skripte
SERBIAN_NUMBER_FORMAT = '[$-407]#,##0.00'
SERBIAN_INTEGER_FORMAT = '[$-407]#,##0'
SERBIAN_PERCENT_FORMAT = '[$-407]0.00%'
SERBIAN_CURRENCY_RSD = '[$-407]#,##0.00 "RSD"'
SERBIAN_CURRENCY_EUR = '[$-407]#,##0.00 "EUR"'
SERBIAN_CURRENCY_USD = '[$-407]#,##0.00 "USD"'
SERBIAN_NEGATIVE_BRACKETS = '[$-407]#,##0.00;([$-407]#,##0.00);"-"'
```

### Tabela formata

| Tip | Format Code | Primer prikaza |
|-----|------------|----------------|
| Broj sa 2 decimale | `[$-407]#,##0.00` | 1.234,56 |
| Ceo broj | `[$-407]#,##0` | 1.235 |
| Procenat | `[$-407]0.00%` | 15,30% |
| RSD valuta | `[$-407]#,##0.00 "RSD"` | 1.234,56 RSD |
| EUR valuta | `[$-407]#,##0.00 "EUR"` | 1.234,56 EUR |
| Negativni u zagradi | `[$-407]#,##0.00;([$-407]#,##0.00);"-"` | (1.234,56) |
| Sa 4 decimale | `[$-407]#,##0.0000` | 1.234,5678 |

### Primeri prikaza

| Python vrednost | Prikaz u Excel-u |
|----------------|-------------------|
| 1000 | 1.000,00 |
| 1234567.89 | 1.234.567,89 |
| 0.5 | 0,50 |
| -1500.75 | -1.500,75 |

## Kako `[$-407]` radi

- `[$-407]` je Windows Locale ID za nemački (Austrija) koji koristi isti format separatora kao srpski
- Excel interno čuva brojeve u standardnom formatu (1234.56)
- Locale tag samo menja **prikaz** — ne menja vrednost
- Formule i kalkulacije rade normalno

## Primena formata na kolone

```python
# Na jednu ćeliju
cell.number_format = SERBIAN_NUMBER_FORMAT

# Na celu kolonu
for row in range(2, max_row + 1):
    ws.cell(row=row, column=col).number_format = SERBIAN_NUMBER_FORMAT

# Na opseg ćelija
for row in ws.iter_rows(min_row=2, min_col=3, max_col=5, max_row=max_row):
    for cell in row:
        cell.number_format = SERBIAN_NUMBER_FORMAT
```

## Datum formati

```python
from datetime import datetime

# Samo datum
cell.value = datetime(2026, 3, 15)
cell.number_format = 'DD.MM.YYYY'          # → 15.03.2026

# Datum sa vremenom
cell.number_format = 'DD.MM.YYYY HH:MM'   # → 15.03.2026 14:30

# Samo vreme
cell.number_format = 'HH:MM:SS'            # → 14:30:00
```

## Formula separator: `;` vs `,` — pojašnjenje

> **Ovo je čest izvor zabune** i važno je razumeti razliku.

### Kako openpyxl čuva formule

openpyxl interno čuva formule u **internacionalnom formatu** gde je zarez (`,`) separator argumenata:
- `=SUM(A1,A10)` — openpyxl interni format
- Ovo je isti format koji koristi Excel interno u XML-u

### Kako Excel prikazuje formule

Excel sa srpskim ili nemačkim locale-om **prikazuje** formule sa tačka-zarezom (`;`):
- `=SUMA(A1;A10)` — prikaz u Excel-u (srpski locale)
- Ovo je samo vizuelna razlika — interno je isto

### Šta ovo znači za kodiranje

openpyxl prihvata **oba** oblika:
```python
# Oba su validna u openpyxl
cell.value = '=SUM(A1;A10)'    # ✅ tačka-zarez — preporučeno
cell.value = '=SUM(A1,A10)'    # ✅ zarez — takođe ispravno
```

### Preporuka

Za konzistentnost sa srpskim Excel prikazom, preporučujemo **tačka-zarez** (`;`). Validaciona skripta (v3) proverava konzistentnost i upozorava na mešovito korišćenje.

---

## Česte greške

### ❌ Korišćenje Python formatiranja umesto Excel formata
```python
# POGREŠNO — stavlja string umesto broja
cell.value = f"{value:,.2f}".replace(',', '.')
# ISPRAVNO — stavlja broj sa Excel formatom
cell.value = value
cell.number_format = SERBIAN_NUMBER_FORMAT
```

### ❌ Zaboravljanje formata na summary/total redovima
```python
# POGREŠNO — total red bez formata
cell.value = '=SUM(B2:B100)'
# ISPRAVNO — total sa formatom
cell.value = '=SUM(B2:B100)'
cell.number_format = SERBIAN_NUMBER_FORMAT
```

### ❌ Formatiranje header reda
```python
# POGREŠNO — format na header-u
for row in range(1, max_row + 1):  # počinje od 1!
    cell.number_format = SERBIAN_NUMBER_FORMAT
# ISPRAVNO — format samo na podatke
for row in range(2, max_row + 1):  # počinje od 2
    cell.number_format = SERBIAN_NUMBER_FORMAT
```
