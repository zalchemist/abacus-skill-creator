# Obrasci storniranja u ERP sistemima

## Princip storniranja

Storniranje je mehanizam za **ponistavanje dokumenta bez brisanja** — umesto DELETE operacije, kreira se novi zapis sa negativnim iznosima koji ponistava originalni.

## Zasto storniranje umesto brisanja?

1. **Revizijski trag (audit trail)** — uvek se vidi sta se desilo
2. **Zakonski zahtevi** — u racunovodstvu, knjizenja se ne smeju brisati
3. **Konzistentnost** — svi izvestaji ostaju tacni za prethodne periode
4. **Oporavak** — moguce je pratiti celu istoriju promena

## Obrazac sufiksa

Cest obrazac u ERP sistemima za identifikaciju storno i re-knjizenja:

```
Original:        KL003-00026      (pozitivni iznosi)
Storno:          KL003-00026/1    (negativni iznosi, ponistava original)
Re-knjizenje:    KL003-00026/2    (pozitivni, ispravljeni podaci)
Storno re-knj.:  KL003-00026/3    (negativni, ponistava /2)
Drugo re-knj.:   KL003-00026/4    (pozitivni, nova ispravka)
...
```

**Pravilo:** Neparni sufiksi (/1, /3, /5) = storno (negativni), Parni (/2, /4, /6) = re-knjizenje (pozitivni)

## Mehanizam storno procedure

Tipican tok storniranja:

1. **Kopira** zapise iz originalne tabele u privremenu (temp) tabelu
2. **Modifikuje** kopije:
   - Menja identifikator (dodaje sufiks)
   - Mnozi sve iznose sa -1
   - Postavlja flag `stornirano = 1`
   - Azurira operatera i timestamp
3. **Oznacava** originalne zapise kao stornirane
4. **Insertuje** storno zapise nazad u originalnu tabelu
5. **Belezi** storno operaciju u posebnu tabelu (registar storniranja)

## Child tabele i propagacija

Storniranje obicno pogadja **vise tabela istovremeno**:

- Robno/materijalno knjizenje
- Finansijske promene (glavna knjiga)
- PDV evidencija
- Trgovacka knjiga
- Log knjizenja
- Serijski brojevi

**Rizik:** Ako storno procedura **ne koristi transakciju** (`BEGIN/COMMIT`), moze doci do parcijalnog storniranja — neke tabele su stornirane, neke nisu.

## Provera konzistentnosti storniranja

### Korak 1: Identifikuj storno parove
```sql
SELECT brnalorig, brnalnovi FROM storniranja;
```

### Korak 2: Proveri prisustvo u svim child tabelama
Za svaki storno par, proveri da li storno zapis postoji u SVIM relevantnim tabelama.

### Korak 3: Proveri sume
```sql
-- Zbir originalnog + storno = 0
SELECT SUM(<iznos>) FROM <tabela>
WHERE brnal IN ('<orig>', '<storno>');
```

### Korak 4: Cross-referencing
- Zapisi u tabeli storniranja koji nemaju parnjake u child tabelama
- Zapisi sa storno sufiksima koji nisu evidentirani u tabeli storniranja

## Ceste zamke

1. **Kolona `stornirano` NIJE uvek pouzdana** — moze imati razlicito znacenje u raznim tabelama
2. **Satelitski nalozi** (npr. razlika u ceni, ispravke) mogu imati storno sufikse ali se ne loguju u tabelu storniranja — to je **by design**
3. **Razlicite storno procedure** mogu imati razlicito ponasanje (sa/bez promene datuma, sa/bez flag-a)
4. **Tabela `veze`** moze cuvati relacije izmedju re-proknjizenih naloga i njihovih prethodnika
5. **Audit log** (log knjizenja) ne mora nuzno imati storno zapis za svaku storno operaciju

## Distribucija storniranja — primer iz prakse

Primer iz analize ERP baze sa 16.000+ storniranja:

| Broj storniranja | Broj naloga | Komentar |
|-----------------|-------------|----------|
| 1x | 11.174 | Najcesci slucaj |
| 2x | 1.748 | Storniran pa ponovo proknjizen pa opet storniran |
| 3x | 426 | Tri ciklusa ispravki |
| 4+ | 48 | Retko, ali moguce (do 7x u praksi) |

## Primer kompletnog zivotnog ciklusa dokumenta

```
KL003-00026      +1.809.068   Original (pogresan datum)
KL003-00026/1    -1.809.068   Storno (ponistava original)
KL003-00026/2    +1.809.068   Re-knjizenje (ispravljeni datum)
KL003-00026/3    -1.809.068   Storno (nova greska)
KL003-00026/4    +1.809.068   Re-knjizenje (ispravljena kolicina)
KL003-00026/5    -1.809.068   Storno
KL003-00026/6    +1.809.068   Finalno re-knjizenje (sve ispravno)
```

Zbir svih verzija = +1.809.068 (finalni aktivni iznos)
