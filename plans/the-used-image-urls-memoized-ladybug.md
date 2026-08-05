# Fix: Nvidia Embeddings encoding_format

## Context

The AI Chat page errors with:
```
Nvidia embeddings do not support base64 encoding_format. Use float instead, or omit encoding_format.
```

The OpenAI Python SDK defaults to `base64` encoding for embeddings, but `nvidia/llama-nemotron-embed-vl-1b-v2:free` on OpenRouter only supports `float`.

## Fix

Add `encoding_format="float"` to the `client.embeddings.create()` call in `embed_text()`.

## File to Modify

**`pages/2_💬AI Assistant Chat.py`** line 91 — add `encoding_format="float"` parameter.

## Verification

1. Run `streamlit run 💼Portfolio.py`
2. Navigate to AI Chat page — it should load without errors
3. Send a test question — should get a valid response
