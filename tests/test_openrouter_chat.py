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


LLM_MODEL = "nvidia/nemotron-3-ultra-550b-a55b:free"


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
    """Send a system prompt + user message and verify the response respects the context."""
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": "Ahmad is an AI Engineer with 13+ years of experience in RAG."},
            {"role": "user", "content": "How many years of experience does Ahmad have?"},
        ],
        max_tokens=60,
    )
    content = response.choices[0].message.content
    assert content is not None
    assert len(content.strip()) > 0
    assert "13" in content


def test_chat_empty_prompt(client):
    """Verify empty input is rejected gracefully by the provider (BadRequestError, not a crash)."""
    with pytest.raises(Exception):
        client.chat.completions.create(
            model=LLM_MODEL,
            messages=[{"role": "user", "content": ""}],
            max_tokens=5,
        )
