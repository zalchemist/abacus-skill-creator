# Saveti za parsiranje MySQL dump fajlova

## Formati dump-ova

### mysqldump (standardni)
```sql
-- MySQL dump 10.13  Distrib 5.7.30
-- Server version   5.7.30
CREATE TABLE `ime_tabele` (
  `kolona1` int(11) NOT NULL,
  `kolona2` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`kolona1`),
  KEY `idx_name` (`kolona2`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### Navicat dump
Slican mysqldump-u ali moze imati dodatne komentare i drugacije formatiranje.

### phpMyAdmin export
Moze sadrzati `SET` naredbe na pocetku i `--` komentare.

## Regex obrasci za parsiranje

### Pronalazenje CREATE TABLE bloka
```python
import re
pattern = r"CREATE TABLE\s+`(\w+)`"
match = re.match(pattern, line, re.IGNORECASE)
```

### Parsiranje kolona
```python
# Kolona sa tipom podataka
col_pattern = r'^`(\w+)`\s+(.+?)(?:,\s*)?$'
```

### Parsiranje primarnog kljuca
```python
pk_pattern = r'^\s*PRIMARY KEY\s*\(([^)]+)\)'
pk_cols = re.findall(r'`(\w+)`', match.group(1))
```

### Parsiranje foreign key-eva
```python
fk_pattern = r'FOREIGN KEY\s*\(([^)]+)\)\s*REFERENCES\s*`(\w+)`\s*\(([^)]+)\)'
```

### Kraj CREATE TABLE bloka
```python
# Prepoznaje se po `)` pracenom sa ENGINE ili tackom-zarezom
if stripped.startswith(')') and ('ENGINE' in stripped or stripped == ');'):
    in_create = False
```

## Cesti problemi pri parsiranju

1. **Encoding** — uvek koristiti `encoding='utf-8', errors='replace'` pri otvaranju fajla
2. **Veliki fajlovi** — citati liniju po liniju, ne ceo fajl u memoriju
3. **Komentari** — `--`, `/*...*/` i `#` komentari mogu prekinuti parsiranje
4. **Multi-line vrednosti** — INSERT naredbe mogu biti izuzetno dugacke
5. **Escape karakteri** — `\'` u string vrednostima
6. **Redosled** — DROP TABLE pre CREATE TABLE u vecini dump-ova
7. **View-ovi** — `CREATE VIEW` se moze pomesati sa `CREATE TABLE`
8. **Stored objekti** — `DELIMITER $$` menja separator naredbi

## Procena velicine

- `.sql` fajl od 100 MB = 20-50 tabela sa podacima, ili 500+ praznih tabela
- Ucitavanje u MariaDB: ~1-3 min po 100 MB
- Parsiranje (samo struktura): ~10 sekundi po 100 MB

## Korisne bash komande za brzu analizu

```bash
# Broj tabela u dump-u
grep -c 'CREATE TABLE' dump.sql

# Lista tabela
grep 'CREATE TABLE' dump.sql | sed 's/CREATE TABLE `\([^`]*\)`.*/\1/'

# Velicina dump-a
du -h dump.sql

# Broj linija
wc -l dump.sql

# MySQL verzija iz dump-a
head -20 dump.sql | grep -i 'mysql\|mariadb\|version'

# Pretraga specificne tabele
grep -n 'CREATE TABLE.*ime_tabele' dump.sql
```
