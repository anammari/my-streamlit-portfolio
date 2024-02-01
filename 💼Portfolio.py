# import the Streamlit library
import streamlit as st
from streamlit_option_menu import option_menu
from utils.constants import *
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import json

# configure page settings
st.set_page_config(page_title='Template' ,layout="wide",initial_sidebar_state="auto", page_icon='👧🏻') # always show the sidebar

# load local CSS styles
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/styles_main.css")

# get the variables from constants.py
pronoun = info['Pronoun']

def load_lottieurl(file_name):
    with open(f"./lottie/{file_name}.json") as f:
        return json.load(f)
    
# loading assets
python_lottie = load_lottieurl("python")
spark_lottie = load_lottieurl("spark")
azure_lottie = load_lottieurl("azure")
aws_lottie = load_lottieurl("aws")
docker_lottie = load_lottieurl("docker")
mlflow_lottie = load_lottieurl("mlflow")
openai_lottie = load_lottieurl("openai")
pandas_lottie = load_lottieurl("pandas")

# app sidebar
with st.sidebar:
    st.markdown("""
                # Chat with my AI assistant
                """)
    with st.expander("Click here to see FAQs"):
        st.info(
            f"""
            - What are {pronoun} strengths and weaknesses?
            - What is {pronoun} expected salary?
            - What is {pronoun} latest work project?
            - When can {pronoun} start to work?
            - Tell me about {pronoun} professional background
            - What is {pronoun} skillset?
            - What is {pronoun} contact?
            - What are {pronoun} achievements?
            """
        )
        
    st.caption(f"© Made by Ahmad Ammari 2024. All rights reserved.")

import requests

def hero(content1, content2):
    st.markdown(f'<h1 style="text-align:center;font-size:60px;border-radius:2%;">'
                f'<span>{content1}</span><br>'
                f'<span style="color:black;font-size:22px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,3])

full_name = info['Full_Name']
with col1:
    hero(f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
    st.write(info['About'])

    from streamlit_extras.switch_page_button import switch_page
    col_1, col_2, temp = st.columns([0.35,0.2,0.45])
    with col_1:
        btn1 = st.button("Chat with My AI Assistant")
        if btn1:
            switch_page("AI_Assistant_Chat")
    with col_2:
        btn2 = st.button("My Resume")
        if btn2:
            switch_page("Resume")

import streamlit.components.v1 as components

def change_button_color(widget_label, background_color='transparent'):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.background = '{background_color}'
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)

change_button_color('Chat with My AI Assistant', '#0cc789') 

from  PIL import Image
with col2:
    profile = Image.open("images/profile.png")
    st.image(profile, width=280)
          
with st.container():
    st.write("---")
    st.subheader('🚀 Project Showcase')

    projects = projects

    def display_project(col, project):
        with col:
            st.markdown(
                f'<a href="{project["link"]}" target="_blank" class="portfolio-item" data-id="3">'
                f'<img src="{project["image_url"]}" style="width:100%;height:auto;"></a>',
                unsafe_allow_html=True,
            )
            st.markdown(f'<p style="font-size: 16px; font-weight: bold;">{project["title"]}</p>', unsafe_allow_html=True)
            st.markdown(f'<p style="font-size: 14px">{project["description"]}</p>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,1,1])
    columns = [col1, col2, col3]

    # adjust the range(0, len(projects), 3) accordingly if the length of your projects is not a multiple of 3
    for i in range(0, len(projects), 3):
        for j, col in enumerate(columns):
            if i + j < len(projects):  # Check if project index is within range
                display_project(col, projects[i + j])
st.markdown(""" <a href={}> <em>👀 Click here to see more </a>""".format(info['Project']), unsafe_allow_html=True)
    
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
    timeline(data, height=600)

# -----------------  PowerBI  -----------------  #
powerbi_html = """
<iframe title="Report Section" width="100%" height="486" src="https://shorturl.at/mrY27" frameborder="0" allowFullScreen="true"></iframe>
"""
with st.container():
    st.markdown("""""")
    st.subheader("📊 PowerBI Skills")
    col1,col2 = st.columns([0.95, 0.05])
    with col1:
        with st.expander('Click here to access my Demo Sales Dashboard'):
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

# ----------------- slideshare ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('✍️ SlideShare')
    col1,col2 = st.columns([0.95, 0.05])
    components.html(embed_rss['rss'],height=300)
    st.markdown(""" <a href={}> <em>👀 Click here to see more</a>""".format(info['Medium']), unsafe_allow_html=True)

st.write("---")
with st.container():  
    col1,col2,col3 = st.columns([0.55, 0.40, 0.05])
        
    with col1:
        st.subheader("👄 Coworker Endorsements")
        components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
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

    with col2:
        st.subheader("📨 Contact Me")
        email = info["Email"]
        contact_form = f"""
        <form action="https://formsubmit.co/{email}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
