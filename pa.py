import streamlit as st
import pandas as pd
import numpy as np

# ==================================================
# CONFIGURAÇÃO DA PÁGINA
# ==================================================
st.set_page_config(
    page_title="Projeto do Ano | Ciência de Dados",
    page_icon="🧠",
    layout="wide"
)

# ==================================================
# ESTILO VISUAL (CSS)
# ==================================================
st.markdown("""
<style>
    .titulo {
        text-align: center;
        color: #1f77b4;
        font-weight: bold;
    }
    .subtitulo {
        text-align: center;
        color: #555;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# ==================================================
# PÁGINAS
# ==================================================

def pagina_inicial():
    st.markdown("<h1 class='titulo'>🚀 Pipeline Interativo de Ciência de Dados</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitulo'>Projeto do Ano – Análise e Limpeza de Dados com Python</p>", unsafe_allow_html=True)

    st.image(
        "https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif",
        width=300
    )

    st.markdown("""
    ## 📌 Sobre o Projeto

    Este projeto foi desenvolvido com o objetivo de **demonstrar, na prática,
    o funcionamento da Ciência de Dados**, desde a teoria até a aplicação real.

    Diferente de exemplos simplificados, aqui o sistema trabalha com **dados reais
    em formato CSV**, que normalmente chegam **desorganizados, incompletos ou inconsistentes**.

    ## 🎯 Objetivos
    - Explicar **o que é Ciência de Dados**
    - Simular o trabalho de um **cientista de dados**
    - Analisar e limpar dados automaticamente
    - Gerar estatísticas confiáveis
    - Exportar dados prontos para análise
    """)

    st.success("📊 Projeto desenvolvido para apresentação acadêmica e portfólio técnico.")

def pagina_ciencia_dados():
    st.markdown("<h1 class='titulo'>🧠 O que é Ciência de Dados?</h1>", unsafe_allow_html=True)

    st.markdown("""
    ## 📘 Conceito

    **Ciência de Dados** é uma área multidisciplinar que utiliza:

    - 📊 Estatística  
    - 🐍 Programação  
    - 🧠 Análise crítica  

    para **extrair conhecimento, padrões e informações relevantes a partir de dados**.

    ---

    ## 🌍 Onde a Ciência de Dados é usada?

    A Ciência de Dados está presente em diversas áreas do cotidiano, como:

    - 🎬 Plataformas de streaming (recomendações)
    - 🏦 Bancos e fintechs (detecção de fraudes)
    - 🏥 Saúde (análise de exames e diagnósticos)
    - 📱 Redes sociais (algoritmos de engajamento)
    - 🛒 Comércio (previsão de vendas)

    ---

    ## 🔄 Etapas do Processo de Ciência de Dados

    1️⃣ Coleta dos dados  
    2️⃣ Limpeza e organização  
    3️⃣ Análise estatística  
    4️⃣ Visualização dos resultados  
    5️⃣ Tomada de decisão  

    📌 **Este projeto foca principalmente nas etapas 2 e 3**, que são consideradas
    as mais importantes na prática profissional.

    > 💡 Sem dados limpos e confiáveis, nenhuma análise gera resultados corretos.
    """)

def pipeline_csv():
    st.markdown("<h1 class='titulo'>🧹 Pipeline de Análise e Limpeza de CSV</h1>", unsafe_allow_html=True)

    st.markdown("""
    ## 🎯 Objetivo do Pipeline

    Este módulo simula um **ambiente real de trabalho em Ciência de Dados**,
    onde o profissional recebe um arquivo CSV e precisa:

    - Avaliar a qualidade dos dados
    - Identificar problemas
    - Corrigir inconsistências
    - Gerar estatísticas confiáveis
    - Entregar dados prontos para uso
    """)

    arquivo = st.file_uploader("📤 Envie um arquivo CSV", type=["csv"])

    if arquivo:
        df = pd.read_csv(arquivo)

        st.markdown("---")
        st.subheader("📄 Visualização dos Dados Originais")
        st.dataframe(df.head())

        st.markdown("---")
        st.subheader("⚠️ Diagnóstico Inicial")

        col1, col2 = st.columns(2)

        with col1:
            st.write("🔎 Valores nulos por coluna:")
            st.write(df.isnull().sum())

        with col2:
            st.write("📂 Tipos de dados:")
            st.write(df.dtypes)

        st.markdown("""
        ## 🧼 Processo de Limpeza Aplicado

        As seguintes etapas são executadas automaticamente:
        - Padronização dos nomes das colunas
        - Remoção de linhas totalmente vazias
        - Remoção de valores nulos
        """)

        df_limpo = df.copy()

        # Padronização dos nomes das colunas
        df_limpo.columns = df_limpo.columns.str.strip().str.lower()

        # Remoção de linhas completamente vazias
        df_limpo = df_limpo.dropna(how="all")

        # Remoção de valores nulos
        df_limpo = df_limpo.dropna()

        st.success("✅ Limpeza de dados concluída com sucesso!")

        st.markdown("---")
        st.subheader("📊 Dados Após Limpeza")
        st.dataframe(df_limpo.head())

        st.markdown("---")
        st.subheader("📈 Estatísticas Descritivas")
        st.dataframe(df_limpo.describe())

        st.download_button(
            "📥 Baixar CSV Tratado",
            df_limpo.to_csv(index=False),
            file_name="dados_tratados.csv",
            mime="text/csv"
        )

        st.info("""
        📌 Este processo representa uma etapa essencial da Ciência de Dados,
        garantindo que as análises sejam realizadas sobre dados confiáveis.
        """)

# ==================================================
# MENU LATERAL
# ==================================================
menu = st.sidebar.radio(
    "📚 Navegação",
    [
        "🏠 Apresentação do Projeto",
        "🧠 O que é Ciência de Dados?",
        "🧹 Pipeline de CSV (Projeto do Ano)"
    ]
)

# ==================================================
# CONTROLE DE NAVEGAÇÃO
# ==================================================
if menu == "🏠 Apresentação do Projeto":
    pagina_inicial()

elif menu == "🧠 O que é Ciência de Dados?":
    pagina_ciencia_dados()

elif menu == "🧹 Pipeline de CSV (Projeto do Ano)":
    pipeline_csv()
