# Biznisoft - Poređenje tabela: opp vs opp7102025

**Datum analize:** 2026-03-29
**opp (master/šifarnici):** 195 tabela | **opp7102025 (transakciona):** 643 tabele

---

## Sumarni pregled

| Kategorija | Broj tabela |
|---|---|
| **Zajedničke tabele** (postoje u obe baze) | 15 |
| **Samo u opp** (master šifarnici/config) | 180 |
| **Samo u opp7102025** (transakcione) | 628 |

---

## 1. Zajedničke tabele (15) — Poređenje broja redova

Ove tabele postoje u OBE baze. Razlike u broju redova ukazuju na stepen sinhronizacije.

| Tabela | Redova u opp | Redova u opp7102025 | Status |
|---|---|---|---|
| `build` | 1 | 1 | ✅ Sinhronizovano |
| `hot_tax` | 0 | 0 | ✅ Prazne obe |
| `kontniplan` | 17,003 | 17,077 | ⚠️ Razlika +74 u opp7102025 |
| `kporacuni` | 1 | 0 | ❌ opp7 prazna |
| `ld130` | 5 | 0 | ❌ opp7 prazna |
| `ld220` | 35 | 35 | ✅ Sinhronizovano |
| `ldvp_opj1` | 14 | 14 | ✅ Sinhronizovano |
| `mybsliveid` | 1 | 1 | ✅ Sinhronizovano |
| `operateri` | 134 | 0 | ❌ opp7 prazna (master u opp) |
| `pk1racuni` | 20 | 0 | ❌ opp7 prazna |
| `poljapozelji` | 0 | 0 | ✅ Prazne obe |
| `puk_stepstrucnespreme` | 4 | 0 | ❌ opp7 prazna |
| `puk_strucnasprema` | 0 | 0 | ✅ Prazne obe |
| `sifobj` | 19 | 0 | ❌ opp7 prazna (master u opp) |
| `tabrac` | 426 | 1,148 | ⚠️ opp7 ima više (+722) |

### Interpretacija zajedničkih tabela:
- **Sinhronizovane:** `build`, `ld220`, `ldvp_opj1`, `mybsliveid` — identične kopije
- **Master u opp:** `operateri`, `sifobj`, `kporacuni`, `ld130`, `pk1racuni`, `puk_stepstrucnespreme` — podaci SAMO u opp, opp7 kopije su prazne
- **Divergentne:** `kontniplan` (kontni plan — opp7 ima 74 konta više), `tabrac` (opp7 ima 722 računa/transakcija više — verovatno korisnički dodati)

---

## 2. Tabele SAMO u opp (180)

Ovo su master šifarnici, konfiguracija i sistemske tabele.

### Kategorija: Sistemska konfiguracija
| Tabela | Redova | Opis |
|---|---|---|
| `cnfg_config` | 1,445 | Sistemski parametri |
| `cnfg_istorija` | 896 | Istorija promena parametara |
| `cnfg_klasifikacija` | 15 | Klasifikacije konfiguracije |
| `cnfg_parametri` | 1,116 | Korisnički parametri |
| `cnfg_vrste` | 4 | Vrste konfiguracije |
| `korisnicki_parametri` | 633 | Korisnički parametri |
| `korisnik` | 1 | Info o korisniku/licenci |
| `propisani_parametri` | 56 | Zakonski parametri |

### Kategorija: Definicije dokumenata i formi
| Tabela | Redova | Opis |
|---|---|---|
| `documents` | 95 | **KLJUČNA** — definicije 95 tipova dokumenata |
| `crmdocs` | 70 | CRM dokumenti |
| `dmsdocuments` | 6 | DMS dokumenti |
| `sifostdokum` | 9 | Šifarnik ostalih dokumenata |
| `reports` | 1,024 | Definicije izveštaja |
| `reportsm` | 796 | Izveštaji (mobilni) |
| `reportbuild` | 1 | Build info izveštaja |

