"""Tests for OpenRouter chat completion integration."""

import os
import pytest
from openai import OpenAI


@pytest.fixture
def client():
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        pytest.skip("OPENROUTER_API_KEY not set")
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )


LLM_MODEL = "openai/gpt-oss-20b:free"


def test_chat_completion(client):
    """Send a simple prompt and verify a non-empty response is returned."""
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": "Say hello in one word."}],
        max_tokens=10,
    )
    content = response.choices[0].message.content
    assert content is not None
    assert len(content.strip()) > 0


def test_chat_with_system_prompt(client):
    """Send a system prompt + user message and verify the response respects it."""
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": "You only reply with the word 'OK'."},
            {"role": "user", "content": "Tell me a story."},
        ],
        max_tokens=20,
    )
    content = response.choices[0].message.content.strip().lower()
    assert "ok" in content


def test_chat_empty_prompt(client):
    """Verify graceful handling of empty/short input."""
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": ""}],
        max_tokens=5,
    )
    # Should not raise an exception; may return empty or a short response
    assert response.choices[0].message.content is not None
