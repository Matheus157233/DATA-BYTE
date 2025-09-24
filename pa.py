import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Configuração da página
st.set_page_config(page_title="Projetos com Notebooks + Py Ciência de Dados", layout="wide")

# TABS principais
tabs = st.tabs([
    "🚀 Introdução à Ciência de Dados",
    "📊 Limpeza de Dados",
    "🧠 Funções Python",
    "📂 Operações com Listas",
    "📊 Visualização Avançada"
])

# -------------------- ABA 1: Introdução à Ciência de Dados --------------------
with tabs[0]:
    st.title("🧠 Py - Sua Porta de Entrada para a Ciência de Dados")
    st.subheader("Aprenda Ciência de Dados do zero com Python de forma prática!")

    st.markdown("---")
    st.header("📌 O que é Ciência de Dados?")
    st.write("""
**Ciência de Dados** combina **programação, estatística e conhecimento do domínio** para gerar insights úteis a partir de dados.
Ela envolve:
- Estatísticas e análise de dados 📊
- Programação (Python, R, SQL) 🐍
- Visualização de dados 📈
- Conhecimento do domínio 🧠
""")

    st.markdown("---")
    st.header("💼 Mercado e Salário")
    st.write("""
O mercado está em **crescimento acelerado**. Salário médio: **R$7.000 a R$12.000 mensais** no Brasil.
""")

    st.markdown("---")
    st.header("🖼️ LeBron James em ação")
    st.image("https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif", use_container_width=True)

    st.markdown("---")
    st.header("🎮 Interatividade divertida")
    idade_slider = st.slider("Escolha sua idade:", 0, 120, 25)
    st.write(f"Você selecionou: {idade_slider} anos 😎")

    if st.checkbox("Mostrar DataFrame exemplo"):
        df = pd.DataFrame({"Nome": ["Ana", "Carlos", "Beatriz"], "Idade": [23, 35, 29]})
        st.dataframe(df)

    pessoa = st.selectbox("Escolha alguém engraçado:", ["😜 Zé", "😂 Maria", "🤪 Pedro"])
    st.write(f"Você escolheu: {pessoa}")

    if st.button("Clique se você ama Python"):
        st.balloons()
        st.success("Python ama você também! 🎉")

    st.markdown("---")
    st.header("📈 Gráfico de linhas exemplo")
    y = np.random.randint(1, 20, 10)
    st.line_chart(y)

    st.subheader("🗺️ Mapa interativo")
    mapa_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon']
    )
    st.map(mapa_data)

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
    st.markdown("---")
    st.header("📌 Matemática é difícil? 😅")
    st.image("https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif", use_container_width=True)

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

# -------------------- ABA 5: Visualização Avançada --------------------
with tabs[4]:
    st.subheader("📊 Visualização Avançada com Streamlit nativa")
    st.write("Exemplos de gráficos usando apenas Streamlit:")

    # Gráfico de linhas
    dados_linha = pd.DataFrame(np.random.randint(10, 50, size=(10,1)), columns=["Vendas"])
    st.line_chart(dados_linha)

    # Gráfico de barras
    dados_barra = pd.DataFrame({"Produto": ["A","B","C","D"], "Quantidade": [23, 45, 12, 34]}).set_index("Produto")
    st.bar_chart(dados_barra)

    # Gráfico de área
    dados_area = pd.DataFrame(np.random.randint(1,20, size=(10,3)), columns=["Setor1","Setor2","Setor3"])
    st.area_chart(dados_area)

    st.markdown("---")
    st.header("📂 Faça upload do seu próprio CSV!")
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
    if uploaded_file is not None:
        user_df = pd.read_csv(uploaded_file)
        st.write("✅ Arquivo carregado com sucesso!")
        st.dataframe(user_df)

        st.subheader("📊 Gráfico de linhas do seu CSV")
        st.line_chart(user_df.select_dtypes(include=[np.number]))

        st.subheader("📈 Gráfico de barras do seu CSV")
        numeric_df = user_df.select_dtypes(include=[np.number])
        if not numeric_df.empty:
            st.bar_chart(numeric_df)
