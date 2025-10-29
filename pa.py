import streamlit as st
import pandas as pd
import numpy as np
import math
import seaborn as sns

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
# MENU LATERAL
# ------------------------------------------------------------
st.sidebar.title("📚 Menu do Curso")
st.sidebar.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3hyMjEydDh2ZnA2N3Zpb2xzcmhoYzRrd3lxMG03bmd4NjFhb3Y5eCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3og0ILmP5mKAzV3faw/giphy.gif", use_column_width=True)

menu = st.sidebar.radio("Navegue entre as seções:", [
    "🏠 Página Inicial",
    "🧩 Introdução à Ciência de Dados",
    "📊 Limpeza de Dados",
    "🧠 Funções Python",
    "📂 Operações com Listas",
    "🧮 Estatística e Probabilidade",
    "📈 Visualização de Dados",
    "⚙️ Análise Exploratória (EDA)",
    "⚡ Módulo Avançado Interativo",
    "❓ Quiz do Curso"
])

st.sidebar.markdown("---")
st.sidebar.info("💡 Explore cada módulo na ordem para aproveitar melhor o conteúdo!")

# ------------------------------------------------------------
# --- 0. PÁGINA INICIAL ---
# ------------------------------------------------------------
if menu == "🏠 Página Inicial":
    st.markdown("<h1 class='main-title'>🚀 Curso Completo de Ciência de Dados com Python</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Do zero à prática — entenda, limpe, analise e visualize dados com Python!</p>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif", width=300)
    st.markdown("---")

    st.header("📖 Sobre o Curso")
    st.write("""
Este curso foi desenvolvido para **introduzir você à Ciência de Dados**, combinando **teoria e prática** em um ambiente interativo com Python.

Você aprenderá:
- 🧮 Conceitos fundamentais de Ciência de Dados  
- 🐍 Programação prática em Python  
- 📊 Limpeza e manipulação de dados com Pandas e Numpy  
- 💡 Funções e estruturas de dados  
- ⚙️ Análise Exploratória  
- 📈 Visualização de Dados  
- ⚡ Criação de Apps Interativos com Streamlit  
""")

    st.video("https://youtu.be/cm_tM0m9zcI")

    st.header("🎯 Objetivos")
    st.write("""
Ao final deste curso, você será capaz de:
- Compreender **fundamentos de análise e visualização de dados**
- Criar e limpar **DataFrames**
- Escrever **funções reutilizáveis**
- Trabalhar com **listas, loops e estruturas**
- Construir **dashboards interativos**
""")

    st.success("✅ Use o menu lateral para navegar entre os módulos!")

# ------------------------------------------------------------
# --- 1. INTRODUÇÃO À CIÊNCIA DE DADOS ---
# ------------------------------------------------------------
elif menu == "🧩 Introdução à Ciência de Dados":
    st.title("🧠 Introdução à Ciência de Dados")
    st.video("https://youtu.be/i6fcwf31htU")

    st.header("📘 O que é Ciência de Dados?")
    st.write("""
A **Ciência de Dados** combina **programação, estatística e conhecimento de negócio**  
para transformar dados em **insights e decisões estratégicas**.

Ela envolve:
- Coleta de dados  
- Limpeza e tratamento  
- Análise exploratória  
- Modelagem preditiva  
- Visualização e comunicação dos resultados
""")

    st.subheader("💼 Áreas de aplicação")
    st.write("""
- Finanças: previsão de crédito e risco  
- Saúde: diagnóstico assistido  
- Marketing: segmentação de clientes  
- Esportes: análise de desempenho  
- Indústria: manutenção preditiva
""")

    st.header("🐍 Primeiro Contato com Python")
    st.code('print("Olá, Ciência de Dados!")', language="python")
    st.write("O comando `print()` mostra uma mensagem na tela — o ponto de partida da programação!")

