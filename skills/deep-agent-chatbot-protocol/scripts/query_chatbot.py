#!/usr/bin/env python3
"""
Skripta za komunikaciju sa Knowledge Brain Chatbot-om.
Koristi se iz DeepAgent sesija.
"""

import os

from abacusai import ApiClient


def _require_env(name: str) -> str:
    """Read a required environment variable or raise a clear error."""
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Set {name} environment variable")
    return value

def get_context(user_prompt: str, api_key: str) -> str:
    """Dobij kontekst od Chatbot-a pre početka rada."""
    client = ApiClient(api_key=api_key)
    deployment_token = _require_env("KB_CHATBOT_DEPLOYMENT_TOKEN")
    deployment_id = _require_env("KB_CHATBOT_DEPLOYMENT_ID")

    response = client.get_chat_response(
        deployment_token=deployment_token,
        deployment_id=deployment_id,
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
    deployment_token = _require_env("KB_CHATBOT_DEPLOYMENT_TOKEN")
    deployment_id = _require_env("KB_CHATBOT_DEPLOYMENT_ID")

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
        deployment_token=deployment_token,
        deployment_id=deployment_id,
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
