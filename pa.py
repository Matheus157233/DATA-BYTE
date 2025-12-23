import streamlit as st
import pandas as pd
import numpy as np

# =============================
# CONFIGURAÇÃO DA PÁGINA
# =============================
st.set_page_config(
    page_title="DATA BYTE | Data Science Project",
    page_icon="📊",
    layout="wide"
)

# =============================
# IDIOMA
# =============================
lang = st.sidebar.selectbox("🌍 Language / Idioma", ["Português", "English"])

def t(pt, en):
    return pt if lang == "Português" else en

# =============================
# TEMA
# =============================
theme = st.sidebar.radio("🎨 Tema / Theme", ["🌞 Light", "🌙 Dark"])

if theme == "🌙 Dark":
    st.markdown("""
    <style>
    body, .stApp {
        background-color: #0e1117;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# =============================
# ESTILO
# =============================
st.markdown("""
<style>
.title {
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 10px;
}
.subtitle {
    font-size: 20px;
    color: gray;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: rgba(255,255,255,0.04);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# =============================
# MENU
# =============================
menu = st.sidebar.selectbox(
    t("Menu","Menu"),
    [
        t("🏠 Início","🏠 Home"),
        t("📚 O que é Ciência de Dados","📚 What is Data Science"),
        t("📂 Upload de Dados","📂 Data Upload"),
        t("🧹 Limpeza de Dados","🧹 Data Cleaning"),
        t("🔍 EDA Profissional","🔍 Professional EDA"),
        t("📈 Correlação","📈 Correlation"),
        t("📌 Conclusão","📌 Conclusion")
    ]
)

# =============================
# INÍCIO
# =============================
if menu == t("🏠 Início","🏠 Home"):
    st.markdown(f"<div class='title'>DATA BYTE</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='subtitle'>{t('Projeto de Ciência de Dados','Data Science Project')}</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    Este projeto apresenta um pipeline completo de Ciência de Dados,
    desde dados brutos até análises exploratórias profissionais.
    </div>
    """, unsafe_allow_html=True)

# =============================
# TEORIA
# =============================
elif menu == t("📚 O que é Ciência de Dados","📚 What is Data Science"):
    st.markdown(f"<div class='title'>{t('Ciência de Dados','Data Science')}</div>", unsafe_allow_html=True)

    st.markdown(
        t(
            """
            Ciência de Dados é a área responsável por extrair conhecimento
            a partir de dados brutos por meio de estatística, programação
            e pensamento analítico.
            
            Envolve etapas como:
            - Coleta
            - Limpeza
            - Análise Exploratória
            - Interpretação
            """,
            """
            Data Science is the field responsible for extracting knowledge
            from raw data using statistics, programming, and analytical thinking.
            
            It involves steps such as:
            - Data collection
            - Data cleaning
            - Exploratory analysis
            - Interpretation
            """
        )
    )

# =============================
# UPLOAD
# =============================
elif menu == t("📂 Upload de Dados","📂 Data Upload"):
    st.markdown(f"<div class='title'>Upload CSV</div>", unsafe_allow_html=True)

    file = st.file_uploader("CSV", type=["csv"])

    if file:
        df = pd.read_csv(file)
        st.session_state["raw"] = df
        st.success(t("Arquivo carregado","File loaded"))
        st.dataframe(df.head())

# =============================
# LIMPEZA
# =============================
elif menu == t("🧹 Limpeza de Dados","🧹 Data Cleaning"):
    st.markdown(f"<div class='title'>{t('Limpeza de Dados','Data Cleaning')}</div>", unsafe_allow_html=True)

    if "raw" in st.session_state:
        df = st.session_state["raw"]

        st.subheader(t("Antes","Before"))
        st.dataframe(df.head())

        clean = df.copy()

        clean.drop_duplicates(inplace=True)

        for col in clean.select_dtypes(include="object"):
            clean[col] = clean[col].fillna(clean[col].mode()[0])

        for col in clean.select_dtypes(include=["int64","float64"]):
            clean[col] = clean[col].fillna(clean[col].mean())

        st.session_state["clean"] = clean

        st.subheader(t("Depois","After"))
        st.dataframe(clean.head())

    else:
        st.warning(t("Envie um CSV primeiro","Upload a CSV first"))

# =============================
# EDA
# =============================
elif menu == t("🔍 EDA Profissional","🔍 Professional EDA"):
    st.markdown(f"<div class='title'>EDA</div>", unsafe_allow_html=True)

    if "clean" in st.session_state:
        df = st.session_state["clean"]

        st.subheader(t("Resumo Estatístico","Statistical Summary"))
        st.dataframe(df.describe())

        num_cols = df.select_dtypes(include=["int64","float64"]).columns

        if len(num_cols) > 0:
            col = st.selectbox(t("Variável","Variable"), num_cols)
            st.line_chart(df[col])
    else:
        st.warning(t("Faça a limpeza primeiro","Run cleaning first"))

# =============================
# CORRELAÇÃO
# =============================
elif menu == t("📈 Correlação","📈 Correlation"):
    st.markdown(f"<div class='title'>{t('Correlação','Correlation')}</div>", unsafe_allow_html=True)

    if "clean" in st.session_state:
        df = st.session_state["clean"]
        num_cols = df.select_dtypes(include=["int64","float64"])

        if len(num_cols.columns) >= 2:
            corr = num_cols.corr()
            st.dataframe(corr)
            st.bar_chart(corr)
    else:
        st.warning(t("Execute a limpeza","Run cleaning"))

# =============================
# CONCLUSÃO
# =============================
elif menu == t("📌 Conclusão","📌 Conclusion"):
    st.markdown(f"<div class='title'>{t('Conclusão','Conclusion')}</div>", unsafe_allow_html=True)

    st.markdown(
        t(
            """
            Este projeto demonstrou como dados reais exigem
            limpeza, análise e interpretação cuidadosa.

            O processo de Ciência de Dados não começa na análise,
            mas na organização dos dados.
            """,
            """
            This project demonstrated how real-world data
            requires careful cleaning, analysis, and interpretation.

            Data Science does not start with analysis,
            but with data preparation.
            """
        )
    )
