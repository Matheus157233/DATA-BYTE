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
    .small-gif {
        max-height: 200px;
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
    "⚡ Módulo Avançado Interativo"
])
st.sidebar.markdown("---")
st.sidebar.info("💡 Dica: explore cada módulo em ordem para aproveitar melhor o conteúdo!")

# ------------------------------------------------------------
# --- 0. PÁGINA INICIAL ---
# ------------------------------------------------------------
if menu == "🏠 Página Inicial":
    st.markdown("<h1 class='main-title'>🚀 Curso Completo de Ciência de Dados com Python</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Do zero à prática — entenda, limpe, analise e visualize dados com Python!</p>", unsafe_allow_html=True)

    st.markdown("---")
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

    st.header("🎯 Objetivo")
    st.write("""
Ao final deste curso, você será capaz de:
- Compreender os **fundamentos da análise de dados**
- Criar e limpar **DataFrames**
- Escrever **funções eficientes**
- Trabalhar com **listas e estruturas dinâmicas**
- Construir **pequenos projetos interativos**
""")

    st.header("🧭 Estrutura do Curso")
    st.write("""
1. **Introdução à Ciência de Dados**  
2. **Limpeza e Tratamento de Dados**  
3. **Funções Python**  
4. **Operações com Listas**  
5. **Módulo Avançado Interativo**
""")

    st.success("✅ Clique no menu lateral para iniciar sua jornada!")

# ------------------------------------------------------------
# --- 1. Introdução à Ciência de Dados ---
# ------------------------------------------------------------
elif menu == "🧩 Introdução à Ciência de Dados":
    st.title("🧠 Py - Sua Porta de Entrada para a Ciência de Dados")
    st.subheader("Aprenda Ciência de Dados do zero com Python de forma prática!")

    st.image("https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif", width=250)

    st.markdown("---")
    st.header("📘 O que é Ciência de Dados?")
    st.write("""
A **Ciência de Dados** une **estatística, programação e análise de dados** para gerar insights e apoiar decisões.

- 📊 **Análise e visualização de dados**
- 🧮 **Modelagem estatística**
- 🐍 **Programação com Python**
- 🧭 **Entendimento do problema e contexto**
""")
    st.video("https://www.youtube.com/watch?v=X3paOmcrTjQ")  # vídeo introdutório

    st.markdown("---")
    st.header("💼 Importância no Mercado de Trabalho")
    st.write("""
O mercado de Ciência de Dados cresce rapidamente:

- 💰 Salários: R$6.000 a R$15.000  
- 🧠 Alta demanda em saúde, finanças, marketing e tecnologia  
- 🌍 Empresas valorizam profissionais que transformam dados em estratégias
""")
    st.video("https://www.youtube.com/watch?v=ua-CiDNNj30")  # vídeo explicativo

    st.markdown("---")
    st.header("🔢 Tipos de Dados em Python")
    st.write("""
- **Numéricos**: `int`, `float` → 10, 3.14  
- **Texto (strings)**: `"Olá", "Python"`  
- **Booleanos**: `True`, `False`  
- **Categorias**: `"Masculino"`, `"Feminino"`, `"Outro"`
""")
    st.video("https://www.youtube.com/watch?v=OT2E5Tj6flE")  # vídeo sobre tipos de dados

    st.markdown("---")
    st.header("🐍 Primeiros Passos com Python")
    st.subheader("✅ Exemplo 1: Olá, Mundo!")
    st.code('print("Olá, mundo da Ciência de Dados com Py!")', language="python")

    st.subheader("✅ Exemplo 2: Variáveis e Arrays com Numpy")
    st.code('''
import numpy as np
idades = np.array([23, 35, 29])
media = np.mean(idades)
print("Média das idades:", media)
''', language="python")
    idades = np.array([23, 35, 29])
    media = np.mean(idades)
    st.success(f"Média das idades: {media}")
    st.video("https://www.youtube.com/watch?v=khKv-8q7YmY")  # vídeo explicando arrays

    st.markdown("---")
    st.header("📦 Trabalhando com pandas (DataFrames)")
    dados = {"Nome": ["Ana", "Carlos", "Beatriz"], "Idade": [23, 35, 29]}
    df = pd.DataFrame(dados)
    st.dataframe(df, use_container_width=True)
    st.write("📈 Estatísticas descritivas:")
    st.dataframe(df.describe())
    st.write("👴 Pessoa mais velha:")
    st.write(df[df["Idade"] == df["Idade"].max()])
    st.video("https://www.youtube.com/watch?v=vmEHCJofslg")  # vídeo pandas intro

    st.markdown("---")
    st.header("🌍 Mapa Interativo de Cidades")
    st.map(pd.DataFrame({
        'lat': [-23.55052, -22.9068, -19.9167],
        'lon': [-46.633308, -43.1729, -43.9345],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
    }))

    st.success("🎯 Parabéns! Você concluiu a introdução à Ciência de Dados!")

