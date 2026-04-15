import streamlit as st
import pandas as pd
import numpy as np
import math
import altair as alt
import sqlite3
import re
from sklearn.linear_model import LinearRegression
# ------------------------------------------------------------
# CONFIGURAÇÃO GERAL DA PÁGINA (TEM QUE SER PRIMEIRO)
# ------------------------------------------------------------
st.set_page_config(
    page_title="Curso Completo: Introdução à Ciência de Dados com Python",
    page_icon="🧠",
    layout="wide"
)
 
# =========================
# LOGIN + CADASTRO (AQUI)
# =========================
import sqlite3
 
conn = sqlite3.connect("usuarios.db", check_same_thread=False)
c = conn.cursor()
 
# 🔥 ADICIONA ISSO AQUI
try:
    c.execute("ALTER TABLE usuarios ADD COLUMN telefone TEXT")
except:
    pass
 
try:
    c.execute("ALTER TABLE usuarios ADD COLUMN foto TEXT")
except:
    pass
 
c.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    senha TEXT,
    telefone TEXT,
    foto TEXT
)
""")
 
if "logado" not in st.session_state:
    st.session_state["logado"] = None
 
if "pagina" not in st.session_state:
    st.session_state["pagina"] = "login"
if "progresso" not in st.session_state:
    st.session_state.progresso = 0
 
if "badges" not in st.session_state:
    st.session_state.badges = []
 
if "nota_quiz" not in st.session_state:
    st.session_state.nota_quiz = 0
 
# -------- LOGIN --------
def tela_login():
    st.title("🔐 Login")
 
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")
 
    if st.button("Entrar"):
        if email == "admin" and senha == "1234":
            st.session_state["logado"] = "admin"
            st.rerun()
        else:
            c.execute("SELECT * FROM usuarios WHERE email=? AND senha=?", (email, senha))
            user = c.fetchone()
 
            if user:
                st.session_state["logado"] = "user"
                st.session_state["email"] = email
                st.rerun()
            else:
                st.error("Login inválido")
 
    if st.button("Criar conta"):
        st.session_state["pagina"] = "cadastro"
        st.rerun()
 
# -------- CADASTRO --------
def tela_cadastro():
    st.title("➕ Cadastro")
 
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")
 
    if st.button("Cadastrar"):
        if not nome or not email or not senha:
            st.warning("Preencha tudo")
        else:
            c.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
            conn.commit()
            st.success("Cadastro realizado!")
            st.session_state["pagina"] = "login"
            st.rerun()
 
    if st.button("Já tenho conta"):
        st.session_state["pagina"] = "login"
        st.rerun()
 
# -------- BLOQUEIO --------
if not st.session_state["logado"]:
    if st.session_state["pagina"] == "login":
        tela_login()
    else:
        tela_cadastro()
    st.stop()
 
# ------------------------
# VERIFICA PERFIL COMPLETO
# ------------------------
if st.session_state["logado"] == "user":
 
    email = st.session_state.get("email")
 
    c.execute("SELECT telefone, foto FROM usuarios WHERE email=?", (email,))
    dados = c.fetchone()
 
    if dados:
        telefone, foto = dados
 
        if not telefone or not foto:
            st.warning("⚠️ Complete seu perfil para acessar o curso")
 
            menu = st.sidebar.radio("Menu", ["👤 Perfil"])
 
            if menu == "👤 Perfil":
                st.title("👤 Complete seu perfil")
 
                telefone_input = st.text_input("📱 Telefone")
                foto_input = st.file_uploader("📸 Foto", type=["png", "jpg"])
 
                if st.button("Salvar"):
                    caminho = None
 
                    if foto_input:
                        caminho = f"foto_{email}.png"
                        with open(caminho, "wb") as f:
                            f.write(foto_input.read())
 
                    c.execute("""
                    UPDATE usuarios
                    SET telefone=?, foto=?
                    WHERE email=?
                    """, (telefone_input, caminho, email))
 
                    conn.commit()
                    st.success("Perfil completo!")
                    st.rerun()
 
            st.stop()
# ------------------------------------------------------------
# CONTROLES GLOBAIS (TEMA E IDIOMA)
# ------------------------------------------------------------
if "tema" not in st.session_state:
    st.session_state.tema = "Claro"
 
if "idioma" not in st.session_state:
    st.session_state.idioma = "PT"
 
def aplicar_tema():
    if st.session_state.tema == "Escuro":
        st.markdown("""