# ------------------------------------------------------------
# --- 2. LIMPEZA DE DADOS ---
# ------------------------------------------------------------
elif menu == "📊 Limpeza de Dados":
    st.title("📊 Limpeza de Dados")
    st.video("https://youtu.be/WQ5rsl8y_dw")

    st.write("""
A **limpeza de dados** é o processo de **corrigir, remover e padronizar informações** antes da análise.
""")

    st.code("""
import pandas as pd

df = pd.read_csv("DADOS_ALUNOS.csv", sep=";")
df.dropna(inplace=True)
df = df.rename(columns={"Nota": "Nota_Final"})
""", language="python")

    st.write("""
Com o **Pandas**, você remove valores nulos com `dropna()`, renomeia colunas e prepara o dataset.
""")

# ------------------------------------------------------------
# --- 3. FUNÇÕES PYTHON ---
# ------------------------------------------------------------
elif menu == "🧠 Funções Python":
    st.title("🧠 Funções em Python")
    st.video("https://www.youtube.com/watch?v=9Os0o3wzS_I")

    st.code("""
def saudacao(nome):
    return f"Olá, {nome}!"
""", language="python")
    st.write("""
Uma função é criada com `def`.  
Ela torna o código **reutilizável e modular**.
""")

# ------------------------------------------------------------
# --- 4. OPERAÇÕES COM LISTAS ---
# ------------------------------------------------------------
elif menu == "📂 Operações com Listas":
    st.title("📂 Operações com Listas")
    st.video("https://www.youtube.com/watch?v=ohCDWZgNIU0")

    st.code("""
lista = [10, 20, 30, 40]
soma = sum(lista)
media = soma / len(lista)
print("Média:", media)
""", language="python")

    st.write("""
As listas permitem armazenar múltiplos valores.  
Com `sum()` e `len()`, você faz operações matemáticas facilmente.
""")

# ------------------------------------------------------------
# --- 5. ESTATÍSTICA ---
# ------------------------------------------------------------
elif menu == "🧮 Estatística e Probabilidade":
    st.title("🧮 Estatística e Probabilidade")
    st.write("""
A estatística é a base da análise de dados.  
Ela permite **resumir, interpretar e prever** comportamentos a partir de informações.
""")

    st.subheader("📊 Exemplo prático: médias e dispersão")
    dados = np.random.normal(50, 10, 100)
    st.write(f"📈 Média: {np.mean(dados):.2f}")
    st.write(f"📉 Desvio Padrão: {np.std(dados):.2f}")
    st.bar_chart(pd.Series(dados))

    st.info("""
**Teoria:**  
- A **média** é a soma dos valores dividida pela quantidade.  
- O **desvio padrão** mostra o quanto os dados variam em torno da média.
""")

# ------------------------------------------------------------
# --- 6. VISUALIZAÇÃO DE DADOS ---
# ------------------------------------------------------------
elif menu == "📈 Visualização de Dados":
    st.title("📈 Visualização de Dados")
    st.write("""
Gráficos transformam dados em **insights visuais**.  
As bibliotecas `matplotlib` e `seaborn` são muito usadas para isso.
""")

    st.subheader("📊 Exemplo prático com Seaborn")
    df = sns.load_dataset("tips")
    st.dataframe(df.head())
    st.bar_chart(df.groupby("day")["total_bill"].mean())
    st.write("Aqui, vemos a média das contas por dia da semana.")

# ------------------------------------------------------------
# --- 7. ANÁLISE EXPLORATÓRIA ---
# ------------------------------------------------------------
elif menu == "⚙️ Análise Exploratória (EDA)":
    st.title("⚙️ Análise Exploratória de Dados")
    st.write("""
A EDA (Exploratory Data Analysis) é usada para **entender o comportamento dos dados** antes da modelagem.
""")

    df = sns.load_dataset("iris")
    st.dataframe(df.head())
    st.write("📏 Estatísticas básicas:")
    st.dataframe(df.describe())
    st.scatter_chart(df, x="sepal_length", y="petal_length")

    st.info("""
**Teoria:**  
Cada ponto do gráfico mostra uma flor.  
Quanto maior a pétala, maior tende a ser a sépala — uma correlação positiva.
""")

