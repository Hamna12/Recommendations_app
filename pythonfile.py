import streamlit as st
import pickle
import pandas as pd

from PIL import Image
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components

#Setting the Page Configuration
#img = Image.open('./images/favicon.png')
#st.set_page_config(page_title='News Recommender Engine' , page_icon=img , layout="centered",initial_sidebar_state="expanded")

#Designing the footer and MainMenu creating the skeleton of the website.
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: visible;}
            footer:after{
                background-color:#a873b0;
                font-size:12px;
                font-weight:5px;
                height:30px;
                margin:1rem;
                padding:0.8rem;
                content:'Copyright © 2022 : Hamna Qaseem 👩‍💻';
                display: flex;
                align-items:center;
                justify-content:center;
                color:white;
            }
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)

#Loading the animation of the streamlit lottie
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# URLS of all the lottie animation used
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_bb9bkg1h.json")
lottie_contact =load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_dhcsd5b5.json")
lottie_loadLine =load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_yyjaansa.json")
lottie_github =load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_S6vWEd.json")

#Sidebar Designing And Functioning
with st.sidebar:
    selected = option_menu(
                menu_title="NEWS ARTICLE Recommender",  # required
                options=["Home", "About Me", "💻 About Website"],  # required
                icons=["house", "person-square", "website"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                 styles={
                "container": {"padding": "5!important", "background-color": "#0E1117" , "Font-family":"Monospace"},
                "icon": {"color": "#A0CFD3", "font-size": "25px"},
                "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px","Font-family":"Monospace"},
                "nav-link-selected": {"background-color": "#90EE90"},
                }
                )
    # Adding Functionality to the sidebar on the basis of option being selected from the main menu.
    if selected == "Home":
        st.empty()

    # The About And Portfolio Section.
    if selected == "About Me":
        st.markdown("""
        <div style='
            background-color:#a873b0; 
            padding:1rem;
            font-size:17px;
            border-radius:8px;
            text-align: justify;
           '>
            I am a fresher currently doing my Bachelor's in Data Science.I have keen interest in website designing and developing.I am from from Pakistan.In addition, I have deep interest and aptitude in telling stories with data.
        </div>
        <br>
       """
                    , unsafe_allow_html=True, )

        # The About And Portfolio Section.
    if selected == "💻 About Website":
        st.markdown("""
           <div style='
               background-color:#a873b0; 
               padding:1rem;
               font-size:17px;
               border-radius:8px;
               text-align: justify;
              '>
               This website is giving you information of News Articles. If you select one News Article then this Recommender system show you Top five similar Articles related to particluar News Article that we select. I collect my data from 
kaggle(https://www.kaggle.com/datasets/rmisra/news-category-dataset).
This dataset contains around 200k news headlines from the year 2012 to 2018 obtained from HuffPost. Each news headline has a corresponding category. 
           </div>
           <br>
          """
                    , unsafe_allow_html=True, )

def recommend(Headline):
    Headline_index = news[news['Headline'] == Headline].index[0]
    distances = cosine_sim_mat[Headline_index]
    Headlines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_Headlines = []
    for i in Headlines_list:
        recommended_Headlines.append(news.iloc[i[0]].Headline)
    return recommended_Headlines

news_dict = pickle.load(open('news_dict.pkl', 'rb'))
news = pd.DataFrame(news_dict)

cosine_sim_mat = pickle.load(open('cosine_sim_mat.pkl', 'rb'))


st.title('Recommender System')

selected_headline_name = st.selectbox(
'Recommended News Headlines:',
news['Headline'].values)

if st.button('Recommend'):
     recommendations = recommend(selected_headline_name)
     for i in recommendations:
         st.write(i)


#The contact me section of the website.Creation of an active form which directly notifies with
# all the details of the sender along with the message om to the mail box

st_lottie(lottie_loadLine,height=300,width=700,key="coding3")
st. markdown("<h1 style='text-align:center; color:#A0CFD3;font-size:60px;font-family:monospace;'> WANT TO CONNECT 👨‍⚖️</h1>", unsafe_allow_html=True)

# Designing of contact form
st.write("")
with st.container():
    contact_form = """
    <form action="https://formsubmit.co/hamnaqaseem@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" style="height:50px; width:300px; font-size:14pt; margin:5px;padding:10px;border-radius:5px;" placeholder="Your name" required>
        <input type="email" name="email" style="height:50px; width:300px; font-size:14pt;margin:5px;padding:10px;border-radius:5px;" placeholder="Your email" required>
        <textarea name="message" style="height:150px; width:300px; font-size:14pt;margin:5px;padding:10px;border-radius:5px;" placeholder="Your message here" required></textarea>
        <button style=" height:50px; width:300px; font-size:14pt; margin:5px; padding:10px;border-radius:5px;background-color:#90EE90" type="submit">Send</button>
</form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

    with right_column:
        st_lottie(lottie_contact, height=300, width=400, key="coding2")


# Primary accent for interactive elements
primaryColor = '#7792E3'

# Background color for the main content area
backgroundColor = '#273346'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#B9F1C0'

# Color used for almost all text
textColor = '#FFFFFF'

# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace)
# Default: "sans serif"
font = "sans serif"
