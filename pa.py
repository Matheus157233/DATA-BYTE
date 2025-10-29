import streamlit as st
import pandas as pd
import numpy as np
import math

# ------------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# ------------------------------------------------------------
st.set_page_config(
    page_title="Curso Completo: Ciência de Dados com Python",
    page_icon="🧠",
    layout="wide"
)

# ------------------------------------------------------------
# ESTILO PERSONALIZADO
# ------------------------------------------------------------
st.markdown("""
<style>
    body {background-color: #f0f2f6;}
    h1, h2, h3 {color: #0E1117;}
    .main-title {text-align: center; color: #1f77b4; font-weight: bold;}
    .sub-title {text-align: center; font-style: italic; color: #555;}
    .block-container {padding-top: 2rem; padding-bottom: 2rem;}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# MENU LATERAL
# ------------------------------------------------------------
st.sidebar.title("📚 Menu do Curso")
menu = st.sidebar.radio("Navegue entre as seções:", [
    "🏠 Página Inicial",
    "🧩 Introdução à Ciência de Dados",
    "📊 Limpeza e Tratamento de Dados",
    "🧠 Funções Python",
    "📂 Operações com Listas",
    "⚡ Módulo Avançado Interativo",
    "❓ Quiz Interativo"
])
st.sidebar.markdown("---")
st.sidebar.info("💡 Explore cada módulo para aprender na prática!")

# ------------------------------------------------------------
# PÁGINA INICIAL
# ------------------------------------------------------------
if menu == "🏠 Página Inicial":
    st.markdown("<h1 class='main-title'>🚀 Curso Completo de Ciência de Dados com Python</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Do zero à prática — entenda, limpe, analise e visualize dados com Python!</p>", unsafe_allow_html=True)
    st.markdown("---")
    st.header("📖 Sobre o Curso")
    st.write("""
Este curso foi desenvolvido para **introduzir você à Ciência de Dados**, combinando **teoria e prática**.
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
- Compreender os fundamentos da análise de dados
- Criar e limpar DataFrames
- Escrever funções eficientes
- Trabalhar com listas e estruturas dinâmicas
- Construir pequenos projetos interativos
""")
    st.header("🧭 Estrutura do Curso")
    st.write("""
1. Introdução à Ciência de Dados  
2. Limpeza e Tratamento de Dados  
3. Funções Python  
4. Operações com Listas  
5. Módulo Avançado Interativo  
6. Quiz Interativo
""")

# ------------------------------------------------------------
# INTRODUÇÃO À CIÊNCIA DE DADOS
# ------------------------------------------------------------
elif menu == "🧩 Introdução à Ciência de Dados":
    st.header("🧩 Introdução à Ciência de Dados")
    st.write("""
A **Ciência de Dados** é a prática de extrair conhecimento e insights a partir de dados.  
Ela combina **estatística, programação e análise visual**, sendo aplicada em diversas áreas.
""")
    st.subheader("Tipos de Dados em Python")
    st.write("""
Python possui vários tipos de dados nativos:
- **int** → números inteiros
- **float** → números decimais
- **str** → textos
- **bool** → verdadeiro ou falso
- **list, tuple, dict, set** → estruturas de dados
""")
    st.subheader("Exemplo prático")
    st.code("""
numero_inteiro = 10
numero_decimal = 3.14
texto = "Olá, mundo!"
verdadeiro_falso = True

print(type(numero_inteiro))
print(type(numero_decimal))
print(type(texto))
print(type(verdadeiro_falso))
""", language="python")
    st.subheader("Prática Interativa")
    numero = st.number_input("Digite um número:", value=5)
    texto_input = st.text_input("Digite um texto:", value="Olá")
    st.write(f"Tipo do número: {type(numero)}")
    st.write(f"Tipo do texto: {type(texto_input)}")

    st.subheader("Curiosidade")
    st.write("💡 Em Python, tudo é objeto! Até números e funções são objetos com métodos próprios.")

# ------------------------------------------------------------
# LIMPEZA E TRATAMENTO DE DADOS
# ------------------------------------------------------------
elif menu == "📊 Limpeza e Tratamento de Dados":
    st.header("📊 Limpeza e Tratamento de Dados")
    st.write("""
Dados reais podem conter:
- Valores nulos
- Dados duplicados
- Erros de digitação
- Formatos inconsistentes
""")
    st.subheader("Exemplo de DataFrame sujo")
    data = {"Nome": ["Ana", "Bruno", "Carlos", None, "Ester", "Ana"],
            "Idade": [23, 35, None, 40, 29, 23],
            "Cidade": ["SP", "RJ", "SP", "MG", None, "SP"]}
    df = pd.DataFrame(data)
    st.write("DataFrame original:")
    st.dataframe(df)

    st.subheader("Tratamento de dados")
    df_clean = df.dropna()
    df_clean = df_clean.drop_duplicates()
    st.write("DataFrame limpo:")
    st.dataframe(df_clean)

    st.subheader("Prática Interativa")
    st.write("Adicione uma nova linha ao DataFrame:")
    nome_novo = st.text_input("Nome:")
    idade_nova = st.number_input("Idade:", min_value=0, max_value=120)
    cidade_nova = st.text_input("Cidade:")
    if st.button("Adicionar"):
        df.loc[len(df)] = [nome_novo, idade_nova, cidade_nova]
        st.dataframe(df)
        st.success("Linha adicionada com sucesso!")

# ------------------------------------------------------------
# FUNÇÕES PYTHON
# ------------------------------------------------------------
elif menu == "🧠 Funções Python":
    st.header("🧠 Funções em Python")
    st.write("""
Funções são blocos de código reutilizáveis que realizam uma tarefa específica.
Elas tornam o código mais organizado e modular.
""")
    st.subheader("Exemplo de função")
    st.code("""
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Maria"))
""", language="python")

    st.subheader("Prática Interativa")
    nome_user = st.text_input("Digite seu nome para receber uma saudação:")
    if nome_user:
        st.write(f"Resultado da função: Olá, {nome_user}!")

    st.subheader("Mini Projeto")
    st.write("Crie uma função que calcula a média de uma lista de números:")
    numeros_input = st.text_input("Digite números separados por vírgula:", value="5,10,15")
    if numeros_input:
        numeros_list = [float(x.strip()) for x in numeros_input.split(",")]
        def media(lista):
            return sum(lista)/len(lista)
        st.write(f"Média dos números: {media(numeros_list)}")

# ------------------------------------------------------------
# OPERAÇÕES COM LISTAS
# ------------------------------------------------------------
elif menu == "📂 Operações com Listas":
    st.header("📂 Trabalhando com Listas")
    st.write("""
Listas são estruturas de dados mutáveis que armazenam múltiplos itens.
Você pode adicionar, remover e modificar elementos facilmente.
""")
    st.subheader("Exemplo")
    st.code("""
frutas = ["maçã", "banana", "laranja"]
frutas.append("uva")
print(frutas)
""", language="python")

    st.subheader("Prática Interativa")
    frutas_input = st.text_input("Adicione uma fruta à lista:", value="morango")
    frutas = ["maçã", "banana", "laranja"]
    frutas.append(frutas_input)
    st.write(f"Lista atualizada: {frutas}")

    st.subheader("Mini Projeto")
    st.write("Ordene a lista e remova duplicatas automaticamente:")
    lista_final = list(set(frutas))
    lista_final.sort()
    st.write(f"Lista final organizada: {lista_final}")

# ------------------------------------------------------------
# MÓDULO AVANÇADO INTERATIVO
# ------------------------------------------------------------
elif menu == "⚡ Módulo Avançado Interativo":
    st.header("⚡ Módulo Avançado Interativo")

    # Calculadora de Potência
    st.subheader("1️⃣ Calculadora de Potência com Números Quebrados")
    base = st.number_input("Digite a base:", value=2.0)
    expoente = st.number_input("Digite o expoente:", value=3.0)
    potencia = base ** expoente
    st.write(f"Resultado: {base}^{expoente} = {potencia}")

    # Upload/Download CSV
    st.subheader("2️⃣ Upload e Download de CSV")
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
    if uploaded_file:
        df_uploaded = pd.read_csv(uploaded_file)
        st.write("Arquivo carregado com sucesso!")
        st.dataframe(df_uploaded)
        st.download_button("📥 Baixar CSV", df_uploaded.to_csv(index=False), "meu_arquivo.csv", "text/csv")

    # Operações numéricas avançadas
    st.subheader("3️⃣ Operações Numéricas Avançadas")
    numeros = st.text_input("Digite números separados por vírgula:", value="1,2,3,4")
    expoentes = st.text_input("Digite expoentes separados por vírgula:", value="2,3")
    if numeros and expoentes:
        numeros_list = [float(x.strip()) for x in numeros.split(",")]
        expoentes_list = [float(x.strip()) for x in expoentes.split(",")]
        resultados = {f"x^{exp}": [n**exp for n in numeros_list] for exp in expoentes_list}
        df_resultados = pd.DataFrame(resultados, index=numeros_list)
        st.dataframe(df_resultados)

    # Mini projeto: gerador de tabela multiplicativa
    st.subheader("4️⃣ Mini Projeto: Tabela Multiplicativa")
    n = st.number_input("Digite até qual número gerar a tabela:", min_value=1, max_value=20, value=5)
    tabela = pd.DataFrame([[i*j for j in range(1,n+1)] for i in range(1,n+1)],
                          columns=[f"{j}" for j in range(1,n+1)],
                          index=[f"{i}" for i in range(1,n+1)])
    st.dataframe(tabela)
    st.success("Tabela multiplicativa gerada com sucesso!")

# ------------------------------------------------------------
# QUIZ INTERATIVO
# ------------------------------------------------------------
elif menu == "❓ Quiz Interativo":
    st.header("❓ Quiz Interativo")
    st.write("Teste seus conhecimentos!")

    score = 0

    q1 = st.radio("1️⃣ Qual o tipo do valor 3.14 em Python?", ["int", "float", "str"])
    if q1 == "float":
        score += 1

    q2 = st.radio("2️⃣ Qual função usamos para criar uma lista em Python?", ["list()", "dict()", "tuple()"])
    if q2 == "list()":
        score += 1

    q3 = st.radio("3️⃣ O que o Pandas faz principalmente?", ["Manipula imagens", "Manipula dados", "Cria jogos"])
    if q3 == "Manipula dados":
        score += 1

    q4 = st.radio("4️⃣ Como chamamos uma função em Python?", ["fun nome()", "nome()", "call nome()"])
    if q4 == "nome()":
        score += 1

    q5 = st.radio("5️⃣ Qual comando remove duplicatas em um DataFrame?", ["drop_duplicates()", "remove()", "clean()"])
    if q5 == "drop_duplicates()":
        score += 1

    q6 = st.radio("6️⃣ Qual comando cria um DataFrame em Pandas?", ["pd.DataFrame()", "pd.Series()", "pd.Matrix()"])
    if q6 == "pd.DataFrame()":
        score += 1

    q7 = st.radio("7️⃣ Qual operador usamos para potência em Python?", ["^", "**", "%"])
    if q7 == "**":
        score += 1

    q8 = st.radio("8️⃣ Como adicionamos um elemento em uma lista?", ["append()", "add()", "insert()"])
    if q8 == "append()":
        score += 1

    st.write(f"✅ Sua pontuação: {score}/8")

    if score == 8:
        st.balloons()
        st.success("Parabéns! Você acertou todas!")
    elif score >= 5:
        st.info("Bom trabalho! Mas ainda dá para melhorar.")
    else:
        st.warning("Continue estudando, você consegue!")

