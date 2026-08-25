# my-streamlit-portfolio

## Project Overview

A Streamlit-based personal portfolio website for Ahmad Ammari, featuring a main portfolio page, an AI-powered chat assistant (RAG over a bio document via OpenRouter), and a resume viewer. Deployed on Streamlit Cloud.

## Tech Stack

- **Framework**: Streamlit 1.41.1
- **AI Chat**: OpenRouter (OpenAI-compatible API) — RAG with in-memory vector search
- **LLM**: `nvidia/nemotron-3-ultra-550b-a55b:free` via OpenRouter
- **Embeddings**: `nvidia/llama-nemotron-embed-vl-1b-v2:free` via OpenRouter
- **Styling**: Custom CSS (`style/styles_main.css`, `style/styles_chat.css`)
- **Animations**: Lottie JSON animations (`lottie/`)
- **Timeline**: `streamlit-timeline` (JSON-driven work history)
- **Deployment**: Streamlit Cloud (secrets via `st.secrets["OPENROUTER_API_KEY"]`)
- **Dev Container**: `.devcontainer/devcontainer.json` (Python 3.11, Codespaces-ready)

## Project Tree

```
my-streamlit-portfolio/
├── 💼Portfolio.py                  # Main portfolio page (hero, projects, skills, timeline, PowerBI, SlideShare, endorsements, contact)
├── pages/
│   ├── 2_💬AI Assistant Chat.py    # AI chat page — RAG over bio.txt via OpenRouter
│   └── 3_📄Resume.py              # Resume viewer (PDF from images/resume.pdf)
├── utils/
│   └── constants.py               # All config: info dict, projects list, endorsements, slides list
├── data/
│   └── bio.txt                     # RAG source document for AI chat
├── images/
│   ├── profile.png                 # Profile photo
│   └── resume.pdf                  # CV PDF
├── style/
│   ├── styles_main.css             # Main page styles
│   └── styles_chat.css             # Chat page styles
├── lottie/                         # Lottie animation JSON files
├── tests/                          # Test suite (see Tests section)
├── work_history.json               # Timeline data for streamlit-timeline
├── .streamlit/config.toml          # Streamlit server/theme config
├── .env                            # Local env (OPENROUTER_API_KEY)
├── .gitignore
├── requirements.txt
├── CLAUDE.md
└── README.md
```

## Key Files

### `💼Portfolio.py`
Main entry point. Sections: Hero + About, Project Showcase (6 projects from constants.py), Skills (Lottie icons), Career History (timeline from work_history.json), PowerBI Dashboard (iframe), SlideShare (curated slide grid from constants.py), Coworker Endorsements (image slideshow), Contact Form (formsubmit.co).

### `pages/2_💬AI Assistant Chat.py`
RAG chatbot using OpenRouter (OpenAI-compatible API). Loads `data/bio.txt` → splits into chunks → embeds via OpenRouter → stores in-memory index. On query: embeds query, finds top-3 similar chunks via cosine similarity, sends context + query to OpenRouter chat completions.

### `utils/constants.py`
Central config file containing:
- `info` dict: Name, Intro, About, links (Project, Medium/SlideShare, Tableau/PowerBI, ScreenPal, Resume, Email)
- `projects` list: 6 project entries with title, description, image_url, link
- `slides` list: 7 curated SlideShare entries with title, url, thumbnail, slides, views
- `endorsements` dict: 5 image URLs for the slideshow
- `chat` dict: Menu styling configs

### `data/bio.txt`
The RAG source document. Contains: About, Current/Past Work Experience, Projects, Career Goal, Skills, Certifications, Achievements, Contact, Strengths/Weaknesses, Interests, Availability, Online Presence, Salary, References.

## How the AI Chat Works

1. On page load, `build_index()` is called (cached via `@st.cache_resource`)
2. It reads `data/bio.txt`, splits into overlapping chunks of ~500 words
3. Each chunk is embedded via OpenRouter's `nvidia/llama-nemotron-embed-vl-1b-v2:free` model
4. Chunks and their embeddings are stored in memory as the index
5. User query is embedded the same way, then cosine similarity finds the top-3 most relevant chunks
6. Retrieved chunks are injected into a system prompt as context
7. The system prompt + user query are sent to OpenRouter's `nvidia/nemotron-3-ultra-550b-a55b:free` for answer generation
8. Chat history is maintained in `st.session_state.messages`

## Dependencies (requirements.txt)

- `openai>=1.12.0`, `numpy`
- `streamlit==1.41.1`, `streamlit-option-menu`, `streamlit-extras`, `streamlit-lottie`, `streamlit-timeline`
- `python-dotenv`
- `pytest`, `pytest-mock` (dev)

## Running Locally

```bash
pip install -r requirements.txt
# Ensure .env has OPENROUTER_API_KEY
streamlit run 💼Portfolio.py
```

## Deployment

Streamlit Cloud. Secrets configured via Streamlit dashboard (`OPENROUTER_API_KEY`).

## Tests

```bash
# All tests
python -m pytest tests/ -v
```

| Test File | What It Tests |
|-----------|---------------|
| `tests/test_constants.py` | Updated About/Intro text, projects structure |
| `tests/test_bio_txt.py` | bio.txt contains new roles, skills, 13+ years |
| `tests/test_slideshare.py` | Curated slide list structure and URL validity |
| `tests/test_rag_pipeline.py` | chunk_text, cosine_similarity, retrieve, mocked ask_bot |
| `tests/test_openrouter_chat.py` | OpenRouter chat completion (requires API key) |
| `tests/test_openrouter_embeddings.py` | OpenRouter embeddings (requires API key) |


