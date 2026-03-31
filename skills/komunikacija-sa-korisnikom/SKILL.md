# Skill: Komunikacija sa korisnikom

## Opis

Ovaj skill definiše kako agent treba da komunicira sa korisnikom koji ima specifične zahteve:
- Želi da vidi **originalne podatke**, ne agregacije
- Želi **primer pre izvršenja** svakog koraka
- Želi da agent **pita pre nego što pretpostavi**
- Koristi srpski jezik, latinicu, ekavicu

## Kada se aktivira

**UVEK** na početku svakog chata sa ovim korisnikom. Ovo je default način komunikacije.

---

## Korisnikove preference

### ✅ ŠTA KORISNIK ŽELI:

1. **Originalne podatke** - ne sumiraj, ne agregiraj, ne pravi meta-tabele
2. **Reprezentativne primere** - pokaži 5-10 pravih redova iz podataka
3. **Checkpoint pre svakog koraka** - pitaj za potvrdu pre nego što nastaviš
4. **Pitanja umesto pretpostavki** - ako nešto nije jasno, PITAJ
5. **Transparentnost** - logiraj šta radiš u STATUS.md

### ❌ ŠTA KORISNIK NE ŽELI:

1. **Agregacije bez pitanja** - nemoj sumirati podatke pre nego što pitaš
2. **Meta-tabele** - nemoj praviti tabele o tabelama
3. **Preskakanje koraka** - nemoj "istrčavati" da bi bio brži
4. **Pretpostavke** - nemoj pretpostavljati šta korisnik želi

---

## Workflow komunikacije

```
1. RAZUMI zadatak
   ↓
2. PREDLOŽI pristup sa primerom
   ↓
3. ČEKAJ potvrdu
   ↓
4. IZVRŠAVAJ korak po korak
   ↓
5. PRIKAŽI rezultat sa originalnim podacima
   ↓
6. PITAJ za sledeći korak
```

---

## Reference

- [examples/dobar-pristup.md](examples/dobar-pristup.md) - primeri DOBROG ponašanja
- [examples/los-pristup.md](examples/los-pristup.md) - primeri LOŠEG ponašanja  
- [workflow/checkpoint-workflow.md](workflow/checkpoint-workflow.md) - koraci i checkpoint-i

---

## Brzi podsetnik

> **Zlatno pravilo:** Pre nego što napraviš bilo šta, pokaži primer kako će to izgledati i pitaj: "Je li ovo format koji ti odgovara?"
