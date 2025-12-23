import streamlit as st
import pandas as pd
import numpy as np

# ================= CONFIG =================
st.set_page_config(
    page_title="DATA BYTE | Data Science Project",
    page_icon="📊",
    layout="wide"
)

# ================= LANGUAGE =================
lang = st.sidebar.radio("🌍 Language / Idioma", ["🇧🇷 Português", "🇺🇸 English"])

def t(pt, en):
    return pt if lang == "🇧🇷 Português" else en

# ================= STYLE =================
st.markdown("""
<style>
.title {font-size:40px;font-weight:700;}
.subtitle {font-size:18px;color:#6c757d;}
.section {margin-top:40px;}
</style>
""", unsafe_allow_html=True)

# ================= FUNCTIONS =================
def diagnose(df):
    return {
        t("Linhas","Rows"): df.shape[0],
        t("Colunas","Columns"): df.shape[1],
        t("Valores nulos","Missing values"): int(df.isnull().sum().sum()),
        t("Duplicados","Duplicates"): int(df.duplicated().sum())
    }

def clean_data(df):
    df = df.copy()

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")

    for col in df.select_dtypes(include=["int64", "float64"]).columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].fillna(t("Não informado", "Not informed"))

    df = df.drop_duplicates()
    return df

# ================= SIDEBAR =================
menu = st.sidebar.radio(
    t("Navegação","Navigation"),
    [
        t("🏠 Apresentação","🏠 Introduction"),
        t("📘 Ciência de Dados","📘 Data Science"),
        t("📂 Upload & Diagnóstico","📂 Upload & Diagnosis"),
        t("🧹 Limpeza Profissional","🧹 Professional Cleaning"),
        t("📊 Análise & Visualização","📊 Analysis & Visualization"),
        t("⬇️ Download Final","⬇️ Final Download")
    ]
)

# ================= PAGES =================
if menu == t("🏠 Apresentação","🏠 Introduction"):
    st.markdown("<div class='title'>📊 DATA BYTE</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='subtitle'>{t('Pipeline profissional de Ciência de Dados','Professional Data Science Pipeline')}</div>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown(
        t(
            """
            ### 🎯 Objetivo do Projeto
            Este projeto demonstra como dados reais e desorganizados
            podem ser transformados em dados confiáveis por meio
            de um pipeline profissional de Ciência de Dados.
            """,
            """
            ### 🎯 Project Objective
            This project demonstrates how real-world messy data
            can be transformed into reliable datasets through
            a professional Data Science pipeline.
            """
        )
    )

elif menu == t("📘 Ciência de Dados","📘 Data Science"):
    st.markdown(f"<div class='title'>{t('Ciência de Dados','Data Science')}</div>", unsafe_allow_html=True)

    st.markdown(
        t(
            """
            Ciência de Dados combina **estatística, programação
            e análise de dados** para gerar conhecimento e apoiar decisões.

            ### Etapas principais:
            - Coleta de dados
            - Diagnóstico
            - Limpeza e preparação
            - Análise exploratória
            - Interpretação
            """,
            """
            Data Science combines **statistics, programming
            and data analysis** to generate knowledge and
            support decision-making.

            ### Main stages:
            - Data collection
            - Diagnosis
            - Cleaning and preparation
            - Exploratory analysis
            - Interpretation
            """
        )
    )

elif menu == t("📂 Upload & Diagnóstico","📂 Upload & Diagnosis"):
    st.markdown(f"<div class='title'>{t('Upload e Diagnóstico','Upload and Diagnosis')}</div>", unsafe_allow_html=True)

    file = st.file_uploader(t("Envie um arquivo CSV","Upload a CSV"), type="csv")

    if file:
        df = pd.read_csv(file)
        st.session_state["raw"] = df

        st.subheader(t("Visualização inicial","Initial preview"))
        st.dataframe(df.head())

        diag = diagnose(df)
        cols = st.columns(4)
        for i, (k, v) in enumerate(diag.items()):
            cols[i].metric(k, v)

elif menu == t("🧹 Limpeza Profissional","🧹 Professional Cleaning"):
    st.markdown(f"<div class='title'>{t('Limpeza Profissional','Professional Cleaning')}</div>", unsafe_allow_html=True)

    if "raw" in st.session_state:
        if st.button(t("Executar limpeza","Run cleaning")):
            clean = clean_data(st.session_state["raw"])
            st.session_state["clean"] = clean

            st.success(t("Limpeza concluída com sucesso","Cleaning completed successfully"))

            c1, c2 = st.columns(2)
            c1.metric(t("Linhas antes","Rows before"), st.session_state["raw"].shape[0])
            c2.metric(t("Linhas depois","Rows after"), clean.shape[0])

            st.subheader(t("Prévia após limpeza","After cleaning preview"))
            st.dataframe(clean.head())
    else:
        st.warning(t("Envie um arquivo primeiro","Upload a file first"))

elif menu == t("📊 Análise & Visualização","📊 Analysis & Visualization"):
    st.markdown(f"<div class='title'>{t('Análise & Visualização','Analysis & Visualization')}</div>", unsafe_allow_html=True)

    if "raw" in st.session_state and "clean" in st.session_state:
        raw = st.session_state["raw"]
        clean = st.session_state["clean"]

        numeric_cols = clean.select_dtypes(include=["int64","float64"]).columns

        if len(numeric_cols) > 0:
            col = st.selectbox(t("Selecione uma coluna numérica","Select a numeric column"), numeric_cols)

            st.markdown(t("### 📉 Antes da limpeza","### 📉 Before cleaning"))
            st.bar_chart(raw[col].dropna())

            st.markdown(t("### 📈 Depois da limpeza","### 📈 After cleaning"))
            st.bar_chart(clean[col].dropna())

            st.markdown(
                t(
                    "A comparação evidencia como a limpeza melhora a consistência dos dados.",
                    "The comparison shows how cleaning improves data consistency."
                )
            )
    else:
        st.warning(t("Execute as etapas anteriores","Run previous steps"))

elif menu == t("⬇️ Download Final","⬇️ Final Download"):
    st.markdown(f"<div class='title'>{t('Download Final','Final Download')}</div>", unsafe_allow_html=True)

    if "clean" in st.session_state:
        csv = st.session_state["clean"].to_csv(index=False).encode("utf-8")

        st.download_button(
            t("Baixar CSV tratado","Download cleaned CSV"),
            csv,
            "dados_tratados.csv",
            "text/csv"
        )
    else:
        st.warning(t("Nenhum dado tratado disponível","No cleaned data available"))
