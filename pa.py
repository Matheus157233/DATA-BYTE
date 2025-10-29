import streamlit as st
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# CONFIGURAÇÃO GERAL DA PÁGINA
# ------------------------------------------------------------
st.set_page_config(
    page_title="Curso Completo: Introdução à Ciência de Dados com Python",
    page_icon="🧠",
    layout="wide"
)

# ------------------------------------------------------------
# ESTILO PERSONALIZADO (CSS)
# ------------------------------------------------------------
st.markdown("""
<style>
    body {
        background-color: #f5f5f5;
    }
    .stApp {
        background-color: #ffffff;
    }
    h1, h2, h3 {
        color: #0E1117;
    }
    .main-title {
        text-align: center;
        color: #1f77b4;
        font-weight: bold;
    }
    .sub-title {
        text-align: center;
        font-style: italic;
        color: #555;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .small-gif {
        max-height: 200px;
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# MENU LATERAL (NAVBAR)
# ------------------------------------------------------------
st.sidebar.title("📚 Menu do Curso")
st.sidebar.image(
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3hyMjEydDh2ZnA2N3Zpb2xzcmhoYzRrd3lxMG03bmd4NjFhb3Y5eCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3og0ILmP5mKAzV3faw/giphy.gif",
    use_column_width=True
)

menu = st.sidebar.radio("Navegue entre as seções:", [
    "🏠 Página Inicial",
    "🧩 Introdução à Ciência de Dados",
    "📊 Limpeza de Dados",
    "🧠 Funções Python",
    "📂 Operações com Listas",
    "⚡ Módulo Avançado Interativo",
    "📝 Quiz Final do Curso"
])

st.sidebar.markdown("---")
st.sidebar.info("💡 Dica: explore cada módulo em ordem para aproveitar melhor o conteúdo!")

# ------------------------------------------------------------
# --- 0. PÁGINA INICIAL ---
# ------------------------------------------------------------
if menu == "🏠 Página Inicial":
    st.markdown("<h1 class='main-title'>🚀 Curso Completo de Ciência de Dados com Python</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Do zero à prática — entenda, limpe, analise e visualize dados com Python!</p>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif", width=300)
    st.header("📖 Sobre o Curso")
    st.write("Curso prático de introdução à Ciência de Dados, combinando teoria e prática com Python.")
    st.video("https://youtu.be/cm_tM0m9zcI")
    st.success("✅ Clique no menu lateral para iniciar sua jornada!")

# ------------------------------------------------------------
# --- 1. Introdução à Ciência de Dados ---
# ------------------------------------------------------------
elif menu == "🧩 Introdução à Ciência de Dados":
    st.title("🧠 Py - Sua Porta de Entrada para a Ciência de Dados")
    st.image("https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif", width=250)
    st.header("📘 O que é Ciência de Dados?")
    st.write("A Ciência de Dados combina estatística, programação e análise para gerar insights.")
    st.video("https://youtu.be/i6fcwf31htU")

# ------------------------------------------------------------
# --- 2. Limpeza de Dados ---
# ------------------------------------------------------------
elif menu == "📊 Limpeza de Dados":
    st.title("📊 Limpeza de Dados")
    st.video("https://youtu.be/WQ5rsl8y_dw")

# ------------------------------------------------------------
# --- 3. Funções Python ---
# ------------------------------------------------------------
elif menu == "🧠 Funções Python":
    st.title("🧠 Funções em Python")
    st.video("https://www.youtube.com/watch?v=9Os0o3wzS_I")
    st.code("""
def saudacao(nome):
    return f"Olá, {nome}!"
""", language="python")

# ------------------------------------------------------------
# --- 4. Operações com Listas ---
# ------------------------------------------------------------
elif menu == "📂 Operações com Listas":
    st.title("📂 Operações com Listas")
    st.video("https://www.youtube.com/watch?v=ohCDWZgNIU0")
    st.code("""
lista = [1, 2, 3, 4, 5]
soma = sum(lista)
media = soma / len(lista)
print(f"Soma: {soma}, Média: {media}")
""", language="python")

# ------------------------------------------------------------
# --- 5. Módulo Avançado Interativo ---
# ------------------------------------------------------------
elif menu == "⚡ Módulo Avançado Interativo":
    st.title("⚡ Módulo Avançado Interativo")
    st.subheader("Experimente funções e cálculos ao vivo com Python!")
    st.image("https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif", width=250)

    # 1️⃣ Saudação personalizada
    nome = st.text_input("Digite seu nome:")
    if nome:
        st.success(f"Olá, {nome}! 👋 Vamos testar um pouco de Python ao vivo!")

    # 2️⃣ Calculadora de potência
    st.markdown("---")
    st.header("🧮 Calculadora de Potência")
    numero = st.number_input("Digite um número:", value=2.0, step=0.1, format="%.2f")
    potencia = st.slider("Escolha o expoente:", 1, 10, 2)
    resultado = numero ** potencia
    st.write(f"🔹 Resultado: {numero} elevado a {potencia} = **{resultado:.4f}**")

    # 3️⃣ Calculadora personalizada
    st.markdown("---")
    st.header("🧠 Mini Calculadora Inteligente (com números decimais)")
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("Valor A:", value=0.0, step=0.1, format="%.2f")
    with col2:
        b = st.number_input("Valor B:", value=0.0, step=0.1, format="%.2f")
    operacao = st.selectbox("Escolha uma operação:", ["Soma", "Subtração", "Multiplicação", "Divisão"])
    if st.button("Calcular"):
        try:
            if operacao == "Soma":
                st.success(f"✅ Resultado: {a + b:.4f}")
            elif operacao == "Subtração":
                st.success(f"✅ Resultado: {a - b:.4f}")
            elif operacao == "Multiplicação":
                st.success(f"✅ Resultado: {a * b:.4f}")
            elif operacao == "Divisão":
                if b != 0:
                    st.success(f"✅ Resultado: {a / b:.4f}")
                else:
                    st.error("❌ Erro: divisão por zero!")
        except Exception as e:
            st.error(f"Erro no cálculo: {e}")

    # 4️⃣ Geração e visualização de dados
    st.markdown("---")
    st.header("📊 Gerador de Dados Aleatórios")
    linhas = st.slider("Número de linhas:", 5, 100, 10)
    df = pd.DataFrame({
        "A": np.random.randn(linhas),
        "B": np.random.rand(linhas),
        "C": np.random.randint(0, 100, linhas)
    })
    st.dataframe(df, use_container_width=True)
    st.line_chart(df)

    # 5️⃣ Upload e análise automática de CSV
    st.markdown("---")
    st.header("📂 Upload de Arquivo CSV para Análise Rápida")
    uploaded_file = st.file_uploader("Envie seu arquivo CSV", type=["csv"])
    if uploaded_file is not None:
        df_user = pd.read_csv(uploaded_file)
        st.write("📄 Visualização das 5 primeiras linhas:")
        st.dataframe(df_user.head(), use_container_width=True)
        st.write("📊 Estatísticas descritivas:")
        st.dataframe(df_user.describe())
        st.bar_chart(df_user.select_dtypes(include=np.number).iloc[:, :2])

    # 6️⃣ Simulador de previsão simples
    st.markdown("---")
    st.header("🤖 Simulador de Previsão (Modelo Linear Simples)")
    x = st.number_input("Digite o valor de X:", value=5.0, step=0.1)
    coef = st.slider("Coeficiente (a):", 0.0, 10.0, 2.0)
    intercepto = st.slider("Intercepto (b):", 0.0, 10.0, 1.0)
    previsao = coef * x + intercepto
    st.write(f"🔮 Previsão: **y = {coef}x + {intercepto} → y = {previsao:.2f}**")

    # 7️⃣ Editor de código Python simples
    st.markdown("---")
    st.header("💬 Experimente seu próprio código Python")
    codigo = st.text_area("Digite seu código Python abaixo:", "print('Olá, Ciência de Dados!')")
    if st.button("Executar código"):
        try:
            with st.redirect_stdout(st.container()):
                exec(codigo)
        except Exception as e:
            st.error(f"❌ Erro ao executar o código: {e}")

    st.success("🎉 Parabéns! Você explorou todos os módulos interativos do curso!")

# ------------------------------------------------------------
# --- 6. QUIZ FINAL DO CURSO ---
# ------------------------------------------------------------
elif menu == "📝 Quiz Final do Curso":
    st.title("📝 Quiz Final do Curso")
    st.subheader("Teste seus conhecimentos em Ciência de Dados e Python!")
    st.image("https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif", width=250)
    st.markdown("---")

    st.info("📚 Responda as perguntas abaixo e veja sua pontuação!")

    perguntas = [
        {
            "pergunta": "1️⃣ O que é Ciência de Dados?",
            "opcoes": [
                "Um tipo de linguagem de programação",
                "A combinação de estatística, programação e análise de dados para gerar insights",
                "Um software de visualização de gráficos",
                "Apenas análise de planilhas"
            ],
            "resposta": 1
        },
        {
            "pergunta": "2️⃣ Qual biblioteca é mais usada para manipulação de tabelas em Python?",
            "opcoes": ["Matplotlib", "Seaborn", "Pandas", "TensorFlow"],
            "resposta": 2
        },
        {
            "pergunta": "3️⃣ Observe o gráfico abaixo. Qual tipo de gráfico ele representa?",
            "opcoes": ["Linha", "Barras", "Pizza", "Dispersão"],
            "resposta": 1,
            "imagem": "https://matplotlib.org/stable/_images/sphx_glr_bar_stacked_001.png"
        },
        {
            "pergunta": "4️⃣ Qual comando remove valores nulos de um DataFrame?",
            "opcoes": ["df.mean()", "df.dropna()", "df.fillna()", "df.describe()"],
            "resposta": 1
        },
        {
            "pergunta": "5️⃣ Em Python, o que o comando print() faz?",
            "opcoes": ["Remove valores", "Mostra uma mensagem na tela", "Cria uma função", "Importa bibliotecas"],
            "resposta": 1
        }
    ]

    pontuacao = 0
    for i, q in enumerate(perguntas):
        st.markdown(f"### {q['pergunta']}")
        if "imagem" in q:
            st.image(q["imagem"], width=400)
        resposta = st.radio("Selecione a resposta:", q["opcoes"], key=i)
        if st.button(f"✅ Confirmar questão {i+1}"):
            if q["opcoes"].index(resposta) == q["resposta"]:
                st.success("Correto! 🎯")
                pontuacao += 1
            else:
                st.error(f"❌ Errado! Resposta correta: **{q['opcoes'][q['resposta']]}**")

    if st.button("📊 Ver resultado final"):
        st.subheader(f"🎯 Sua pontuação final: **{pontuacao} / {len(perguntas)}**")
        if pontuacao == len(perguntas):
            st.success("🏆 Excelente! Você dominou todos os conceitos de Ciência de Dados com Python!")
        elif pontuacao >= 3:
            st.info("👏 Muito bom! Continue praticando e explore mais exemplos.")
        else:
            st.warning("📘 Estude um pouco mais e tente novamente!")
