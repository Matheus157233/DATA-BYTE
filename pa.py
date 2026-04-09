import streamlit as st
import pandas as pd
import numpy as np
import math
import altair as alt

# ------------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA (PRECISA VIR PRIMEIRO)
# ------------------------------------------------------------
st.set_page_config(
    page_title="Curso Completo: Introdução à Ciência de Dados com Python",
    page_icon="🧠",
    layout="wide"
)

# ------------------------------------------------------------
# CONTROLES GLOBAIS (TEMA E IDIOMA)
# ------------------------------------------------------------
if "tema" not in st.session_state:
    st.session_state.tema = "Claro"

if "idioma" not in st.session_state:
    st.session_state.idioma = "PT"

def aplicar_tema():
    if st.session_state.tema == "Escuro":
        st.markdown("""
        <style>
        body { background-color: #0e1117; color: white; }
        </style>
        """, unsafe_allow_html=True)

def t(pt, en):
    return pt if st.session_state.idioma == "PT" else en

aplicar_tema()

# ------------------------------------------------------------
# ESTILO PERSONALIZADO (CSS)
# ------------------------------------------------------------
st.markdown("""
<style>
.main-title {
    text-align: center;
    color: #1f77b4;
    font-weight: bold;
}
.sub-title {
    text-align: center;
    font-style: italic;
    color: #555;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# MENU LATERAL (NAVBAR)
# ------------------------------------------------------------
st.sidebar.title("📚 Menu do Curso")
st.sidebar.image(
    "https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif",
    use_column_width=True
)

menu = st.sidebar.radio("Navegue entre as seções:", [
    "🏠 Página Inicial",
    "🧩 Introdução à Ciência de Dados",
    "📊 Limpeza de Dados",
    "🧹 Limpeza de CSV (Profissional)",
    "📈 Análise de Dados",
    "🧠 Funções Python",
    "📂 Operações com Listas",
    "⚡ Módulo Avançado Interativo",
    "❓ Quiz do Curso"
])

# Preferências
st.sidebar.markdown("### ⚙️ Preferências")

st.session_state.tema = st.sidebar.selectbox(
    "🌗 Tema",
    ["Claro", "Escuro"],
    index=0 if st.session_state.tema == "Claro" else 1
)

st.session_state.idioma = st.sidebar.selectbox(
    "🌎 Idioma",
    ["PT", "EN"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 Dica: explore cada módulo em ordem para aproveitar melhor o conteúdo!")

# ------------------------------------------------------------
# --- 0. PÁGINA INICIAL ---
# ------------------------------------------------------------
if menu == "🏠 Página Inicial":
    st.markdown("<h1 class='main-title'>🚀 Curso Completo da introdução de Ciência de Dados com Python</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Do zero à prática — entenda, limpe, analise e visualize dados com Python!</p>", unsafe_allow_html=True)

    st.markdown("---")
    st.image("https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif", width=300)

    st.header("📖 Sobre o Curso")
    st.write("""
Este curso foi desenvolvido para **introduzir você à Ciência de Dados**, combinando teoria e prática em um ambiente interativo com Python.

Você aprenderá:
- Conceitos fundamentais de Ciência de Dados
- Programação prática em Python
- Limpeza e manipulação de dados com Pandas e Numpy
- Funções e estruturas de dados
- Interatividade com Streamlit
""")

    st.video("https://youtu.be/cm_tM0m9zcI")

    st.header("🎯 Objetivo do Curso")
    st.write("""
Ao final deste curso, você será capaz de:
- Compreender análise de dados
- Criar e limpar DataFrames
- Escrever funções eficientes
- Trabalhar com listas
- Criar apps com Streamlit
""")

    st.success("Clique no menu lateral para iniciar!")

# ------------------------------------------------------------
# INTRODUÇÃO
# ------------------------------------------------------------
elif menu == "🧩 Introdução à Ciência de Dados":
    st.title("🧠 Introdução à Ciência de Dados")

    st.video("https://youtu.be/i6fcwf31htU")

    st.code('print("Olá, mundo da Ciência de Dados!")', language="python")

    idades = np.array([23, 35, 29])
    media = np.mean(idades)

    st.success(f"Média das idades: {media}")

    dados = {"Nome": ["Ana", "Carlos", "Beatriz"], "Idade": [23, 35, 29]}
    df = pd.DataFrame(dados)

    st.dataframe(df)
    st.dataframe(df.describe())

# ------------------------------------------------------------
# LIMPEZA CSV
# ------------------------------------------------------------
elif menu == "🧹 Limpeza de CSV (Profissional)":
    file = st.file_uploader("Upload do CSV", type=["csv"])

    if file:
        df = pd.read_csv(file)
        st.dataframe(df)

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        df.drop_duplicates(inplace=True)

        for col in df.columns:
            if df[col].dtype == "object":
                df[col].fillna("Desconhecido", inplace=True)
            else:
                df[col].fillna(df[col].mean(), inplace=True)

        st.success("Limpeza concluída")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Baixar CSV",
            data=csv,
            file_name="dados_tratados.csv",
            mime="text/csv"
        )

# ------------------------------------------------------------
# MÓDULO INTERATIVO
# ------------------------------------------------------------
elif menu == "⚡ Módulo Avançado Interativo":
    st.title("Módulo Interativo")

    numero = st.number_input("Número", value=2.0)
    expoente = st.number_input("Expoente", value=2.0)

    resultado = numero ** expoente
    st.success(f"Resultado: {resultado}")

# ------------------------------------------------------------
# QUIZ
# ------------------------------------------------------------
elif menu == "❓ Quiz do Curso":
    pontuacao = 0

    q1 = st.radio("O que é Ciência de Dados?", [
        "Apenas gráficos",
        "Estatística + programação",
        "Planilhas"
    ])

    if q1 == "Estatística + programação":
        pontuacao += 1

    if st.button("Ver resultado"):
        st.success(f"Pontuação: {pontuacao}/1")
