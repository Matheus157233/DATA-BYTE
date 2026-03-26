# ========================= DATASTART PRO MAX =========================
# Plataforma com AULAS NÍVEL PROFESSOR

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import random

st.set_page_config(page_title="DataStart PRO MAX", layout="wide")

# ========================= STATE =========================
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "level" not in st.session_state:
    st.session_state.level = 1

# ========================= FUNÇÕES =========================
def add_xp(x):
    st.session_state.xp += x
    if st.session_state.xp >= st.session_state.level * 100:
        st.session_state.level += 1
        st.success("🔥 LEVEL UP!")

# ========================= SIDEBAR =========================
st.sidebar.title("🚀 DataStart")
menu = st.sidebar.radio("Menu", [
    "🏠 Home",
    "📚 Módulo 1",
    "🧠 Módulo 2",
    "🐍 Módulo 3",
    "📊 Módulo 4",
    "📈 Módulo 5",
    "🤖 Módulo 6",
    "🏁 Módulo 7"
])

st.sidebar.write(f"XP: {st.session_state.xp}")
st.sidebar.write(f"Level: {st.session_state.level}")

# ========================= HOME =========================
if menu == "🏠 Home":
    st.title("🚀 Plataforma Profissional de Ciência de Dados")
    st.write("Aprenda com metodologia aplicada ao mercado")

# ========================= MODULO 1 =========================
elif menu == "📚 Módulo 1":
    st.title("📚 Introdução à Ciência de Dados")

    st.subheader("📖 Aula")
    st.write("Ciência de Dados é uma área interdisciplinar que combina estatística, programação e conhecimento de negócio para extrair valor de dados.")

    st.info("💡 Exemplo real: Netflix usa ciência de dados para recomendar filmes com base no seu comportamento.")

    st.subheader("📌 Conceitos-chave")
    st.markdown("""
- Dados estruturados e não estruturados
- Análise descritiva
- Análise preditiva
- Data-driven decision
""")

    st.subheader("🧪 Quiz")
    r = st.radio("Qual o objetivo da ciência de dados?", ["Criar jogos", "Gerar insights", "Desenhar gráficos"])
    if r == "Gerar insights":
        st.success("Perfeito!")
        add_xp(20)

# ========================= MODULO 2 =========================
elif menu == "🧠 Módulo 2":
    st.title("🧠 Pensamento Analítico")

    st.subheader("📖 Aula")
    st.write("Pensamento analítico é a capacidade de decompor problemas complexos em partes menores.")

    st.warning("⚠️ Analistas não apenas veem dados, eles fazem perguntas sobre os dados.")

    st.subheader("📌 Exemplo")
    st.write("Uma empresa quer saber por que as vendas caíram. Um analista investiga regiões, produtos e comportamento do cliente.")

    st.subheader("🧪 Exercício")
    r = st.text_input("Sequência: 3, 6, 12, 24, ?")
    if r == "48":
        st.success("Boa!")
        add_xp(20)

# ========================= MODULO 3 =========================
elif menu == "🐍 Módulo 3":
    st.title("🐍 Python para Dados")

    st.subheader("📖 Aula")
    st.write("Python é amplamente utilizado por sua simplicidade e poder em análise de dados.")

    st.code("""
# Variáveis
x = 10
# Saída
print(x)
""")

    st.subheader("📌 Dica")
    st.info("Sempre teste pequenos trechos de código para entender o comportamento.")

    st.subheader("💻 Prática")
    code = st.text_area("Digite seu código:", "print('Olá Ciência de Dados')")
    if st.button("Executar"):
        try:
            exec(code)
            add_xp(10)
        except Exception as e:
            st.error(e)

# ========================= MODULO 4 =========================
elif menu == "📊 Módulo 4":
    st.title("📊 Manipulação de Dados")

    st.subheader("📖 Aula")
    st.write("DataFrames são estruturas tabulares usadas para manipular dados.")

    st.code("df.head()  # mostra as primeiras linhas")

    st.subheader("📌 Conceito importante")
    st.warning("Limpeza de dados é essencial antes de qualquer análise.")

    file = st.file_uploader("Envie um CSV")
    if file:
        df = pd.read_csv(file)
        st.dataframe(df)
        st.write(df.describe())
        add_xp(30)

# ========================= MODULO 5 =========================
elif menu == "📈 Módulo 5":
    st.title("📈 Visualização de Dados")

    st.subheader("📖 Aula")
    st.write("Gráficos ajudam a comunicar dados de forma clara.")

    st.info("💡 Gráficos de barras são usados para comparação.")

    df = pd.DataFrame({"Produto":["A","B","C"],"Vendas":[100,200,150]})
    fig = px.bar(df, x="Produto", y="Vendas")
    st.plotly_chart(fig)

    add_xp(10)

# ========================= MODULO 6 =========================
elif menu == "🤖 Módulo 6":
    st.title("🤖 Introdução à IA")

    st.subheader("📖 Aula")
    st.write("Machine Learning permite que sistemas aprendam padrões a partir de dados.")

    st.warning("⚠️ Modelos precisam de dados de qualidade para funcionar bem.")

    n = st.slider("Entrada",0,100)
    st.write("Previsão:", n*2 + random.randint(-5,5))

    add_xp(20)

# ========================= MODULO 7 =========================
elif menu == "🏁 Módulo 7":
    st.title("🏁 Projeto Final")

    st.subheader("📖 Desafio")
    st.write("Agora você aplicará tudo que aprendeu.")

    st.markdown("""
### Etapas:
1. Carregar dados
2. Analisar
3. Criar gráfico
4. Tirar conclusão
""")

    file = st.file_uploader("Envie seu dataset")
    if file:
        df = pd.read_csv(file)
        st.dataframe(df)
        st.plotly_chart(px.histogram(df))
        st.success("Parabéns, você concluiu!")
        add_xp(100)

# ========================= FOOTER =========================
st.markdown("---")
st.write("Plataforma educacional nível profissional 🚀")
