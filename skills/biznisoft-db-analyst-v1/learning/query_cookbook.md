# SQL Cookbook — Korisni upiti za BizniSoft baze

Upiti koji su se pokazali vrednim tokom analiza. Svaki upit ima opis, SQL i napomenu kada ga koristiti.

---

## Osnovni pregled baze

### Prebroj tabele, procedure, trigere i funkcije
```sql
-- Tabele
SELECT table_schema, COUNT(*) as br_tabela 
FROM information_schema.tables 
WHERE table_schema NOT IN ('information_schema','mysql','performance_schema','sys') 
GROUP BY table_schema;

-- Procedure
SELECT routine_schema, COUNT(*) as br_procedura 
FROM information_schema.routines 
WHERE routine_type='PROCEDURE' 
  AND routine_schema NOT IN ('information_schema','mysql','performance_schema','sys') 
GROUP BY routine_schema;

-- Trigeri
SELECT trigger_schema, COUNT(*) as br_trigera 
FROM information_schema.triggers 
WHERE trigger_schema NOT IN ('information_schema','mysql','performance_schema','sys') 
GROUP BY trigger_schema;
```
**Kada koristiti:** Na početku svake analize za brzi pregled.

---

## Provera integriteta

### Finansijska ravnoteža (finprom)
```sql
-- Pronađi naloge gde duguje != potrazuje
SELECT vrstad, brnal, 
       SUM(duguje) as ukupno_duguje, 
       SUM(potrazuje) as ukupno_potrazuje,
       SUM(duguje) - SUM(potrazuje) as razlika
FROM finprom 
GROUP BY vrstad, brnal 
HAVING ABS(SUM(duguje) - SUM(potrazuje)) > 0.01;
```
**Kada koristiti:** Provera finansijske konzistentnosti.

### Siročići — partneri bez šifarnika
```sql
-- Partneri u finprom koji ne postoje u kupci
SELECT DISTINCT f.sifpar 
FROM finprom f 
LEFT JOIN kupci k ON f.sifpar = k.sifra 
WHERE k.sifra IS NULL AND f.sifpar != '' AND f.sifpar IS NOT NULL;
```
**Kada koristiti:** Provera referentnog integriteta šifarnika.

---

<!-- Dodavati nove upite kako se budu pokazali korisnim -->
