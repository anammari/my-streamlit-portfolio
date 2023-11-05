import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from constant import *
from PIL import Image
import openai
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.indexes import VectorstoreIndexCreator
import os
from dotenv import load_dotenv, find_dotenv
import json

st.set_page_config(page_title='Template' ,layout="wide",page_icon='👧🏻')
_ = load_dotenv(find_dotenv()) # read local .env file

# -----------------  loading assets  ----------------- #
st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)
    
def load_lottieurl(file_name):
    with open(f"./lottie/{file_name}.json") as f:
        return json.load(f)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

# loading assets
lottie_gif = load_lottieurl("lottie")
python_lottie = load_lottieurl("python")
spark_lottie = load_lottieurl("spark")
azure_lottie = load_lottieurl("azure")
aws_lottie = load_lottieurl("aws")
docker_lottie = load_lottieurl("docker")
mlflow_lottie = load_lottieurl("mlflow")
openai_lottie = load_lottieurl("openai")
pandas_lottie = load_lottieurl("pandas")

# load the bio file
loader = CSVLoader(file_path="bio.csv", encoding='utf-8')

# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,3])

full_name = info['Full_Name']
with col1:
    gradient('#FFD4DD','#000395','e0fbfc',f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
    st.write(info['About'])
    
    
with col2:
    st_lottie(lottie_gif, height=280, key="data")
        

# -----------------  chatbot  ----------------- #
# Set up the OpenAI key
openai_api_key = os.environ['OPENAI_API_KEY']
openai.api_key = (openai_api_key)

pronoun = info["Pronoun"]
name = info["Name"]
def ask_bot(input_text):
    # define LLM
    llm_model = "gpt-3.5-turbo"
    llm = ChatOpenAI(temperature = 0.0, model=llm_model)
    # define embedding
    embeddings = OpenAIEmbeddings()
    # load index
    index = VectorstoreIndexCreator(
        vectorstore_cls=DocArrayInMemorySearch,
        embedding=embeddings
        ).from_loaders([loader]) 
    
    # query LlamaIndex and GPT-3.5 for the AI's response
    PROMPT_QUESTION = f"""You are Buddy, an AI assistant dedicated to assisting {name} in her job search by providing recruiters with relevant and concise information. 
    If you do not know the answer, politely admit it and let recruiters know how to contact {name} to get more information directly from {pronoun}. 
    Don't put "Buddy" or a breakline in the front of your answer.
    Answer the question very specifically and just to the point. Do not write the whole available information about {name}.
    Human: {input_text}
    """
    output = index.query(PROMPT_QUESTION, llm=llm)
    return output

with st.container():
    st.subheader('🤖 Ask AI about me!')

# get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("To know more about me, you can write down your questions to my AI agent, Buddy, and hit Enter!", key="input")
    return input_text

#st.markdown("Chat With Me Now")
user_input = get_text()

if user_input:
  #text = st.text_area('Enter your questions')
  if openai_api_key.startswith('sk-'):
    st.markdown(ask_bot(user_input))

# ----------------- skillset ----------------- #
with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=70,width=70, key="python", speed=0.5)
    with col2:
        st_lottie(spark_lottie, height=70,width=70, key="spark", speed=0.5)
    with col3:
        st_lottie(azure_lottie,height=70,width=70, key="azure", speed=0.5)
    with col4:
        st_lottie(aws_lottie,height=70,width=70, key="aws", speed=0.5)
    with col1:
        st_lottie(docker_lottie,height=50,width=50, key="docker", speed=0.5)
    with col2:
        st_lottie(mlflow_lottie,height=70,width=70, key="mlflow", speed=0.5)
    with col3:
        st_lottie(openai_lottie,height=50,width=50, key="openai", speed=0.5)
    with col4:
        st_lottie(pandas_lottie,height=50,width=50, key="pandas", speed=0.5)

