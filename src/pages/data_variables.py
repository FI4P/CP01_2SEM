import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

# Configuração da página
st.set_page_config(page_title="Acidentes Ferroviários", page_icon="🚆", layout="wide")

# Carregar os dados
file_path = "src/data/railway_accidents_data.csv"  # Substituir pelo caminho correto

def load_data():
    try:
        df = pd.read_csv(file_path, encoding="ISO-8859-1", delimiter=";")
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
        st.markdown("\n".join([f"- **{var}**" for var in qualitative_vars]))
    
    with col2:
        st.markdown("### Variáveis Quantitativas")
        st.write("Variáveis que representam valores numéricos:")
        st.markdown("\n".join([f"- **{var}**" for var in quantitative_vars]))
    
    # Distinguir entre variáveis nominais e ordinais (qualitativas)
    st.subheader("Variáveis Qualitativas: Nominais vs. Ordinais", divider="grey")
    


    nominal_vars = ["Concessionaria", "UF", "Municipio", "Linha", "Causa_direta", "Causa_contributiva", "Natureza"]
    ordinal_vars = ["Gravidade"]  # Exemplo
    
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("##### Variáveis Nominais")
        st.markdown("\n".join([f"- **{var}**" for var in nominal_vars]))
    with col4:
        st.markdown("##### Variáveis Ordinais")
        st.markdown("\n".join([f"- **{var}**" for var in ordinal_vars]))

    # Distinguir entre variáveis quantitativas discretas e contínuas
    st.subheader("Variáveis Quantitativas: Discretas vs. Contínuas", divider="grey")
    

    
    discrete_vars = ["N_Trem", "N_feridos", "N_obitos"]
    continuous_vars = ["Prejuízo_Financeiro"]
    
    col5, col6 = st.columns(2)
    with col5:
        st.markdown("##### Variáveis Discretas")
        st.markdown("\n".join([f"- **{var}**" for var in discrete_vars]))
    with col6:
        st.markdown("##### Variáveis Contínuas")
        st.markdown("\n".join([f"- **{var}**" for var in continuous_vars]))

    st.subheader("", divider='grey')

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
    
    st.subheader("Análise dos Dados", divider="grey")
    
    st.markdown("""
    ### **1. Distribuição Geográfica dos Acidentes**
    - O local médio dos acidentes está em torno do **km 277**.
    - O alto desvio padrão (**252 km**) sugere que os acidentes estão bem distribuídos ao longo das ferrovias.
    
    ### **2. Tempo de Interrupção**
    - A interrupção média foi de **4,12 horas**, mas há variações grandes.
    - O desvio padrão elevado (**12,38 horas**) indica que alguns acidentes causaram longas paralisações.
    - A mediana provavelmente é baixa (~0,1h), mostrando que a maioria dos eventos causou pequenas interrupções.
    
    ### **3. Número de Trens Envolvidos**
    - A média é **0,96**, o que sugere que normalmente **apenas um trem** está envolvido.
    - A baixa variação (**desvio padrão de 0,19**) confirma essa tendência.
    
    ### **4. Gravidade dos Acidentes**
    - **Número de feridos**: Em média, **0,34 feridos por acidente**.
    - **Número de óbitos**: A média é **0,15 óbitos por acidente**, mostrando que a maioria não resulta em fatalidades.
    - A distribuição indica que há **poucos acidentes muito graves**, que elevam a média geral.
    
    ### **Conclusões**
    - Acidentes estão espalhados por grandes áreas, mas ocorrem com mais frequência ao redor do km 277.
    - A maioria das interrupções é curta, mas algumas poucas causam paralisações longas.
    - Na maioria dos casos, há apenas um trem envolvido e os acidentes têm baixa letalidade.
    """)

  
else:
    st.error("Não foi possível carregar os dados.")