# ------------------------------------------------------------
# --- 8. MÓDULO AVANÇADO INTERATIVO ---
# ------------------------------------------------------------
elif menu == "⚡ Módulo Avançado Interativo":
    st.title("⚡ Módulo Avançado Interativo — Pratique com Python em tempo real!")

    # Saudação
    nome = st.text_input("Digite seu nome:")
    if nome:
        st.success(f"Olá, {nome}! 👋 Vamos começar os exercícios práticos!")

    # CALCULADORA DE POTÊNCIA
    st.header("🧮 Calculadora de Potência")
    num = st.number_input("Número:", value=2.0, step=0.1)
    exp = st.number_input("Expoente:", value=3.0, step=0.1)
    st.success(f"{num} elevado a {exp} = {num**exp:.2f}")

    st.info("Esta operação usa **aritmética básica e potenciação**, essencial em modelagem matemática.")

    # NOVA: CALCULADORA CIENTÍFICA
    st.markdown("---")
    st.header("🔢 Calculadora Científica Avançada")
    opcao = st.selectbox("Escolha a operação:", ["Seno", "Cosseno", "Raiz Quadrada", "Logaritmo"])
    valor = st.number_input("Digite um valor:", value=1.0, step=0.1)
    if opcao == "Seno":
        res = math.sin(valor)
    elif opcao == "Cosseno":
        res = math.cos(valor)
    elif opcao == "Raiz Quadrada":
        res = math.sqrt(valor)
    else:
        res = math.log(valor)
    st.success(f"Resultado: {res:.4f}")

    st.info("""
Essas operações são úteis para **modelos trigonométricos e exponenciais**, muito comuns em machine learning.
""")

    # GERADOR DE DADOS + DOWNLOAD
    st.markdown("---")
    st.header("📊 Gerador de Dados Aleatórios + Download CSV")
    linhas = st.slider("Número de linhas:", 5, 200, 20)
    df_random = pd.DataFrame({
        "Altura": np.random.normal(1.70, 0.1, linhas),
        "Peso": np.random.normal(70, 10, linhas),
        "Idade": np.random.randint(18, 60, linhas)
    })
    st.dataframe(df_random.head())
    st.line_chart(df_random)
    st.download_button("📥 Baixar dados gerados", df_random.to_csv(index=False).encode("utf-8"),
                       file_name="dados_gerados.csv", mime="text/csv")

    st.info("""
Aqui, simulamos uma base de dados real.  
Essas técnicas são usadas para testar modelos antes de usar dados reais.
""")

# ------------------------------------------------------------
# --- 9. QUIZ DO CURSO ---
# ------------------------------------------------------------
elif menu == "❓ Quiz do Curso":
    st.title("❓ Quiz Final - Ciência de Dados com Python")
    st.subheader("Teste seus conhecimentos sobre o conteúdo do curso!")
    pontuacao = 0

    perguntas = {
        "O que é Ciência de Dados?": ["A união de estatística, programação e análise de dados", "Apenas criar gráficos"],
        "Qual biblioteca é usada para DataFrames?": ["Pandas", "Math"],
        "Função de exibir texto no Python": ["print()", "show()"],
        "Comando que remove valores nulos": ["df.dropna()", "df.remove()"],
        "Palavra-chave para criar função": ["def", "lambda"],
        "Biblioteca usada para cálculos numéricos": ["NumPy", "Streamlit"],
        "Qual biblioteca ajuda na visualização?": ["Seaborn", "Pandas"],
        "Comando que lê CSV": ["pd.read_csv()", "pd.load_csv()"],
        "O que faz np.mean()?": ["Calcula a média", "Calcula a soma"],
        "Qual comando cria gráfico de linha no Streamlit?": ["st.line_chart()", "st.plot()"]
    }

    for pergunta, opcoes in perguntas.items():
        resposta = st.radio(pergunta, opcoes, key=pergunta)
        if resposta == opcoes[0]:
            pontuacao += 1

    if st.button("Ver Resultado"):
        st.success(f"🎯 Você acertou {pontuacao}/{len(perguntas)} questões!")
        if pontuacao == len(perguntas):
            st.balloons()
            st.success("🏆 Excelente! Você dominou o conteúdo!")
        elif pontuacao >= 6:
            st.info("💪 Muito bom! Revise apenas alguns conceitos.")
        else:
            st.warning("📘 Continue praticando para consolidar o aprendizado!")
