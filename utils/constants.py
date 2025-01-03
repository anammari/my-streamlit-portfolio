chat = {
    "TITLE1": "About Me",
    "TITLE2": "AI Chat",
    "menu_v": {
   "container": {"background-color": "#a7c5ff"},
   "icon": {"color": "white", "font-size": "25px"}, 
   "nav-link": {"font-size": "25px", "text-align": "center", "color": "white", "margin":"0px", "--hover-color": "#1b97ff"},
   "nav-link-selected": {"background-color": "#1b97ff"}
    },
    "menu_h": {
        "container": {"padding": "0px",
                      "display": "grid",
                      "margin": "0!important",
                      "background-color": "#212121"
                      },
        "icon": {"color": "#bd93f9", "font-size": "14px"},
        "nav-link": {
            "font-size": "14px",
            "text-align": "center",
            "margin": "auto",
            "background-color": "#262626",
            "height": "30px",
            "width": "13rem",
            "color": "#edff85",
            "border-radius": "5px"
        },
        "nav-link-selected": {
            "background-color": "#212121",
            "font-weight": "300",
            "color": "#f7f8f2",
            "border": "1px solid #e55381"
        }
    }
}

info = {
   "Pronoun": "his", 
   "Subject": "he", 
   "Name": "Ahmad",
   "Full_Name":"Ahmad Ammari", 
   "Intro": "A Data Analytics Professional and Educator",
   "About":"Hi there! I'm Ahmad, a Data Scientist and Analytics Instructor with 11+ years of experience uncovering actionable insights from complex datasets. My expertise spans NLP, data visualization, and machine learning, utilizing tools like Python, Azure ML, and Power BI. Passionate about bridging the gap between data and understanding, I also share my knowledge through teaching and mentorship.",
   "Project":"https://www.linkedin.com/in/ahmadammari/",
   "Medium":"https://www.slideshare.net/anammari/presentations",
   "Tableau":"https://shortit.me/4sf62",
   "ScreenPal":"https://screenpal.com/watch/c0XefrVE9SH",
   "City":"Geelong, Victoria, Australia",
   "Resume": "https://shortit.me/2od45",
   "Email": "ammariect@gmail.com" 
}

projects = [
        {
            "title": "BioMed AI Navigator - Your Intelligent Research Companion",
            "description": "An advanced AI-powered assistant designed to simplify biomedical research by leveraging Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG). This tool provides instant answers to complex biomedical queries, summarizes research articles, recommends related studies, and offers conversational interaction to make navigating vast biomedical literature effortless and accessible for both experts and non-experts alike.",
            "image_url": "https://i.imgur.com/rwUj6D3.jpg",
            "link": "https://github.com/anammari/BioMedical-ai-assistant" 
        },
        {
            "title": "Microscope AI: Classifying Tiny Images with Computer Vision",
            "description": "Developed a deep neural network on CIFAR-100 dataset to classify tiny 32x32 images into 20 categories. Curated image data, engineered features, customized DenseNet architecture, and deployed model to web app. Leveraged TensorFlow, GPUs, AWS, and TaiPy.",
            "image_url": "https://i.imgur.com/Xi6zcQy.jpg",
            "link": "https://github.com/anammari/machine-learning-zoomcamp-capstone-2023"
        },
        {
            "title": "Intelligent Wine Grader: Assessing Quality with ML",
            "description": "Built machine learning models to predict wine quality scores from chemical properties. Curated dataset, tuned regressors, and deployed predictor API using Scikit-Learn, Docker, and Amazon Lightsail.",
            "image_url": "https://i.imgur.com/AJc1Wha.jpg",
            "link": "https://github.com/anammari/wine-quality-prediction"
        },
        {
            "title": "DC Fare Forecaster: Streamlining Taxi Prediction with MLOps",
            "description": "Built an automated ML pipeline to estimate DC taxi fares using location coordinates. Tracked experiments in MLFlow, deployed predictor API with Docker and AWS, and monitored model drift using Grafana. Orchestrated workflow, infrastructure, metrics with Prefect, Terraform, and Evidently.",
            "image_url": "https://i.imgur.com/jYw9vjO.jpg",
            "link": "https://github.com/anammari/mlops-zoomcamp-project-2023"
        },
        {
            "title": "FlightQuest: Navigating Delays with Data Pipelines",
            "description": "Built automated pipelines to ingest, process, and analyze US flight data for predicting delays. Designed data lake architecture on GCP, leveraging BigQuery, Dataproc, Cloud Run, GitHub Actions. Productionized batch and streaming ETL, established data governance.",
            "image_url": "https://i.imgur.com/GE4tGqd.jpg",
            "link": "https://github.com/anammari/de-zoomcamp-project/"
        },
        {
            "title": "DocVision: Unlocking Text from Documents with Computer Vision",
            "description": "Developed a Faster R-CNN model to detect and extract key text sections in complex documents. Annotated image data, tuned object detector on COCO dataset, and predicted regions of interest. Showcased proficiency in PyTorch, model evaluation, and deployment.",
            "image_url": "https://i.imgur.com/HYLMNd6.jpg",
            "link": "https://github.com/anammari/regtransform_challenge/"
        }                  
    ]

endorsements = {
    "img1": "https://i.imgur.com/Nrrm87R.png",
    "img2": "https://i.imgur.com/rLZvEl3.png",
    "img3": "https://i.imgur.com/sGHWQQ6.png",
    "img4": "https://i.imgur.com/AgmdSCL.png",
    "img5": "https://i.imgur.com/wtzoaYQ.png"
}

embed_rss= {
    'rss':"""
    <div style="overflow-y: scroll; height:300px; background-color:white;"> 
        <div id="retainable-rss-embed" 
            data-rss="https://www.slideshare.net/rss/user/anammari"
            data-maxcols="3" 
            data-layout="grid"
            data-poststyle="inline" 
            data-readmore="Read the rest" 
            data-buttonclass="btn btn-primary" 
            data-offset="0">
        </div>
    </div> 
    <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>
    <style>
        #retainable-rss-embed img {
            width: 33%;
            height: auto;
        }
    </style>
    """
}