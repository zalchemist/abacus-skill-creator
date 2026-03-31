# Rad sa bazama bez eksplicitnih FK veza

## Uvod

Mnoge poslovne aplikacije, posebno ERP sistemi, koriste **implicitne veze** izmedju tabela — referentni integritet se odrzava na nivou aplikacije, ne na nivou baze podataka.

## Razlozi za odsustvo FK constraints

1. **Performanse** — FK constraints dodaju overhead pri INSERT/UPDATE/DELETE operacijama
2. **Fleksibilnost** — lakse migracije i izmene seme
3. **Legacy sistemi** — stari sistemi dizajnirani pre siroke podrske za FK
4. **Bulk operacije** — masovni unos podataka je brzi bez FK provera
5. **Cross-database reference** — veze izmedju razlicitih baza/sema

## Kako pronaci implicitne veze

### Metod 1: Konvencije imenovanja kolona

Najcesci obrazac — kolone sa istim ili slicnim imenom u razlicitim tabelama:

```sql
-- Pronadji kolone koje se pojavljuju u mnogo tabela
SELECT column_name, COUNT(DISTINCT table_name) AS cnt
FROM information_schema.columns
WHERE table_schema = '<baza>'
GROUP BY column_name
HAVING cnt > 5
ORDER BY cnt DESC;
```

### Metod 2: Poklapanje vrednosti

Za svaku potencijalnu vezu — proveri koliko vrednosti u child tabeli postoji u parent tabeli:

```sql
SELECT
  COUNT(DISTINCT c.<col>) AS distinct_values,
  (SELECT COUNT(DISTINCT c2.<col>)
   FROM <child> c2
   INNER JOIN <parent> p ON c2.<col> = p.<pk>) AS matched
FROM <child> c
WHERE c.<col> IS NOT NULL AND c.<col> != '';
```

Procenat poklapanja:
- **100%** = potvrdjena veza
- **90-99%** = verovatna veza (mali broj orphan-a)
- **<50%** = verovatno NIJE veza

### Metod 3: Analiza koda/procedura

Stored procedure i trigeri cesto otkrivaju veze:
```sql
SHOW CREATE PROCEDURE <ime>;
SHOW CREATE TRIGGER <ime>;
```
Potrazi `JOIN`, `WHERE ... = ...`, `INSERT INTO ... SELECT`.

## Cest problem: Neuniformni nazivi kolona

**KRITICNO:** Isti entitet moze biti referenciran **razlicitim imenima kolona** u raznim tabelama.

Primer iz prakse:

| Entitet | Moguca imena kolone | Master tabela |
|---------|---------------------|---------------|
| Partner/kupac | `sifkup`, `sifpar`, `partner`, `posp`, `kupac` | `kupci.sifra` |
| Objekat/lokacija | `sifobj`, `objekat`, `lokacija` | `objekti.sifra` |
| Artikal | `sifra`, `sifart`, `artikal` | `artikli.sifra` |
| Konto | `racun`, `konto`, `kontod`, `kontop` | `kontniplan.racun` |
| Dokument | `brnal`, `brdok`, `brnalorig`, `biznisoftbrnal` | Interni ID |

**Preporuka:** Uvek napravi mapu naziva kolona za iste entitete na pocetku analize.

## Identifikacija master tabela (sifarnika)

Master tabele (sifarnici) se prepoznaju po:
1. **Jednostavan PK** — obicno jedan `sifra` ili `id` integer
2. **Kolona `naziv`** — deskriptivan naziv entiteta
3. **Mali broj zapisa** u poredjenju sa transakcionim tabelama
4. **Pojavljuju se kao FK** u mnogim drugim tabelama
5. **Retko se menjaju** — staticki podaci

Tipicni sifarnici u poslovnim aplikacijama:
- Objekti/lokacije
- Kupci/partneri/dobavljaci
- Artikli/proizvodi/usluge
- Kontni plan
- Grupe/kategorije
- Operateri/korisnici

## Verifikacija pronadjenih veza

Za svaku pronadjenu vezu, obavezno:

1. **SQL verifikacija** — proveri procenat poklapanja
2. **Tip podataka** — proveri da li su kompatibilni tipovi (int-int, varchar-varchar)
3. **NULL vrednosti** — filtriraj NULL i prazne stringove pre provere
4. **Nulte vrednosti** — `0` cesto znaci "nije postavljeno", a ne FK ka zapisu sa ID=0
5. **Sample podaci** — prikazi par primera sa JOIN-om za potvrdu smisla veze
