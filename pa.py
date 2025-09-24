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
    st.header("🐍 Primeiros passos com Python")
    st.write("O Python é simples e poderoso. Vamos ver exemplos básicos:")

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
    
    st.subheader("🐼 pandas – Manipulação de dados")
    st.write("Vamos criar um DataFrame e explorar algumas operações básicas:")
    
    dados = {
        "Nome": ["Ana", "Carlos", "Beatriz", "João", "Maria"],
        "Idade": [23, 35, 29, 19, 22],
        "Nota": [8.5, 7.0, 9.0, 6.5, 7.5]
    }
    df = pd.DataFrame(dados)
    st.dataframe(df)

    st.subheader("📊 Estatísticas rápidas")
    st.write("Podemos calcular média, máximo e mínimo:")
    st.write(f"Média de idade: {df['Idade'].mean():.2f}")
    st.write(f"Maior nota: {df['Nota'].max()}")
    st.write(f"Menor idade: {df['Idade'].min()}")

    st.subheader("📈 Gráfico simples com pandas")
    st.bar_chart(df.set_index("Nome")["Nota"])

    st.subheader("🔢 numpy – Cálculos avançados")
    idades = np.array(df["Idade"])
    st.write(f"Desvio padrão das idades: {np.std(idades):.2f}")
    st.write(f"Soma das idades: {np.sum(idades)}")

    st.markdown("---")
    st.header("📊 Prática: Filtrando Dados")
    st.write("Filtrando alunos com nota maior que 7:")
    df_filtrado = df[df["Nota"] > 7]
    st.dataframe(df_filtrado)

    st.subheader("📌 Desafio prático")
    st.write("Tente criar uma nova coluna que indique se o aluno passou (nota >= 7) ou não:")
    df["Status"] = df["Nota"].apply(lambda x: "Aprovado" if x >= 7 else "Reprovado")
    st.dataframe(df)

    st.markdown("---")
    st.header("🎯 Mini Projeto: Notas de Alunos")
    st.write("Visualizando a distribuição das notas:")
    st.bar_chart(df.set_index("Nome")["Nota"])

    st.write("Parabéns! Você já aprendeu a criar DataFrames, calcular estatísticas, filtrar dados e criar gráficos simples com pandas e numpy.")

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
    st.subheader("📂 Operações com Listas")
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
