# my-streamlit-portfolio

A personal portfolio website built with **Streamlit** — featuring an interactive resume, project showcase, and an AI assistant that answers questions about my background using RAG (Retrieval-Augmented Generation).

👉 **[Live Demo](https://my-data-science-portfolio.streamlit.app/)**

---

## ✨ Features

- **Portfolio Page** — Hero section, project showcase, my YouTube channel playlists, skills with animations, career timeline, PowerBI dashboard, SlideShare gallery, coworker endorsements, and a contact form
- **AI Assistant Chat** — Ask questions about my background, skills, experience, and projects. Powered by a free OpenRouter LLM with RAG over my bio document
- **Resume Viewer** — In-browser PDF viewer

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Framework** | Streamlit |
| **AI Chat** | OpenRouter (`nvidia/nemotron-3-ultra-550b-a55b:free` + `nvidia/llama-nemotron-embed-vl-1b-v2:free`) |
| **RAG** | In-memory vector search with cosine similarity |
| **Styling** | Custom CSS |
| **Animations** | Lottie JSON |
| **Timeline** | streamlit-timeline |
| **Deployment** | Streamlit Cloud |

---

## 📁 Project Structure

```
my-streamlit-portfolio/
├── 💼Portfolio.py                 # Main portfolio page
├── pages/
│   ├── 2_💬AI Assistant Chat.py  # AI chat with RAG
│   └── 3_📄Resume.py             # Resume PDF viewer
├── utils/constants.py             # All config (projects, slides, youtube_playlists, etc.)
├── data/bio.txt                   # RAG source document for AI chat
├── images/                        # Profile photo + resume PDF
├── style/                         # Custom CSS files
├── lottie/                        # Lottie animation JSON files
├── tests/                         # Test suite
├── work_history.json              # Career timeline data
└── requirements.txt
```

---

## 🚀 Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/anammari/my-streamlit-portfolio.git
cd my-streamlit-portfolio

# 2. Install dependencies
pip install -r requirements.txt

# 3. Get an OpenRouter API key
#    Go to https://openrouter.ai/keys, sign up (free), and create a key

# 4. Set up your environment
cp .env.example .env
# Then edit .env and paste your OpenRouter API key

# 5. Run the app
streamlit run 💼Portfolio.py
```

---

## ☁️ Deploy to Streamlit Cloud

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Add `OPENROUTER_API_KEY` in **Streamlit Cloud → Settings → Secrets**
4. The app auto-deploys on every push to `main`

---

## 🧪 Running Tests

```bash
python -m pytest tests/ -v
```

---

## 📄 License

© 2025 Ahmad Ammari. All rights reserved.
