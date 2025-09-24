import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

# Configuração da página
st.set_page_config(page_title="Projetos com Notebooks + Py Ciência de Dados", layout="wide")

# TABS principais
tabs = st.tabs([
    "🚀 Introdução à Ciência de Dados",
    "📊 Limpeza de Dados",
    "🧠 Funções Python",
    "📂 Operações com Listas"
])

# -------------------- ABA 1: Introdução à Ciência de Dados --------------------
with tabs[0]:
    st.title("🧠 Py - Sua Porta de Entrada para a Ciência de Dados")
    st.subheader("Aprenda Ciência de Dados do zero com Python de forma prática!")

    st.markdown("---")
    st.header("📌 O que é Ciência de Dados?")
    st.write("""
**Ciência de Dados** é o processo de coletar, organizar, analisar e interpretar dados para tomar decisões informadas.
Ela envolve:
- Estatísticas 📊
- Programação (Python é a linguagem mais usada!) 🐍
- Visualização de dados 📈
- Conhecimento do domínio (entender o problema) 🧠
""")

    st.markdown("---")
    st.header("🖼️ Imagem divertida")
    st.image("https://media.giphy.com/media/26FPy3QZQqGtDcrja/giphy.gif", use_container_width=True)

    st.markdown("---")
    st.header("🎮 Interatividade divertida")
    idade_slider = st.slider("Escolha sua idade:", 0, 120, 25)
    st.write(f"Você selecionou: {idade_slider} anos 😎")

    if st.checkbox("Mostrar DataFrame engraçado"):
        df = pd.DataFrame({"Nome": ["Ana", "Carlos", "Beatriz"], "Idade": [23, 35, 29]})
        st.dataframe(df)

    pessoa = st.selectbox("Escolha alguém engraçado:", ["😜 Zé", "😂 Maria", "🤪 Pedro"])
    st.write(f"Você escolheu: {pessoa}")

    if st.button("Clique se você ama Python"):
        st.balloons()
        st.success("Python ama você também! 🎉")

    st.markdown("---")
    st.header("📊 Gráficos divertidos")
    y = np.random.randint(1, 20, 10)
    st.line_chart(y)

    st.subheader("📈 Gráfico com emojis")
    df_emojis = pd.DataFrame({
        "Python": [5, 8, 12, 4, 9],
        "Data": [7, 3, 11, 8, 6]
    })
    st.bar_chart(df_emojis)

    st.markdown("---")
    st.header("🎯 Mini Projeto: Notas de Alunos")
    notas = {"Aluno": ["João", "Maria", "Pedro", "Ana"], "Nota": [7.5, 9.0, 6.0, 8.5]}
    notas_df = pd.DataFrame(notas)
    st.dataframe(notas_df)

    st.subheader("📊 Gráfico das Notas com emojis")
    chart_data = pd.DataFrame({
        "Notas": notas_df["Nota"]
    }, index=notas_df["Aluno"])
    st.bar_chart(chart_data)

# -------------------- ABA 2: Limpeza de Dados --------------------
with tabs[1]:
    st.title("📘 Limpeza de Dados")
    st.subheader("📊 Preparando e organizando dados sujos")

    with st.expander("📥 Importação de bibliotecas"):
        st.code("import pandas as pd\nimport numpy as np", language="python")

    with st.expander("📄 Leitura de CSV"):
        st.code('df = pd.read_csv("DADOS_ALUNOS.csv", sep=";")\ndf.head()', language="python")

    with st.expander("🔍 Tratamento de valores ausentes"):
        st.code('df.isnull().sum()\ndf["Nota"] = df["Nota"].fillna(0)', language="python")

    with st.expander("🧹 Remoção de duplicatas"):
        st.code('df = df.drop_duplicates()\ndf.head()', language="python")

# -------------------- ABA 3: Funções Python --------------------
with tabs[2]:
    st.subheader("🧠 Funções em Python")

    with st.expander("🙋‍♀️ Saudação divertida"):
        st.code("""def saudacao(nome):
    return f"Olá, {nome}! Python te saúda! 😎" """, language="python")

    with st.expander("📐 Função com parâmetro padrão"):
        st.code("""def potencia(base, expoente=2):
    return base ** expoente

potencia(3)
potencia(3, 3)""", language="python")

    with st.expander("🔁 Retorno múltiplo"):
        st.code("""def operacoes(a, b):
    soma = a + b
    sub = a - b
    return soma, sub

s, sub = operacoes(10, 5)
print(f"Soma: {s}, Subtração: {sub}")""", language="python")

    with st.expander("💬 Repetição engraçada"):
        st.code("""def mensagem(texto, vezes=1):
    for _ in range(vezes):
        print(texto + " 😂")

mensagem("Aprendendo Python", 3)""", language="python")

# -------------------- ABA 4: Operações com Listas --------------------
with tabs[3]:
    st.subheader("📂 Manipulação de Listas")

    with st.expander("➕ Soma e média"):
        st.code("""lista = [1, 2, 3, 4, 5]
soma = sum(lista)
media = soma / len(lista)
print(f"Soma: {soma}, Média: {media}")""", language="python")

    with st.expander("📐 Quadrados com list comprehension"):
        st.code("""quadrados = [x**2 for x in lista]
print(quadrados)""", language="python")

    with st.expander("📍 Enumerando elementos"):
        st.code("""for i, valor in enumerate(lista):
    print(f"Índice: {i}, Valor: {valor}")""", language="python")

    with st.expander("📏 Fatiamento e modificação"):
        st.code("""print(lista[1:4])
lista.append(6)
lista.remove(2)
print(lista)""", language="python")

    st.subheader("🎉 Dica divertida")
    st.write("Você pode criar listas de nomes engraçados e brincar com elas no Python! 😎")

