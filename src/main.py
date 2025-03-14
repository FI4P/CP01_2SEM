import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

def execute():
    
    pages = {

    "Introdução": [
        st.Page('pages/introducao.py', title='Introdução', icon=':material/info:'),
    ],

    "Home": [
        st.Page('pages/sobre_mim.py', title='Sobre mim', icon=':material/person:'),
        st.Page('pages/objetivos_pessoais.py', title='Objetivos pessoais', icon=':material/target:'),
    ],

    "Skills": [
        st.Page('pages/tools.py', title='Techs & Tools', icon=':material/code:'),
        
    ],


    "Analises": [
        st.Page('pages/data_variables.py', title='Dados e variáveis', icon=':material/monitoring:'),
        st.Page('pages/analysis.py', title='Medidas centrais, dispersão e correlação ', icon=':material/monitoring:'),
    ]
    
}   
    
    st.logo('src/assets/logo.png', size='large', link='https://linkedin.com/in/enzorodrigues03')

    # Run all pages.
    pg = st.navigation(pages)
    pg.run()


try:
    execute();
except Exception as err:
    print('Erro ao executar a aplicação')