# Deep Agent - Chatbot Protocol

Ovaj skill definiše OBAVEZNU proceduru komunikacije između DeepAgent-a i Knowledge Brain Chatbot-a.

## KADA SE KORISTI
UVEK kada DeepAgent započinje bilo koji zadatak za korisnika.

## PROCEDURA

### KORAK 0: PRE POČETKA RADA (OBAVEZNO)

Pre nego što počneš bilo šta da radiš, MORAŠ da:

1. Pozoveš Chatbot API sa formatom [DEEP_AGENT_QUERY]
2. Sačekaš odgovor sa kontekstom
3. Tek onda počneš sa zadatkom

**API poziv:**
```python
from abacusai import ApiClient

client = ApiClient(api_key="<USER_API_KEY>")
response = client.get_chat_response(
    deployment_token='<YOUR_CHATBOT_DEPLOYMENT_TOKEN>',
    deployment_id='<YOUR_CHATBOT_DEPLOYMENT_ID>',
    messages=[{
        'is_user': True,
        'text': f'''[DEEP_AGENT_QUERY]
Korisnik traži: "{korisnikov_prompt}"

Daj mi:
1. Relevantno znanje o ovoj temi
2. Prethodne greške da izbegnem
3. Korisnikove preferencije
4. Prioriteti za ovaj tip zadatka
5. Anti-patterns - šta NE raditi'''
    }]
)
kontekst = response['messages'][-1]['text']
```

### KORAK N: TOKOM RADA

Ako naiđeš na značajnu grešku ili naučiš nešto novo, možeš (opciono) poslati update:

```python
client.get_chat_response(
    deployment_token='<YOUR_CHATBOT_DEPLOYMENT_TOKEN>',
    deployment_id='<YOUR_CHATBOT_DEPLOYMENT_ID>',
    messages=[{
        'is_user': True,
        'text': f'''[DEEP_AGENT_UPDATE]
Greška: {opis_greske}
Rešenje: {kako_sam_resio}'''
    }]
)
```

### KORAK FINAL: NAKON ZAVRŠETKA (OBAVEZNO)

Kada završiš zadatak, MORAŠ da pošalješ izveštaj:

```python
client.get_chat_response(
    deployment_token='<YOUR_CHATBOT_DEPLOYMENT_TOKEN>',
    deployment_id='<YOUR_CHATBOT_DEPLOYMENT_ID>',
    messages=[{
        'is_user': True,
        'text': f'''[DEEP_AGENT_REPORT]
## Korisnikov zahtev
{originalni_prompt}

## Šta sam uradio
{lista_koraka}

## Greške i kako sam ih rešio
{greske_i_resenja}

## Korisnikov feedback
{feedback_ako_postoji}

## Naučene lekcije
{sta_sam_naucio}

## Preporuke za ubuduće
{preporuke}'''
    }]
)
```

## PRIORITETI ZNANJA (od Chatbot-a)

Kada dobiješ odgovor od Chatbot-a, poštuj prioritete:
1. **ANTI-PATTERNS** - ovo NIKAD ne radi
2. **PRETHODNE GREŠKE** - izbegavaj iste greške
3. **KORISNIKOVE PREFERENCIJE** - poštuj stil i format
4. **RELEVANTNO ZNANJE** - koristi kao kontekst

## GITHUB SINHRONIZACIJA

Za trajno čuvanje, koristi GitHub strukturu:
- `abacus-workspace/projects/biznisoft_skill_input/knowledge/` - znanje
- `abacus-workspace/projects/biznisoft_skill_input/sessions/` - logovi sesija
- `abacus-workspace/projects/biznisoft_skill_input/learning/` - obrasci

## NAPOMENA

Ovaj protokol osigurava da DeepAgent:
- Nikad ne počinje "od nule"
- Uči iz prethodnih sesija
- Poštuje korisnikove preferencije
- Ne ponavlja iste greške
