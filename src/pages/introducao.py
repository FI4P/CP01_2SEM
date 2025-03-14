import streamlit as st
import pandas as pd
import numpy as np



# Configurando a página
st.set_page_config(page_title="Acidentes Ferroviários", page_icon="🚆", layout="wide")

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
        Este trabalho tem como objetivo realizar uma análise detalhada dos acidentes ferroviários ocorridos no Brasil entre dezembro de 2020 e dezembro de 2024. Através da coleta e processamento de dados oficiais relacionados a esses incidentes, provenientes de órgãos responsáveis pelo monitoramento do transporte ferroviário, busca-se identificar padrões e fatores que contribuem para a ocorrência desses acidentes. A análise será conduzida com base em informações provenientes de registros da Agência Nacional de Transportes Terrestres (ANTT), e se concentrará em diferentes aspectos dos acidentes, como causas, localização, severidade e consequências. O intuito é fornecer uma visão abrangente e fundamentada sobre a situação dos acidentes ferroviários no período em questão, além de contribuir para a identificação de possíveis áreas de melhoria e prevenção para o futuro.
    </div>
""", unsafe_allow_html=True)


st.subheader("Mapa da Concessão Ferroviária do Brasil")
st.image("https://www.gov.br/antt/pt-br/assuntos/ferrovias/concessoes-ferroviarias/ferrovia-centro-atlantica-s-a/arquivos/concessoes-ferroviarias.jpg", caption='Concessões ferroviárias')
