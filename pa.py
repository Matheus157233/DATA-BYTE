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
# ESTILO PERSONALIZADO
# ------------------------------------------------------------
st.markdown("""
<style>
    body {background-color: #f5f5f5;}
    .stApp {background-color: #ffffff;}
    h1, h2, h3 {color: #0E1117;}
    .main-title {text-align: center; color: #1f77b4; font-weight: bold;}
    .sub-title {text-align: center; font-style: italic; color: #555;}
    .block-container {padding-top: 2rem; padding-bottom: 2rem;}
    .small-gif {max-height: 200px;}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# MENU LATERAL
# ------------------------------------------------------------
st.sidebar.title("📚 Menu do Curso")
st.sidebar.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3hyMjEydDh2ZnA2N3Zpb2xzcmhoYzRrd3lxMG03bmd4NjFhb3Y5eCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3og0ILmP5mKAzV3faw/giphy.gif", use_column_width=True)
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
st.sidebar.info("💡 Dica: explore cada módulo em ordem para aproveitar melhor o conteúdo!")

# ------------------------------------------------------------
# PÁGINA INICIAL
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
    
    st.markdown("""
## 🚀 Você aprenderá:
Durante este curso, você vai explorar o universo da **Ciência de Dados** de forma prática e didática.  
Cada módulo foi pensado para te guiar passo a passo, da teoria à aplicação real.

---

### 🧮 Conceitos Fundamentais de Ciência de Dados
Você vai entender o que é **Ciência de Dados**, como os dados são coletados, processados e analisados.  
Aprenderá sobre **estatística, visualização e tomada de decisão baseada em dados**, entendendo como esses elementos se conectam para gerar insights valiosos.

---

### 🐍 Programação Prática em Python
Python é a linguagem mais usada no mundo dos dados!  
Aqui, você aprenderá desde os comandos básicos até o uso de bibliotecas específicas para manipulação e análise.  
Vai descobrir como **automatizar tarefas**, criar algoritmos e resolver problemas de forma eficiente.

---

### 📊 Limpeza e Manipulação de Dados com Pandas e Numpy
Nem todos os dados vêm prontos — muitos estão sujos, incompletos ou desorganizados.  
Neste módulo, você vai aprender a **tratar valores nulos, corrigir erros e padronizar informações**.  
Com **Pandas** e **NumPy**, será possível transformar dados brutos em tabelas organizadas prontas para análise.

---

### 💡 Funções e Estruturas de Dados em Python
Você entenderá como criar **funções reutilizáveis**, economizando tempo e tornando seu código mais limpo e modular.  
Além disso, vai dominar **estruturas de dados** como listas, dicionários e tuplas — elementos essenciais para armazenar e manipular informações de forma inteligente.

---

### ⚡ Interatividade com Streamlit
Por fim, você aprenderá a transformar seus códigos em **aplicações interativas e visualmente atraentes**.  
Com o Streamlit, é possível criar **dashboards, simuladores e ferramentas web** que mostram seus resultados de maneira prática e profissional.

---

💬 Este curso é o seu primeiro passo para dominar a Ciência de Dados — do básico à criação de projetos reais!
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
6. **Quiz Interativo**
""")

    st.success("✅ Clique no menu lateral para iniciar sua jornada!")

# ------------------------------------------------------------
# INTRODUÇÃO À CIÊNCIA DE DADOS
# ------------------------------------------------------------
elif menu == "🧩 Introdução à Ciência de Dados":
    st.header("🧩 Introdução à Ciência de Dados")
    st.write("""
A **Ciência de Dados** é a prática de extrair conhecimento e insights a partir de dados, combinando **estatística, programação e análise visual**.
Ela está presente em áreas como negócios, saúde, tecnologia, marketing e muito mais.
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
    st.write("Vamos criar algumas variáveis e imprimir seus tipos:")
    code_intro = """
# Tipos de dados
numero_inteiro = 10
numero_decimal = 3.14
texto = "Olá, mundo!"
verdadeiro_falso = True

print(type(numero_inteiro))
print(type(numero_decimal))
print(type(texto))
print(type(verdadeiro_falso))
"""
    st.code(code_intro, language="python")
    
    st.write("✅ Aqui você viu os principais tipos de dados em Python e como identificá-los usando `type()`.")

    st.subheader("Prática Interativa")
    st.write("Crie seus próprios dados e veja os tipos:")
    numero = st.number_input("Digite um número:", value=5)
    texto_input = st.text_input("Digite um texto:", value="Olá")
    st.write(f"Tipo do número: {type(numero)}")
    st.write(f"Tipo do texto: {type(texto_input)}")
    st.success("Prática concluída: você testou tipos de dados em tempo real!")

# ------------------------------------------------------------
# LIMPEZA E TRATAMENTO DE DADOS
# ------------------------------------------------------------
elif menu == "📊 Limpeza e Tratamento de Dados":
    st.header("📊 Limpeza e Tratamento de Dados")
    st.write("""
Antes de analisar dados, é fundamental **limpá-los e organizá-los**.
Dados reais podem conter:
- Valores nulos
- Dados duplicados
- Erros de digitação
- Formatos inconsistentes
""")
    
    st.subheader("Exemplo de DataFrame sujo")
    data = {
        "Nome": ["Ana", "Bruno", "Carlos", None, "Ester", "Ana"],
        "Idade": [23, 35, None, 40, 29, 23],
        "Cidade": ["SP", "RJ", "SP", "MG", None, "SP"]
    }
    df = pd.DataFrame(data)
    st.write("DataFrame original:")
    st.dataframe(df)

    st.subheader("Tratamento de dados")
    st.write("""
- **Remover linhas com valores nulos**
- **Preencher valores ausentes**
- **Remover duplicatas**
""")
    df_clean = df.dropna()
    df_clean = df_clean.drop_duplicates()
    st.write("DataFrame limpo:")
    st.dataframe(df_clean)
    st.success("Você aprendeu a limpar dados usando Pandas!")

# ------------------------------------------------------------
# FUNÇÕES PYTHON
# ------------------------------------------------------------
elif menu == "🧠 Funções Python":
    st.header("🧠 Funções em Python")
    st.write("""
Funções são **blocos de código reutilizáveis** que realizam uma tarefa específica.
Elas ajudam a tornar o código **mais organizado e modular**.
""")
    st.subheader("Exemplo de função")
    code_func = """
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Maria"))
"""
    st.code(code_func, language="python")
    st.write("✅ Você viu como criar e chamar uma função simples.")

    st.subheader("Prática Interativa")
    nome_user = st.text_input("Digite seu nome para receber uma saudação:")
    if nome_user:
        st.write(f"Resultado da função: Olá, {nome_user}!")

# ------------------------------------------------------------
# OPERAÇÕES COM LISTAS
# ------------------------------------------------------------
elif menu == "📂 Operações com Listas":
    st.header("📂 Trabalhando com Listas")
    st.write("""
Listas são **estruturas de dados mutáveis** que armazenam múltiplos itens.
""")
    st.subheader("Exemplo")
    code_list = """
frutas = ["maçã", "banana", "laranja"]
frutas.append("uva")
print(frutas)
"""
    st.code(code_list, language="python")
    
    st.subheader("Prática Interativa")
    frutas_input = st.text_input("Adicione uma fruta à lista:", value="morango")
    frutas = ["maçã", "banana", "laranja"]
    frutas.append(frutas_input)
    st.write(f"Lista atualizada: {frutas}")

# ------------------------------------------------------------
# MÓDULO AVANÇADO INTERATIVO
# ------------------------------------------------------------
elif menu == "⚡ Módulo Avançado Interativo":
    st.header("⚡ Módulo Avançado Interativo")
    st.subheader("1️⃣ Calculadora de Potência com Números Quebrados")
    base = st.number_input("Digite a base:", value=2.0)
    expoente = st.number_input("Digite o expoente:", value=3.0)
    potencia = base ** expoente
    st.write(f"Resultado: {base}^{expoente} = {potencia}")
    
    st.subheader("2️⃣ Upload de CSV")
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
    if uploaded_file:
        df_uploaded = pd.read_csv(uploaded_file)
        st.write("Arquivo carregado com sucesso!")
        st.dataframe(df_uploaded)
        st.download_button("📥 Baixar CSV", df_uploaded.to_csv(index=False), "meu_arquivo.csv", "text/csv")

    st.subheader("3️⃣ Operações Numéricas Avançadas")
    st.write("Crie uma tabela com números elevados a potências diferentes:")
    numeros = st.text_input("Digite números separados por vírgula:", value="1,2,3,4")
    expoentes = st.text_input("Digite expoentes separados por vírgula:", value="2,3")
    if numeros and expoentes:
        numeros_list = [float(x.strip()) for x in numeros.split(",")]
        expoentes_list = [float(x.strip()) for x in expoentes.split(",")]
        resultados = {f"x^{exp}": [n**exp for n in numeros_list] for exp in expoentes_list}
        df_resultados = pd.DataFrame(resultados, index=numeros_list)
        st.dataframe(df_resultados)
        st.success("✅ Operações concluídas com sucesso!")

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

    st.write(f"✅ Sua pontuação: {score}/5")

    if score == 5:
        st.balloons()
        st.success("Parabéns! Você acertou todas!")
    elif score >= 3:
        st.info("Bom trabalho! Mas ainda dá para melhorar.")
    else:
        st.warning("Continue estudando, você consegue!")

