import streamlit as st
import pandas as pd
import numpy as np

# ==================================================
# CONFIGURAÇÃO DA PÁGINA
# ==================================================
st.set_page_config(
    page_title="Curso de Ciência de Dados com Python",
    page_icon="🧠",
    layout="wide"
)

# ==================================================
# ESTILO (CSS)
# ==================================================
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #1f77b4;
        font-weight: bold;
    }
    .sub-title {
        text-align: center;
        color: #555;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# ==================================================
# FUNÇÕES DAS PÁGINAS
# ==================================================

def pagina_inicial():
    st.markdown("<h1 class='main-title'>🚀 Curso de Ciência de Dados com Python</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Do zero à análise profissional de dados</p>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif", width=300)

    st.markdown("""
    ### 📌 O que você vai aprender
    - Fundamentos de Ciência de Dados  
    - Python aplicado à análise  
    - Limpeza de dados reais  
    - Estatística básica  
    - Projetos interativos com Streamlit  
    """)

def introducao_cd():
    st.title("🧠 Introdução à Ciência de Dados")
    st.write("""
    Ciência de Dados combina **estatística, programação e análise** para gerar insights.
    """)
    st.code('print("Olá, mundo da Ciência de Dados!")', language="python")

    idades = np.array([18, 22, 25, 30])
    st.success(f"Média das idades: {np.mean(idades)}")

def limpeza_dados():
    st.title("📊 Limpeza de Dados")
    st.write("""
    A limpeza de dados é uma das etapas mais importantes da Ciência de Dados.
    """)
    st.markdown("""
    ✔ Remover valores nulos  
    ✔ Corrigir tipos de dados  
    ✔ Padronizar colunas  
    ✔ Tratar erros e inconsistências  
    """)

def funcoes_python():
    st.title("🧠 Funções em Python")
    st.code("""
def saudacao(nome):
    return f"Olá, {nome}!"
""", language="python")

    nome = st.text_input("Digite seu nome:")
    if nome:
        st.success(saudacao := f"Olá, {nome}!")

def listas_python():
    st.title("📂 Operações com Listas")
    lista = [10, 20, 30, 40]
    st.write("Lista:", lista)
    st.success(f"Soma: {sum(lista)} | Média: {sum(lista)/len(lista)}")

def modulo_interativo():
    st.title("⚡ Módulo Interativo")

    st.subheader("🧮 Calculadora de Potência")
    num = st.number_input("Número:", value=2.0)
    exp = st.number_input("Expoente:", value=2.0)
    st.success(f"Resultado: {num ** exp}")

    st.subheader("📊 Gerador de Dados")
    linhas = st.slider("Quantidade de linhas", 5, 100, 10)
    df = pd.DataFrame({
        "A": np.random.randn(linhas),
        "B": np.random.rand(linhas),
        "C": np.random.randint(0, 100, linhas)
    })
    st.dataframe(df)
    st.line_chart(df)

def analise_csv_profissional():
    st.title("🧹 Análise e Limpeza de CSV (Profissional)")
    st.write("Envie um arquivo CSV real para análise automática.")

    arquivo = st.file_uploader("📤 Envie um CSV", type=["csv"])

    if arquivo:
        df = pd.read_csv(arquivo)

        st.subheader("📄 Visualização Inicial")
        st.dataframe(df.head())

        st.subheader("📉 Valores Nulos")
        st.write(df.isnull().sum())

        st.subheader("📐 Estatísticas")
        st.dataframe(df.describe())

        st.subheader("🧼 Limpeza Automática")
        df_limpo = df.copy()
        df_limpo.columns = df_limpo.columns.str.strip().str.lower()
        df_limpo = df_limpo.dropna()

        st.success("Dados limpos com sucesso!")
        st.dataframe(df_limpo.head())

        st.download_button(
            "📥 Baixar CSV Limpo",
            df_limpo.to_csv(index=False),
            file_name="dados_limpos.csv",
            mime="text/csv"
        )

def quiz():
    st.title("❓ Quiz de Ciência de Dados")

    pontos = 0

    q1 = st.radio("O que é Pandas?", ["Biblioteca", "Linguagem", "Sistema Operacional"])
    if q1 == "Biblioteca":
        pontos += 1

    q2 = st.radio("Para que serve df.describe()?", [
        "Excluir colunas",
        "Mostrar estatísticas",
        "Criar gráficos"
    ])
    if q2 == "Mostrar estatísticas":
        pontos += 1

    q3 = st.radio("O que significa CSV?", [
        "Código Simples Visual",
        "Comma-Separated Values",
        "Cálculo de Séries Variadas"
    ])
    if q3 == "Comma-Separated Values":
        pontos += 1

    if st.button("Ver Resultado"):
        st.success(f"🎯 Pontuação final: {pontos}/3")
        if pontos == 3:
            st.balloons()

# ==================================================
# MENU LATERAL
# ==================================================
menu = st.sidebar.radio(
    "📚 Navegação",
    [
        "🏠 Página Inicial",
        "🧩 Introdução à Ciência de Dados",
        "📊 Limpeza de Dados",
        "🧠 Funções Python",
        "📂 Operações com Listas",
        "⚡ Módulo Interativo",
        "🧹 Análise e Limpeza de CSV (Profissional)",
        "❓ Quiz"
    ]
)

# ==================================================
# ROTEAMENTO
# ==================================================
if menu == "🏠 Página Inicial":
    pagina_inicial()
elif menu == "🧩 Introdução à Ciência de Dados":
    introducao_cd()
elif menu == "📊 Limpeza de Dados":
    limpeza_dados()
elif menu == "🧠 Funções Python":
    funcoes_python()
elif menu == "📂 Operações com Listas":
    listas_python()
elif menu == "⚡ Módulo Interativo":
    modulo_interativo()
elif menu == "🧹 Análise e Limpeza de CSV (Profissional)":
    analise_csv_profissional()
elif menu == "❓ Quiz":
    quiz()
