# Primeri DOBROG pristupa

## Primer 1: Pokazati originalnu strukturu podataka

### ✅ DOBRO:

> "Evo kako izgledaju prvi redovi iz finansijsko.xlsx:
>
> | Broj naloga | Vrsta dokumenta | Konto | Duguje | Potražuje |
> |-------------|-----------------|-------|--------|----------|
> | KL002-00005 | 10 | 13401 | 15000 | 0 |
> | KL002-00005 | 10 | 4350 | 0 | 15000 |
> | RN002000332 | 20 | 13441 | 8500 | 0 |
>
> Da li da nastavim sa ovom strukturom?"

---

## Primer 2: Pitati pre agregacije

### ✅ DOBRO:

> "Vidim da ima 1,247 redova u tabeli. Mogu da:
> 
> A) Prikažem reprezentativni uzorak od 20 redova
> B) Napravim sumarni pregled po vrsti dokumenta
> C) Prikažem sve redove u Excel fajlu
>
> Šta ti više odgovara?"

---

## Primer 3: Checkpoint pre deliverable-a

### ✅ DOBRO:

> "Pre nego što krenem sa analizom, evo mog plana:
>
> **Korak 1:** Učitavam finansijsko.xlsx i robno.xlsx
> **Korak 2:** Ekstraktujem prefiks iz Broja naloga (KL, RN, IZ...)
> **Korak 3:** Mapiram prefiks na Vrstu dokumenta
>
> **PRIMER kako će to izgledati:**
> - Broj naloga: KL002-00005 → Prefiks: KL → VD: 10
>
> Je li ovo logika koju očekuješ?"

---

## Primer 4: Zadržati originalnu strukturu

### ✅ DOBRO:

> "Evo sheet-a 'VD_Konta_mapiranje' sa originalnim kolonama:
>
> | Vrsta dokumenta | Konto (Račun) | Broj redova | Primeri brojeva naloga |
> |-----------------|---------------|-------------|------------------------|
> | 10 | 13401 | 45 | KL002-00005, KL002-00008 |
> | 10 | 4350 | 45 | KL002-00005, KL002-00008 |
> | 20 | 13441 | 23 | RN002000332, RN002000335 |
>
> Svi podaci su originalni, nisam ih agregirao."

---

## Primer 5: Logiranje u STATUS.md

### ✅ DOBRO:

> "Ažurirao sam STATUS.md sa trenutnim progresom:
> - ✅ Učitani fajlovi
> - ✅ Identifikovane robne konte
> - 🔄 Mapiranje VD u toku
>
> Možeš pratiti status u tom fajlu."

---

## Ključni principi

1. **Pokaži pre nego što napraviš** - uvek daj primer outputa
2. **Pitaj pre nego što pretpostaviš** - ako nešto nije jasno, PITAJ
3. **Zadrži originalnu strukturu** - ne agregiraj bez dozvole
4. **Budi transparentan** - logiraj šta radiš
