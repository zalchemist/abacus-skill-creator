# Pravila za Excel Table objekte

## Osnovno pravilo

Svaki dataset u Excel fajlu **MORA** biti kreiran kao Excel Table objekat (`ws.add_table()`). Ovo obezbeđuje:
- Automatski AutoFilter na header redu
- Strukturirane reference u formulama
- Automatsko proširenje pri dodavanju novih redova
- Profesionalan izgled sa TableStyle

## Kreiranje Table-a

```python
from openpyxl.worksheet.table import Table, TableStyleInfo

# Definiši opseg (samo podaci, BEZ total reda)
table_ref = f"A1:E{last_data_row}"

# Kreiraj Table
table = Table(displayName="TabelaPodaci", ref=table_ref)
table.tableStyleInfo = TableStyleInfo(
    name="TableStyleMedium9",
    showFirstColumn=False,
    showLastColumn=False,
    showRowStripes=True,
    showColumnStripes=False
)
ws.add_table(table)
```

## ⚠️ KRITIČNO: Nikada dupli AutoFilter

```python
# ❌ GREŠKA — izaziva "Excel repair" dijalog
table = Table(displayName="MojaTabela", ref="A1:F100")
ws.add_table(table)
ws.auto_filter.ref = "A1:F100"  # NIKADA OVO!

# ✅ ISPRAVNO — Table sam upravlja filterom
table = Table(displayName="MojaTabela", ref="A1:F100")
ws.add_table(table)
# NEMA ws.auto_filter.ref
```

**Zašto:** Excel Table interno definiše `<autoFilter>` u svojoj XML strukturi. Ako dodaš i worksheet-level `auto_filter.ref`, Excel detektuje konflikt i pokreće "repair" proceduru koja može oštetiti formatiranje.

## Total/Summary redovi

Total red mora biti **VAN opsega** Excel Table-a:

```python
# Table pokriva samo podatke (redovi 1 do last_data_row)
table = Table(displayName="Podaci", ref=f"A1:E{last_data_row}")
ws.add_table(table)

# Total red je ISPOD Table-a
total_row = last_data_row + 1
ws.cell(row=total_row, column=1, value='UKUPNO')
ws.cell(row=total_row, column=1).font = Font(bold=True)
ws.cell(row=total_row, column=5, value=f'=SUM(E2:E{last_data_row})')
ws.cell(row=total_row, column=5).number_format = SERBIAN_NUMBER_FORMAT
ws.cell(row=total_row, column=5).font = Font(bold=True)
```

### ❌ Greška: Total red unutar Table-a

```python
# POGREŠNO — Total je deo Table-a, filter ga tretira kao podatak
table = Table(displayName="Podaci", ref="A1:E101")  # Red 101 je total
ws['A101'] = 'UKUPNO'
ws['E101'] = '=SUM(E2:E100)'
```

## Imenovanje Table-a

- Naziv mora biti jedinstven u workbook-u
- Bez razmaka i specijalnih karaktera
- CamelCase ili underscore: `TabelaPodaci`, `Tabela_Podaci`
- Ako ima više sheet-ova, koristiti prefiks: `FakturaPodaci`, `SumarnoMesecno`

## Preporučeni Table stilovi

| Stil | Upotreba |
|------|----------|
| `TableStyleMedium9` | Standardni poslovni izveštaji |
| `TableStyleMedium2` | Svetliji ton, manje formalan |
| `TableStyleLight1` | Minimalan stil |
| `TableStyleDark1` | Naglašen, za prezentacije |

## AutoFilter bez Table-a

Ako iz nekog razloga ne koristiš Table objekat, **tada** možeš koristiti `ws.auto_filter.ref`:

```python
# Dozvoljeno SAMO ako nema Table-a na sheet-u
ws.auto_filter.ref = "A1:E100"
```

## Više Table-a na jednom sheet-u

Tehnički moguće, ali **nije preporučeno**. Ako je neophodno:
- Ostavi minimum 2 prazna reda između Table-a
- Svaki Table mora imati jedinstven naziv
- Nikada ne preklapaj opsege
