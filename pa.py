import streamlit as st import pandas as pd import numpy as np import math

------------------------------------------------------------
CONFIGURAÇÃO GERAL DA PÁGINA
------------------------------------------------------------
st.set_page_config( page_title="Curso Completo: Introdução à Ciência de Dados com Python", page_icon="🧠", layout="wide" )

------------------------------------------------------------
ESTILO PERSONALIZADO (CSS)
------------------------------------------------------------
st.markdown("""

<style> body { background-color: #f5f5f5; } .stApp { background-color: #ffffff; } h1, h2, h3 { color: #0E1117; } .main-title { text-align: center; color: #1f77b4; font-weight: bold; } .sub-title { text-align: center; font-style: italic; color: #555; } .block-container { padding-top: 2rem; padding-bottom: 2rem; } </style>

""", unsafe_allow_html=True)

------------------------------------------------------------
MENU LATERAL (NAVBAR)
------------------------------------------------------------
st.sidebar.title("📚 Menu do Curso") st.sidebar.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3hyMjEydDh2ZnA2N3Zpb2xzcmhoYzRrd3lxMG03bmd4NjFhb3Y5eCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3og0ILmP5mKAzV3faw/giphy.gif", use_column_width=True) menu = st.sidebar.radio("Navegue entre as seções:", [ "🏠 Página Inicial", "🧩 Introdução à Ciência de Dados", "📊 Limpeza de Dados", "🧠 Funções Python", "📂 Operações com Listas", "⚡ Módulo Avançado Interativo", "❓ Quiz do Curso" ]) st.sidebar.markdown("---") st.sidebar.info("💡 Dica: explore cada módulo em ordem para aproveitar melhor o conteúdo!")

