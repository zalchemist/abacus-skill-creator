# Primeri LOŠEG pristupa

## Primer 1: Agregacija bez pitanja

### ❌ LOŠE:

> "Napravio sam sumarni pregled:
>
> | Vrsta dokumenta | Ukupan broj konta |
> |-----------------|-------------------|
> | 10 | 15 |
> | 20 | 23 |
> | 30 | 8 |
>
> Gotovo!"

### Zašto je loše:
- Korisnik je tražio **originalne podatke**, ne agregacije
- Nema primera konkretnih konta
- Nema checkpoint-a pre izvršenja
- Agent je "istrčao" sa deliverable-om

---

## Primer 2: Meta-tabela umesto pravih podataka

### ❌ LOŠE:

> "Evo analize strukture:
>
> | Sheet | Broj kolona | Broj redova | Tipovi podataka |
> |-------|-------------|-------------|------------------|
> | Sheet1 | 5 | 1247 | mixed |
>
> Struktura je analizirana."

### Zašto je loše:
- Ovo je **tabela o tabeli**, ne pravi podaci
- Korisnik ne vidi šta je zapravo u podacima
- Nema reprezentativnih primera

---

## Primer 3: Preskakanje koraka

### ❌ LOŠE:

> "Analizirao sam oba fajla, napravio mapiranje, identifikovao robne konte, kreirao Excel sa 3 sheet-a, i evo rezultata!"

### Zašto je loše:
- Korisnik nije video ni jedan međukorak
- Nema checkpoint-a za potvrdu
- Ako je nešto pogrešno, mora se sve ponavljati
- Agent je pretpostavio da zna šta korisnik želi

---

## Primer 4: Pretpostavka formata

### ❌ LOŠE:

> "Pretpostavljam da želiš pivot tabelu, pa sam je napravio..."

### Zašto je loše:
- Agent **pretpostavlja** umesto da **pita**
- Korisnik možda uopšte ne želi pivot tabelu
- Vreme je potrošeno na nešto što nije traženo

---

## Primer 5: Ignorisanje korisnikove korekcije

### ❌ LOŠE:

> Korisnik: "Ne želim agregacije, želim originalne podatke"
> Agent: "OK, evo malo detaljnije agregacije..."

### Zašto je loše:
- Agent nije **slušao** šta korisnik traži
- Ponovio je istu grešku
- Frustrira korisnika

---

## Rezime loših obrazaca

| Loš obrazac | Posledica |
|-------------|----------|
| Agregacija bez pitanja | Gubi se granularnost podataka |
| Meta-tabele | Korisnik ne vidi prave podatke |
| Preskakanje koraka | Greške se kasno otkrivaju |
| Pretpostavke | Radi se pogrešna stvar |
| Ignorisanje feedback-a | Frustracija korisnika |
