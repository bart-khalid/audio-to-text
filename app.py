from PIL import Image

import streamlit as st
import requests
import dill

# load icon image
im = Image.open("AudioToText.png")
# config
st.set_page_config(
     page_title="BARTAOUCH Khalid Audio To Text App",
     layout="wide",
     initial_sidebar_state="expanded",
     page_icon=im,
     menu_items={
         'About': "# BARTAOUCH KHALID Audio To Text APP. This is a free app!"
     }
 )

# title
title = """
<h1 style="color: orange; text-align:center;"> تحويل أوديو إلى نص </h1>
</div>
"""
st.markdown(title,unsafe_allow_html=True)

#Author
author="""
<style>
a:link, a:visited{
color: black;
background-color: white;
text-decoration: underline;
}
a:hover, a:active {
color: red;
background-color: white;
text-decoration: underline;
}
.author{
width:auto;
text-align: center;
padding: 10px;
z-index: 999999999;
}
</style>
<div class="author">
<p>Developed with ❤ by &nbsp; <a href="https://www.linkedin.com/in/bartaouchkhalid" target="_blank">** BARTAOUCH Khalid **</a></p>
</div>
"""
st.markdown(author,unsafe_allow_html=True)
st.write('\n')
st.write('\n')

# layout define
col1, col2, col3 = st.columns([5,4,3])
x=0

# credentials
with open('API_URL_MEDIUM.pkl', 'rb') as file:
    API_URL_MEDIUM = dill.load(file)
with open('API_URL_BASE.pkl', 'rb') as file2:
    API_URL_BASE = dill.load(file2)
with open('headers.pkl', 'rb') as file3:
    headers = dill.load(file3)

@st.cache_resource(show_spinner="...طلبكم قيد المعالجة")
def query_base(data):
    response = requests.post(API_URL_BASE, headers=headers, data=data)
    return response.json()
    
@st.cache_resource(show_spinner="...طلبكم قيد المعالجة")
def query_medium(data):
    response = requests.post(API_URL_MEDIUM, headers=headers, data=data)
    return response.json()

# layout
with col3:
    option = st.selectbox(
        'إختر__الخوارزمية__المناسبة__لك',
        ('دقة مناسبة، وقت أسرع', 'دقة أكثر، وقت معالجة أكثر'))

    if option == 'دقة أكثر، وقت معالجة أكثر' :
        option = 'medium'
    else :
        option = 'base'

    audio = st.file_uploader("إرفع المقطع الصوتي", type=["mp3", "wav", "ogg", "flac", "m4a", "aac"])

with col2:
    if audio is not None:
        st.write('\n')
        with st.spinner("...طلبكم قيد المعالجة"):
            if option == 'base':
                st.info('...لم يتبقى الكثير، المرجو الإنتظار')
                result = query_base(audio.read())
            else :
                st.info('...لم يتبقى الكثير، المرجو الإنتظار')
                result = query_medium(audio.read())
            st.header("النتيجة")
            st.success(result["text"])
            x=1
           
with col1:
    if x==1:
        st.subheader("لنسخ النص")
        st.code(result["text"])

#footer 
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
#footer End