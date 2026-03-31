#!/usr/bin/env python3
"""
Skripta za komunikaciju sa Knowledge Brain Chatbot-om.
Koristi se iz DeepAgent sesija.
"""

from abacusai import ApiClient
import os

DEPLOYMENT_TOKEN = 'aa12e1f29bf945c8a5fa0ae203873ff2'
DEPLOYMENT_ID = '14e982c370'

def get_context(user_prompt: str, api_key: str) -> str:
    """Dobij kontekst od Chatbot-a pre početka rada."""
    client = ApiClient(api_key=api_key)
    
    response = client.get_chat_response(
        deployment_token=DEPLOYMENT_TOKEN,
        deployment_id=DEPLOYMENT_ID,
        messages=[{
            'is_user': True,
            'text': f'''[DEEP_AGENT_QUERY]
Korisnik traži: "{user_prompt}"

Daj mi:
1. Relevantno znanje o ovoj temi
2. Prethodne greške da izbegnem
3. Korisnikove preferencije
4. Prioriteti za ovaj tip zadatka
5. Anti-patterns - šta NE raditi'''
        }]
    )
    
    return response['messages'][-1]['text']

def send_report(report: dict, api_key: str) -> str:
    """Pošalji izveštaj o sesiji Chatbot-u."""
    client = ApiClient(api_key=api_key)
    
    report_text = f'''[DEEP_AGENT_REPORT]
## Korisnikov zahtev
{report.get('user_prompt', 'N/A')}

## Šta sam uradio
{report.get('steps', 'N/A')}

## Greške i kako sam ih rešio
{report.get('errors', 'Bez grešaka')}

## Korisnikov feedback
{report.get('feedback', 'Nema feedback-a')}

## Naučene lekcije
{report.get('lessons', 'N/A')}

## Preporuke za ubuduće
{report.get('recommendations', 'N/A')}'''
    
    response = client.get_chat_response(
        deployment_token=DEPLOYMENT_TOKEN,
        deployment_id=DEPLOYMENT_ID,
        messages=[{'is_user': True, 'text': report_text}]
    )
    
    return response['messages'][-1]['text']

if __name__ == '__main__':
    # Test
    api_key = os.environ.get('ABACUS_API_KEY')
    if api_key:
        print(get_context("Test prompt", api_key))
    else:
        print("Set ABACUS_API_KEY environment variable")
