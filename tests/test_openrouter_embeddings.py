"""Tests for OpenRouter embeddings integration."""

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


EMBED_MODEL = "nvidia/llama-nemotron-embed-vl-1b-v2:free"


def test_embed_single_text(client):
    """Embed a short string and verify the response contains a valid embedding vector."""
    response = client.embeddings.create(
        model=EMBED_MODEL,
        input="Hello, world!",
        encoding_format="float",
    )
    assert len(response.data) == 1
    embedding = response.data[0].embedding
    assert isinstance(embedding, list)
    assert len(embedding) > 0
    assert all(isinstance(v, (int, float)) for v in embedding)


def test_embed_multiple_texts(client):
    """Embed an array of strings and verify the correct number of embeddings."""
    texts = ["First text", "Second text", "Third text"]
    response = client.embeddings.create(
        model=EMBED_MODEL,
        input=texts,
        encoding_format="float",
    )
    assert len(response.data) == 3
    for item in response.data:
        assert isinstance(item.embedding, list)
        assert len(item.embedding) > 0


def test_embedding_dimensions(client):
    """Verify the embedding vector has consistent dimensions."""
    response = client.embeddings.create(
        model=EMBED_MODEL,
        input="Consistency check",
        encoding_format="float",
    )
    dims = len(response.data[0].embedding)
    assert dims > 0
    # Embed the same text again and verify same dimensions
    response2 = client.embeddings.create(
        model=EMBED_MODEL,
        input="Another text",
        encoding_format="float",
    )
    assert len(response2.data[0].embedding) == dims