### Kategorija: Kontni plan i finansijski izveštaji
| Tabela | Redova | Opis |
|---|---|---|
| `kplprevod` | 2,133 | Prevod kontnog plana |
| `kplvezna` | 420 | Vezna tabela kontnog plana |
| `kontniplan2021dpl` | 1,783 | Kontni plan DPL 2021 |
| `kontniplan2021pdp` | 2,322 | Kontni plan PDP 2021 |
| `tabrac2021dpl` | 201 | Računi DPL 2021 |
| `tabrac2021pdp` | 203 | Računi PDP 2021 |
| `vezna2021dpl` | 76 | Vezne DPL 2021 |
| `vezna2021pdp` | 189 | Vezne PDP 2021 |
| `fkopis` | 892 | Opisi finansijskih kategorija |

### Kategorija: Finansijski izveštaji (FIZ)
| Tabela | Redova | Opis |
|---|---|---|
| `finiz_aop` | 1,122 | AOP pozicije |
| `finiz_aoprn` | 542 | AOP za RN |
| `finiz_vp` | 7 | Vrste FI |
| `fiz_aop_prom` | 2,480 | AOP promene |
| `fiz_aop_sum` | 2,471 | AOP sumiranja |
| `fiz_aop_uslovi` | 212 | AOP uslovi |
| `fiz_celine` | 142 | Celine FI |
| `fiz_cel_aop` | 2,336 | Veze celina-AOP |
| `fiz_kolone` | 732 | Kolone FI |
| `fiz_kontrola` | 849 | Kontrole FI |
| `fiz_prevod` | 2,355 | Prevodi FI |
| `fiz_vrste` | 40 | Vrste FI |

### Kategorija: Šifarnici — Geografija i opšti
| Tabela | Redova | Opis |
|---|---|---|
| `drzave` | 252 | Šifarnik država |
| `opstine` | 207 | Šifarnik opština |
| `pbrmesto` | 1,525 | Poštanski brojevi i mesta |
| `ptt_brojevi` | 1,994 | PTT brojevi |
| `sifzem` | 249 | Šifarnik zemalja |
| `sifval` | 37 | Šifarnik valuta |
| `nazmes` | 12 | Nazivi meseci |
| `jbkjs` | 55,036 | JBKJS registar |

### Kategorija: Šifarnici — Kadrovi/Plate
| Tabela | Redova | Opis |
|---|---|---|
| `sifzanimanja` | 2,963 | Šifarnik zanimanja |
| `sifplac` | 200 | Šifarnik plaćanja |
| `sifpla2konta` | 21 | Veze plaćanja-konta |
| `ldkategpok` | 6 | LD kategorije pokrajine |
| `ldkategugod` | 79 | LD kategorije godišnje |
| `ldkategugod_cg` | 16 | LD kategorije CG |
| `ldkategugod_racuni` | 159 | LD kategorije računi |
| `ldkategzap` | 47 | LD kategorije zaposlenih |
| `ldkategzap_opsta` | 45 | LD kategorije opšta |
| `puk_slike` | 1,290 | Slike zaposlenih |
| `puk_stranijezici` | 3 | Strani jezici |
| `puk_stepskolskespreme` | 6 | Stepeni školske spreme |
| `puk_konfesije` | 1 | Konfesije |
| `puk_stepkvalifikacije` | 0 | Stepeni kvalifikacija |
| `istekugorad` | 1,585 | Isteci ugovora o radu |

### Kategorija: Šifarnici — PDV i porezi
| Tabela | Redova | Opis |
|---|---|---|
| `pdvstope` | 9 | PDV stope |
| `pdvstopelabele` | 6 | Labele PDV stopa |
| `tabakciza` | 0 | Tabela akciza |
| `stope` | 1 | Poreske stope |

### Kategorija: Šifarnici — OS (osnovna sredstva)
| Tabela | Redova | Opis |
|---|---|---|
| `osamgdet` | 1,460 | OS amortizacione grupe detalj |
| `osamgzag` | 123 | OS amortizacione grupe zaglavlje |
| `oskateg` | 15 | OS kategorije |
| `osporgrupe` | 6 | OS poreske grupe |
| `osporpodgr` | 92 | OS poreske podgrupe |

