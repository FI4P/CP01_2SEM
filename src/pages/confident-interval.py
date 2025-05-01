import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import plotly.graph_objects as go
import plotly.express as px

# Configuração do Streamlit
st.set_page_config(page_title="Desmatamento em regiões da Amazônia", page_icon="🌱", layout="wide")   

file_path = "src/data/prodes.csv"

def load_data():
    try:
        df = pd.read_csv(file_path, encoding="ISO-8859-1", delimiter=";")
        return df
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None

df = load_data()




if df is not None:

        # Header
    st.header("Análise Estatística com Intervalo de Confiança", divider="grey")

    # Interface de seleção
    estado_selecionado = st.selectbox("Selecione um estado para a análise estatística:", df.columns[1:-1])

    # Estatísticas gerais
    media_total = df["area_total_desmatamento"].mean()
    desvio_total = df["area_total_desmatamento"].std()
    n = df.shape[0]
    z = stats.norm.ppf(0.975)

    ic_menor_total = media_total - z * (desvio_total / np.sqrt(n))
    ic_maior_total = media_total + z * (desvio_total / np.sqrt(n))

    media_estado = df[estado_selecionado].mean()
    desvio_estado = df[estado_selecionado].std()
    ic_menor_estado = media_estado - z * (desvio_estado / np.sqrt(n))
    ic_maior_estado = media_estado + z * (desvio_estado / np.sqrt(n))

    media_prop = df[estado_selecionado] / df["area_total_desmatamento"]
    media_prop_mean = media_prop.mean()
    media_prop_std = media_prop.std()
    ic_prop = stats.t.interval(0.95, df=n-1, loc=media_prop_mean, scale=media_prop_std / np.sqrt(n))

    # Gráficos
    fig_total = go.Figure()
    fig_total.add_trace(go.Scatter(x=df["referencia"], y=df["area_total_desmatamento"],
                                mode="lines+markers", name="Área desmatada total"))
    fig_total.add_trace(go.Scatter(x=df["referencia"], y=[ic_maior_total]*n, fill=None,
                                mode='lines', line_color='lightgray', showlegend=False))
    fig_total.add_trace(go.Scatter(x=df["referencia"], y=[ic_menor_total]*n, fill='tonexty',
                                mode='lines', line_color='lightgray', name='IC 95% da média total'))
    fig_total.update_layout(title="Distribuição da área total desmatada com IC 95%",
                        xaxis_title="Ano", yaxis_title="Área total desmatada (km²)")

    fig_estado = go.Figure()
    fig_estado.add_trace(go.Scatter(x=df["referencia"], y=df[estado_selecionado],
                                    mode="lines+markers", name=f"{estado_selecionado.capitalize()}"))
    fig_estado.add_trace(go.Scatter(x=df["referencia"], y=[ic_maior_estado]*n, fill=None,
                                    mode='lines', line_color='lightgray', showlegend=False))
    fig_estado.add_trace(go.Scatter(x=df["referencia"], y=[ic_menor_estado]*n, fill='tonexty',
                                    mode='lines', line_color='lightgray', name=f'IC 95% - {estado_selecionado.capitalize()}'))
    fig_estado.update_layout(title=f"Distribuição da área desmatada no estado de {estado_selecionado.capitalize()} com IC 95%",
                            xaxis_title="Ano", yaxis_title="Área desmatada (km²)")

    fig_bar = px.bar(df, x="referencia", y=estado_selecionado,
                    title=f"Desmatamento no estado de {estado_selecionado.capitalize()} com margem de erro (aproximada)",
                    labels={"referencia": "Ano", estado_selecionado: f"Área desmatada ({estado_selecionado}) (km²)"},
                    error_y=media_prop_std * df[estado_selecionado] / df["area_total_desmatamento"])

    # Texto explicativo
    st.markdown("""
    Nesta análise optamos por trabalhar com **média** e **proporção** porque são medidas robustas para descrever a tendência central e a participação relativa de cada estado no desmatamento total.  
    A **média** permite resumir a área desmatada ao longo dos anos de forma objetiva, enquanto a **proporção** nos mostra a importância relativa de um estado específico.
    """)

    # IC da média total
    st.markdown(f"""
    **Média geral da área total desmatada:** {media_total:,.2f} km²  
    **Intervalo de confiança (95%) da média:** de {ic_menor_total:,.2f} a {ic_maior_total:,.2f} km²
    """, unsafe_allow_html=False)

    st.markdown(r"""
    $$
    IC = \bar{x} \pm Z_{0.975} \cdot \frac{s}{\sqrt{n}}
    $$
    """, unsafe_allow_html=False)

    st.markdown("""
    Onde: $ \\bar{x} $ é a média amostral, $ s $ é o desvio padrão amostral e $ n $ é o tamanho da amostra.
    """, unsafe_allow_html=False)

    st.plotly_chart(fig_total, use_container_width=True)

    # 🔎 Interpretação do gráfico total
    st.markdown("""
    **🔎 Interpretação do gráfico acima:**  
    O gráfico apresenta a evolução da **área total desmatada na Amazônia Legal ao longo dos anos**.  
    As linhas cinzas representam os limites superior e inferior do **intervalo de confiança de 95% da média total**.  
    Valores fora desses limites indicam possíveis **anos atípicos** que merecem atenção, podendo refletir alterações em políticas públicas ou eventos climáticos extremos.
    """)

    # IC da média do estado
    st.markdown(f"""
    **Média do estado de {estado_selecionado.capitalize()}:** {media_estado:,.2f} km²  
    **Intervalo de confiança (95%) da média:** de {ic_menor_estado:,.2f} a {ic_maior_estado:,.2f} km²
    """, unsafe_allow_html=False)

    st.markdown(r"""
    $$
    IC = \bar{x} \pm Z_{0.975} \cdot \frac{s}{\sqrt{n}}
    $$
    """, unsafe_allow_html=False)

    st.plotly_chart(fig_estado, use_container_width=True)

    # 🔎 Interpretação do gráfico do estado
    st.markdown(f"""
    **🔎 Interpretação do gráfico acima (Estado: {estado_selecionado.capitalize()}):**  
    Este gráfico mostra a série temporal da **área desmatada especificamente no estado de {estado_selecionado.capitalize()}**.  
    As faixas de intervalo de confiança ajudam a entender o quanto os dados de cada ano estão próximos ou distantes da média estimada, evidenciando **picos ou quedas incomuns**.
    """)

    # IC da proporção do estado
    st.markdown(f"""
    **Proporção média do estado de {estado_selecionado.capitalize()}:** {media_prop_mean:.4f}  
    **Intervalo de confiança (95%) da proporção:** de {ic_prop[0]:.4f} a {ic_prop[1]:.4f}
    """, unsafe_allow_html=False)

    st.markdown(r"""
    $$
    IC = \hat{p} \pm t_{\alpha/2, \, n-1} \cdot \frac{s}{\sqrt{n}}
    $$
    """, unsafe_allow_html=False)

    st.markdown("""
    Onde $ \hat{p} $ é a proporção média, $ s $ o desvio padrão da proporção e $ n $ o número de observações.  
    A análise mostra a relevância estatística da participação de cada estado no desmatamento da Amazônia.
    """, unsafe_allow_html=False)

    st.plotly_chart(fig_bar, use_container_width=True)

    # 🔎 Interpretação do gráfico de proporção
    st.markdown(f"""
    **🔎 Interpretação do gráfico acima (Proporção do estado de {estado_selecionado.capitalize()}):**  
    Este gráfico permite visualizar como o estado de {estado_selecionado.capitalize()} contribuiu para o total de desmatamento ano a ano.  
    A margem de erro indica a variabilidade esperada, e valores fora dessa faixa sugerem **participações acima ou abaixo do esperado**, sendo útil para planejar **ações de fiscalização ou políticas ambientais regionais**.
    """)
else:
    st.error("Erro ao carregar dados")