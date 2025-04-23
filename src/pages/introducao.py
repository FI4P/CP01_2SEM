import streamlit as st
import pandas as pd
import numpy as np



# Configurando a página
st.set_page_config(page_title="Desmatamento em regiões da Amazônia", page_icon="🌱", layout="wide")

#Header
st.header("Introdução", divider="grey");

#Texto personalizado
st.markdown("""
    <style>

        .intro-text {
            font-size: 20px;
            color: white;
            line-height: 1.6;
            padding-top: 1rem;
            padding-bottom: 2rem;

        }
    </style>

    <div class="intro-text">
        O desmatamento na região Amazônica é uma das principais preocupações ambientais do Brasil, com impactos diretos sobre o clima, a biodiversidade e os recursos hídricos. Compreender o comportamento do desmatamento ao longo do tempo e em diferentes estados da Amazônia Legal pode fornecer subsídios importantes para políticas públicas, ações de fiscalização e iniciativas sustentáveis. Este trabalho tem como objetivo analisar os dados históricos de desmatamento fornecidos pelo Projeto PRODES, gerando insights visuais por meio de um dashboard interativo com Streamlit.
    </div>
""", unsafe_allow_html=True)


st.subheader("Desmatamento em regiões da Amazônia")
st.image("", caption='Desmatamento') ## Adicionar uma imagem que reflete o desmatamento atual da amazonia
