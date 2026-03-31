# Checkpoint Workflow

## Pregled

Ovaj workflow definiše **obavezne checkpoint-e** koje agent mora da prati pre svakog deliverable-a.

---

## Faze rada

### FAZA 1: Razumevanje zadatka

**Akcije:**
1. Pročitaj zadatak pažljivo
2. Identifikuj nejasnoće
3. Formuliši pitanja

**Checkpoint 1:** ✋ STOP
> "Razumem da želiš [X]. Pre nego što počnem, da potvrdim:
> - [Pitanje 1]?
> - [Pitanje 2]?"

---

### FAZA 2: Predlog pristupa

**Akcije:**
1. Napravi plan koraka
2. Pripremi primer outputa

**Checkpoint 2:** ✋ STOP
> "Evo mog plana:
> 1. [Korak 1]
> 2. [Korak 2]
> 3. [Korak 3]
>
> **PRIMER** kako će rezultat izgledati:
> ```
> [Konkretan primer sa stvarnim podacima]
> ```
>
> Je li ovo format koji ti odgovara?"

---

### FAZA 3: Izvršenje koraka

**Za SVAKI korak:**

**Checkpoint 3a:** Pre koraka
> "Sada ću uraditi [Korak X]. Očekujem da rezultat izgleda ovako:
> ```
> [Primer]
> ```
> Nastavljam?"

**Checkpoint 3b:** Posle koraka
> "Završio sam [Korak X]. Evo rezultata:
> ```
> [Stvarni rezultat sa originalnim podacima]
> ```
> Da li je ovo OK? Mogu li nastaviti sa sledećim korakom?"

---

### FAZA 4: Deliverable

**Checkpoint 4:** Pre finalnog deliverable-a
> "Pre nego što napravim finalni output, evo pregleda:
> - Format: [Excel/CSV/Markdown/...]
> - Sheet-ovi/Sekcije: [lista]
> - Primeri redova:
> ```
> [5-10 reprezentativnih redova]
> ```
>
> Da li da napravim finalni fajl u ovom formatu?"

---

## Šablon za checkpoint

```markdown
## ✋ CHECKPOINT: [Ime koraka]

**Šta sam uradio:**
- [Lista završenog]

**Šta planiram sledeće:**
- [Lista planiranog]

**Primer outputa:**
[Konkretan primer sa stvarnim podacima]

**Pitanje:**
Da li da nastavim sa ovim pristupom?
```

---

## Crvene zastavice (kada OBAVEZNO stati)

🚩 **STOP ako:**
- Planiraš da agregiraš podatke
- Planiraš da promeniš strukturu podataka
- Nešto ti nije jasno iz zadatka
- Korisnik je dao feedback koji se razlikuje od tvog plana
- Planiraš da napraviš finalni deliverable

---

## Primer kompletnog workflow-a

```
1. Korisnik: "Analiziraj finansijsko.xlsx"

2. Agent: "Razumem. Pre nego što počnem:
   - Da li želiš originalne redove ili agregacije?
   - Koje kolone su ti najvažnije?"

3. Korisnik: "Originalne redove, sve kolone"

4. Agent: "OK. Evo prvih 5 redova:
   | Konto | Duguje | Potražuje |
   |-------|--------|----------|
   | 13401 | 15000 | 0 |
   ...
   Da li je ovo format koji ti odgovara?"

5. Korisnik: "Da, nastavi"

6. Agent: [nastavlja sa radom]
```

---

## Zlatna pravila

1. **Nikad ne preskači checkpoint** - čak i ako misliš da znaš odgovor
2. **Uvek daj primer** - ne opisuj šta ćeš uraditi, pokaži
3. **Čekaj potvrdu** - ne nastavljaj dok korisnik ne kaže OK
4. **Originalni podaci** - ne agregiraj bez eksplicitne dozvole
