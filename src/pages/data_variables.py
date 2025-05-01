import streamlit as st
import pandas as pd
from streamlit_extras.app_logo import add_logo

# Configuração da página
st.set_page_config(
    page_title="Desmatamento em regiões da Amazônia",
    page_icon="🌱",
    layout="wide"
)

# Caminho do arquivo
file_path = "src/data/prodes.csv"  # Atualize esse caminho conforme a localização real do arquivo

# Carregar os dados
def load_data():
    try:
        df = pd.read_csv(file_path, encoding="ISO-8859-1", delimiter=",")
        return df
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None

df = load_data()

# Header
st.header("Conjunto de dados", divider="grey")

if df is not None:
    st.write("Visualização inicial dos dados:")
    st.dataframe(df.head())

    st.subheader("Resumo estatístico")
    st.write("Visualização estatística das variáveis numéricas, média, desvio padrão, valores mínimos, máximos e quartis (25%, 50% e 75%):")
    st.write(df.describe())

    st.subheader("Classificação das Variáveis", divider="grey")

    # Classificar variáveis em qualitativas e quantitativas
    qualitative_vars = df.select_dtypes(include=['object', 'category']).columns.tolist()
    quantitative_vars = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Variáveis Qualitativas")
        st.write("Variáveis que representam categorias ou rótulos:")
        if qualitative_vars:
            st.markdown("\n".join([f"- **{var}**" for var in qualitative_vars]))
        else:
            st.info("Nenhuma variável qualitativa foi identificada.")

    with col2:
        st.markdown("### Variáveis Quantitativas")
        st.write("Variáveis que representam valores numéricos:")
        st.markdown("\n".join([f"- **{var}**" for var in quantitative_vars]))

    # Separar variáveis qualitativas (nominais vs. ordinais)
    st.subheader("Variáveis Qualitativas: Nominais vs. Ordinais", divider="grey")

    nominal_vars = []  # Dataset não possui variáveis categóricas nomeadas
    ordinal_vars = []  # Dataset não possui variáveis categóricas ordenadas

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("##### Variáveis Nominais")
        if nominal_vars:
            st.markdown("\n".join([f"- **{var}**" for var in nominal_vars]))
        else:
            st.info("Nenhuma variável nominal foi identificada.")

    with col4:
        st.markdown("##### Variáveis Ordinais")
        if ordinal_vars:
            st.markdown("\n".join([f"- **{var}**" for var in ordinal_vars]))
        else:
            st.info("Nenhuma variável ordinal foi identificada.")

    # Separar variáveis quantitativas (discretas vs. contínuas)
    st.subheader("Variáveis Quantitativas: Discretas vs. Contínuas", divider="grey")

    # As variáveis são áreas medidas (em km²), geralmente contínuas
    discrete_vars = ["referencia"]  # anos são valores discretos
    continuous_vars = [var for var in quantitative_vars if var != "referencia"]

    col5, col6 = st.columns(2)
    with col5:
        st.markdown("##### Variáveis Discretas")
        st.markdown("\n".join([f"- **{var}**" for var in discrete_vars]))

    with col6:
        st.markdown("##### Variáveis Contínuas")
        st.markdown("\n".join([f"- **{var}**" for var in continuous_vars]))
else:
    st.error("Não foi possível carregar os dados.")