### Kategorija: Kursna lista i cenovnici
| Tabela | Redova | Opis |
|---|---|---|
| `zirklista` | 10 | Kursna lista |
| `datkl` | 138,204 | Datumski kursevi (velika tabela!) |

### Kategorija: Partneri i ovlašćenja
| Tabela | Redova | Opis |
|---|---|---|
| `rnpartnkli` | 167,690 | Registar partnera/klijenata |
| `ovlpofirmama` | 66,486 | Ovlašćenja po firmama |
| `ovlpoizvest` | 46,552 | Ovlašćenja po izveštajima |
| `klijenti` | 4 | Klijenti (firme/baze) |
| `kliatributi` | 0 | Atributi klijenata |

### Kategorija: RFZO (zdravstvo) — sve prazne
| Tabela | Redova | Opis |
|---|---|---|
| `rfzo_*` (26 tabela) | 0 | RFZO šifarnici (neaktivni) |

### Kategorija: Javna preduzeća
| Tabela | Redova | Opis |
|---|---|---|
| `jp_funkcionalnaklasifikacija` | 141 | Funkcionalna klasifikacija |
| `jp_tabele` | 319 | JP tabele |

### Kategorija: Operativne/Log tabele
| Tabela | Redova | Opis |
|---|---|---|
| `logfile` | 231,752 | Sistemski log |
| `bcklog` | 6,690 | Backup log |
| `bsnotif` | 26,369 | Notifikacije |
| `arh_log` | 4,800 | Arhivski log |
| `radizvodizag` | 4,145 | Radni izvodi zaglavlje |
| `radizvodidet` | 52,793 | Radni izvodi detalji |
| `favorites` | 3,489 | Favoriti korisnika |
| `scheduler` | 122 | Zakazani zadaci |
| `safeguard` | 242 | Bezbednosne provere |

---

## 3. Tabele SAMO u opp7102025 (628)

Transakcione tabele — svi poslovni dokumenti, knjiženja, stanja. Previše za kompletnu listu, ali ključne kategorije:

### Robno-materijalno (primeri):
`artikli`, `robno`, `trstanje`, `kalkulacije`, `nivelacije`, `fakture`, `popis`, `pazari`, `kasa`, ...

### Finansije:
`gk` (glavna knjiga), `gkstavke`, `fintrans`, `blagajna`, `blgpromet`, ...

### Plate/Kadrovi:
`zaposleni`, `ldstavke`, `ldrekapitulacija`, `ldvirmanizag`, ...

### Osnovna sredstva:
`ossredstva`, `osamortizacija`, `ospromene`, ...

### Proizvodnja:
`radnal`, `radnalst`, `receptura`, ...

*(Kompletna lista svih 628 tabela dostupna na zahtev)*

---

## 4. Rezime arhitekture

```
┌─────────────────────────────────────────────┐
│              opp (MASTER BAZA)              │
│         195 tabela — šifarnici/config       │
│                                             │
│  ┌─────────────┐  ┌──────────────────────┐  │
│  │ documents   │  │ šifarnici: drzave,   │  │
│  │ (95 tipova) │  │ pdvstope, sifval,    │  │
│  └──────┬──────┘  │ sifzanimanja, ...    │  │
│         │         └──────────┬───────────┘  │
│  ┌──────┴───────┐  ┌────────┴──────────┐   │
│  │ rnpartnkli   │  │ datkl (138K kurs) │   │
│  │ (167K partn) │  │ zirklista (kurs)  │   │
│  └──────┬───────┘  └────────┬──────────┘   │
└─────────┼───────────────────┼──────────────┘
          │  ČITA SE IZ opp   │
          ▼                   ▼
┌─────────────────────────────────────────────┐
│          opp7102025 (TRANSAKCIONA)          │
│       643 tabele — dokumenti/transakcije    │
│                                             │
│  15 procedura + 2 trigera referenciraju opp │
│  ┌──────────────────────────────────────┐   │
│  │ fakture, kalkulacije, robno, gk ...  │   │
│  └──────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```
