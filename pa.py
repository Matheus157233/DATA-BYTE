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
    iframe {
        width: 100%;
        height: 315px;
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# MENU LATERAL (NAVBAR)
# ------------------------------------------------------------
st.sidebar.title("📚 Menu do Curso")
st.sidebar.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3hyMjEydDh2ZnA2N3Zpb2xzcmhoYzRrd3lxMG03bmd4NjFhb3Y5eCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3og0ILmP5mKAzV3faw/giphy.gif", width=150)
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
    st.image("https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif", width=200)

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

    st.markdown("---")
    st.header("📘 O que é Ciência de Dados?")
    st.video("https://www.youtube.com/embed/p37z3Uibq14")
    st.write("""
A **Ciência de Dados** é o campo que une **estatística, programação e análise de dados** para descobrir padrões, gerar insights e tomar decisões baseadas em fatos.

Ela envolve:
- 📊 **Análise e visualização de dados**
- 🧮 **Modelagem estatística**
- 🐍 **Programação com Python**
- 🧭 **Entendimento do problema e contexto**
""")

    st.markdown("---")
    st.header("💼 Importância no Mercado de Trabalho")
    st.video("https://www.youtube.com/embed/eKZ4p1vK8tA")
    st.write("""
O mercado de Ciência de Dados está em constante crescimento:

- 💰 **Salário médio**: R$6.000 a R$15.000  
- 🧠 **Alta demanda** em setores como saúde, finanças, marketing e tecnologia  
- 🌍 **Empresas buscam profissionais capazes de transformar dados em estratégias**
""")

    st.markdown("---")
    st.header("🔢 Tipos de Dados em Python")
    st.video("https://www.youtube.com/embed/4NUFqF0i0-k")
    st.write("""
- **Numéricos**: `int`, `float` → 10, 3.14  
- **Texto (strings)**: `"Olá", "Python"`  
- **Booleanos**: `True`, `False`  
- **Categorias**: `"Masculino", "Feminino", "Outro"`
""")

    st.markdown("---")
    st.header("🐍 Primeiros Passos com Python")
    st.video("https://www.youtube.com/embed/7aXkNiZsds0")
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

    st.markdown("---")
    st.header("📦 Trabalhando com pandas (DataFrames)")
    st.video("https://www.youtube.com/embed/RgJovGQXGdc")
    dados = {"Nome": ["Ana", "Carlos", "Beatriz"], "Idade": [23, 35, 29]}
    df = pd.DataFrame(dados)
    st.dataframe(df, use_container_width=True)
    st.write("📈 Estatísticas descritivas:")
    st.dataframe(df.describe())
    st.write("👴 Pessoa mais velha:")
    st.write(df[df["Idade"] == df["Idade"].max()])

    st.markdown("---")
    st.header("🌍 Mapa Interativo de Cidades")
    st.map(pd.DataFrame({
        'lat': [-23.55052, -22.9068, -19.9167],
        'lon': [-46.633308, -43.1729, -43.9345],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
    }))

    st.success("🎯 Parabéns! Você concluiu a introdução à Ciência de Dados!")
