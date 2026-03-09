import streamlit as st
import pandas as pd

from Dados import carregar_dados
from Graficos.criar_grafico_salario import criar_grafico_salario
from Graficos.grafico_estado_civil import criar_grafico_estado_civil
from Graficos.grafico_grau_de_instrucao import criar_grafico_grau_de_instrucao
from Graficos.criar_grafico_numero_filhos import criar_grafico_numero_filhos
    
st.set_page_config(page_title="Dashboard", layout="wide")

st.title("Dashboard")

data_frame = pd.DataFrame(carregar_dados())

largura = 4
altura = 2
col1, col2 = st.columns(2)

with col1:
    st.subheader("GRÁFICO DE PIZZA")
    fig_estado_civil = criar_grafico_estado_civil(data_frame, largura, altura)
    st.pyplot(fig_estado_civil)
#FIM GRAFICO ESTADO CIVIL

#GRAFICO GRAU DE INSTRUÇÃO
with col2:
    st.subheader("GRÁFICO DE BARRAS")
    fig_grau_de_instrucao = criar_grafico_grau_de_instrucao(data_frame, largura, altura=3.07)
    st.pyplot(fig_grau_de_instrucao)

#FIM GRAFICO GRAU DE INSTRUÇÃO

col3, col4 = st.columns(2)

with col3:
    st.subheader("GRÁFICO DE BARRAS HORIZONTAIS")
    fig_numero_filhos = criar_grafico_numero_filhos(data_frame, largura, altura)
    st.pyplot(fig_numero_filhos)

with col4:
    st.subheader("GRÁFICO DE HISTOGRAMA")
    fig_salario = criar_grafico_salario(data_frame, largura, altura)
    st.pyplot(fig_salario)