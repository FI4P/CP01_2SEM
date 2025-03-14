import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

#Page config
st.set_page_config(page_title="Acidentes Ferroviários", page_icon="🚆", layout="wide")


#Header
st.header("Objetivos pessoais", divider="grey");

#Grid mapping
col1, col2 = st.columns([1, 2]);



#Profile
#Texto personalizado
st.markdown("""
    <style>

        .about-me {
            margin-top: .8rem;
            display: flex;
            align-items: center;
            gap: 3rem;
        }
            
        img {
                border-radius: 1rem
            }

         .description {
            font-size: 20px;
            color: white;
            line-height: 1.6;
            text-align: justify;
            padding: 0 1.6rem;
        }
        
            
    </style>

    <div class="about-me">
       <img src="https://media.licdn.com/dms/image/v2/D5603AQExLDqI5-nUsg/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1724757377155?e=1747267200&v=beta&t=XbyHD1ZW6Xe7TcKQLTjDQFpZOJCjmcDhwBI60Hv1ZyQ" />

       <div class="description">Tenho como principal objetivo me desenvolver como profissional na área de tecnologia, aprimorando constantemente minhas habilidades e adquirindo experiência para construir uma carreira sólida no setor. Além disso, almejo conquistar uma carreira internacional consolidada, trabalhando em projetos globais e expandindo minha atuação para diferentes mercados. Para isso, busco constantemente tirar certificações de grande relevância na área de tecnologia, como AWS, Azure e outras, que me permitirão aprofundar meus conhecimentos e me destacar no mercado. Fora do âmbito profissional, um dos meus maiores desejos é conhecer o maior número possível de lugares ao redor do mundo, explorando novas culturas e vivendo experiências únicas que contribuam para o meu crescimento pessoal.</div>
                   
    </div>
            
        
""", unsafe_allow_html=True)
