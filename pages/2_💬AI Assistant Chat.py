import os
import streamlit as st
from utils.constants import *
from llama_index.core import Settings
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import SimpleDirectoryReader, GPTVectorStoreIndex

# Local env ONLY
#from dotenv import load_dotenv, find_dotenv

# Local env ONLY
#_ = load_dotenv(find_dotenv())  # read local .env file

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

# Local env ONLY
#GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')
# Streamlit cloud
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]

# Set the Google and Gemini API key
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["GEMINI_API_KEY"] = GOOGLE_API_KEY

# Initialize the Gemini model and embeddings
Settings.llm = Gemini(model='models/gemini-2.5-flash-lite')

Settings.embed_model = GeminiEmbedding()

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

# Load documents and build the index
if not os.path.exists("data") or not os.listdir("data"):
    st.write("Data directory is missing or empty.")
with st.spinner("Initiating the AI assistant. Please hold..."):
    try:
        path = "data"
        reader = SimpleDirectoryReader(path, recursive=True)
        documents = reader.load_data()
        index = GPTVectorStoreIndex.from_documents(documents)
    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.exception(e)

def ask_bot(user_query):
    global index

    PROMPT_QUESTION = """You are Buddy, an AI assistant dedicated to assisting {name} in {pronoun} job search by providing recruiters with relevant information about {pronoun} qualifications and achievements. 
    Your goal is to support {name} in presenting {pronoun} self effectively to potential employers and promoting {pronoun} candidacy for job opportunities.
    If you do not know the answer, politely admit it and let recruiters know how to contact {name} to get more information directly from {pronoun}. 
    Don't put "Buddy" or a breakline in the front of your answer.
    Human: {input}
    """

    # Query the index for the AI's response
    query_engine = index.as_query_engine()
    response = query_engine.query(PROMPT_QUESTION.format(name=name, pronoun=pronoun, input=user_query))
    return response

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
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
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
    st.session_state.messages.append({"role": "assistant", "content": response.response})  # display the AI message afterwards

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