import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Configuração do Streamlit
st.set_page_config(page_title="Análise de Acidentes Ferroviários", layout="wide")

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

# Função para limpar e preparar os dados
def prepare_data(df):
    if df is None:
        return None
    
    # Converter Interrupção para numérico
    df['Interrupção'] = pd.to_numeric(df['Interrupção'], errors='coerce')
    
    # Criar coluna de data
    df['Data_Ocorrencia'] = pd.to_datetime(df['Data_Ocorrencia'], format='%d/%m/%Y', errors='coerce')
    
    # Criar coluna de mês/ano para análise Poisson
    df['Mes_Ano'] = df['Data_Ocorrencia'].dt.to_period('M')
    
    return df

# Função para plotar distribuição Normal
def plot_normal_distribution(data, column, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plotar histograma
    sns.histplot(data[column].dropna(), kde=True, stat="density", ax=ax)
    
    # Calcular parâmetros da distribuição normal
    mu, sigma = stats.norm.fit(data[column].dropna())
    
    # Plotar a curva normal teórica
    x = np.linspace(min(data[column].dropna()), max(data[column].dropna()), 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2, label=f'Normal (μ={mu:.2f}, σ={sigma:.2f})')
    
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Densidade')
    plt.legend()
    return fig, mu, sigma

# Função para plotar distribuição Poisson
def plot_poisson_distribution(data, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Contar acidentes por mês
    monthly_counts = data.groupby('Mes_Ano').size()
    
    # Plotar histograma dos dados reais
    plt.hist(monthly_counts, bins=range(max(monthly_counts)+1), density=True, alpha=0.7, label='Dados reais')
    
    # Calcular lambda (média) para Poisson
    lambda_param = monthly_counts.mean()
    
    # Plotar a distribuição Poisson teórica
    x = np.arange(0, max(monthly_counts)+1)
    plt.plot(x, stats.poisson.pmf(x, lambda_param), 'ro-', label=f'Poisson (λ={lambda_param:.2f})')
    
    plt.title(title)
    plt.xlabel('Número de Acidentes por Mês')
    plt.ylabel('Probabilidade')
    plt.legend()
    return fig, lambda_param

def main():
    st.title("Análise Probabilística de Acidentes Ferroviários")
    
    if df is not None:
        df_prepared = prepare_data(df)
        
        # Sidebar para opções
        st.sidebar.header("Filtros")
        uf_options = df_prepared['UF'].unique().tolist()
        selected_uf = st.sidebar.multiselect("Selecione UF(s)", uf_options, default=uf_options)
        
        # Filtrar dados
        filtered_df = df_prepared[df_prepared['UF'].isin(selected_uf)]
        
        # Mostrar dados brutos
        if st.checkbox("Mostrar dados brutos"):
            st.write(filtered_df)
        
        # Distribuição Normal para tempo de interrupção
        st.subheader("Distribuição Normal - Tempo de Interrupção")
        normal_fig, mu, sigma = plot_normal_distribution(filtered_df, 'Interrupção', 
                                                       'Distribuição do Tempo de Interrupção dos Acidentes')
        st.pyplot(normal_fig)
        
        # Distribuição Poisson para número de acidentes por mês
        st.subheader("Distribuição Poisson - Acidentes por Mês")
        poisson_fig, lambda_param = plot_poisson_distribution(filtered_df, 
                                                            'Distribuição do Número de Acidentes por Mês')
        st.pyplot(poisson_fig)
        

        # Conclusão
        st.subheader("Conclusão")
        conclusion = f"""
        Com base na análise probabilística dos dados de acidentes ferroviários no Brasil entre 2020 e 2024, observa-se que:

        1. **Tempo de Interrupção (Distribuição Normal)**: O tempo de interrupção segue aproximadamente uma distribuição Normal com média (μ) de {mu:.2f} horas e desvio padrão (σ) de {sigma:.2f} horas. Isso indica que a maioria dos acidentes gera interrupções próximas à média, com alguns eventos extremos (ex.: descarrilamentos prolongados) aumentando a variabilidade. Este padrão pode ser útil para estimar o impacto médio no cronograma ferroviário e planejar respostas a emergências.

        2. **Frequência de Acidentes (Distribuição Poisson)**: O número de acidentes por mês é bem modelado por uma distribuição Poisson, com uma taxa média (λ) de {lambda_param:.2f} acidentes por mês. Isso sugere que os acidentes ocorrem de forma aleatória e relativamente estável ao longo do tempo, permitindo previsões para planejamento de segurança e manutenção.

        3. **Insights Qualitativos**: As causas mais frequentes incluem "Casos Fortuitos ou de Força Maior" (ex.: animais na via) e "Interferência de Terceiro" (ex.: atropelamentos), além de falhas na "Via Permanente" (ex.: bitola aberta). O número de feridos e óbitos é geralmente baixo, mas os prejuízos financeiros podem ser significativos em eventos graves.

        **Recomendações**: Investir em barreiras contra interferências externas (ex.: cercas, sinalização) e na manutenção da infraestrutura da via permanente pode reduzir a frequência e gravidade dos acidentes. Os modelos probabilísticos aqui apresentados oferecem uma base sólida para gestão de riscos e alocação de recursos.

        *Nota*: Esta conclusão assume um bom ajuste das distribuições aos dados. Para uma análise mais precisa, valide os resultados com os gráficos e considere possíveis limitações, como dados ausentes ou padrões regionais não capturados.
        """
        st.markdown(conclusion)

main()