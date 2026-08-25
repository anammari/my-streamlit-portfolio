import os
import streamlit as st
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from utils.constants import *

# Load local .env file (no-op if running on Streamlit Cloud)
load_dotenv(find_dotenv())

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

# Resolve API key: local .env first, then Streamlit Cloud secrets
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    api_key = st.secrets["OPENROUTER_API_KEY"]

# OpenRouter client (OpenAI-compatible)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

EMBED_MODEL = "nvidia/llama-nemotron-embed-vl-1b-v2:free"
LLM_MODEL = "nvidia/nemotron-3-ultra-550b-a55b:free"

# Set up Streamlit app
st.title("💬 Chat with My AI Assistant")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/styles_chat.css")

# Get the variables from constants.py
pronoun = info['Pronoun']
name = info['Name']
subject = info['Subject']
full_name = info['Full_Name']

# Initialize the chat history
if "messages" not in st.session_state:
    welcome_msg = f"Hi! I'm {name}'s AI Assistant, Buddy. How may I assist you today?"
    st.session_state.messages = [{"role": "assistant", "content": welcome_msg}]

# App sidebar
with st.sidebar:
    st.markdown("""
                # Chat with my AI assistant
                """)
    with st.expander("Click here to see FAQs"):
        st.info(
            f"""
            - Tell me a brief about {name}.
            - What does {subject} currently work?
            - What are {pronoun} strengths and weaknesses?
            - What is {pronoun} latest project?
            - When can {subject} start to work?
            - Tell me about {pronoun} professional background
            - What is {pronoun} skillset?
            - What is {pronoun} contact?
            - What are {pronoun} achievements?
            """
        )

    import json
    messages = st.session_state.messages
    if messages is not None:
        st.download_button(
            label="Download Chat",
            data=json.dumps(messages),
            file_name='chat.json',
            mime='json',
        )

    st.caption(f"© Made by {full_name} 2025. All rights reserved.")


def cosine_similarity(a, b):
    """Compute cosine similarity between two vectors."""
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def embed_text(text):
    """Embed a single text string via OpenRouter and return the embedding vector."""
    response = client.embeddings.create(
        model=EMBED_MODEL,
        input=text,
        encoding_format="float",
    )
    return response.data[0].embedding


def chunk_text(text, chunk_size=500, overlap=50):
    """Split text into overlapping chunks of approximately chunk_size characters."""
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks


# Create a cached function so the index is only built once
@st.cache_resource(show_spinner=False)
def build_index():
    with st.spinner("Initiating the AI assistant. Please hold..."):
        try:
            if not os.path.exists("data") or not os.listdir("data"):
                st.error("Data directory is missing or empty.")
                return None

            # Read the bio file
            bio_path = os.path.join("data", "bio.txt")
            with open(bio_path, "r", encoding="utf-8") as f:
                text = f.read()

            # Split into chunks
            chunks = chunk_text(text)

            # Embed each chunk
            index_data = []
            for chunk in chunks:
                embedding = embed_text(chunk)
                index_data.append({"text": chunk, "embedding": embedding})

            return index_data
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return None


def retrieve(query, index, top_k=3):
    """Retrieve the top_k most relevant chunks for a query."""
    query_embedding = embed_text(query)
    scored = []
    for item in index:
        score = cosine_similarity(query_embedding, item["embedding"])
        scored.append((score, item["text"]))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [text for _, text in scored[:top_k]]


# Load the index
index = build_index()

# Stop execution if index failed to load
if index is None:
    st.stop()


def ask_bot(user_query):
    """Generate a response using RAG: retrieve relevant context and query the LLM."""
    # Retrieve relevant chunks
    relevant_chunks = retrieve(user_query, index)

    # Build context from retrieved chunks
    context = "\n\n".join(relevant_chunks)

    system_prompt = f"""You are Buddy, an AI assistant dedicated to assisting {name} in {pronoun} job search by providing recruiters with relevant information about {pronoun} qualifications and achievements.
Your goal is to support {name} in presenting {pronoun} self effectively to potential employers and promoting {pronoun} candidacy for job opportunities.
Don't put "Buddy" or a breakline in the front of your answer.

Base your answer EXCLUSIVELY on the context below. Do not use any outside or prior knowledge, and do not guess or invent facts.
If the context states a specific fact (such as availability, salary, contact details, dates, or experience), report it EXACTLY as written in the context and never contradict, alter, or substitute a different value.
If the context does not contain the answer, politely say you don't know and direct the recruiter to contact {name} directly.

Context:
{context}"""

    # Call OpenRouter chat completions
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query},
        ],
        temperature=0.2,
        max_tokens=512,
    )

    return response.choices[0].message.content


# After the user enters a message, append that message to the message history
if prompt := st.chat_input("Your question"):  # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

# Iterate through the message history and display each message
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If the last message is not from the assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            response = ask_bot(prompt)
            st.write(response)
            message = {"role": "assistant", "content": response}
            st.session_state.messages.append(message)  # Add response to message history

# Suggested questions
questions = [
    f'Tell me a brief about {name}',
    f'What does {subject} currently work?',
    f'What certifications does {subject} have?',
    f'When can {subject} start to work?'
]

def send_button_ques(question):
    st.session_state.disabled = True
    response = ask_bot(question)
    st.session_state.messages.append({"role": "user", "content": question})  # display the user's message first
    st.session_state.messages.append({"role": "assistant", "content": response})  # display the AI message afterwards

if 'button_question' not in st.session_state:
    st.session_state['button_question'] = ""
if 'disabled' not in st.session_state:
    st.session_state['disabled'] = False

if st.session_state['disabled'] == False:
    for n, msg in enumerate(st.session_state.messages):
        # Render suggested question buttons
        buttons = st.container()
        if n == 0:
            for q in questions:
                button_ques = buttons.button(label=q, on_click=send_button_ques, args=[q], disabled=st.session_state.disabled)
