import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

#Page config
st.set_page_config(page_title="Acidentes Ferroviários", page_icon="🚆", layout="wide")


#Header
st.header("Techs & Tools", divider="grey");

st.subheader("Techs");


#Texto personalizado
st.markdown("""
    <style>
         .icons{
            
                padding-bottom: 2rem;
            
            }   
    </style>

    <div class="icons">
        <img src="https://skillicons.dev/icons?i=js,python,typescript,html,css,nodejs,express,php,laravel,java,react,sass,tailwind,jest,mysql" />
    </div>
""", unsafe_allow_html=True)


st.subheader("Tools");

#Texto personalizado
st.markdown("""
    <style>
            
    </style>

    <div class="icons">
        <img src="https://skillicons.dev/icons?i=vscode,postman,figma,eclipse,linux,docker,obsidian,notion" />
    </div>
""", unsafe_allow_html=True)


