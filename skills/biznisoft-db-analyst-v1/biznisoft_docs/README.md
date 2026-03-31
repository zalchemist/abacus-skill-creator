# BizniSoft dokumentacija sa sajta

Ovaj folder sadrži uputstva i novosti preuzete sa zvaničnog BizniSoft sajta:
https://www.biznisoft.com/podrska

## Struktura

```
biznisoft_docs/
├── README.md                  ← ovaj fajl
├── tekstualna_uputstva/       ← uputstva sa https://www.biznisoft.com/podrska#tekstualna-uputstva
│   └── *.md                   ← jedno uputstvo = jedan .md fajl
├── video_uputstva/            ← linkovi i opisi video uputstava
│   └── *.md                   ← jedno video uputstvo = jedan .md fajl (link + opis + tagovi)
└── verzije_i_novosti/         ← novosti o verzijama i ažuriranjima
    └── *.md                   ← jedna verzija/novost = jedan .md fajl
```

## Kako se ažurira

Ovaj folder **ažurira poseban agent** (BizniSoft docs scraper) koji:
1. Periodično posećuje https://www.biznisoft.com/podrska
2. Preuzima nova i izmenjena uputstva
3. Konvertuje HTML sadržaj u Markdown format
4. Čuva fajlove u odgovarajuće podfoldere
5. Commit-uje izmene u git

### Konvencije imenovanja fajlova

- **Tekstualna uputstva:** `tema-uputstva.md` (npr. `kalkulacije-robe.md`, `pdv-evidencija.md`)
- **Video uputstva:** `video-naziv-teme.md` (npr. `video-fakturisanje.md`)
- **Verzije:** `verzija-XXXX.md` (npr. `verzija-1082.md`)

### Format pojedinačnog fajla

```markdown
---
naslov: Naslov uputstva
izvor_url: https://www.biznisoft.com/...
datum_preuzimanja: 2026-03-30
kategorija: tekstualno | video | verzija
tagovi: [tag1, tag2, tag3]
---

# Naslov

Sadržaj uputstva u Markdown formatu...
```

## Napomene

- **Ne menjati ručno** — sadržaj se automatski regeneriše pri sledećem ažuriranju
- Ako agent za analizu baze otkrije da neko uputstvo nedostaje, može zatražiti ažuriranje
- Fajlovi se ne brišu automatski — samo dodaju ili ažuriraju
- Ovaj folder je **read-only** za biznisoft-db-analyst skill — koristi ga samo kao referencu
