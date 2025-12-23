import streamlit as st
import pandas as pd
import numpy as np

# ================= CONFIGURAÇÃO DA PÁGINA =================
st.set_page_config(
    page_title="DATA BYTE | Projeto do Ano",
    page_icon="📊",
    layout="wide"
)

# ================= ESTILO VISUAL =================
st.markdown("""
<style>
.big-title {
    font-size: 42px;
    font-weight: bold;
}
.subtitle {
    font-size: 20px;
    color: #6c757d;
}
.section {
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.title("📊 DATA BYTE")
st.sidebar.markdown("Projeto do Ano – Ciência de Dados")

menu = st.sidebar.radio(
    "Navegação",
    [
        "🏠 Apresentação",
        "📘 Ciência de Dados",
        "📂 Upload & Diagnóstico",
        "🧹 Limpeza Profissional",
        "📊 Análises",
        "⬇️ Download Final"
    ]
)

# ================= FUNÇÕES =================
def diagnostico(df):
    return {
        "Linhas": df.shape[0],
        "Colunas": df.shape[1],
        "Valores nulos": int(df.isnull().sum().sum()),
        "Duplicados": int(df.duplicated().sum())
    }

def limpar_dados(df):
    df = df.copy()

    # Padronizar colunas
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    # Converter números
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")

    for col in df.select_dtypes(include=["float", "int"]).columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].fillna("Não informado")

    df = df.drop_duplicates()

    return df

# ================= PÁGINAS =================
if menu == "🏠 Apresentação":
    st.markdown('<div class="big-title">📊 DATA BYTE</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Projeto do Ano – Ciência de Dados</div>', unsafe_allow_html=True)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **Aluno:** Matheus  
        **Curso:** Ensino Médio Técnico em Ciência de Dados  
        **Instituição:** SENAC Nações Unidas  
        """)

    with col2:
        st.markdown("""
        🎯 **Objetivo do Projeto**  
        Demonstrar como dados reais, frequentemente desorganizados,
        podem ser diagnosticados, tratados e analisados de forma profissional,
        garantindo informações confiáveis para tomada de decisão.
        """)

    st.markdown("### 💡 Por que este projeto importa?")
    st.markdown("""
    Empresas dependem de dados para decisões estratégicas.  
    Dados incorretos geram **prejuízos financeiros**, **erros operacionais**
    e **análises enganosas**.

    Este projeto simula um cenário real enfrentado por cientistas de dados.
    """)

elif menu == "📘 Ciência de Dados":
    st.markdown('<div class="big-title">📘 Ciência de Dados</div>', unsafe_allow_html=True)

    st.markdown("""
    **Ciência de Dados** é a área que combina **estatística, programação e análise**
    para extrair conhecimento de dados.

    ### 🔍 Etapas principais:
    - Coleta de dados  
    - Diagnóstico de qualidade  
    - Limpeza e preparação  
    - Análise estatística  
    - Interpretação dos resultados  

    ### ⚠️ Importância da Limpeza
    Dados do mundo real raramente estão prontos para uso.
    Erros simples podem comprometer toda a análise.

    Este sistema demonstra um **pipeline completo**, do dado bruto ao dado confiável.
    """)

elif menu == "📂 Upload & Diagnóstico":
    st.markdown('<div class="big-title">📂 Upload & Diagnóstico</div>', unsafe_allow_html=True)

    file = st.file_uploader("Envie um arquivo CSV", type=["csv"])

    if file:
        df = pd.read_csv(file)
        st.session_state["df_original"] = df

        st.markdown("### 📄 Pré-visualização dos dados")
        st.dataframe(df.head())

        diag = diagnostico(df)

        st.markdown("### 🔎 Diagnóstico Inicial")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Linhas", diag["Linhas"])
        c2.metric("Colunas", diag["Colunas"])
        c3.metric("Valores nulos", diag["Valores nulos"])
        c4.metric("Duplicados", diag["Duplicados"])

elif menu == "🧹 Limpeza Profissional":
    st.markdown('<div class="big-title">🧹 Limpeza Profissional</div>', unsafe_allow_html=True)

    if "df_original" in st.session_state:
        df = st.session_state["df_original"]

        st.markdown("""
        Clique no botão abaixo para executar um **processo automatizado de limpeza**,
        simulando um pipeline profissional de Ciência de Dados.
        """)

        if st.button("🚀 Executar Limpeza"):
            df_limpo = limpar_dados(df)
            st.session_state["df_limpo"] = df_limpo

            st.success("Limpeza concluída com sucesso!")

            c1, c2 = st.columns(2)
            c1.metric("Linhas antes", df.shape[0])
            c2.metric("Linhas depois", df_limpo.shape[0])

            st.markdown("### 📄 Dados após limpeza")
            st.dataframe(df_limpo.head())

    else:
        st.warning("Envie um arquivo CSV primeiro.")

elif menu == "📊 Análises":
    st.markdown('<div class="big-title">📊 Análises Estatísticas</div>', unsafe_allow_html=True)

    if "df_limpo" in st.session_state:
        df = st.session_state["df_limpo"]

        st.markdown("""
        Abaixo estão estatísticas descritivas geradas **após a limpeza**,
        garantindo análises mais confiáveis.
        """)

        st.dataframe(df.describe(include="all"))
    else:
        st.warning("Execute a limpeza antes.")

elif menu == "⬇️ Download Final":
    st.markdown('<div class="big-title">⬇️ Download Final</div>', unsafe_allow_html=True)

    if "df_limpo" in st.session_state:
        csv = st.session_state["df_limpo"].to_csv(index=False).encode("utf-8")

        st.markdown("Arquivo pronto para uso em análises e decisões.")
        st.download_button(
            "📥 Baixar CSV Tratado",
            csv,
            "dados_tratados.csv",
            "text/csv"
        )
    else:
        st.warning("Nenhum dado tratado disponível.")