# ------------------------------------------------------------
# --- 2. Limpeza de Dados ---
# ------------------------------------------------------------
elif menu == "📊 Limpeza de Dados":
    st.title("📊 Limpeza de Dados")
    st.subheader("Preparando e organizando dados sujos para análise")
    st.image("https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif", width=200)

    st.write("""
Antes de analisar dados, é essencial **limpá-los e estruturá-los** corretamente.
Este módulo mostra exemplos práticos usando a biblioteca **pandas**.
""")
    st.video("https://www.youtube.com/watch?v=otCriSKVV_8")  # vídeo limpeza de dados

    with st.expander("📥 Importação de bibliotecas"):
        st.code("import pandas as pd\nimport numpy as np", language="python")

    with st.expander("📄 Leitura e visualização inicial"):
        st.code('df = pd.read_csv("DADOS_ALUNOS.csv", sep=";")\ndf.head()', language="python")

    with st.expander("🔍 Verificação e tratamento de dados ausentes"):
        st.code('df.isnull().sum()\ndf["Nota"] = df["Nota"].fillna(0)', language="python")

    with st.expander("🧹 Remoção de duplicatas e renomeação de colunas"):
        st.code('df = df.drop_duplicates()\ndf = df.rename(columns={"Nota": "Nota_Final"})\ndf.head()', language="python")

# ------------------------------------------------------------
# --- 3. Funções Python ---
# ------------------------------------------------------------
elif menu == "🧠 Funções Python":
    st.title("🧠 Funções em Python")
    st.subheader("Organizando códigos e automatizando tarefas")
    st.image("https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif", width=200)

    st.write("""
Funções permitem **automatizar tarefas repetitivas** e deixar seu código **mais limpo e organizado**.
""")
    st.video("https://www.youtube.com/watch?v=9Os0o3wzS_I")  # vídeo sobre funções

    with st.expander("🙋‍♀️ Saudação personalizada"):
        st.code("""
def saudacao(nome):
    return f"Olá, {nome}!"
""", language="python")

    with st.expander("📐 Função com parâmetro padrão"):
        st.code("""
def potencia(base, expoente=2):
    return base ** expoente
""", language="python")

    with st.expander("🔁 Retorno múltiplo"):
        st.code("""
def operacoes(a, b):
    soma = a + b
    sub = a - b
    return soma, sub
""", language="python")

# ------------------------------------------------------------
# --- 4. Operações com Listas ---
# ------------------------------------------------------------
elif menu == "📂 Operações com Listas":
    st.title("📂 Operações com Listas")
    st.subheader("Aprenda manipular dados de forma prática")
    st.image("https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif", width=200)

    st.write("""
Listas são estruturas de dados que permitem **armazenar múltiplos valores**, podendo manipulá-los facilmente.
""")
    st.video("https://www.youtube.com/watch?v=ohCDWZgNIU0")  # vídeo listas

    with st.expander("➕ Soma e média"):
        st.code("""
lista = [1, 2, 3, 4, 5]
soma = sum(lista)
media = soma / len(lista)
print(f"Soma: {soma}, Média: {media}")
""", language="python")

    with st.expander("📐 Quadrados com list comprehension"):
        st.code("""
quadrados = [x**2 for x in lista]
print("Quadrados:", quadrados)
""", language="python")

    with st.expander("📍 Enumerando elementos"):
        st.code("""
for i, valor in enumerate(lista):
    print(f"Índice: {i}, Valor: {valor}")
""", language="python")

    with st.expander("📏 Fatiamento e modificação"):
        st.code("""
print(lista[1:4])
lista.append(6)
lista.remove(2)
print(lista)
""", language="python")

# ------------------------------------------------------------
# --- 5. Módulo Avançado Interativo ---
# ------------------------------------------------------------
elif menu == "⚡ Módulo Avançado Interativo":
    st.title("⚡ Módulo Avançado Interativo")
    st.subheader("Experimente interações em tempo real com Python e Dados!")
    st.image("https://media.giphy.com/media/LKqDgLlK6SuIM/giphy.gif", width=200)

    st.write("""
Aqui você poderá testar **funções matemáticas**, carregar **CSV próprios** e explorar **estatísticas descritivas**.
""")
    st.video("https://www.youtube.com/watch?v=rfscVS0vtbw")  # vídeo interatividade streamlit

    st.markdown("### 1️⃣ Calculadora de Média Interativa")
    numeros = st.text_input("Digite números separados por vírgula (ex: 10,20,30):")
    if numeros:
        try:
            nums = [float(n.strip()) for n in numeros.split(",")]
            media = np.mean(nums)
            st.success(f"A média dos números é: {media}")
        except:
            st.error("❌ Erro: digite apenas números separados por vírgula.")

    st.markdown("### 2️⃣ Operações Matemáticas")
    operacao = st.selectbox("Escolha a operação:", ["Quadrado", "Raiz Quadrada", "Fatorial"])
    valor = st.number_input("Digite um número:", min_value=0, step=1)
    if operacao and valor is not None:
        if operacao == "Quadrado":
            st.write(f"{valor}² = {valor**2}")
        elif operacao == "Raiz Quadrada":
            st.write(f"√{valor} = {math.sqrt(valor)}")
        elif operacao == "Fatorial":
            st.write(f"{valor}! = {math.factorial(int(valor))}")

    st.markdown("### 3️⃣ Upload de CSV para Explorar Dados")
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
    if uploaded_file:
        user_df = pd.read_csv(uploaded_file)
        st.write("✅ Seu arquivo CSV carregado com sucesso:")
        st.dataframe(user_df)
        st.write("📈 Estatísticas descritivas:")
        st.dataframe(user_df.describe())

    st.markdown("---")
    st.success("🎓 Parabéns! Você concluiu o módulo final do curso de Ciência de Dados!")

    st.markdown("### 🏆 Melhor Projeto do Ano!")
    st.image("https://media.giphy.com/media/V8vOT1JVj1ok/giphy.gif", width=200)

    st.markdown("### 🎈 Celebre seu aprendizado!")
    if st.button("Clique para soltar balões!"):
        st.balloons()

