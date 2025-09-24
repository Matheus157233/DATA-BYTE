import streamlit as st
import pandas as pd
import numpy as np

# Configuração da página
st.set_page_config(page_title="Projetos com Notebooks + Py Ciência de Dados", layout="wide")

# TABS principais
tabs = st.tabs([
    "🚀 Introdução à Ciência de Dados",
    "📊 Limpeza de Dados",
    "🧠 Funções Python",
    "📂 Operações com Listas"
])

# --- Introdução à Ciência de Dados ---
with tabs[0]:
    st.title("🧠 Py - Sua Porta de Entrada para a Ciência de Dados")
    st.subheader("Aprenda Ciência de Dados do zero com Python de forma prática!")

    st.image("https://www.python.org/static/community_logos/python-logo.png", caption="Python Logo", use_column_width=True)
    st.image("https://media.giphy.com/media/3o7aCTPPm4OHfRLSH6/giphy.gif", caption="Data Science é divertido!", use_column_width=True)

    st.markdown("---")
    st.header("📌 O que é Ciência de Dados?")
    st.write("""
**Ciência de Dados** é o processo de coletar, organizar, analisar e interpretar dados para tomar decisões informadas.
Ela envolve estatísticas, programação (Python é a mais usada), visualização de dados e conhecimento do domínio.
""")

    st.markdown("---")
    st.header("📊 Mini-Projeto 1: Tabela de Alunos")
    dados = {
        "Nome": ["Ana", "Carlos", "Beatriz", "Pedro", "João"],
        "Idade": [23, 35, 29, 22, 28],
        "Nota": [8.5, 9.0, 7.0, 6.5, 10.0],
        "Turma": ["A", "B", "A", "B", "A"]
    }
    df = pd.DataFrame(dados)
    st.dataframe(df)

    st.subheader("📊 Gráficos")
    st.bar_chart(df.set_index("Nome")["Nota"])
    st.line_chart(df.set_index("Nome")["Nota"])
    st.area_chart(df.set_index("Nome")["Nota"])

    st.subheader("🔢 Estatísticas com Numpy")
    idades = np.array(df["Idade"])
    notas = np.array(df["Nota"])
    st.write(f"Média das idades: {np.mean(idades):.2f}")
    st.write(f"Desvio padrão das notas: {np.std(notas):.2f}")

    st.subheader("📊 Mini-Projeto 2: Filtragem Interativa")
    media_nota = st.slider("Escolha a nota mínima para filtrar alunos:", 0.0, 10.0, 7.0)
    st.dataframe(df[df["Nota"] >= media_nota])

    st.subheader("📊 Mini-Projeto 3: Simulação de Vendas")
    meses = [f"Mês {i}" for i in range(1, 13)]
    vendas = np.random.randint(50, 200, size=12)
    df_vendas = pd.DataFrame({"Mês": meses, "Vendas": vendas})
    st.line_chart(df_vendas.set_index("Mês")["Vendas"])
    st.dataframe(df_vendas)

    st.subheader("📍 Localização (mapa de exemplo)")
    st.map(pd.DataFrame({
        "lat": np.random.uniform(-23.6, -23.5, size=5),
        "lon": np.random.uniform(-46.7, -46.6, size=5)
    }, columns=["lat", "lon"]))

# --- Limpeza de Dados ---
with tabs[1]:
    st.title("📘 Projeto: Limpeza de Dados")
    st.subheader("📊 Limpeza e Preparação de Dados")
    
    with st.expander("📥 Importação de bibliotecas"):
        st.code("import pandas as pd\nimport numpy as np", language="python")

    with st.expander("📄 Leitura e visualização inicial"):
        st.code('df = pd.read_csv("DADOS_ALUNOS.csv", sep=";")\ndf.head()', language="python")

    with st.expander("🔍 Tratamento de dados ausentes"):
        st.code('df.isnull().sum()\ndf["Nota"] = df["Nota"].fillna(0)', language="python")

    with st.expander("🧹 Remoção de duplicatas e renomeação"):
        st.code('df = df.drop_duplicates()\ndf = df.rename(columns={"Nota": "Nota_Final"})\ndf.head()', language="python")

# --- Funções Python ---
with tabs[2]:
    st.subheader("🧠 Funções em Python")
    
    with st.expander("🙋‍♀️ Saudação personalizada"):
        st.code("""def saudacao(nome):\n    return f"Olá, {nome}!"\n""", language="python")

    with st.expander("📐 Função com parâmetro padrão"):
        st.code("""def potencia(base, expoente=2):\n    return base ** expoente\npotencia(3)\npotencia(3,3)\n""", language="python")

    with st.expander("🔁 Retorno múltiplo"):
        st.code("""def operacoes(a,b):\n    soma=a+b\n    sub=a-b\n    return soma, sub\ns, sub = operacoes(10,5)\nprint(f'Soma: {s}, Sub: {sub}')\n""", language="python")

    with st.expander("💬 Repetição com argumentos nomeados"):
        st.code("""def mensagem(texto, vezes=1):\n    for _ in range(vezes):\n        print(texto)\nmensagem("Estudando funções", 3)\n""", language="python")

# --- Operações com Listas ---
with tabs[3]:
    st.subheader("📂 Operações com Listas")
    
    with st.expander("➕ Soma e média"):
        st.code("""lista=[1,2,3,4,5]\nsoma=sum(lista)\nmedia=soma/len(lista)\nprint(f"Soma: {soma}, Média: {media}")\n""", language="python")

    with st.expander("📐 Quadrados com list comprehension"):
        st.code("""quadrados=[x**2 for x in lista]\nprint(quadrados)\n""", language="python")

    with st.expander("📍 Enumerando elementos"):
        st.code("""for i,valor in enumerate(lista):\n    print(f"Índice: {i}, Valor: {valor}")\n""", language="python")

    with st.expander("📏 Fatiamento e modificação"):
        st.code("""print(lista[1:4])\nlista.append(6)\nlista.remove(2)\nprint(lista)\n""", language="python")