<style>
        body { background-color: #0e1117; color: white; }
</style>
        """, unsafe_allow_html=True)
 
def t(pt, en):
    return pt if st.session_state.idioma == "PT" else en
 
aplicar_tema()
 
# ------------------------------------------------------------
# ESTILO PERSONALIZADO (CSS)
# ------------------------------------------------------------
st.markdown("""
<style>
.stButton>button {
    background: linear-gradient(90deg, #4CAF50, #00c6ff);
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
}
 
.stTextInput>div>div>input {
    border-radius: 10px;
}
 
[data-testid="stSidebar"] {
    background-color: #111;
}
</style>
""", unsafe_allow_html=True)
# ------------------------------------------------------------
# MENU LATERAL (NAVBAR)
# ------------------------------------------------------------
st.sidebar.title("📚 Menu do Curso")
st.sidebar.image(
    "https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif",
    use_column_width=True
)
 
menu = st.sidebar.radio("Navegue entre as seções:", [
    "🏠 Página Inicial",
    "🧩 Introdução à Ciência de Dados",
    "📊 Limpeza de Dados",
    "🧹 Limpeza de CSV (Profissional)",
    "📈 Análise de Dados",
    "🧠 Funções Python",
    "📂 Operações com Listas",
    "⚡ Módulo Avançado Interativo",
    "❓ Quiz do Curso",
    "🔒 Área Admin",
    "👤 Perfil",
    "🐍 Python Básico",
    "📊 Pandas Avançado",
    "🤖 Machine Learning",
])
 
# Agora os controles de tema e idioma
st.sidebar.markdown("### ⚙️ Preferências")
 
st.session_state.tema = st.sidebar.selectbox(
    "🌗 Tema",
    ["Claro", "Escuro"],
    index=0 if st.session_state.tema == "Claro" else 1
)
 
st.session_state.idioma = st.sidebar.selectbox(
    "🌎 Idioma",
    ["PT", "EN"]
)
 
st.sidebar.markdown("---")
st.sidebar.info("💡 Dica: explore cada módulo em ordem para aproveitar melhor o conteúdo!")
 
# ------------------------------------------------------------
# --- 0. PÁGINA INICIAL ---
# ------------------------------------------------------------
if menu == "🏠 Página Inicial":
    col1, col2, col3 = st.columns(3)
    col1.metric("📚 Módulos", "10")
    col2.metric("⏱ Tempo", "3h+")
    col3.metric("📊 Progresso", f"{st.session_state.progresso}%")
    st.markdown("<h1 class='main-title'>🚀 Curso Completo da introdução de Ciência de Dados com Python</h1>", unsafe_allow_html=True)
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
 
    st.header("🎯 Objetivo do Curso")
    st.write("""
Ao final deste curso, você será capaz de:
- Compreender os **fundamentos da análise de dados**
- Criar e limpar **DataFrames**
- Escrever **funções eficientes**
- Trabalhar com **listas e estruturas dinâmicas**
- Construir **projetos interativos com Streamlit**
""")
    st.success("✅ Clique no menu lateral para iniciar sua jornada!")
 
 
# ------------------------------------------------------------
# --- 1. Introdução à Ciência de Dados ---
# ------------------------------------------------------------
elif menu == "🧩 Introdução à Ciência de Dados":
    st.title("🧠 Introdução à Ciência de Dados")
    st.image("https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif", width=250)
 
 
    st.header("📘 O que é Ciência de Dados?")
    st.write("""
A **Ciência de Dados** une **estatística, programação e análise de dados** para gerar insights e apoiar decisões.
 
 
Ela é usada em praticamente todas as áreas: negócios, saúde, finanças, tecnologia, e até esportes!
""")
 
 
    st.video("https://youtu.be/i6fcwf31htU")
 
 
    st.header("🐍 Primeiros Passos com Python")
    st.code('print("Olá, mundo da Ciência de Dados!")', language="python")
 
 
    st.write("""
O comando `print()` serve para **exibir mensagens na tela**.  
Ele é o primeiro passo de qualquer pessoa aprendendo Python.
""")
 
 
    st.subheader("Exemplo prático com Numpy")
    st.code("""
import numpy as np
idades = np.array([23, 35, 29])
media = np.mean(idades)
print("Média das idades:", media)
""", language="python")
 
 
    idades = np.array([23, 35, 29])
    media = np.mean(idades)
    st.success(f"Média das idades: {media}")
 
 
    st.write("""
O NumPy é uma biblioteca usada para cálculos matemáticos e estatísticos.  
Aqui, `np.mean()` calcula a **média** de uma lista de números.
""")
 
 
    st.header("📦 Trabalhando com pandas (DataFrames)")
    dados = {"Nome": ["Ana", "Carlos", "Beatriz"], "Idade": [23, 35, 29]}
    df = pd.DataFrame(dados)
    st.dataframe(df)
    st.write("📈 Estatísticas descritivas:")
    st.dataframe(df.describe())
 
 
    st.write("""
O Pandas permite criar tabelas chamadas **DataFrames**.  
Elas são essenciais para manipular, filtrar e analisar dados estruturados.
""")
 
 
# ------------------------------------------------------------
# --- 2. Limpeza de Dados ---
# ------------------------------------------------------------
elif menu == "📊 Limpeza de Dados":
    st.title("📊 Limpeza de Dados")
    st.subheader("Preparando e organizando dados sujos para análise")
    st.image("https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif", width=200)
 
 
    st.write("""
Antes de analisar dados, é essencial **limpá-los e estruturá-los** corretamente.
Este processo é chamado de **data cleaning**.
""")
    st.video("https://youtu.be/WQ5rsl8y_dw")
 
 
    st.write("""
O Pandas facilita essa etapa, permitindo:
- Verificar valores ausentes (`df.isnull()`)
- Remover linhas com `df.dropna()`
- Preencher dados vazios com `df.fillna()`
- Padronizar tipos de dados e nomes de colunas
""")
 
 
elif menu == "🧹 Limpeza de CSV (Profissional)":
    st.title("🧹 Limpeza Profissional de Arquivos CSV")
    st.write(t(
        "Envie um CSV bagunçado, limpe automaticamente e baixe o arquivo tratado.",
        "Upload a messy CSV, clean it automatically and download the processed file."
    ))
 
 
    file = st.file_uploader("📂 Upload do CSV", type=["csv"])
 
 
    if file:
        df = pd.read_csv(file)
        st.subheader("📄 Dados Originais")
        st.dataframe(df)
 
 
        st.subheader("⚙️ Processo de Limpeza")
        df_limpo = df.copy()
 
 
        # Padronizar colunas
        df_limpo.columns = (
            df_limpo.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )
 
 
        # Remover duplicados
        df_limpo.drop_duplicates(inplace=True)
 
 
        # Tratar valores nulos
        for col in df_limpo.columns:
            if df_limpo[col].dtype == "object":
                df_limpo[col].fillna("Desconhecido", inplace=True)
            else:
                df_limpo[col].fillna(df_limpo[col].mean(), inplace=True)
 
 
        st.success("✅ Limpeza concluída com sucesso!")
        st.subheader("📊 Dados Tratados")
        st.dataframe(df_limpo)
 
 
        csv = df_limpo.to_csv(index=False).encode("utf-8")
        st.download_button(
            "📥 Baixar CSV Tratado",
            data=csv,
            file_name="dados_tratados.csv",
            mime="text/csv"
        )
 
# ------------------------------------------------------------
# --- 3. Funções Python ---
# ------------------------------------------------------------
elif menu == "🧠 Funções Python":
    st.title("🧠 Funções em Python")
    st.subheader("Organizando códigos e automatizando tarefas")
    st.video("https://www.youtube.com/watch?v=9Os0o3wzS_I")
 
 
    st.markdown("""
Funções são **blocos de código reutilizáveis**.  
Elas ajudam a deixar o código **mais limpo, rápido e organizado**.
""")
 
 
    st.code("""
def saudacao(nome):
    return f"Olá, {nome}!"
""", language="python")
 
 
    st.write("""
Aqui, `def` define a função, `nome` é o parâmetro e `return` devolve o resultado.
""")
 
 
# ------------------------------------------------------------
# --- 4. Operações com Listas ---
# ------------------------------------------------------------
elif menu == "📂 Operações com Listas":
    st.title("📂 Operações com Listas")
    st.video("https://www.youtube.com/watch?v=ohCDWZgNIU0")
 
 
    st.markdown("""
Listas armazenam **múltiplos valores em uma única variável**.
""")
 
 
    st.code("""
lista = [1, 2, 3, 4, 5]
soma = sum(lista)
media = soma / len(lista)
print(f"Soma: {soma}, Média: {media}")
""", language="python")
 
 
    st.write("""
Com `sum()` somamos os valores, e com `len()` contamos os itens da lista.  
A média é a soma dividida pela quantidade de elementos.
""")
 
 
# ------------------------------------------------------------
# --- 5. Módulo Avançado Interativo ---
# ------------------------------------------------------------
elif menu == "⚡ Módulo Avançado Interativo":
    st.title("⚡ Módulo Avançado Interativo")
    st.subheader("Coloque a mão na massa! Aqui você vai testar, calcular e analisar dados em tempo real!")
 
 
    st.image("https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif", width=250)
 
 
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
**Teoria:**  
Este exercício mostra como Python pode realizar **operações matemáticas** usando variáveis.  
A expressão `numero ** expoente` significa “número elevado ao expoente”.
""")
 
 
    # 2️⃣ Calculadora personalizada
    st.markdown("---")
    st.header("🧠 Mini Calculadora Inteligente")
    a = st.number_input("Valor A:", value=0.0, step=0.1)
    b = st.number_input("Valor B:", value=0.0, step=0.1)
    operacao = st.selectbox("Escolha uma operação:", ["Soma", "Subtração", "Multiplicação", "Divisão"])
    if st.button("Calcular"):
        if operacao == "Soma":
            st.success(f"✅ Resultado: {a + b}")
        elif operacao == "Subtração":
            st.success(f"✅ Resultado: {a - b}")
        elif operacao == "Multiplicação":
            st.success(f"✅ Resultado: {a * b}")
        elif operacao == "Divisão":
            st.success(f"✅ Resultado: {a / b if b != 0 else 'Erro: divisão por zero!'}")
 
 
    st.info("""
**Teoria:**  
Aqui, você usa **condicionais (if/elif)** para decidir qual operação executar.  
É o mesmo raciocínio usado em modelos de decisão em Ciência de Dados.
""")
 
 
    # 3️⃣ Gerador de dados
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
 
 
    st.info("""
**Teoria:**  
Aqui, o NumPy gera **valores aleatórios** simulando dados reais.  
Esses valores são organizados em um **DataFrame**, e depois visualizados em um gráfico de linha.
""")
 
 
    # 4️⃣ Download e upload de CSV
    st.markdown("---")
    st.header("📥 Baixe o arquivo CSV de exemplo e faça upload")
    csv_content = """Nome,Idade,Nota,Presenca
Ana,22,8.5,Sim
Bruno,25,7.8,Sim
Carla,23,9.2,Não
Diego,21,,Sim
Elisa,24,6.9,Não
Felipe,22,8.0,Sim
Gabriela,26,7.5,Sim
Henrique,20,5.8,Não
Isabela,23,,Sim
João,25,9.5,Sim
"""
    st.download_button("📩 Baixar arquivo DADOS_ALUNOS.csv", data=csv_content, file_name="DADOS_ALUNOS.csv", mime="text/csv")
 
 
    uploaded_file = st.file_uploader("Envie seu arquivo CSV", type=["csv"])
    if uploaded_file is not None:
        df_user = pd.read_csv(uploaded_file)
        st.write("📄 Visualização inicial:")
        st.dataframe(df_user.head())
        st.write("📊 Estatísticas:")
        st.dataframe(df_user.describe())
 
 
    st.info("""
**Teoria:**  
O CSV é um formato amplamente usado para armazenar dados.  
Com `pandas.read_csv()`, você lê o arquivo e pode analisá-lo diretamente com Python.
""")
 
 
    # 5️⃣ Simulador de previsão simples
    st.markdown("---")
    st.header("🤖 Simulador de Previsão Linear")
    x = st.number_input("Digite o valor de X:", value=5.0)
    coef = st.slider("Coeficiente (a):", 0.0, 10.0, 2.0)
    intercepto = st.slider("Intercepto (b):", 0.0, 10.0, 1.0)
    previsao = coef * x + intercepto
    st.success(f"🔮 Previsão: **y = {coef}x + {intercepto} → y = {previsao:.2f}**")
 
 
    st.info("""
**Teoria:**  
Esta é a base de um **modelo de regressão linear simples**, usado para prever valores.  
A equação `y = ax + b` mostra como uma variável (x) afeta outra (y).
""")
 
 
    # 6️⃣ Código livre
    st.markdown("---")
    st.header("💬 Execute seu próprio código Python")
    codigo = st.text_area("Digite seu código Python abaixo:", "print('Olá, Ciência de Dados!')")
    if st.button("Executar código"):
        try:
            exec(codigo)
        except Exception as e:
            st.error(f"❌ Erro ao executar o código: {e}")
 
 
    st.info("""
**Teoria:**  
Com o comando `exec()`, você pode **executar qualquer código Python** dinamicamente.  
Isso permite testar ideias e algoritmos rapidamente.
""")
 
 
    st.success("🎉 Parabéns! Você concluiu o módulo interativo!")
 
 
# ------------------------------------------------------------
# --- PERFIL DO USUÁRIO
# ------------------------------------------------------------
elif menu == "👤 Perfil":
    st.header("🏅 Conquistas")
    for badge in st.session_state.badges:
        st.write(badge)
 
    st.title("👤 Meu Perfil")
 
    email = st.session_state.get("email")
 
    c.execute("SELECT nome, email, telefone, foto FROM usuarios WHERE email=?", (email,))
    user = c.fetchone()
 
    if user:
        nome, email, telefone, foto = user
 
        st.write(f"Nome: {nome}")
        st.write(f"Email: {email}")
 
        telefone_input = st.text_input("📱 Telefone", value=telefone if telefone else "")
        foto_input = st.file_uploader("📸 Foto de perfil", type=["png", "jpg", "jpeg"])
 
        if st.button("Salvar Perfil"):
            caminho_foto = foto
 
            if foto_input:
                caminho_foto = f"foto_{email}.png"
                with open(caminho_foto, "wb") as f:
                    f.write(foto_input.read())
 
            c.execute("""
            UPDATE usuarios
            SET telefone=?, foto=?
            WHERE email=?
            """, (telefone_input, caminho_foto, email))
 
            conn.commit()
            st.success("Perfil atualizado!")
            st.rerun()
 
        if foto:
            st.image(foto, width=150)
 
# ------------------------------------------------------------
# --- 6. Análise de Dados ---
# ------------------------------------------------------------
elif menu == "📈 Análise de Dados":
    st.title("📈 Análise de Dados")
    st.subheader("Explore, visualize e entenda seus dados!")
 
 
    uploaded_file = st.file_uploader("📂 Envie um arquivo CSV para análise", type=["csv"])
 
 
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        # --- Visualização básica ---
        st.subheader("📄 Visualização das primeiras linhas")
        st.dataframe(df)
 
 
        st.subheader("📊 Estatísticas descritivas")
        st.dataframe(df.describe())
 
 
        st.subheader("📌 Informações do DataFrame")
        st.write(f"Linhas: {df.shape[0]}, Colunas: {df.shape[1]}")
        st.text(df.info())
 
 
        # --- Seleção de colunas numéricas ---
        numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
        if numeric_cols:
            st.subheader("🔹 Gráficos das colunas numéricas")
            col_to_plot = st.selectbox("Escolha a coluna para visualizar", numeric_cols)
 
 
            # Histograma
            st.write(f"📈 Histograma de **{col_to_plot}**")
            st.bar_chart(df[col_to_plot].value_counts().sort_index())
 
 
            # Boxplot
            st.write(f"📦 Boxplot de **{col_to_plot}**")
            st.box_chart(df[col_to_plot])
 
 
            # Dispersão (scatter) entre duas colunas numéricas
            st.subheader("📊 Gráfico de Dispersão")
            col_x = st.selectbox("Escolha o eixo X", numeric_cols, index=0)
            col_y = st.selectbox("Escolha o eixo Y", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)
            st.write(f"Scatter plot entre **{col_x}** e **{col_y}**")
            st.altair_chart(
                alt.Chart(df).mark_circle(size=60).encode(
                    x=col_x,
                    y=col_y,
                    tooltip=numeric_cols
                ).interactive(),
                use_container_width=True
            )
 
 
            # Correlação
            st.subheader("📌 Matriz de Correlação")
            st.dataframe(df[numeric_cols].corr())
        else:
            st.info("Nenhuma coluna numérica encontrada para análise e gráficos.")
 
 
#-----------------------------------------------------------------------
#pandas avançado
# ----------------------------------------------------------------------            
 
elif menu == "📊 Pandas Avançado":
 
    st.title("📊 Pandas Avançado")
    st.subheader("Manipulação e análise de dados como um profissional")
 
    st.markdown("---")
 
    # 🎬 VÍDEO
    st.video("https://youtu.be/vmEHCJofslg")
 
    # 📖 INTRODUÇÃO
    st.header("📖 O que é Pandas?")
    st.write("""
Pandas é uma biblioteca usada para manipulação e análise de dados.
 
Com ela você pode:
- 📊 Ler arquivos (CSV, Excel)
- 🧹 Limpar dados
- 🔍 Filtrar informações
- 📈 Analisar dados
""")
 
    st.info("💡 Pandas é uma das ferramentas mais usadas em Ciência de Dados.")
 
    st.markdown("---")
 
    # 📂 IMPORTAÇÃO DE DADOS
    st.header("📂 Importando dados")
 
    st.code("""
import pandas as pd
df = pd.read_csv("dados.csv")
""")
 
    arquivo = st.file_uploader("Envie um CSV", type=["csv"])
 
    if arquivo:
        df = pd.read_csv(arquivo)
 
        st.subheader("📄 Dados carregados")
        st.dataframe(df)
 
        st.markdown("---")
 
        # 🔍 INFO
        st.header("🔍 Informações do DataFrame")
        st.write(f"Linhas: {df.shape[0]}")
        st.write(f"Colunas: {df.shape[1]}")
        st.dataframe(df.describe())
 
        st.markdown("---")
 
        # 🧹 LIMPEZA
        st.header("🧹 Limpeza de Dados")
 
        if st.button("Remover valores nulos"):
            df = df.dropna()
            st.success("Valores nulos removidos")
            st.dataframe(df)
 
        if st.button("Preencher nulos com média"):
            for col in df.select_dtypes(include="number"):
                df[col].fillna(df[col].mean(), inplace=True)
            st.success("Valores preenchidos")
            st.dataframe(df)
 
        st.warning("⚠️ Dados sujos geram análises erradas.")
 
        st.markdown("---")
 
        # 🔍 FILTRO
        st.header("🔍 Filtrando dados")
 
        colunas = df.columns.tolist()
        coluna = st.selectbox("Escolha uma coluna", colunas)
 
        valor = st.text_input("Digite valor para filtrar")
 
        if valor:
            filtrado = df[df[coluna].astype(str).str.contains(valor)]
            st.dataframe(filtrado)
 
        st.markdown("---")
 
        # 📊 AGRUPAMENTO
        st.header("📊 Agrupamento (GroupBy)")
 
        col_group = st.selectbox("Agrupar por", colunas)
        col_valor = st.selectbox("Coluna numérica", df.select_dtypes(include="number").columns)
 
        if st.button("Agrupar"):
            agrupado = df.groupby(col_group)[col_valor].mean()
            st.dataframe(agrupado)
 
        st.markdown("---")
 
        # 🔗 MERGE (TEORIA)
        st.header("🔗 Junção de dados (merge)")
 
        st.code("""
df_final = pd.merge(df1, df2, on="id")
""")
 
        st.write("""
O merge permite juntar duas tabelas com base em uma coluna em comum.
""")
 
        st.markdown("---")
 
        # 📈 VISUALIZAÇÃO
        st.header("📈 Visualização de dados")
 
        col_num = df.select_dtypes(include="number").columns
 
        if len(col_num) > 0:
            coluna_grafico = st.selectbox("Escolha coluna para gráfico", col_num)
 
            st.bar_chart(df[coluna_grafico])
            st.line_chart(df[coluna_grafico])
 
        st.markdown("---")
 
        # 📥 EXPORTAÇÃO
        st.header("📥 Exportar dados")
 
        csv = df.to_csv(index=False).encode("utf-8")
 
        st.download_button(
            "📥 Baixar CSV tratado",
            data=csv,
            file_name="dados_tratados.csv",
            mime="text/csv"
        )
 
    else:
        st.info("📂 Envie um arquivo CSV para começar")
 
    st.markdown("---")
 
    # 🎯 RESUMO
    st.header("🎯 Resumo")
 
    st.success("""
Você aprendeu:
- 📂 Importar dados
- 🧹 Limpar dados
- 🔍 Filtrar
- 📊 Agrupar
- 📈 Visualizar
- 📥 Exportar
 
🚀 Agora você domina o Pandas!
""")
 
# ------------------------------------------------------------
# --- ÁREA ADMIN (CORRETA)
# ------------------------------------------------------------
elif menu == "🔒 Área Admin":
 
    if st.session_state["logado"] != "admin":
        st.warning("🔒 Apenas admin pode acessar")
        st.stop()
 
    st.title("📊 Usuários cadastrados")
 
    c.execute("SELECT id, nome, email FROM usuarios")
    dados = c.fetchall()
 
    df = pd.DataFrame(dados, columns=["ID", "Nome", "Email"])
 
    st.metric("👤 Usuários", len(df))
 
    st.dataframe(df, use_container_width=True)
 
#---------------------------------------------------------------------
#python Basico
#---------------------------------------------------------------------
 
elif menu == "🐍 Python Básico":
 
    st.title("🐍 Python Básico")
    st.subheader("Aprenda os fundamentos da programação com Python")
 
    st.markdown("---")
 
    # 🎬 VÍDEO
    st.video("https://youtu.be/rfscVS0vtbw")
 
    # 📖 TEORIA
    st.header("📖 O que é Python?")
    st.write("""
Python é uma linguagem de programação simples e poderosa.
 
Ela é usada para:
- 📊 Ciência de Dados
- 🌐 Desenvolvimento Web
- 🤖 Inteligência Artificial
- 📈 Automação de tarefas
 
👉 É uma das linguagens mais usadas do mundo.
""")
 
    st.info("💡 Curiosidade: empresas como Google e Netflix usam Python.")
 
    st.markdown("---")
 
    # 🧠 VARIÁVEIS
    st.header("🧠 Variáveis")
 
    st.write("""
Variáveis servem para guardar informações na memória.
""")
 
    st.code("""
nome = "João"
idade = 20
altura = 1.75
""")
 
    nome = st.text_input("Digite seu nome:")
    if nome:
        st.success(f"Olá, {nome}!")
 
    st.warning("⚠️ Erro comum: esquecer as aspas em textos.")
 
    st.markdown("---")
 
    # 🔢 TIPOS DE DADOS
    st.header("🔢 Tipos de Dados")
 
    st.write("""
Os principais tipos são:
- int → números inteiros (10, 20)
- float → números decimais (1.5, 2.7)
- str → textos ("olá")
- bool → verdadeiro ou falso (True/False)
""")
 
    valor = st.text_input("Digite algo:")
    if valor:
        st.write(f"Tipo detectado: {type(valor)}")
 
    st.markdown("---")
 
    # 🖨️ PRINT
    st.header("🖨️ Exibindo informações (print)")
 
    st.code("""
print("Olá mundo!")
""")
 
    st.success("O comando print mostra informações na tela.")
 
    st.markdown("---")
 
    # ➕ OPERAÇÕES
    st.header("➕ Operações Matemáticas")
 
    a = st.number_input("Digite o primeiro número:", value=0)
    b = st.number_input("Digite o segundo número:", value=0)
 
    st.write(f"Soma: {a + b}")
    st.write(f"Subtração: {a - b}")
    st.write(f"Multiplicação: {a * b}")
    if b != 0:
        st.write(f"Divisão: {a / b}")
    else:
        st.warning("⚠️ Não é possível dividir por zero")
 
    st.markdown("---")
 
    # 🔀 CONDIÇÕES
    st.header("🔀 Condições (if/else)")
 
    numero = st.number_input("Digite um número para testar:", value=0)
 
    if numero > 0:
        st.success("Número positivo")
    elif numero < 0:
        st.error("Número negativo")
    else:
        st.info("Número é zero")
 
    st.code("""
if numero > 0:
    print("positivo")
else:
    print("negativo ou zero")
""")
 
    st.markdown("---")
 
    # 🔁 LAÇOS
    st.header("🔁 Laços de repetição (for)")
 
    st.code("""
for i in range(5):
    print(i)
""")
 
    if st.button("Mostrar contagem"):
        for i in range(5):
            st.write(i)
 
    st.markdown("---")
 
    # 📋 LISTAS
    st.header("📋 Listas")
 
    st.write("""
Listas armazenam vários valores:
""")
 
    st.code("""
lista = [1, 2, 3, 4]
""")
 
    lista = [1, 2, 3, 4]
    st.write(f"Lista: {lista}")
    st.write(f"Soma: {sum(lista)}")
 
    st.markdown("---")
 
    # 🎯 RESUMO
    st.header("🎯 Resumo Final")
 
    st.success("""
Você aprendeu:
- 🧠 Variáveis
- 🔢 Tipos de dados
- 🖨️ Print
- ➕ Operações
- 🔀 Condições
- 🔁 Laços
- 📋 Listas
 
🚀 Agora você já sabe o básico de Python!
""")
 
#--------------------------------------------------------------------
#Machine Learning
#--------------------------------------------------------------------
elif menu == "🤖 Machine Learning":
 
    st.title("🤖 Machine Learning")
    st.subheader("Aprenda a criar modelos que fazem previsões")
 
    st.markdown("---")
 
    # 🎬 VÍDEO
    st.video("https://youtu.be/GwIo3gDZCVQ")
 
    # 📖 INTRODUÇÃO
    st.header("📖 O que é Machine Learning?")
    st.write("""
Machine Learning (Aprendizado de Máquina) é uma área da Inteligência Artificial
que permite que sistemas aprendam com dados.
 
👉 Em vez de programar regras, você ensina o modelo com exemplos.
""")
 
    st.info("💡 Ex: Netflix recomendando filmes, Instagram mostrando posts, bancos detectando fraudes.")
 
    st.markdown("---")
 
    # 🧠 TIPOS
    st.header("🧠 Tipos de Machine Learning")
 
    st.write("""
- 📊 Supervisionado → aprende com dados rotulados
- 🔍 Não supervisionado → encontra padrões sozinho
- 🎮 Reforço → aprende com tentativa e erro
""")
 
    st.markdown("---")
 
    # 📊 EXEMPLO PRÁTICO
    st.header("📊 Exemplo: Previsão com Regressão Linear")
 
    st.write("""
Vamos criar um modelo que prevê valores com base em uma relação matemática.
""")
    # Dados fake
    x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
    y = np.array([2, 4, 6, 8, 10])
 
    modelo = LinearRegression()
    modelo.fit(x, y)
 
    valor = st.number_input("Digite um valor de entrada (X):", value=6)
 
    previsao = modelo.predict([[valor]])
 
    st.success(f"🔮 Previsão do modelo: {previsao[0]:.2f}")
 
    st.code("""
from sklearn.linear_model import LinearRegression
 
modelo = LinearRegression()
modelo.fit(x, y)
previsao = modelo.predict([[valor]])
""")
 
    st.markdown("---")
 
    # 📈 VISUALIZAÇÃO
    st.header("📈 Visualização do Modelo")
 
    df = pd.DataFrame({
        "X": x.flatten(),
        "Y": y
    })
 
    st.dataframe(df)
    st.line_chart(df)
 
    st.markdown("---")
 
    # 🧪 TESTE COM CSV
    st.header("🧪 Teste com seus próprios dados")
 
    arquivo = st.file_uploader("Envie um CSV com 2 colunas numéricas", type=["csv"])
 
    if arquivo:
        df_user = pd.read_csv(arquivo)
 
        st.dataframe(df_user)
 
        if len(df_user.columns) >= 2:
            col_x = df_user.columns[0]
            col_y = df_user.columns[1]
 
            X = df_user[[col_x]]
            Y = df_user[col_y]
 
            modelo2 = LinearRegression()
            modelo2.fit(X, Y)
 
            valor_user = st.number_input("Digite um valor para prever:", value=0.0)
 
            pred = modelo2.predict([[valor_user]])
 
            st.success(f"🔮 Previsão: {pred[0]:.2f}")
 
        else:
            st.error("O CSV precisa ter pelo menos 2 colunas")
 
    st.markdown("---")
 
    # ⚠️ CONCEITOS IMPORTANTES
    st.header("⚠️ Conceitos importantes")
 
    st.write("""
- Overfitting → modelo decora os dados
- Underfitting → modelo aprende pouco
- Treino vs Teste → separar dados
""")
 
    st.markdown("---")
 
    # 🎯 RESUMO
    st.header("🎯 Resumo")
 
    st.success("""
Você aprendeu:
- 🤖 O que é Machine Learning
- 🧠 Tipos de aprendizado
- 📊 Regressão Linear
- 🔮 Fazer previsões
- 📂 Usar seus próprios dados
 
🚀 Você já começou no mundo da IA!
""")
# ------------------------------------------------------------
# --- 7. Quiz ---
# ------------------------------------------------------------
elif menu == "❓ Quiz do Curso":
    st.title("❓ Quiz - Ciência de Dados com Python")
    st.subheader("Teste seus conhecimentos adquiridos no curso!")
 
 
    pontuacao = 0
    erros = []
 
 
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
