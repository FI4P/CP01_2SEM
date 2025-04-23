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
        st.Page('pages/dataset.py', title='Dataset', icon=':material/monitoring:'),
        st.Page('pages/perguntas_hipoteses.py', title='Perguntas investigativas', icon=':material/target:'),
    ],

    "Analises": [
        st.Page('pages/data_variables.py', title='Dados e variáveis', icon=':material/monitoring:'),
        st.Page('pages/analysis.py', title='Medidas centrais, dispersão e correlação ', icon=':material/monitoring:'),
    ],

    "Testes de hipótese": [
        st.Page('pages/testes_hipotese.py', title='Testes de hipótese', icon=':material/code:'),
        
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