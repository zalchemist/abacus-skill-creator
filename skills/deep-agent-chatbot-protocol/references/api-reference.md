# Chatbot API Reference

## Endpoint
Abacus.AI Python SDK: `get_chat_response()`

## Credentials
- deployment handle: `<DEPLOYMENT_HANDLE>`
- deployment identifier: `<DEPLOYMENT_IDENTIFIER>`
- api_key: Korisnikov API ključ (https://abacus.ai/app/profile/apikey)

## Response format
```json
{
  "messages": [
    {"is_user": true, "text": "..."},
    {"is_user": false, "text": "ODGOVOR CHATBOTA"}
  ]
}
```