------------------------------------------------------------
--- 0. PÁGINA INICIAL ---
------------------------------------------------------------
if menu == "🏠 Página Inicial": st.markdown("<h1 class='main-title'>🚀 Curso Completo da introdução de Ciência de Dados com Python", unsafe_allow_html=True) st.markdown("<p class='sub-title'>Do zero à prática — entenda, limpe, analise e visualize dados com Python!

", unsafe_allow_html=True) st.markdown("---") st.image("https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif", width=300)
st.header("📖 Sobre o Curso")
st.write("""
Este curso foi desenvolvido para introduzir você à Ciência de Dados, combinando teoria e prática em um ambiente interativo com Python.

Você aprenderá:

🧮 Conceitos fundamentais de Ciência de Dados

🐍 Programação prática em Python

📊 Limpeza e manipulação de dados com Pandas e Numpy

💡 Funções e estruturas de dados em Python

⚡ Interatividade com Streamlit
""") st.video("https://youtu.be/cm_tM0m9zcI") st.header("🎯 Objetivo do Curso") st.write(""" Ao final deste curso, você será capaz de:

Compreender os fundamentos da análise de dados

Criar e limpar DataFrames

Escrever funções eficientes

Trabalhar com listas e estruturas dinâmicas

Construir projetos interativos com Streamlit """) st.success("✅ Clique no menu lateral para iniciar sua jornada!")

------------------------------------------------------------
--- 1. Introdução à Ciência de Dados ---
------------------------------------------------------------
elif menu == "🧩 Introdução à Ciência de Dados": st.title("🧠 Introdução à Ciência de Dados") st.image("https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif", width=250) st.header("📘 O que é Ciência de Dados?") st.write("""

A Ciência de Dados une estatística, programação e análise de dados para gerar insights e apoiar decisões.

Ela é usada em praticamente todas as áreas: negócios, saúde, finanças, tecnologia, e até esportes! """) st.video("https://youtu.be/i6fcwf31htU")

st.header("🐍 Primeiros Passos com Python")
st.code('print("Olá, mundo da Ciência de Dados!")', language="python")

st.write("""
O comando print() serve para exibir mensagens na tela.
Ele é o primeiro passo de qualquer pessoa aprendendo Python. """) st.subheader("Exemplo prático com Numpy") st.code("""

import numpy as np idades = np.array([23, 35, 29]) media = np.mean(idades) print("Média das idades:", media) """, language="python") idades = np.array([23, 35, 29]) media = np.mean(idades) st.success(f"Média das idades: {media}")

st.write("""
O NumPy é uma biblioteca usada para cálculos matemáticos e estatísticos.
Aqui, np.mean() calcula a média de uma lista de números. """) st.header("📦 Trabalhando com pandas (DataFrames)") dados = {"Nome": ["Ana", "Carlos", "Beatriz"], "Idade": [23, 35, 29]} df = pd.DataFrame(dados) st.dataframe(df) st.write("📈 Estatísticas descritivas:") st.dataframe(df.describe())

st.write("""
O Pandas permite criar tabelas chamadas DataFrames.
Elas são essenciais para manipular, filtrar e analisar dados estruturados. """)

------------------------------------------------------------
--- 2. Limpeza de Dados ---
------------------------------------------------------------
elif menu == "📊 Limpeza de Dados": st.title("📊 Limpeza de Dados") st.subheader("Preparando e organizando dados sujos para análise") st.image("https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif", width=200) st.write("""

Antes de analisar dados, é essencial limpá-los e estruturá-los corretamente. Este processo é chamado de data cleaning. """) st.video("https://youtu.be/WQ5rsl8y_dw") st.write("""

O Pandas facilita essa etapa, permitindo:

Verificar valores ausentes (df.isnull())
Remover linhas com df.dropna()
Preencher dados vazios com df.fillna()
Padronizar tipos de dados e nomes de colunas """)
------------------------------------------------------------
--- 3. Funções Python ---
------------------------------------------------------------
elif menu == "🧠 Funções Python": st.title("🧠 Funções em Python") st.subheader("Organizando códigos e automatizando tarefas") st.video("https://www.youtube.com/watch?v=9Os0o3wzS_I") st.markdown("""

Funções são blocos de código reutilizáveis.
Elas ajudam a deixar o código mais limpo, rápido e organizado. """) st.code("""

def saudacao(nome): return f"Olá, {nome}!" """, language="python") st.write("""

Aqui, def define a função, nome é o parâmetro e return devolve o resultado. """)

------------------------------------------------------------
--- 4. Operações com Listas ---
------------------------------------------------------------
elif menu == "📂 Operações com Listas": st.title("📂 Operações com Listas") st.video("https://www.youtube.com/watch?v=ohCDWZgNIU0") st.markdown("""

Listas armazenam múltiplos valores em uma única variável. """) st.code("""

lista = [1, 2, 3, 4, 5] soma = sum(lista) media = soma / len(lista) print(f"Soma: {soma}, Média: {media}") """, language="python") st.write("""

Com sum() somamos os valores, e com len() contamos os itens da lista.
A média é a soma dividida pela quantidade de elementos. """)

------------------------------------------------------------
--- 5. Módulo Avançado Interativo ---
------------------------------------------------------------
elif menu == "⚡ Módulo Avançado Interativo": st.title("⚡ Módulo Avançado Interativo") st.subheader("Coloque a mão na massa! Aqui você vai testar, calcular e analisar dados em tempo real!") st.image("https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif", width=250)

# Saudação
nome = st.text_input("Digite seu nome:")
if nome:
    st.success(f"Olá, {nome}! 👋 Vamos testar um pouco de Python ao vivo!")

# 1️⃣ Calculadora de potência
st.markdown("---")
st.header("🧮 Calculadora de Potência")
numero = st.number_input("Digite um número (pode ser decimal):", value=2.0, step=0.1)
expoente = st.number_input("Digite o expoente:", value=2.0, step=0.1)
resultado = numero ** expoente
st.success(f"🔹 Resultado: {numero} elevado a {expoente} = **{resultado}**")

st.info("""
Teoria:
Este exercício mostra como Python pode realizar operações matemáticas usando variáveis.
A expressão numero ** expoente significa “número elevado ao expoente”. """) # 2️⃣ Calculadora personalizada st.markdown("---") st.header("🧠 Mini Calculadora Inteligente") a = st.number_input("Valor A:", value=0.0, step=0.1) b = st.number_input("Valor B:", value=0.0, step=0.1) operacao = st.selectbox("Escolha uma operação:", ["Soma", "Subtração", "Multiplicação", "Divisão"]) if st.button("Calcular"): if operacao == "Soma": st.success(f"✅ Resultado: {a + b}") elif operacao == "Subtração": st.success(f"✅ Resultado: {a - b}") elif operacao == "Multiplicação": st.success(f"✅ Resultado: {a * b}") elif operacao == "Divisão": st.success(f"✅ Resultado: {a / b if b != 0 else 'Erro: divisão por zero!'}")

st.info("""
Teoria:
Aqui, você usa condicionais (if/elif) para decidir qual operação executar.
É o mesmo raciocínio usado em modelos de decisão em Ciência de Dados. """) # 3️⃣ Gerador de dados st.markdown("---") st.header("📊 Gerador de Dados Aleatórios") linhas = st.slider("Número de linhas:", 5, 100, 10) df = pd.DataFrame({ "A": np.random.randn(linhas), "B": np.random.rand(linhas), "C": np.random.randint(0, 100, linhas) }) st.dataframe(df) st.line_chart(df)

st.info("""
Teoria:
Aqui, o NumPy gera valores aleatórios simulando dados reais.
Esses valores são organizados em um DataFrame, e depois visualizados em um gráfico de linha. """) # 4️⃣ Download e upload de CSV st.markdown("---") st.header("📥 Baixe o arquivo CSV de exemplo e faça upload") csv_content = """Nome,Idade,Nota,Presenca

Ana,22,8.5,Sim Bruno,25,7.8,Sim Carla,23,9.2,Não Diego,21,,Sim Elisa,24,6.9,Não Felipe,22,8.0,Sim Gabriela,26,7.5,Sim Henrique,20,5.8,Não Isabela,23,,Sim João,25,9.5,Sim """ st.download_button("📩 Baixar arquivo DADOS_ALUNOS.csv", data=csv_content, file_name="DADOS_ALUNOS.csv", mime="text/csv") uploaded_file = st.file_uploader("Envie seu arquivo CSV", type=["csv"]) if uploaded_file is not None: df_user = pd.read_csv(uploaded_file) st.write("📄 Visualização inicial:") st.dataframe(df_user.head()) st.write("📊 Estatísticas:") st.dataframe(df_user.describe())

st.info("""
Teoria:
O CSV é um formato amplamente usado para armazenar dados.
Com pandas.read_csv(), você lê o arquivo e pode analisá-lo diretamente com Python. """) # 5️⃣ Simulador de previsão simples st.markdown("---") st.header("🤖 Simulador de Previsão Linear") x = st.number_input("Digite o valor de X:", value=5.0) coef = st.slider("Coeficiente (a):", 0.0, 10.0, 2.0) intercepto = st.slider("Intercepto (b):", 0.0, 10.0, 1.0) previsao = coef * x + intercepto st.success(f"🔮 Previsão: **y = {coef}x + {intercepto} → y = {previsao:.2f}**")

st.info("""
Teoria:
Esta é a base de um modelo de regressão linear simples, usado para prever valores.
A equação y = ax + b mostra como uma variável (x) afeta outra (y). """) # 6️⃣ Código livre st.markdown("---") st.header("💬 Execute seu próprio código Python") codigo = st.text_area("Digite seu código Python abaixo:", "print('Olá, Ciência de Dados!')") if st.button("Executar código"): try: exec(codigo) except Exception as e: st.error(f"❌ Erro ao executar o código: {e}")

st.info("""
Teoria:
Com o comando exec(), você pode executar qualquer código Python dinamicamente.
Isso permite testar ideias e algoritmos rapidamente. """) st.success("🎉 Parabéns! Você concluiu o módulo interativo!")

------------------------------------------------------------
--- 6. Quiz ---
------------------------------------------------------------
elif menu == "❓ Quiz do Curso": st.title("❓ Quiz - Ciência de Dados com Python") st.subheader("Teste seus conhecimentos adquiridos no curso!") pontuacao = 0 erros = []

q1 = st.radio("1️⃣ O que é Ciência de Dados?", [
    "Apenas criar gráficos",
    "A união de estatística, programação e análise de dados",
    "Somente mexer em planilhas"
])
if q1 == "A união de estatística, programação e análise de dados":
    pontuacao += 1
else:
    erros.append("1️⃣ O que é Ciência de Dados")

q2 = st.radio("2️⃣ Qual biblioteca é usada para DataFrames?", ["NumPy", "Pandas", "Math"])
if q2 == "Pandas":
    pontuacao += 1
else:
    erros.append("2️⃣ Biblioteca para DataFrames")

q3 = st.radio("3️⃣ O que faz a função print()?", ["Mostra mensagens na tela", "Apaga dados", "Fecha o programa"])
if q3 == "Mostra mensagens na tela":
    pontuacao += 1
else:
    erros.append("3️⃣ Função print()")

q4 = st.radio("4️⃣ Qual comando remove valores nulos?", ["df.remove()", "df.dropna()", "df.fillna()"])
if q4 == "df.dropna()":
    pontuacao += 1
else:
    erros.append("4️⃣ Remover valores nulos")

q5 = st.radio("5️⃣ Qual palavra define uma função?", ["lambda", "def", "func"])
if q5 == "def":
    pontuacao += 1
else:
    erros.append("5️⃣ Definir função")

# 🆕 NOVAS PERGUNTAS
q6 = st.radio("6️⃣ O que significa o operador ** em Python?", [
    "Multiplicação simples",
    "Potência (elevação a um número)",
    "Divisão inteira"
])
if q6 == "Potência (elevação a um número)":
    pontuacao += 1
else:
    erros.append("6️⃣ Operador **")

q7 = st.radio("7️⃣ O que faz o comando df.describe()?", [
    "Apaga colunas do DataFrame",
    "Mostra estatísticas descritivas",
    "Adiciona novas linhas"
])
if q7 == "Mostra estatísticas descritivas":
    pontuacao += 1
else:
    erros.append("7️⃣ df.describe()")

q8 = st.radio("8️⃣ Qual dessas opções NÃO é uma biblioteca de dados em Python?", [
    "Pandas", "NumPy", "HTML"
])
if q8 == "HTML":
    pontuacao += 1
else:
    erros.append("8️⃣ Biblioteca não relacionada")

q9 = st.radio("9️⃣ Qual comando é usado para importar bibliotecas em Python?", [
    "load", "import", "include"
])
if q9 == "import":
    pontuacao += 1
else:
    erros.append("9️⃣ Comando importação")

q10 = st.radio("🔟 O que é um DataFrame?", [
    "Um tipo de gráfico de barras",
    "Uma tabela de dados bidimensional do Pandas",
    "Uma função do NumPy"
])
if q10 == "Uma tabela de dados bidimensional do Pandas":
    pontuacao += 1
else:
    erros.append("🔟 DataFrame")

if st.button("Ver resultado"):
    st.success(f"🎯 Sua pontuação final: **{pontuacao}/10**")
    if pontuacao == 10:
        st.balloons()
        st.success("🏆 Excelente! Você dominou o conteúdo!")
    elif pontuacao >= 7:
        st.info("💪 Bom trabalho! Reveja alguns conceitos para aperfeiçoar.")
    else:
        st.warning("📘 Continue estudando! Volte aos módulos e pratique mais.")

    if erros:
        st.error("❌ Você errou as seguintes perguntas:")
        for e in erros:
            st.write(f"• {e}")
    else:
        st.success("🎉 Você acertou todas as perguntas!")
