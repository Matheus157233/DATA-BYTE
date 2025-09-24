import streamlit as st
import pandas as pd
import numpy as np
import math

# Configuração da página
st.set_page_config(page_title="Projetos com Notebooks + Py Ciência de Dados", layout="wide")

# TABS principais
tabs = st.tabs([
    "🚀 Introdução à Ciência de Dados",
    "📊 Limpeza de Dados",
    "🧠 Funções Python",
    "📂 Operações com Listas",
    "⚡ Avançado Interativo"
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
    st.header("📊 Importância no Mercado")
    st.write("""
A demanda por profissionais de Ciência de Dados está crescendo rapidamente:
- Média salarial: **R$6.000 a R$15.000** dependendo do nível de experiência
- Empresas buscam pessoas que saibam **analisar dados e gerar insights**
- Aplicações: negócios, saúde, finanças, esportes, marketing
""")

    st.markdown("---")
    st.header("🔢 Tipos de Dados")
    st.write("""
- **Numéricos**: int, float (ex: 10, 3.14)  
- **Texto (strings)**: "Olá", "Ciência"  
- **Booleanos**: True, False  
- **Categorias**: "Masculino", "Feminino", "Outros"
""")

    st.markdown("---")
    st.header("🐍 Primeiros passos com Python")
    st.subheader("✅ Exemplo 1: Olá, Mundo!")
    st.code('print("Olá, mundo da Ciência de Dados com Py!")', language="python")

    st.subheader("✅ Exemplo 2: Variáveis e arrays com numpy")
    st.code('''
import numpy as np
idades = np.array([23, 35, 29])
media = np.mean(idades)
print("Média das idades:", media)
''', language="python")
    idades = np.array([23, 35, 29])
    media = np.mean(idades)
    st.write(f"Média das idades: {media}")

    st.markdown("---")
    st.header("📦 Trabalhando com pandas")
    dados = {
        "Nome": ["Ana", "Carlos", "Beatriz"],
        "Idade": [23, 35, 29]
    }
    df = pd.DataFrame(dados)
    st.dataframe(df)
    st.write("Estatísticas descritivas:")
    st.dataframe(df.describe())
    st.write("Pessoa mais velha:")
    st.write(df[df["Idade"] == df["Idade"].max()])

    st.markdown("---")
    st.header("🌍 Mapa interativo")
    st.map(pd.DataFrame({
        'lat': [-23.55052, -22.9068, -19.9167],
        'lon': [-46.633308, -43.1729, -43.9345],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
    }))

    st.markdown("---")
    
# --- Limpeza de Dados ---
with tabs[1]:
    st.title("📊 Limpeza de Dados")
    st.subheader("Preparando e organizando dados sujos")

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
    st.image("https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif", use_container_width=True)

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

# --- Operações com Listas ---
with tabs[3]:
    st.subheader("📂 Operações com Listas")
    st.image("https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif", use_container_width=True)

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

# --- Avançado Interativo ---
with tabs[4]:
    st.title("⚡ Avançado Interativo")
    st.subheader("Experimente interações com Python e dados!")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTZnMHZobTZreG5lNHN1bHYyY2M2Y281enM1OGx6MXdqYTkyaDIwNCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/LKqDgLlK6SuIM/giphy.gif", use_container_width=True)

    st.markdown("### 1️⃣ Calculadora de Média Interativa")
    numeros = st.text_input("Digite números separados por vírgula (ex: 10,20,30):")
    if numeros:
        try:
            nums = [float(n.strip()) for n in numeros.split(",")]
            media = np.mean(nums)
            st.success(f"A média dos números é: {media}")
        except:
            st.error("Erro: digite apenas números separados por vírgula.")

    st.markdown("### 2️⃣ Escolha uma operação matemática divertida")
    operacao = st.selectbox("Escolha a operação:", ["Quadrado", "Raiz Quadrada", "Fatorial"])
    valor = st.number_input("Digite um número:", min_value=0, step=1)
    if operacao and valor is not None:
        if operacao == "Quadrado":
            st.write(f"{valor}² = {valor**2}")
        elif operacao == "Raiz Quadrada":
            st.write(f"√{valor} = {math.sqrt(valor)}")
        elif operacao == "Fatorial":
            st.write(f"{valor}! = {math.factorial(int(valor))}")

    st.markdown("### 3️⃣ Upload de CSV para explorar seus dados")
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
    if uploaded_file:
        user_df = pd.read_csv(uploaded_file)
        st.write("Seu arquivo CSV carregado:")
        st.dataframe(user_df)
        st.write("Estatísticas descritivas:")
        st.dataframe(user_df.describe())

    st.markdown("### 4️⃣ GIFs Motivacionais e Engraçados na  apenas na cabeça do Matue Dnv")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcW9mdGhmaTU1cGwzdHlxZG41NmVsMGVqMjFycG04bGdqNzgxOWFmdCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/s5wFafpHxqKbIEERl9/giphy.gif", use_container_width=True)
    st.markdown("### E esse foi nosso site espero que tenham gostado")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcW9mdGhmaTU1cGwzdHlxZG41NmVsMGVqMjFycG04bGdqNzgxOWFmdCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/lxxOGaDRk4f7R5TkBd/giphy.gif", use_container_width=True)
    
    st.markdown("### Melhor Projeto do ano de todos os tempos")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTZnMHZobTZreG5lNHN1bHYyY2M2Y281enM1OGx6MXdqYTkyaDIwNCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/V8vOT1JVj1ok/giphy.gif",use_container_width=True)
    
    st.markdown("### 5️⃣ Celebre com Balões 🎈")
    if st.button("Clique para soltar balões!"):
        st.balloons()



