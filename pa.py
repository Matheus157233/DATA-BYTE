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

    st.header("🎯 Objetivo")
    st.write("""
Ao final deste curso, você será capaz de:
- Compreender os **fundamentos da análise de dados**
- Criar e limpar **DataFrames**
- Escrever **funções eficientes**
- Trabalhar com **listas e estruturas dinâmicas**
- Construir **pequenos projetos interativos**
""")

    st.success("✅ Clique no menu lateral para iniciar sua jornada!")

# ------------------------------------------------------------
# --- 1. INTRODUÇÃO À CIÊNCIA DE DADOS ---
# ------------------------------------------------------------
elif menu == "🧩 Introdução à Ciência de Dados":
    st.title("🧠 Py - Sua Porta de Entrada para a Ciência de Dados")
    st.subheader("Aprenda Ciência de Dados do zero com Python de forma prática!")
    st.image("https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif", width=250)

    st.header("📘 O que é Ciência de Dados?")
    st.write("""
A **Ciência de Dados** une **estatística, programação e análise de dados** para gerar insights e apoiar decisões.

- 📊 **Análise e visualização de dados**
- 🧮 **Modelagem estatística**
- 🐍 **Programação com Python**
- 🧭 **Entendimento do problema e contexto**
""")
    st.video("https://youtu.be/i6fcwf31htU")

    st.header("💼 Importância no Mercado de Trabalho")
    st.write("""
O mercado de Ciência de Dados cresce rapidamente:

- 💰 Salários: R$6.000 a R$15.000  
- 🧠 Alta demanda em saúde, finanças, marketing e tecnologia  
- 🌍 Empresas valorizam profissionais que transformam dados em estratégias
""")

    st.header("🔢 Tipos de Dados em Python")
    st.write("""
- **Numéricos**: `int`, `float` → 10, 3.14  
- **Texto (strings)**: `"Olá", "Python"`  
- **Booleanos**: `True`, `False`  
- **Categorias**: `"Masculino"`, `"Feminino"`, `"Outro"`
""")
    st.video("https://youtu.be/2ckX4M3ocdQ")

    st.subheader("✅ Exemplo: Variáveis e Arrays com Numpy")
    st.code('''
import numpy as np
idades = np.array([23, 35, 29])
media = np.mean(idades)
print("Média das idades:", media)
''', language="python")

    idades = np.array([23, 35, 29])
    media = np.mean(idades)
    st.success(f"Média das idades: {media}")

    st.header("📦 Trabalhando com pandas (DataFrames)")
    dados = {"Nome": ["Ana", "Carlos", "Beatriz"], "Idade": [23, 35, 29]}
    df = pd.DataFrame(dados)
    st.dataframe(df)
    st.write("📈 Estatísticas descritivas:")
    st.dataframe(df.describe())

    st.map(pd.DataFrame({
        'lat': [-23.55052, -22.9068, -19.9167],
        'lon': [-46.633308, -43.1729, -43.9345],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
    }))

    st.success("🎯 Parabéns! Você concluiu a introdução à Ciência de Dados!")

# ------------------------------------------------------------
# --- 2. LIMPEZA DE DADOS ---
# ------------------------------------------------------------
elif menu == "📊 Limpeza de Dados":
    st.title("📊 Limpeza de Dados")
    st.image("https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif", width=200)
    st.write("""
Antes de analisar dados, é essencial **limpá-los e estruturá-los** corretamente.
Este módulo mostra exemplos práticos usando a biblioteca **pandas**.
""")
    st.video("https://youtu.be/WQ5rsl8y_dw")

    with st.expander("📥 Importação de bibliotecas"):
        st.code("import pandas as pd\nimport numpy as np", language="python")
    with st.expander("📄 Leitura e visualização inicial"):
        st.code('df = pd.read_csv("DADOS_ALUNOS.csv", sep=";")\ndf.head()', language="python")
    with st.expander("🔍 Tratamento de dados ausentes"):
        st.code('df.isnull().sum()\ndf["Nota"] = df["Nota"].fillna(0)', language="python")

# ------------------------------------------------------------
# --- 3. FUNÇÕES PYTHON ---
# ------------------------------------------------------------
elif menu == "🧠 Funções Python":
    st.title("🧠 Funções em Python")
    st.subheader("Organizando códigos e automatizando tarefas")
    st.video("https://www.youtube.com/watch?v=9Os0o3wzS_I")

    st.code("""
def saudacao(nome):
    return f"Olá, {nome}!"
""", language="python")

    with st.expander("📐 Função com parâmetro padrão"):
        st.code("""
def potencia(base, expoente=2):
    return base ** expoente
""", language="python")

