"""Tests for the RAG pipeline logic (without Streamlit UI)."""

import os
import sys
import importlib.util
import numpy as np
import pytest
from unittest.mock import patch, MagicMock

# Set a dummy API key before importing the chat module (avoids st.secrets lookup)
os.environ["OPENROUTER_API_KEY"] = "sk-or-test-key"

# Dynamically load the chat module (filename has emoji and spaces)
CHAT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "pages", "2_💬AI Assistant Chat.py")
spec = importlib.util.spec_from_file_location("chat_module", CHAT_PATH)
chat = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chat)

chunk_text = chat.chunk_text
cosine_similarity = chat.cosine_similarity
retrieve = chat.retrieve


# --- chunk_text tests ---

def test_chunk_text_basic():
    """Verify chunk_text splits text into expected number of chunks."""
    text = "word " * 1000  # 1000 words
    chunks = chunk_text(text, chunk_size=200, overlap=20)
    assert len(chunks) > 0
    for chunk in chunks:
        assert len(chunk.split()) <= 200


def test_chunk_text_small_input():
    """Verify chunk_text handles text smaller than chunk_size."""
    text = "small text here"
    chunks = chunk_text(text, chunk_size=500, overlap=50)
    assert len(chunks) == 1
    assert chunks[0] == text


def test_chunk_text_empty_input():
    """Verify chunk_text handles empty input."""
    chunks = chunk_text("", chunk_size=500, overlap=50)
    assert chunks == []


# --- cosine_similarity tests ---

def test_cosine_similarity_identical():
    """Verify cosine similarity returns 1.0 for identical vectors."""
    v = [1.0, 2.0, 3.0]
    assert cosine_similarity(v, v) == pytest.approx(1.0)


def test_cosine_similarity_orthogonal():
    """Verify cosine similarity returns ~0 for orthogonal vectors."""
    a = [1.0, 0.0]
    b = [0.0, 1.0]
    assert cosine_similarity(a, b) == pytest.approx(0.0, abs=1e-10)


def test_cosine_similarity_opposite():
    """Verify cosine similarity returns -1.0 for opposite vectors."""
    a = [1.0, 2.0]
    b = [-1.0, -2.0]
    assert cosine_similarity(a, b) == pytest.approx(-1.0, abs=1e-10)


# --- retrieve tests ---

def make_fake_index():
    """Create a small fake index for testing retrieval."""
    return [
        {"text": "Ahmad is an AI Engineer working on agentic systems.", "embedding": [1.0, 0.0, 0.0]},
        {"text": "Python is a programming language used for data science.", "embedding": [0.0, 1.0, 0.0]},
        {"text": "Temporal.io is used for orchestrating workflows.", "embedding": [0.0, 0.0, 1.0]},
    ]


@patch.object(chat, "embed_text")
def test_retrieve_top_k(mock_embed_text):
    """Verify retrieve returns the correct number of results in similarity order."""
    mock_embed_text.return_value = [0.9, 0.1, 0.0]

    index = make_fake_index()
    results = retrieve("AI Engineer query", index, top_k=2)

    assert len(results) == 2
    assert "AI Engineer" in results[0]


@patch.object(chat, "embed_text")
def test_retrieve_relevance(mock_embed_text):
    """Verify the most relevant chunk is ranked first."""
    mock_embed_text.return_value = [0.0, 0.0, 0.9]

    index = make_fake_index()
    results = retrieve("workflow orchestration", index, top_k=3)

    assert "Temporal.io" in results[0]


@patch.object(chat, "embed_text")
def test_retrieve_empty_index(mock_embed_text):
    """Verify retrieve handles an empty index gracefully."""
    mock_embed_text.return_value = [0.0, 0.0, 0.0]
    results = retrieve("anything", [], top_k=3)
    assert results == []


@patch.object(chat, "client")
@patch.object(chat, "embed_text")
def test_ask_bot(mock_embed_text, mock_client):
    """Verify ask_bot generates a response using mocked OpenRouter client."""
    if chat.index is None:
        pytest.skip("Index not loaded (no data/ directory or API key)")

    mock_embed_text.return_value = [0.0, 0.0, 0.0]

    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = "Ahmad is an AI Engineer."
    mock_client.chat.completions.create.return_value = mock_response

    response = chat.ask_bot("Tell me about Ahmad")
    assert response == "Ahmad is an AI Engineer."
