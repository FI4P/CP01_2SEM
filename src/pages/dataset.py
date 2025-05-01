import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from streamlit_extras.app_logo import add_logo

#Page config
st.set_page_config(page_title="Desmatamento em regiões da Amazônia", page_icon="🌱", layout="wide")

# Caminho do arquivo
file_path = "src/data/prodes.csv"  # Atualize esse caminho conforme a localização real do arquivo

def load_data():
    try:
        df = pd.read_csv(file_path, encoding="ISO-8859-1", delimiter=",")
        return df
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None

df = load_data()


if df is not None:

    #Estilo Global
    st.markdown("""
        <style>
        
            /* Elementos de markdown */
            .stMarkdown p, .stText {
                font-family: 'Segoe UI', sans-serif !important;
                font-size: 20px !important;
                line-height: 1.6 !important;
            }

            /* Tabelas interativas */
            .stDataFrame div {
                font-size: 16px !important;
            }
        </style>
    """, unsafe_allow_html=True)


    #Header
    st.header("Apresentando o Dataset", divider="grey");

    st.markdown("""
    O conjunto de dados utilizado foi extraído do **Projeto PRODES**, que monitora o desmatamento por corte raso na Amazônia Legal. Ele contém informações anuais sobre a área desmatada em diversos estados brasileiros da região amazônica.

    - **Total de registros:** 35 anos (linhas)
    - **Total de atributos (colunas):** 11
    - **Período coberto:** representado pela coluna `referencia`, que indica o ano
    - **Estados monitorados:** `acre`, `amazonas`, `amapa`, `maranhao`, `mato_grosso`, `para`, `rondonia`, `roraima`, `tocantins`
    - **Coluna principal:** `area_total_desmatamento` – soma das áreas desmatadas por estado em cada ano
    - **Tipos de dados:** Todos os valores são do tipo inteiro (`int64`)
    - **Dados ausentes:** Nenhum valor nulo identificado no dataset
    """)

    # Gráfico de evolução do desmatamento
    st.subheader("Evolução do desmatamento total por ano")

    fig = px.line(
        df,
        x="referencia",
        y="area_total_desmatamento",
        markers=True,
        title="Desmatamento total anual na Amazônia Legal (PRODES)",
        labels={"referencia": "Ano", "area_total_desmatamento": "Área desmatada (km²)"}
    )

    fig.update_traces(line_color="green")
    fig.update_layout(title_x=0.05)

    st.plotly_chart(fig, use_container_width=True)

    # Mapa do desmatamento
    # Coordenadas aproximadas dos estados da Amazônia Legal
    estados_coords = {
        "acre": [-70.55, -9.02],
        "amazonas": [-64.70, -3.47],
        "amapa": [-51.05, 1.41],
        "maranhao": [-45.27, -5.42],
        "mato_grosso": [-56.10, -12.64],
        "para": [-52.00, -4.27],
        "rondonia": [-63.90, -10.83],
        "roraima": [-61.22, 2.05],
        "tocantins": [-48.30, -10.17]
    }

    st.subheader("Mapa do desmatamento por estado")

    # Filtro do ano
    ano = st.selectbox("Selecione o ano para visualizar o mapa:", sorted(df["referencia"].unique(), reverse=True), key="mapa")

    # Filtra os dados
    linha = df[df["referencia"] == ano].squeeze()

    # Monta o DataFrame para o mapa
    dados_mapa = pd.DataFrame({
        "Estado": estados_coords.keys(),
        "Área desmatada (km²)": [linha[estado] for estado in estados_coords.keys()],
        "lon": [estados_coords[estado][0] for estado in estados_coords.keys()],
        "lat": [estados_coords[estado][1] for estado in estados_coords.keys()]
    })

    # Cria o mapa
    fig = px.scatter_mapbox(
        dados_mapa,
        lat="lat",
        lon="lon",
        size="Área desmatada (km²)",
        color="Área desmatada (km²)",
        color_continuous_scale="YlOrRd",
        size_max=30,
        zoom=3.5,
        mapbox_style="carto-positron",
        hover_name="Estado",
        title=f"Desmatamento nos estados da Amazônia Legal em {ano}"
    )

    fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0})

    st.plotly_chart(fig, use_container_width=True)

    # Conclusão dinâmica com base no total de desmatamento
    total_desmatado = dados_mapa["Área desmatada (km²)"].sum()
    estado_top = dados_mapa.loc[dados_mapa["Área desmatada (km²)"].idxmax(), "Estado"]
    area_top = dados_mapa["Área desmatada (km²)"].max()

    st.markdown(f"""
    **Conclusão para {ano}:**

    Em {ano}, a área total desmatada na Amazônia Legal foi de **{total_desmatado:,.0f} km²**.  
    O estado com maior desmatamento foi **{estado_top.capitalize()}**, com aproximadamente **{area_top:,.0f} km²** de vegetação suprimida.

    Esses dados reforçam a importância do monitoramento contínuo e da atuação direcionada nas regiões mais críticas.
    """)
else:
    st.error("Erro ao carregar dados")