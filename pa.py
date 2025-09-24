import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Projetos com Notebooks + Py Ciência de Dados", layout="wide")

# TABS principais (Introdução à Ciência de Dados em primeiro)
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
    
    st.markdown("---")
    st.header("📌 O que é Ciência de Dados?")
    st.write("""
**Ciência de Dados** é o processo de coletar, organizar, analisar e interpretar dados para tomar decisões informadas.

Ela envolve:
- Estatísticas
- Programação (Python é a linguagem mais usada!)
- Visualização de dados
- Conhecimento do domínio (entender o problema)
""")

    st.markdown("---")
    st.header("🔢 O que são Dados?")
    st.write("""
Dados são **informações brutas**, que ainda precisam ser organizadas para fazer sentido.

Exemplos de dados:
- Números de vendas
- Notas de alunos
- Temperaturas registradas ao longo do dia
""")

    st.markdown("---")
    st.header("🧱 Tipos de Dados")
    st.write("""
- **Numéricos** (int, float): 10, 3.14  
- **Texto (strings)**: "Olá", "Ciência"  
- **Booleanos**: `True`, `False`  
- **Categorias**: "Masculino", "Feminino", "Outros"
""")

    st.markdown("---")
    st.header("🐍 Primeiros passos com Python")
    st.write("O Python é uma linguagem simples e poderosa, perfeita para Ciência de Dados. Vamos começar com alguns exemplos básicos:")

    st.subheader("✅ Exemplo 1: Olá, Mundo!")
    st.code('print("Olá, mundo da Ciência de Dados com Py!")', language="python")

    st.subheader("✅ Exemplo 2: Trabalhando com Variáveis")
    st.code('''
nome = "Ana"
idade = 25
print(nome, idade)
''', language="python")

    st.markdown("---")
    st.header("📦 Bibliotecas úteis")

    st.subheader("🐼 pandas – Para trabalhar com tabelas")
    st.write("A biblioteca `pandas` facilita a manipulação de dados em forma de tabelas (DataFrames).")
    dados = {
        "Nome": ["Ana", "Carlos", "Beatriz"],
        "Idade": [23, 35, 29]
    }
    df = pd.DataFrame(dados)
    st.dataframe(df)

    st.subheader("📊 matplotlib – Para criar gráficos")
    # Dados de exemplo
    x = np.arange(0, 10, 1)        # eixo X: 0 a 9
    y = np.array([2, 3, 5, 7, 6, 8, 7, 9, 10, 12])  # eixo Y

    # Criando o gráfico de linhas
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', linestyle='-', color='blue', label='Valores')
    ax.set_title('Exemplo de Gráfico de Linhas')
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.legend()
    ax.grid(True)

    fig, ax = plt.subplots()
    ax.bar(df['Nome'], df['Idade'], color='mediumseagreen')
    ax.set_title('Idade por Pessoa')
    ax.set_xlabel('Nome')
    ax.set_ylabel('Idade')
    st.pyplot(fig)

    st.subheader("🔢 numpy – Para cálculos e arrays")
    idades = np.array([23, 35, 29])
    media = np.mean(idades)
    st.write(f"Média das idades: {media}")

    st.markdown("---")
    st.header("📊 Análise Simples de Dados")
    st.subheader("📈 Estatísticas Descritivas")
    st.dataframe(df.describe())

    st.subheader("🔍 Quem é a pessoa mais velha?")
    mais_velha = df[df["Idade"] == df["Idade"].max()]
    st.write(mais_velha)

    st.markdown("---")
    st.header("🎯 Mini Projeto: Notas de Alunos")
    notas = {
        "Aluno": ["João", "Maria", "Pedro", "Ana"],
        "Nota": [7.5, 9.0, 6.0, 8.5]
    }
    notas_df = pd.DataFrame(notas)
    st.dataframe(notas_df)

    st.subheader("📊 Gráfico das Notas")
    fig, ax = plt.subplots()
    ax.bar(notas_df["Aluno"], notas_df["Nota"], color="orange")
    ax.set_title("Notas dos Alunos")
    ax.set_ylim(0, 10)
    st.pyplot(fig)

    st.markdown("---")
    st.header("✅ Conclusão")
    st.write("""
Parabéns! 🎉 Você aprendeu:
- O que é Ciência de Dados
- Como usar Python para manipulação e visualização de dados
- Criar gráficos e fazer análises simples
""")

# --- Limpeza de Dados ---
with tabs[1]:
    st.title("📘 Projeto: Visualização de Notebooks")
    st.subheader("📊 Limpeza e Preparação de Dados")
    with st.expander("📥 Importação de bibliotecas"):
        st.code("import pandas as pd\nimport numpy as np", language="python")

    with st.expander("📄 Leitura e visualização inicial"):
        st.code('df = pd.read_csv("DADOS_ALUNOS.csv", sep=";")\ndf.head()', language="python")

    with st.expander("🔍 Verificação e tratamento de dados ausentes"):
        st.code('df.isnull().sum()\ndf["Nota"] = df["Nota"].fillna(0)', language="python")

    with st.expander("🧹 Remoção de duplicatas e renomeação"):
        st.code('df = df.drop_duplicates()\ndf = df.rename(columns={"Nota": "Nota_Final"})\ndf.head()', language="python")

# --- Funções Python ---
with tabs[2]:
    st.subheader("🧠 Funções em Python")
    with st.expander("🙋‍♀️ Saudação personalizada"):
        st.code("""
def saudacao(nome):
    return f"Olá, {nome}!"
""", language="python")

    with st.expander("📐 Função com parâmetro padrão"):
        st.code("""
def potencia(base, expoente=2):
    return base ** expoente

potencia(3)
potencia(3, 3)
""", language="python")

    with st.expander("🔁 Retorno múltiplo"):
        st.code("""
def operacoes(a, b):
    soma = a + b
    sub = a - b
    return soma, sub

s, sub = operacoes(10, 5)
print(f"Soma: {s}, Subtração: {sub}")
""", language="python")

    with st.expander("💬 Repetição com argumentos nomeados"):
        st.code("""
def mensagem(texto, vezes=1):
    for _ in range(vezes):
        print(texto)

mensagem("Estudando funções", 3)
""", language="python")

# --- Listas e Operações ---
with tabs[3]:
    st.subheader("📂 Operações com Listas (2CDD02)")
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

