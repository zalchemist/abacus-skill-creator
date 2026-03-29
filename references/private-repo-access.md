# Pristup Abacus platformi sa privatnim GitHub repozitorijumom

**Svrha:** Kako dozvoliti samo Abacus AI aplikaciji da čita privatni GitHub repozitorijum, bez javnog postavljanja repozitorijuma.

---

## Pregled

Kada je `zalchemist/abacus-skills` repozitorijum **privatan**, Abacus AI ne može da ga učita direktno preko GitHub URL-a — osim ako mu je eksplicitno dat pristup.

Postoje dva načina za to:

| Metod | Opis | Preporučeno |
|-------|------|-------------|
| **GitHub Deploy Key** | SSH ključ vezan za jedan repozitorijum, samo za čitanje | ✅ Da |
| **Personal Access Token (PAT)** | Fine-grained token ograničen na jedan repozitorijum, samo za čitanje | ✅ Da |

---

## Metod 1: GitHub Deploy Key (preporučeno)

Deploy Key je SSH ključ koji se dodaje **isključivo jednom repozitorijumu**. Daje Abacus AI pravo čitanja bez pristupa ostatku naloga.

### Korak 1: Generisanje SSH ključ para

Na lokalnoj mašini ili u terminalu:

```bash
ssh-keygen -t ed25519 -C "abacus-deploy-key" -f ~/.ssh/abacus_deploy_key -N ""
```

Ovo kreira:
- `~/.ssh/abacus_deploy_key` — **privatni ključ** (za Abacus AI)
- `~/.ssh/abacus_deploy_key.pub` — **javni ključ** (za GitHub)

> ⚠️ **Bezbednost:** Privatni ključ nema lozinku (`-N ""`), što je potrebno za automatizovani pristup. Čuvaj fajl `~/.ssh/abacus_deploy_key` na bezbednom mestu i nikad ga ne deli javno niti komituj u repozitorijum.

### Korak 2: Dodavanje javnog ključa na GitHub

1. Otvori: `https://github.com/zalchemist/abacus-skills/settings/keys`
2. Klikni **Add deploy key**
3. Popuni:
   - **Title:** `Abacus AI Read Access`
   - **Key:** Zalepi sadržaj fajla `~/.ssh/abacus_deploy_key.pub`
   - **Allow write access:** ❌ (ostavi **isključeno** — samo čitanje)
4. Klikni **Add key**

### Korak 3: Unos privatnog ključa u Abacus AI

1. Otvori Abacus AI → **Settings** → **Integrations** → **GitHub**
2. Izaberi opciju **SSH Deploy Key** ili **Private Repository Access**
3. Zalepi sadržaj `~/.ssh/abacus_deploy_key` (privatni ključ)
4. Sačuvaj podešavanja

> **Napomena:** Tačan naziv opcije u Abacus AI interfejsu zavisi od verzije platforme. Ako opcija nije dostupna, koristi Metod 2.

---

## Metod 2: Fine-Grained Personal Access Token

GitHub fine-grained PAT može biti ograničen na **jedan repozitorijum** sa pravom samo čitanja.

### Korak 1: Kreiranje fine-grained PAT

1. Otvori: `https://github.com/settings/tokens?type=beta`
2. Klikni **Generate new token**
3. Popuni:
   - **Token name:** `abacus-skills-read`
   - **Expiration:** Po potrebi (npr. 1 godina)
   - **Repository access:** Izaberi **Only select repositories** → dodaj `zalchemist/abacus-skills`
   - **Permissions → Contents:** Podesi na **Read-only**
   - Sve ostale permisije ostave na **No access**
4. Klikni **Generate token** i **kopiraj token odmah** (prikazuje se samo jednom)

### Korak 2: Unos PAT u Abacus AI

1. Otvori Abacus AI → **Settings** → **Integrations** → **GitHub**
2. Unesi token u polje za GitHub Personal Access Token
3. Sačuvaj

---

## Verifikacija pristupa

Nakon konfiguracije, testiraj uvoz:

1. Abacus AI → **Agent Settings** → **Customize & Add Skills** → **+ New Skill**
2. Izaberi **GitHub** tab
3. Unesi URL privatnog repozitorijuma, npr.:
   `https://github.com/zalchemist/abacus-skills/tree/main/stock-analyzer/`
4. Klikni **Import from GitHub**

Ako je pristup ispravno konfigurisan, skill će se učitati bez greške.

---

## Revokacija pristupa

Da isključiš Abacus AI pristup u budućnosti:

- **Deploy Key:** `https://github.com/zalchemist/abacus-skills/settings/keys` → Delete
- **PAT:** `https://github.com/settings/tokens` → Delete token

Nakon revokacije, Abacus AI više neće moći da čita repozitorijum.

---

**Generisano od:** abacus-skill-creator  
**Primena:** Privatni repozitorijumi sa Abacus AI integracijom