# ----------------- timeline ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('📌 Career History')

    # load data
    with open('work_history.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=400)

# -----------------  PowerBI  -----------------  #
powerbi_html = """
<iframe title="Report Section" width="100%" height="486" src="https://shorturl.at/mrY27" frameborder="0" allowFullScreen="true"></iframe>
"""
with st.container():
    st.markdown("""""")
    st.subheader("📊 PowerBI Dashboard I did!")
    col1,col2 = st.columns([0.95, 0.05])
    with col1:
        with st.expander('Explore my Demo Sales Dashboard'):
            components.html(
                f"""
                <!DOCTYPE html>
                <html>  
                    <title>Basic HTML</title>  
                    <body style="width:100%">  
                    {powerbi_html}
                    </body>  
                </HTML>
                """
            , height=486, width=1100, scrolling=True
            )
    st.markdown(""" <a href={}> <em>🔗 Access Dashboard on the Web </a>""".format(info['Tableau']), unsafe_allow_html=True)
    st.markdown(""" <a href={}> <em>👀 Watch a Dashboard Demo</a>""".format(info['ScreenPal']), unsafe_allow_html=True)

# -----------------  endorsement  ----------------- #
with st.container():
    # Divide the container into three columns
    col1,col2,col3 = st.columns([0.55, 0.40, 0.05])
    # In the first column (col1)        
    with col1:
        # Add a subheader to introduce the coworker endorsement slideshow
        st.subheader("👄 Coworker Endorsements")
        # Embed an HTML component to display the slideshow
        components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Styles for the slideshow -->
        <style>
            * {{box-sizing: border-box;}}
            .mySlides {{display: none;}}
            img {{vertical-align: middle;}}

            /* Slideshow container */
            .slideshow-container {{
            position: relative;
            margin: auto;
            width: 100%;
            }}

            /* The dots/bullets/indicators */
            .dot {{
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #eaeaea;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
            }}

            .active {{
            background-color: #6F6F6F;
            }}

            /* Fading animation */
            .fade {{
            animation-name: fade;
            animation-duration: 1s;
            }}

            @keyframes fade {{
            from {{opacity: .4}} 
            to {{opacity: 1}}
            }}

            /* On smaller screens, decrease text size */
            @media only screen and (max-width: 300px) {{
            .text {{font-size: 11px}}
            }}
            </style>
        </head>
        <body>
            <!-- Slideshow container -->
            <div class="slideshow-container">
                <div class="mySlides fade">
                <img src={endorsements["img1"]} style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src={endorsements["img2"]} style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src={endorsements["img3"]} style="width:100%">
                </div>
                
                <div class="mySlides fade">
                <img src={endorsements["img4"]} style="width:100%">
                </div>
                
                <div class="mySlides fade">
                <img src={endorsements["img5"]} style="width:100%">
                </div>

            </div>
            <br>
            <!-- Navigation dots -->
            <div style="text-align:center">
                <span class="dot"></span> 
                <span class="dot"></span> 
                <span class="dot"></span>
                <span class="dot"></span>
                <span class="dot"></span>
            </div>

            <script>
            let slideIndex = 0;
            showSlides();

            function showSlides() {{
            let i;
            let slides = document.getElementsByClassName("mySlides");
            let dots = document.getElementsByClassName("dot");
            for (i = 0; i < slides.length; i++) {{
                slides[i].style.display = "none";  
            }}
            slideIndex++;
            if (slideIndex > slides.length) {{slideIndex = 1}}    
            for (i = 0; i < dots.length; i++) {{
                dots[i].className = dots[i].className.replace("active", "");
            }}
            slides[slideIndex-1].style.display = "block";  
            dots[slideIndex-1].className += " active";
            }}

            var interval = setInterval(showSlides, 10000); // Change image every 10 seconds

            function pauseSlides(event)
            {{
                clearInterval(interval); // Clear the interval we set earlier
            }}
            function resumeSlides(event)
            {{
                interval = setInterval(showSlides, 10000);
            }}
            // Set up event listeners for the mySlides
            var mySlides = document.getElementsByClassName("mySlides");
            for (i = 0; i < mySlides.length; i++) {{
            mySlides[i].onmouseover = pauseSlides;
            mySlides[i].onmouseout = resumeSlides;
            }}
            </script>

            </body>
            </html> 

            """,
                height=270,
    )  

# -----------------  contact  ----------------- #
    with col2:
        st.subheader("📨 Contact Me")
        contact_form = f"""
        <form action="https://formsubmit.co/{info["Email"]}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
