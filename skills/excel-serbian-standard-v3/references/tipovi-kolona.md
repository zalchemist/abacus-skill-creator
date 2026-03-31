# Pravila za tipove kolona — Inteligentna konverzija

## Princip

Ne konvertuj slepo sve u brojeve. Analiziraj sadržaj kolone i primeni odgovarajući tip.

## Konto i račun kolone

### Pravilo: UVEK tekst

Ako naziv kolone sadrži "konto", "račun", "account", "šifra konta" ili slično:

```python
# Označi kolonu kao tekstualnu
cell.value = str(konto_value)       # Čuvaj kao string
cell.number_format = '@'             # Excel tekst format
```

### Zašto?

Kontni plan koristi šifre sa vodećim nulama:
- `00410` — Ispravke vrednosti nematerijalne imovine
- `0200` — Zemljište
- `1020` — Sirovine i materijal

Ako konvertuješ u broj: `00410` → `410` — **izgubljeni podaci!**

### Kako prepoznati konto kolonu

```python
def is_konto_column(column_name):
    """Proveri da li je kolona konto/račun tip."""
    konto_keywords = ['konto', 'račun', 'account', 'šifra konta',
                      'konto broj', 'broj računa', 'acc', 'acct']
    name_lower = column_name.lower().strip()
    return any(keyword in name_lower for keyword in konto_keywords)
```

## Kolone sa vodećim nulama

Čak i kad kolona nije konto, ako vrednosti imaju vodeće nule — **ostavi kao tekst**:

```python
def should_keep_as_text(values):
    """Proveri da li vrednosti imaju vodeće nule."""
    for val in values:
        s = str(val).strip()
        if s and s[0] == '0' and len(s) > 1 and s.isdigit():
            return True
    return False
```

Primeri:
- `00123` → tekst (vodeća nula)
- `0` → broj (samo nula, nema gubitka)
- `123` → broj (nema vodeće nule)
- `A123` → tekst (nije čist broj)

## Datum kolone

### Prepoznavanje

Ako naziv sadrži "datum", "date", "vreme", "time", ili ako vrednosti odgovaraju datum patternima.

### Konverzija

```python
from datetime import datetime

# Česti srpski formati
date_formats = [
    '%d.%m.%Y',          # 15.03.2026
    '%d.%m.%Y %H:%M',   # 15.03.2026 14:30
    '%d.%m.%Y %H:%M:%S', # 15.03.2026 14:30:00
    '%d/%m/%Y',          # 15/03/2026
    '%Y-%m-%d',          # 2026-03-15 (ISO)
    '%Y-%m-%d %H:%M:%S', # 2026-03-15 14:30:00
]

def parse_date(value):
    """Pokušaj parsiranje datuma iz različitih formata."""
    for fmt in date_formats:
        try:
            return datetime.strptime(str(value).strip(), fmt)
        except ValueError:
            continue
    return None
```

### Excel format

```python
# Samo datum
cell.number_format = 'DD.MM.YYYY'

# Datum sa vremenom
cell.number_format = 'DD.MM.YYYY HH:MM'
```

## Numeričke kolone

Sve kolone koje sadrže numeričke vrednosti i nisu konto/tekst:

```python
def smart_convert(value, column_name):
    """Inteligentna konverzija vrednosti."""
    # 1. Konto kolone — uvek tekst
    if is_konto_column(column_name):
        return str(value), '@'

    s = str(value).strip()

    # 2. Prazne vrednosti
    if not s or s.lower() in ('nan', 'none', ''):
        return None, None

    # 3. Vodeće nule — tekst
    if s[0] == '0' and len(s) > 1 and s.replace('.', '').replace(',', '').isdigit():
        return s, '@'

    # 4. Pokušaj konverziju u broj
    try:
        # Zameni srpski format (1.234,56 → 1234.56)
        cleaned = s.replace('.', '').replace(',', '.')
        num = float(cleaned)
        return num, SERBIAN_NUMBER_FORMAT
    except ValueError:
        pass

    # 5. Pokušaj datum
    date = parse_date(s)
    if date:
        return date, 'DD.MM.YYYY'

    # 6. Ostavi kao tekst
    return s, '@'
```

## Sumarno — Algoritam odlučivanja

```
Naziv kolone sadrži "konto"/"račun"?
  → DA: Tekst (@)
  → NE: Vrednosti imaju vodeće nule?
    → DA: Tekst (@)
    → NE: Vrednosti su datumi?
      → DA: Datum (DD.MM.YYYY)
      → NE: Vrednosti su brojevi?
        → DA: Broj ([$-407]#,##0.00)
        → NE: Tekst (@)
```
