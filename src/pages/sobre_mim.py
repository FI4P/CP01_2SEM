import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

#Page config
st.set_page_config(page_title="Acidentes Ferroviários", page_icon="🚆", layout="wide")


#Header
st.header("Sobre mim", divider="grey");


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

       <div class="description">Meu nome é Enzo Rodrigues e tenho 21 anos. Atualmente, estou cursando o segundo ano de Engenharia de Software na FIAP e trabalho como Estagiário de Verificação e Validação de Software na Alstom. No meu estágio, estou aprendendo bastante sobre as etapas de entrega de um software, com ênfase na verificação e validação dos sistemas, o que tem me proporcionado uma visão detalhada dos processos que garantem a qualidade dos produtos de software. Fora do trabalho e da faculdade, gosto de jogar futebol, correr e jogar no computador, hobbies que me ajudam a manter o equilíbrio e a produtividade tanto no meu dia a dia profissional quanto pessoal.</div>
                   
    </div>
            
        
""", unsafe_allow_html=True)
