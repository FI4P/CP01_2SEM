import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

#Page config
st.set_page_config(page_title="Desmatamento em regiões da Amazônia", page_icon="🌱", layout="wide")


#Header
st.header("Perguntas investigativas e hipóteses", divider="grey");


##Trocar por perguntas relacionadas ao tema
st.subheader("Principais Perguntas de Análise")
st.markdown(
        """
        1. **Tendências Temporais** 
           - Existe um padrão sazonal na ocorrência dos acidentes ferroviários?  
           - Os acidentes ocorrem com mais frequência em determinados meses ou períodos do dia?  

        2. **Distribuição e Padrões Espaciais** 
           - Quais estados ou municípios registram o maior número de acidentes?  
           - Existe correlação entre a densidade ferroviária e a frequência dos acidentes?  
           - Há regiões críticas onde os acidentes são recorrentes?  

        3. **Causas e Impactos dos Acidentes** 
           - Quais são os principais fatores contribuintes para os acidentes? (falha humana, mecânica, infraestrutura, clima)  
           - Certos tipos de trens ou cargas estão mais propensos a acidentes?  

        4. **Correlação entre Variáveis**   
           - A quantidade de vítimas está relacionada à velocidade do trem no momento do acidente?    
           - Certos horários ou condições climáticas influenciam no número de ocorrências?  

        5. **Comparação de Anos e Evolução da Segurança**  
           - Houve uma redução no número de acidentes com o tempo?  
           - Como a frequência e gravidade dos acidentes mudaram ao longo do período analisado?  
        """
    )
    