# ------------------------------------------------------------
# --- 4. OPERAÇÕES COM LISTAS ---
# ------------------------------------------------------------
elif menu == "📂 Operações com Listas":
    st.title("📂 Operações com Listas")
    st.video("https://www.youtube.com/watch?v=ohCDWZgNIU0")

    with st.expander("➕ Soma e média"):
        st.code("""
lista = [1, 2, 3, 4, 5]
soma = sum(lista)
media = soma / len(lista)
print(f"Soma: {soma}, Média: {media}")
""", language="python")

# ------------------------------------------------------------
# --- 5. MÓDULO AVANÇADO INTERATIVO ---
# ------------------------------------------------------------
elif menu == "⚡ Módulo Avançado Interativo":
    st.title("⚡ Módulo Avançado Interativo")
    st.subheader("Experimente funções e cálculos ao vivo")

    nome = st.text_input("Digite seu nome:")
    if nome:
        st.success(f"Olá, {nome}! 👋 Vamos testar um pouco de Python ao vivo!")

    # Calculadora com floats
    st.markdown("---")
    st.header("🧮 Calculadora Inteligente")
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("Valor A:", value=0.0, step=0.1, format="%.2f")
    with col2:
        b = st.number_input("Valor B:", value=0.0, step=0.1, format="%.2f")
    operacao = st.selectbox("Escolha a operação:", ["Soma", "Subtração", "Multiplicação", "Divisão"])
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
                    st.error("❌ Divisão por zero!")
        except Exception as e:
            st.error(f"Erro: {e}")

    # Gerador de dados
    st.markdown("---")
    st.header("📊 Gerador de Dados Aleatórios")
    linhas = st.slider("Número de linhas:", 5, 100, 10)
    df = pd.DataFrame({
        "A": np.random.randn(linhas),
        "B": np.random.rand(linhas),
        "C": np.random.randint(0, 100, linhas)
    })
    st.dataframe(df)
    st.line_chart(df)

    # Upload de CSV
    st.markdown("---")
    st.header("📂 Upload de Arquivo CSV")
    uploaded_file = st.file_uploader("Envie seu arquivo CSV", type=["csv"])
    if uploaded_file:
        df_user = pd.read_csv(uploaded_file)
        st.dataframe(df_user.head())
        st.dataframe(df_user.describe())
        st.bar_chart(df_user.select_dtypes(include=np.number).iloc[:, :2])

    # Simulador linear
    st.markdown("---")
    st.header("🤖 Simulador de Previsão Linear")
    x = st.number_input("Digite o valor de X:", value=5.0, step=0.1)
    coef = st.slider("Coeficiente (a):", 0.0, 10.0, 2.0)
    intercepto = st.slider("Intercepto (b):", 0.0, 10.0, 1.0)
    previsao = coef * x + intercepto
    st.write(f"🔮 y = {coef}x + {intercepto} → y = **{previsao:.2f}**")

    st.success("🎉 Parabéns! Você explorou os módulos práticos do curso!")

# ------------------------------------------------------------
# --- 6. QUIZ FINAL ---
# ------------------------------------------------------------
elif menu == "📝 Quiz Final do Curso":
    st.title("📝 Quiz Final do Curso")
    st.subheader("Teste seus conhecimentos!")
    st.image("https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif", width=250)

    perguntas = [
        {"pergunta": "O que é Ciência de Dados?",
         "opcoes": ["Estudo de cores", "Combinação de estatística, programação e análise de dados", "Apenas visualização"],
         "resposta": 1},
        {"pergunta": "Qual biblioteca usamos para manipular tabelas?",
         "opcoes": ["Matplotlib", "Seaborn", "Pandas"], "resposta": 2},
        {"pergunta": "Qual comando remove valores nulos?",
         "opcoes": ["df.mean()", "df.dropna()", "df.describe()"], "resposta": 1},
        {"pergunta": "O que o comando print() faz?",
         "opcoes": ["Remove valores", "Mostra uma mensagem na tela", "Cria gráficos"], "resposta": 1}
    ]

    pontuacao = 0
    for i, q in enumerate(perguntas):
        st.markdown(f"### {q['pergunta']}")
        resposta = st.radio("Selecione:", q["opcoes"], key=i)
        if st.button(f"Confirmar questão {i+1}"):
            if q["opcoes"].index(resposta) == q["resposta"]:
                st.success("Correto! 🎯")
                pontuacao += 1
            else:
                st.error(f"Errado! Resposta correta: **{q['opcoes'][q['resposta']]}**")

    if st.button("📊 Ver resultado final"):
        st.subheader(f"Sua pontuação final: **{pontuacao} / {len(perguntas)}**")
        if pontuacao == len(perguntas):
            st.success("🏆 Excelente! Você dominou todos os conceitos!")
        elif pontuacao >= 2:
            st.info("👏 Muito bom! Continue praticando.")
        else:
            st.warning("📘 Revise o conteúdo e tente novamente.")
