import streamlit as st
import pandas as pd
import numpy as np
import math

# ------------------------------------------------------------
# CONFIGURAÇÃO GERAL DA PÁGINA
# ------------------------------------------------------------
st.set_page_config(
    page_title="Curso Completo: Introdução à Ciência de Dados com Python",
    page_icon="🧠",
    layout="wide"
)

# ------------------------------------------------------------
# ESTILO PERSONALIZADO (CSS)
# ------------------------------------------------------------
st.markdown("""
<style>
    body {
        background-color: #f5f5f5;
    }
    .stApp {
        background-color: #ffffff;
    }
    h1, h2, h3 {
        color: #0E1117;
    }
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
st.sidebar.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3hyMjEydDh2ZnA2N3Zpb2xzcmhoYzRrd3lxMG03bmd4NjFhb3Y5eCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3og0ILmP5mKAzV3faw/giphy.gif", use_column_width=True)
menu = st.sidebar.radio("Navegue entre as seções:", [
    "🏠 Página Inicial",
    "🧩 Introdução à Ciência de Dados",
    "📊 Limpeza de Dados",
    "🧠 Funções Python",
    "📂 Operações com Listas",
    "⚡ Módulo Avançado Interativo",
    "❓ Quiz do Curso"
])
st.sidebar.markdown("---")
st.sidebar.info("💡 Dica: explore cada módulo em ordem para aproveitar melhor o conteúdo!")

# ------------------------------------------------------------
# --- 0. PÁGINA INICIAL ---
# ------------------------------------------------------------
if menu == "🏠 Página Inicial":
    st.markdown("<h1 class='main-title'>🚀 Curso Completo de Ciência de Dados com Python</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Do zero à prática — entenda, limpe, analise e visualize dados com Python!</p>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif", width=300)

    st.header("📖 Sobre o Curso")
    st.write("""
Este curso foi desenvolvido para **introduzir você à Ciência de Dados**, combinando **teoria e prática** em um ambiente interativo com Python.

Você aprenderá:
- 🧮 Conceitos fundamentais de Ciência de Dados  
- 🐍 Programação prática em Python  
- 📊 Limpeza e manipulação de dados com Pandas e Numpy  
- 💡 Funções e estruturas de dados em Python  
- ⚡ Interatividade com Streamlit  
""")

    st.video("https://youtu.be/cm_tM0m9zcI")
    st.success("✅ Clique no menu lateral para iniciar sua jornada!")

# ------------------------------------------------------------
# --- 1. Introdução à Ciência de Dados ---
# ------------------------------------------------------------
elif menu == "🧩 Introdução à Ciência de Dados":
    st.title("🧠 Introdução à Ciência de Dados")
    st.image("https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif", width=250)

    st.header("📘 O que é Ciência de Dados?")
    st.write("""
A **Ciência de Dados** une **estatística, programação e análise de dados** para gerar insights e apoiar decisões.
""")
    st.video("https://youtu.be/i6fcwf31htU")

    st.header("🐍 Primeiros Passos com Python")
    st.code('print("Olá, mundo da Ciência de Dados!")', language="python")
    idades = np.array([23, 35, 29])
    st.success(f"Média das idades: {np.mean(idades)}")

    st.header("📦 Trabalhando com pandas (DataFrames)")
    dados = {"Nome": ["Ana", "Carlos", "Beatriz"], "Idade": [23, 35, 29]}
    df = pd.DataFrame(dados)
    st.dataframe(df)
    st.write("📈 Estatísticas descritivas:")
    st.dataframe(df.describe())

# ------------------------------------------------------------
# --- 2. Limpeza de Dados ---
# ------------------------------------------------------------
elif menu == "📊 Limpeza de Dados":
    st.title("📊 Limpeza de Dados")
    st.subheader("Preparando e organizando dados sujos para análise")
    st.image("https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif", width=200)
    st.write("""
Antes de analisar dados, é essencial **limpá-los e estruturá-los** corretamente.
""")
    st.video("https://youtu.be/WQ5rsl8y_dw")

# ------------------------------------------------------------
# --- 3. Funções Python ---
# ------------------------------------------------------------
elif menu == "🧠 Funções Python":
    st.title("🧠 Funções em Python")
    st.subheader("Organizando códigos e automatizando tarefas")
    st.video("https://www.youtube.com/watch?v=9Os0o3wzS_I")

    st.code("""
def saudacao(nome):
    return f"Olá, {nome}!"
""", language="python")

# ------------------------------------------------------------
# --- 4. Operações com Listas ---
# ------------------------------------------------------------
elif menu == "📂 Operações com Listas":
    st.title("📂 Operações com Listas")
    st.video("https://www.youtube.com/watch?v=ohCDWZgNIU0")

    st.code("""
lista = [1, 2, 3, 4, 5]
soma = sum(lista)
media = soma / len(lista)
print(f"Soma: {soma}, Média: {media}")
""", language="python")

# ------------------------------------------------------------
# --- 5. Módulo Avançado Interativo ---
# ------------------------------------------------------------
elif menu == "⚡ Módulo Avançado Interativo":
    st.title("⚡ Módulo Avançado Interativo")
    st.subheader("Experimente funções e cálculos ao vivo com Python!")
    st.image("https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif", width=250)

    # 1️⃣ Saudação
    nome = st.text_input("Digite seu nome:")
    if nome:
        st.success(f"Olá, {nome}! 👋 Vamos testar um pouco de Python ao vivo!")

    # 2️⃣ Calculadora de Potência
    st.markdown("---")
    st.header("🧮 Calculadora de Potência")
    numero = st.number_input("Digite um número (pode ser decimal):", value=2.0, step=0.1)
    expoente = st.number_input("Digite o expoente:", value=2.0, step=0.1)
    resultado = numero ** expoente
    st.success(f"🔹 Resultado: {numero} elevado a {expoente} = **{resultado}**")

    # 3️⃣ Calculadora simples
    st.markdown("---")
    st.header("🧠 Mini Calculadora Inteligente")
    a = st.number_input("Valor A:", value=0.0, step=0.1)
    b = st.number_input("Valor B:", value=0.0, step=0.1)
    operacao = st.selectbox("Escolha uma operação:", ["Soma", "Subtração", "Multiplicação", "Divisão"])
    if st.button("Calcular"):
        if operacao == "Soma":
            st.success(f"✅ Resultado: {a + b}")
        elif operacao == "Subtração":
            st.success(f"✅ Resultado: {a - b}")
        elif operacao == "Multiplicação":
            st.success(f"✅ Resultado: {a * b}")
        elif operacao == "Divisão":
            st.success(f"✅ Resultado: {a / b if b != 0 else 'Erro: divisão por zero!'}")

    # 4️⃣ Geração de dados
    st.markdown("---")
    st.header("📊 Gerador de Dados Aleatórios")
    linhas = st.slider("Número de linhas:", 5, 100, 10)
    df = pd.DataFrame({
        "A": np.random.randn(linhas),
        "B": np.random.rand(linhas),
        "C": np.random.randint(0, 100, linhas)
    })
    st.dataframe(df)
    st.line_chart(df)

    # 5️⃣ Download do CSV de exemplo
    st.markdown("---")
    st.header("📥 Baixe o arquivo CSV de exemplo para praticar")
    csv_content = """Nome,Idade,Nota,Presenca
Ana,22,8.5,Sim
Bruno,25,7.8,Sim
Carla,23,9.2,Não
Diego,21,,Sim
Elisa,24,6.9,Não
Felipe,22,8.0,Sim
Gabriela,26,7.5,Sim
Henrique,20,5.8,Não
Isabela,23,,Sim
João,25,9.5,Sim
"""
    st.download_button(
        label="📩 Baixar arquivo DADOS_ALUNOS.csv",
        data=csv_content,
        file_name="DADOS_ALUNOS.csv",
        mime="text/csv"
    )

    # 6️⃣ Upload e análise de CSV
    st.markdown("---")
    st.header("📂 Upload e Análise de CSV")
    uploaded_file = st.file_uploader("Envie seu arquivo CSV", type=["csv"])
    if uploaded_file is not None:
        df_user = pd.read_csv(uploaded_file)
        st.write("📄 Visualização inicial:")
        st.dataframe(df_user.head())
        st.write("📊 Estatísticas:")
        st.dataframe(df_user.describe())

    st.success("🎉 Parabéns! Você explorou todos os módulos interativos do curso!")

# ------------------------------------------------------------
# --- 6. Quiz do Curso ---
# ------------------------------------------------------------
elif menu == "❓ Quiz do Curso":
    st.title("❓ Quiz - Ciência de Dados com Python")
    st.subheader("Teste seus conhecimentos adquiridos no mini curso!")

    pontuacao = 0

    q1 = st.radio("1️⃣ O que é Ciência de Dados?", [
        "Apenas criar gráficos",
        "A união de estatística, programação e análise de dados",
        "Somente análise de planilhas"
    ])
    if q1 == "A união de estatística, programação e análise de dados":
        pontuacao += 1

    q2 = st.radio("2️⃣ Qual biblioteca é usada para manipular tabelas de dados?", [
        "NumPy",
        "Matplotlib",
        "Pandas"
    ])
    if q2 == "Pandas":
        pontuacao += 1

    q3 = st.radio("3️⃣ O que a função `print()` faz em Python?", [
        "Cria gráficos",
        "Mostra mensagens ou resultados na tela",
        "Apaga variáveis"
    ])
    if q3 == "Mostra mensagens ou resultados na tela":
        pontuacao += 1

    q4 = st.radio("4️⃣ Qual comando remove valores nulos em um DataFrame Pandas?", [
        "df.remove_nulls()",
        "df.fillna()",
        "df.dropna()"
    ])
    if q4 == "df.dropna()":
        pontuacao += 1

    q5 = st.radio("5️⃣ Qual é o símbolo para definir uma função em Python?", [
        "func",
        "def",
        "lambda"
    ])
    if q5 == "def":
        pontuacao += 1

    st.markdown("---")
    if st.button("Ver resultado"):
        st.success(f"🎯 Sua pontuação final: **{pontuacao}/5**")
        if pontuacao == 5:
            st.balloons()
            st.success("🏆 Excelente! Você dominou o conteúdo do curso!")
        elif pontuacao >= 3:
            st.info("💪 Bom trabalho! Reveja alguns conceitos para aperfeiçoar ainda mais.")
        else:
            st.warning("📘 Continue estudando! Volte aos módulos e pratique mais.")

