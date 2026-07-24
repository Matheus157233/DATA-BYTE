import streamlit as st
import pandas as pd
import numpy as np
import math
import altair as alt
import sqlite3
import re
import io
from datetime import datetime
from sklearn.linear_model import LinearRegression
try:
    from fpdf import FPDF
    FPDF_OK = True
except ImportError:
    FPDF_OK = False
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
try:
    c.execute("ALTER TABLE usuarios ADD COLUMN modulos_concluidos TEXT DEFAULT ''")
except:
    pass
try:
    c.execute("ALTER TABLE usuarios ADD COLUMN nota_quiz INTEGER DEFAULT -1")
except:
    pass
try:
    c.execute("ALTER TABLE usuarios ADD COLUMN data_cadastro TEXT")
except:
    pass
c.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    senha TEXT,
    telefone TEXT,
    foto TEXT,
    modulos_concluidos TEXT DEFAULT '',
    nota_quiz INTEGER DEFAULT -1,
    data_cadastro TEXT
)
""")
conn.commit()

# Lista oficial de módulos do curso (usada para calcular progresso real)
MODULOS_CURSO = [
    "Introdução à Ciência de Dados",
    "Python Básico",
    "Funções Python",
    "Operações com Listas",
    "Limpeza de Dados",
    "Limpeza de CSV (Profissional)",
    "Pandas Avançado",
    "Análise de Dados",
    "Módulo Avançado Interativo",
    "Machine Learning",
    "Ética e Privacidade de Dados (LGPD)",
]

def marcar_modulo_concluido(nome_modulo):
    """Marca um módulo como concluído para o usuário logado e persiste no banco."""
    email = st.session_state.get("email")
    if not email:
        return
    c.execute("SELECT modulos_concluidos FROM usuarios WHERE email=?", (email,))
    row = c.fetchone()
    atuais = set(filter(None, (row[0] or "").split("|"))) if row else set()
    if nome_modulo not in atuais:
        atuais.add(nome_modulo)
        novos = "|".join(atuais)
        c.execute("UPDATE usuarios SET modulos_concluidos=? WHERE email=?", (novos, email))
        conn.commit()
        if nome_modulo not in st.session_state.badges:
            st.session_state.badges.append(nome_modulo)
    st.session_state.modulos_concluidos = atuais

def carregar_progresso():
    """Carrega do banco quantos módulos o usuário já concluiu."""
    email = st.session_state.get("email")
    if not email:
        return set()
    c.execute("SELECT modulos_concluidos FROM usuarios WHERE email=?", (email,))
    row = c.fetchone()
    return set(filter(None, (row[0] or "").split("|"))) if row else set()

def gerar_certificado_pdf(nome_aluno, nota=None):
    """Gera um certificado de conclusão em PDF (usa fpdf2, biblioteca leve e sem dependências externas)."""
    if not FPDF_OK:
        return None
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_fill_color(14, 17, 23)
    pdf.rect(0, 0, 297, 210, "F")
    pdf.set_draw_color(0, 198, 255)
    pdf.set_line_width(1.5)
    pdf.rect(10, 10, 277, 190)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 30)
    pdf.ln(25)
    pdf.cell(0, 15, "CERTIFICADO DE CONCLUSAO", align="C")
    pdf.ln(20)
    pdf.set_font("Helvetica", "", 16)
    pdf.cell(0, 10, "Curso de Introducao a Ciencia de Dados com Python", align="C")
    pdf.ln(20)
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(0, 198, 255)
    nome_limpo = nome_aluno.encode("latin-1", "replace").decode("latin-1")
    pdf.cell(0, 12, nome_limpo, align="C")
    pdf.ln(15)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "", 13)
    texto = "concluiu com sucesso o curso, demonstrando dominio dos fundamentos de Python, Pandas e Ciencia de Dados."
    if nota is not None:
        texto += f" Nota final no quiz: {nota}/10."
    pdf.multi_cell(0, 8, texto, align="C")
    pdf.ln(10)
    pdf.set_font("Helvetica", "I", 11)
    pdf.cell(0, 10, f"Emitido em {datetime.now().strftime('%d/%m/%Y')}", align="C")
    out = pdf.output()
    if isinstance(out, str):
        out = out.encode("latin-1")
    return bytes(out)

def botao_concluir_modulo(nome_modulo):
    """Renderiza o botão padrão de 'marcar módulo como concluído' no fim de cada aba."""
    concluidos = st.session_state.get("modulos_concluidos", set())
    st.markdown("---")
    if nome_modulo in concluidos:
        st.success(f"✅ Módulo **{nome_modulo}** concluído! Continue para o próximo.")
    else:
        if st.button(f"🏁 Marcar '{nome_modulo}' como concluído", key=f"concluir_{nome_modulo}"):
            marcar_modulo_concluido(nome_modulo)
            st.balloons()
            st.rerun()
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
if "modulos_concluidos" not in st.session_state:
    st.session_state.modulos_concluidos = set()
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
                st.session_state.modulos_concluidos = carregar_progresso()
                st.session_state.badges = list(st.session_state.modulos_concluidos)
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
            c.execute(
                "INSERT INTO usuarios (nome, email, senha, data_cadastro) VALUES (?, ?, ?, ?)",
                (nome, email, senha, datetime.now().strftime("%Y-%m-%d %H:%M")),
            )
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
    """Aplica o tema Claro/Escuro em toda a interface (não só no <body>, que o
    Streamlit sobrescreve por padrão — por isso o botão de tema parecia não funcionar)."""
    if st.session_state.tema == "Escuro":
        bg_app, bg_card, bg_sidebar = "#0e1117", "#1c1f26", "#12151b"
        texto, borda = "#f5f5f5", "#2b2f38"
    else:
        bg_app, bg_card, bg_sidebar = "#ffffff", "#f7f9fc", "#eef1f6"
        texto, borda = "#1a1a1a", "#dfe3e8"

    st.markdown(f"""
<style>
.stApp {{
    background-color: {bg_app};
    color: {texto};
}}
section[data-testid="stSidebar"] {{
    background-color: {bg_sidebar};
}}
section[data-testid="stSidebar"] * {{
    color: {texto} !important;
}}
.stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp p, .stApp li, .stApp span, .stApp label {{
    color: {texto};
}}
[data-testid="stMetricValue"], [data-testid="stMetricLabel"] {{
    color: {texto} !important;
}}
div[data-testid="stDataFrame"], .stTabs {{
    background-color: {bg_card};
    border-radius: 10px;
}}
div[data-testid="stExpander"] {{
    background-color: {bg_card};
    border: 1px solid {borda};
    border-radius: 10px;
}}
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
    border: none;
    transition: transform 0.15s ease;
}
.stButton>button:hover {
    transform: translateY(-2px);
    filter: brightness(1.08);
}
.stTextInput>div>div>input {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)
# ------------------------------------------------------------
# MENU LATERAL (NAVBAR) — agora organizado em trilha lógica por categoria
# ------------------------------------------------------------
st.sidebar.title("📚 " + t("Menu do Curso", "Course Menu"))
st.sidebar.image(
    "https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif",
    use_column_width=True
)

CATEGORIAS_MENU = {
    t("🏠 Início", "🏠 Home"): ["🏠 Página Inicial", "🎯 Sobre o Projeto"],
    t("🐍 Fundamentos", "🐍 Fundamentals"): ["🐍 Python Básico", "🧠 Funções Python", "📂 Operações com Listas"],
    t("📊 Ciência de Dados", "📊 Data Science"): [
        "🧩 Introdução à Ciência de Dados", "📊 Limpeza de Dados",
        "🧹 Limpeza de CSV (Profissional)", "📊 Pandas Avançado", "📈 Análise de Dados",
    ],
    t("⚡ Prática Avançada", "⚡ Advanced Practice"): ["⚡ Módulo Avançado Interativo", "🤖 Machine Learning"],
    t("⚖️ Cidadania Digital", "⚖️ Digital Citizenship"): ["⚖️ Ética e Dados (LGPD)"],
    t("❓ Avaliação", "❓ Assessment"): ["❓ Quiz do Curso"],
    t("👤 Conta", "👤 Account"): ["👤 Perfil"] + (["🔒 Área Admin"] if st.session_state["logado"] == "admin" else []),
}

categoria_selecionada = st.sidebar.selectbox(t("Categoria", "Category"), list(CATEGORIAS_MENU.keys()))
menu = st.sidebar.radio(t("Navegue entre as seções:", "Navigate the sections:"), CATEGORIAS_MENU[categoria_selecionada])

# Agora os controles de tema e idioma (com índice correto — antes eles "resetavam" a cada clique)
st.sidebar.markdown("### ⚙️ " + t("Preferências", "Preferences"))
st.session_state.tema = st.sidebar.selectbox(
    "🌗 " + t("Tema", "Theme"),
    ["Claro", "Escuro"],
    index=0 if st.session_state.tema == "Claro" else 1
)
st.session_state.idioma = st.sidebar.selectbox(
    "🌎 " + t("Idioma", "Language"),
    ["PT", "EN"],
    index=0 if st.session_state.idioma == "PT" else 1
)
st.sidebar.markdown("---")

concluidos_sb = st.session_state.get("modulos_concluidos", set())
progresso_pct = int(100 * len(concluidos_sb) / len(MODULOS_CURSO)) if MODULOS_CURSO else 0
st.session_state.progresso = progresso_pct
st.sidebar.progress(progresso_pct / 100)
st.sidebar.caption(f"📈 {t('Progresso do curso', 'Course progress')}: {progresso_pct}% ({len(concluidos_sb)}/{len(MODULOS_CURSO)})")
st.sidebar.info("💡 " + t("Dica: explore cada módulo em ordem para aproveitar melhor o conteúdo!",
                          "Tip: go through each module in order to get the most out of the content!"))
# ------------------------------------------------------------
# --- 0. PÁGINA INICIAL ---
# ------------------------------------------------------------
if menu == "🏠 Página Inicial":
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📚 " + t("Módulos", "Modules"), str(len(MODULOS_CURSO)))
    col2.metric("⏱ " + t("Tempo", "Time"), "3h+")
    col3.metric("📊 " + t("Progresso", "Progress"), f"{st.session_state.progresso}%")
    col4.metric("🏅 " + t("Badges", "Badges"), str(len(st.session_state.get("modulos_concluidos", set()))))

    st.markdown("<h1 class='main-title'>🚀 " + t(
        "Curso Completo de Introdução à Ciência de Dados com Python",
        "Complete Introduction to Data Science with Python"
    ) + "</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>" + t(
        "Do zero à prática — entenda, limpe, analise e visualize dados com Python!",
        "From zero to practice — understand, clean, analyze and visualize data with Python!"
    ) + "</p>", unsafe_allow_html=True)
    st.markdown("---")

    st.progress(st.session_state.progresso / 100)
    st.caption(t(
        f"Você já concluiu {len(st.session_state.get('modulos_concluidos', set()))} de {len(MODULOS_CURSO)} módulos.",
        f"You have completed {len(st.session_state.get('modulos_concluidos', set()))} of {len(MODULOS_CURSO)} modules."
    ))

    st.image("https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif", width=300)
    st.header("📖 " + t("Sobre o Curso", "About the Course"))
    st.write(t("""
Este curso foi desenvolvido para **introduzir você à Ciência de Dados**, combinando **teoria e prática** em um ambiente interativo com Python.
Você aprenderá:
- 🧮 Conceitos fundamentais de Ciência de Dados
- 🐍 Programação prática em Python
- 📊 Limpeza e manipulação de dados com Pandas e Numpy
- 💡 Funções e estruturas de dados em Python
- ⚖️ Ética e privacidade no uso de dados (LGPD)
- ⚡ Interatividade com Streamlit
""", """
This course was designed to **introduce you to Data Science**, combining **theory and practice** in an interactive Python environment.
You will learn:
- 🧮 Fundamental Data Science concepts
- 🐍 Practical Python programming
- 📊 Data cleaning and manipulation with Pandas and Numpy
- 💡 Functions and data structures in Python
- ⚖️ Data ethics and privacy (LGPD)
- ⚡ Interactivity with Streamlit
"""))
    st.video("https://youtu.be/cm_tM0m9zcI")
    st.header("🎯 " + t("Objetivo do Curso", "Course Objective"))
    st.write(t("""
Ao final deste curso, você será capaz de:
- Compreender os **fundamentos da análise de dados**
- Criar e limpar **DataFrames**
- Escrever **funções eficientes**
- Trabalhar com **listas e estruturas dinâmicas**
- Construir **projetos interativos com Streamlit**
""", """
By the end of this course, you will be able to:
- Understand the **fundamentals of data analysis**
- Create and clean **DataFrames**
- Write **efficient functions**
- Work with **lists and dynamic data structures**
- Build **interactive projects with Streamlit**
"""))
    st.info("👉 " + t(
        "Quer entender por que este curso existe e qual problema ele ajuda a resolver? Veja a aba **🎯 Sobre o Projeto**.",
        "Want to understand why this course exists and what problem it helps solve? Check the **🎯 About the Project** tab."
    ))
    st.success("✅ " + t("Clique no menu lateral para iniciar sua jornada!", "Click the sidebar menu to start your journey!"))

# ------------------------------------------------------------
# --- SOBRE O PROJETO (o problema social que o curso combate) ---
# ------------------------------------------------------------
elif menu == "🎯 Sobre o Projeto":
    st.title("🎯 " + t("Sobre o Projeto", "About the Project"))
    st.subheader(t(
        "Um curso gratuito de Ciência de Dados para combater a exclusão digital e o descompasso entre mercado de trabalho e formação",
        "A free Data Science course to fight digital exclusion and the gap between the job market and education"
    ))
    st.markdown("---")

    st.header("🧩 " + t("O problema", "The problem"))
    st.write(t("""
O Brasil forma muito menos profissionais de dados do que o mercado precisa, e a maior parte dos cursos de
qualidade nessa área é **paga e concentrada nos grandes centros urbanos**. Quem estuda em escola pública,
mora longe das capitais ou não tem condições de pagar um curso, fica de fora — mesmo sendo essa uma das
áreas que mais cresce em vagas de emprego no mundo todo.

Isso é um problema de **exclusão digital e desigualdade educacional**: o acesso à tecnologia deveria ser
um direito, não um privilégio.
""", """
Brazil trains far fewer data professionals than the market needs, and most quality courses in this field
are **paid and concentrated in big cities**. Students from public schools, people who live far from major
cities, or those who can't afford a paid course are left out — even though this is one of the
fastest-growing job fields in the world.

This is a problem of **digital exclusion and educational inequality**: access to technology should be a
right, not a privilege.
"""))

    col1, col2, col3 = st.columns(3)
    col1.metric("🇧🇷 " + t("Vagas em aberto na área de dados", "Open data-related jobs"), t("Milhares", "Thousands"))
    col2.metric("💰 " + t("Custo médio de cursos pagos", "Avg. cost of paid courses"), "R$ 800+")
    col3.metric("🆓 " + t("Custo deste curso", "Cost of this course"), t("Gratuito", "Free"))

    st.markdown("---")
    st.header("💡 " + t("Nossa solução", "Our solution"))
    st.write(t("""
Este é um curso **100% gratuito, em português, sem pré-requisitos**, que qualquer estudante pode acessar
com um computador simples e internet. Ele foi criado para ser o **primeiro passo** de alguém que nunca
programou na vida e quer entrar na área de dados.

O que o torna diferente de só "ler sobre o assunto":
- 🧑‍🏫 Teoria explicada em linguagem simples, sem jargão desnecessário
- ⌨️ Exercícios práticos dentro do próprio navegador, sem precisar instalar nada
- 🏅 Sistema de progresso e badges, para acompanhar sua evolução
- 📜 Certificado de conclusão, um item real para colocar no currículo ou LinkedIn
- ⚖️ Um módulo dedicado a ética e privacidade de dados (LGPD), formando não só técnicos, mas cidadãos digitais conscientes
""", """
This is a **100% free course, with no prerequisites**, that any student can access with a simple computer
and internet connection. It was built to be the **first step** for someone who has never coded before and
wants to break into the data field.

What makes it different from just "reading about the topic":
- 🧑‍🏫 Theory explained in plain language, no unnecessary jargon
- ⌨️ Practical exercises right in the browser, no installation needed
- 🏅 Progress and badge system, to track your evolution
- 📜 Certificate of completion, a real item to add to your résumé or LinkedIn
- ⚖️ A dedicated module on data ethics and privacy (LGPD), forming not just technicians but conscious digital citizens
"""))

    st.markdown("---")
    st.header("👥 " + t("Para quem é este curso", "Who this course is for"))
    st.write(t("""
- Estudantes de escolas públicas curiosos sobre tecnologia
- Pessoas em transição de carreira que não podem pagar por um curso
- Qualquer pessoa que queira entender melhor o mundo dos dados, mesmo sem virar programador
""", """
- Public school students curious about technology
- People changing careers who can't afford a paid course
- Anyone who wants to better understand the world of data, even without becoming a programmer
"""))
    st.success("🚀 " + t(
        "Cada módulo concluído é um passo a mais rumo a mais oportunidades — para você e para quem vier depois de você.",
        "Every module you complete is one more step toward more opportunities — for you and for whoever comes after you."
    ))

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

    with st.expander("📚 Teoria completa: as etapas de um projeto de Ciência de Dados"):
        st.markdown("""
Todo projeto de Ciência de Dados costuma seguir um ciclo parecido, independente da área de aplicação:

1. **Coleta** — reunir os dados (planilhas, bancos de dados, formulários, sensores, APIs).
2. **Limpeza** — tratar valores ausentes, duplicados e inconsistentes (você verá isso no módulo *Limpeza de Dados*).
3. **Exploração (EDA)** — entender o que os dados dizem através de estatísticas e gráficos.
4. **Modelagem** — quando aplicável, treinar um modelo para prever ou classificar algo (módulo *Machine Learning*).
5. **Comunicação** — transformar o resultado técnico em uma conclusão que outras pessoas entendam.

Um erro comum de quem está começando é pular direto para a modelagem, sem entender bem os dados —
por isso a limpeza e a exploração ocupam a maior parte do tempo de um profissional de dados no dia a dia
(estimativas de mercado apontam até 70-80% do tempo em tarefas de preparação de dados).
""")

    botao_concluir_modulo("Introdução à Ciência de Dados")

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

    with st.expander("📚 Teoria completa: por que dados sujos quebram análises"):
        st.markdown("""
**Dados sujos** são a causa mais comum de conclusões erradas em Ciência de Dados. Alguns problemas típicos:

- **Valores ausentes (`NaN`)**: podem distorcer médias e somas se não forem tratados.
- **Duplicatas**: contam a mesma informação mais de uma vez, inflando resultados.
- **Tipos incorretos**: uma coluna de números lida como texto impede cálculos.
- **Inconsistência de categorias**: "SP", "São Paulo" e "sao paulo" sendo tratados como três valores diferentes.

A regra prática do mercado é conhecida como *"Garbage in, garbage out"*: nenhum modelo, por mais sofisticado
que seja, corrige um problema causado por dados de má qualidade na entrada.
""")

    botao_concluir_modulo("Limpeza de Dados")

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
    botao_concluir_modulo("Limpeza de CSV (Profissional)")
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

    with st.expander("📚 Teoria completa: parâmetros, retorno e reutilização"):
        st.markdown("""
- **Parâmetros** são as "entradas" de uma função — podem ter valores padrão (`def saudacao(nome="visitante")`).
- **`return`** devolve um valor para quem chamou a função; sem ele, a função devolve `None`.
- Funções bem escritas fazem **uma coisa só** e têm nomes que dizem o que fazem — isso é chamado de
  princípio da responsabilidade única, e facilita muito encontrar erros depois.
- Reutilizar funções evita repetir código (o princípio *DRY — Don't Repeat Yourself*).
""")

    botao_concluir_modulo("Funções Python")

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

    with st.expander("📚 Teoria completa: listas no dia a dia da Ciência de Dados"):
        st.markdown("""
Listas são a base de estruturas mais avançadas usadas depois no curso, como colunas de um **DataFrame** do Pandas.

Operações comuns:
- `lista.append(x)` — adiciona um item ao final
- `lista[0]` — acessa o primeiro item (índices começam em 0!)
- `lista[-1]` — acessa o último item
- `sorted(lista)` — retorna a lista ordenada
- List comprehension: `[x*2 for x in lista]` — cria uma nova lista transformando cada item
""")

    botao_concluir_modulo("Operações com Listas")

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
    botao_concluir_modulo("Módulo Avançado Interativo")

# ------------------------------------------------------------
# --- PERFIL DO USUÁRIO
# ------------------------------------------------------------
elif menu == "👤 Perfil":
    st.title("👤 Meu Perfil")
    email = st.session_state.get("email")
    c.execute("SELECT nome, email, telefone, foto, nota_quiz FROM usuarios WHERE email=?", (email,))
    user = c.fetchone()

    concluidos = st.session_state.get("modulos_concluidos", set())
    progresso_perfil = int(100 * len(concluidos) / len(MODULOS_CURSO)) if MODULOS_CURSO else 0

    col1, col2 = st.columns([2, 1])
    with col1:
        if user:
            nome, email, telefone, foto, nota_quiz_db = user
            st.subheader(f"Olá, {nome}! 👋")
            st.write(f"📧 **Email:** {email}")
        st.progress(progresso_perfil / 100)
        st.caption(f"Progresso geral: {progresso_perfil}% ({len(concluidos)}/{len(MODULOS_CURSO)} módulos)")
    with col2:
        if user and foto:
            st.image(foto, width=140)

    st.markdown("---")
    st.header("🏅 Conquistas")
    if concluidos:
        badge_cols = st.columns(3)
        for i, badge in enumerate(sorted(concluidos)):
            with badge_cols[i % 3]:
                st.success(f"🏅 {badge}")
    else:
        st.info("Você ainda não concluiu nenhum módulo. Marque um módulo como concluído para ganhar seu primeiro badge!")

    st.markdown("---")
    st.header("📜 Certificado de conclusão")
    if progresso_perfil == 100:
        st.success("🎉 Parabéns! Você concluiu todos os módulos do curso!")
        if FPDF_OK:
            pdf_bytes = gerar_certificado_pdf(nome if user else email, nota=nota_quiz_db if user and nota_quiz_db and nota_quiz_db >= 0 else None)
            st.download_button(
                "📥 Baixar meu certificado (PDF)",
                data=pdf_bytes,
                file_name=f"certificado_{(nome if user else 'aluno').replace(' ', '_')}.pdf",
                mime="application/pdf",
            )
        else:
            st.warning("Instale a biblioteca `fpdf2` (`pip install fpdf2`) para habilitar o download do certificado em PDF.")
    else:
        st.info(f"Complete os {len(MODULOS_CURSO)} módulos do curso para desbloquear seu certificado. Faltam {len(MODULOS_CURSO) - len(concluidos)} módulo(s).")

    st.markdown("---")
    st.header("⚙️ Editar dados")
    if user:
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
        buffer_info = io.StringIO()
        df.info(buf=buffer_info)
        st.text(buffer_info.getvalue())

        # --- Seleção de colunas numéricas ---
        numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
        if numeric_cols:
            st.subheader("🔹 Gráficos das colunas numéricas")
            col_to_plot = st.selectbox("Escolha a coluna para visualizar", numeric_cols)

            # Histograma
            st.write(f"📈 Histograma de **{col_to_plot}**")
            st.bar_chart(df[col_to_plot].value_counts().sort_index())

            # Boxplot (st.box_chart não existe no Streamlit — corrigido usando Altair)
            st.write(f"📦 Boxplot de **{col_to_plot}**")
            st.altair_chart(
                alt.Chart(df).mark_boxplot(size=60).encode(y=col_to_plot),
                use_container_width=True,
            )

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

    botao_concluir_modulo("Análise de Dados")

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
    botao_concluir_modulo("Pandas Avançado")
# ------------------------------------------------------------
# --- ÁREA ADMIN (CORRETA)
# ------------------------------------------------------------
elif menu == "🔒 Área Admin":
    if st.session_state["logado"] != "admin":
        st.warning("🔒 Apenas admin pode acessar")
        st.stop()

    st.title("📊 Painel de Impacto")
    st.caption("Métricas que mostram o alcance real do projeto — quantas pessoas ele está ajudando a capacitar.")

    c.execute("SELECT id, nome, email, modulos_concluidos, nota_quiz, data_cadastro FROM usuarios")
    dados = c.fetchall()
    df_admin = pd.DataFrame(dados, columns=["ID", "Nome", "Email", "ModulosConcluidos", "NotaQuiz", "DataCadastro"])

    total_usuarios = len(df_admin)
    df_admin["QtdModulos"] = df_admin["ModulosConcluidos"].fillna("").apply(lambda x: len([m for m in x.split("|") if m]))
    concluiram_curso = int((df_admin["QtdModulos"] >= len(MODULOS_CURSO)).sum())
    notas_validas = df_admin.loc[df_admin["NotaQuiz"].fillna(-1) >= 0, "NotaQuiz"]
    nota_media = round(notas_validas.mean(), 1) if len(notas_validas) > 0 else 0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("👤 Alunos cadastrados", total_usuarios)
    col2.metric("🎓 Concluíram o curso", concluiram_curso)
    col3.metric("📈 Taxa de conclusão", f"{int(100*concluiram_curso/total_usuarios) if total_usuarios else 0}%")
    col4.metric("📝 Nota média no quiz", f"{nota_media}/10")

    st.markdown("---")
    st.subheader("📅 Cadastros ao longo do tempo")
    if df_admin["DataCadastro"].notna().any():
        df_datas = df_admin.dropna(subset=["DataCadastro"]).copy()
        df_datas["Data"] = pd.to_datetime(df_datas["DataCadastro"], errors="coerce").dt.date
        contagem = df_datas.groupby("Data").size().reset_index(name="Cadastros")
        st.bar_chart(contagem.set_index("Data"))
    else:
        st.info("Ainda não há dados de data de cadastro suficientes para o gráfico.")

    st.markdown("---")
    st.subheader("👥 Usuários cadastrados")
    st.dataframe(df_admin[["ID", "Nome", "Email", "QtdModulos", "NotaQuiz", "DataCadastro"]], use_container_width=True)
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

    with st.expander("📚 Teoria completa: por que Python é a linguagem mais usada em dados"):
        st.markdown("""
Python virou o padrão de fato em Ciência de Dados por alguns motivos:

- **Sintaxe simples**, próxima do inglês, o que reduz a barreira de entrada para iniciantes.
- **Ecossistema maduro**: bibliotecas como Pandas, NumPy, Scikit-learn e Matplotlib cobrem praticamente
  todo o fluxo de um projeto de dados.
- **Comunidade enorme**: praticamente qualquer erro que você encontrar, alguém já perguntou e respondeu
  publicamente antes.
- **Interoperabilidade**: Python conversa bem com bancos de dados, APIs, planilhas e até com outras
  linguagens (C, Java) quando é preciso mais performance.
""")

    botao_concluir_modulo("Python Básico")
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

    with st.expander("📚 Teoria completa: como um modelo realmente aprende"):
        st.markdown("""
Por trás da Regressão Linear que você testou acima, o modelo busca a reta `y = a*x + b` que **minimiza o erro**
entre a previsão e o valor real — esse processo se chama **otimização**, e o critério mais comum é o
**erro quadrático médio (MSE)**.

Outros pontos importantes para ir além da Regressão Linear:
- **Classificação vs Regressão**: regressão prevê números (preço, temperatura); classificação prevê categorias (spam/não-spam).
- **Métricas de avaliação**: acurácia, precisão, recall (classificação) e MSE, R² (regressão).
- **Validação cruzada**: testar o modelo em vários pedaços diferentes dos dados, para garantir que ele generaliza bem.
- Nem todo problema de dados precisa de Machine Learning — muitas vezes uma boa análise estatística já responde a pergunta.
""")

    botao_concluir_modulo("Machine Learning")

# ------------------------------------------------------------
# --- ÉTICA E PRIVACIDADE DE DADOS (LGPD) ---
# ------------------------------------------------------------
elif menu == "⚖️ Ética e Dados (LGPD)":
    st.title("⚖️ Ética e Privacidade de Dados")
    st.subheader("Ciência de Dados também é sobre responsabilidade")
    st.markdown("---")

    st.header("📖 Por que isso importa?")
    st.write("""
Trabalhar com dados significa, quase sempre, trabalhar com **informações sobre pessoas reais**: nomes,
endereços, hábitos de consumo, localização, saúde. Um profissional de dados responsável precisa saber
**o que pode e o que não pode** ser feito com essas informações — não só por lei, mas por respeito a quem
está do outro lado dos dados.
""")

    st.header("📜 O que é a LGPD?")
    st.write("""
A **Lei Geral de Proteção de Dados (Lei nº 13.709/2018)** é a legislação brasileira que regula como
empresas e pessoas podem coletar, armazenar e usar dados pessoais. Alguns princípios centrais:

- **Finalidade**: os dados só podem ser usados para o propósito informado no momento da coleta.
- **Consentimento**: em geral, a pessoa precisa autorizar o uso dos seus dados.
- **Minimização**: coletar apenas os dados realmente necessários — nunca "por via das dúvidas".
- **Direito ao esquecimento**: a pessoa pode pedir a exclusão dos seus dados.
""")

    st.info("💡 Este próprio curso segue esse princípio: pedimos telefone e foto apenas para o cadastro do curso, e não compartilhamos com terceiros.")

    st.header("🕵️ Anonimização e dados sensíveis")
    st.write("""
Duas técnicas comuns para proteger a privacidade em uma análise de dados:

- **Anonimização**: remover ou embaralhar identificadores (nome, CPF, e-mail) para que a pessoa não possa
  mais ser identificada nos dados.
- **Agregação**: mostrar apenas totais e médias (ex: "idade média dos alunos"), nunca o dado individual de cada pessoa.

Já dados **sensíveis** (saúde, orientação sexual, religião, dados de crianças) exigem cuidado redobrado —
mesmo anonimizados, o vazamento desse tipo de informação pode causar dano real a alguém.
""")

    with st.expander("📚 Teoria completa: vieses em dados e modelos"):
        st.markdown("""
Além da privacidade, um cientista de dados responsável também se preocupa com **viés (bias)**: se os dados
usados para treinar um modelo refletem desigualdades já existentes na sociedade (por exemplo, histórico de
contratações que favoreceu um grupo específico), o modelo pode **repetir e até amplificar** essa
desigualdade nas suas previsões.

Por isso, antes de confiar cegamente em um modelo, vale perguntar:
- De onde vieram esses dados?
- Que grupos podem estar sub-representados nessa amostra?
- As previsões afetam pessoas de forma desigual?
""")

    st.success("🎯 Um bom profissional de dados não é só quem sabe programar — é quem usa dados com responsabilidade.")
    botao_concluir_modulo("Ética e Privacidade de Dados (LGPD)")

# ------------------------------------------------------------
# --- 7. Quiz ---
# ------------------------------------------------------------
elif menu == "❓ Quiz do Curso":
    st.markdown("""
<style>
.quiz-card {
    background: linear-gradient(135deg, #1c1f26 0%, #262b35 100%);
    border: 1px solid #333a46;
    border-radius: 16px;
    padding: 26px 30px;
    margin: 10px 0 20px 0;
}
.quiz-card * { color: #f5f5f5 !important; }
.quiz-progress-label {
    font-size: 0.85rem;
    opacity: 0.8;
    margin-bottom: 6px;
}
.quiz-score-circle {
    text-align: center;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

    QUIZ_PERGUNTAS = [
        {"pergunta": "O que é Ciência de Dados?",
         "opcoes": ["Apenas criar gráficos", "A união de estatística, programação e análise de dados", "Somente mexer em planilhas"],
         "correta": "A união de estatística, programação e análise de dados"},
        {"pergunta": "Qual biblioteca é usada para DataFrames?",
         "opcoes": ["NumPy", "Pandas", "Math"], "correta": "Pandas"},
        {"pergunta": "O que faz a função print()?",
         "opcoes": ["Mostra mensagens na tela", "Apaga dados", "Fecha o programa"], "correta": "Mostra mensagens na tela"},
        {"pergunta": "Qual comando remove valores nulos?",
         "opcoes": ["df.remove()", "df.dropna()", "df.fillna()"], "correta": "df.dropna()"},
        {"pergunta": "Qual palavra define uma função?",
         "opcoes": ["lambda", "def", "func"], "correta": "def"},
        {"pergunta": "O que significa o operador ** em Python?",
         "opcoes": ["Multiplicação simples", "Potência (elevação a um número)", "Divisão inteira"],
         "correta": "Potência (elevação a um número)"},
        {"pergunta": "O que faz o comando df.describe()?",
         "opcoes": ["Apaga colunas do DataFrame", "Mostra estatísticas descritivas", "Adiciona novas linhas"],
         "correta": "Mostra estatísticas descritivas"},
        {"pergunta": "Qual dessas opções NÃO é uma biblioteca de dados em Python?",
         "opcoes": ["Pandas", "NumPy", "HTML"], "correta": "HTML"},
        {"pergunta": "Qual comando é usado para importar bibliotecas em Python?",
         "opcoes": ["load", "import", "include"], "correta": "import"},
        {"pergunta": "O que é um DataFrame?",
         "opcoes": ["Um tipo de gráfico de barras", "Uma tabela de dados bidimensional do Pandas", "Uma função do NumPy"],
         "correta": "Uma tabela de dados bidimensional do Pandas"},
    ]
    total_perguntas = len(QUIZ_PERGUNTAS)

    if "quiz_indice" not in st.session_state:
        st.session_state.quiz_indice = 0
    if "quiz_respostas" not in st.session_state:
        st.session_state.quiz_respostas = {}
    if "quiz_finalizado" not in st.session_state:
        st.session_state.quiz_finalizado = False

    st.title("❓ Quiz - Ciência de Dados com Python")
    st.caption("Teste seus conhecimentos adquiridos no curso!")

    if not st.session_state.quiz_finalizado:
        idx = st.session_state.quiz_indice
        pergunta = QUIZ_PERGUNTAS[idx]

        st.progress(idx / total_perguntas)
        st.markdown(f"<div class='quiz-progress-label'>Pergunta {idx + 1} de {total_perguntas}</div>", unsafe_allow_html=True)

        st.markdown("<div class='quiz-card'>", unsafe_allow_html=True)
        resposta_salva = st.session_state.quiz_respostas.get(idx)
        indice_padrao = pergunta["opcoes"].index(resposta_salva) if resposta_salva in pergunta["opcoes"] else 0
        resposta = st.radio(
            f"**{idx + 1}. {pergunta['pergunta']}**",
            pergunta["opcoes"],
            index=indice_padrao,
            key=f"quiz_q_{idx}",
        )
        st.markdown("</div>", unsafe_allow_html=True)

        col_a, col_b = st.columns(2)
        with col_a:
            if idx > 0 and st.button("⬅️ Anterior", use_container_width=True):
                st.session_state.quiz_respostas[idx] = resposta
                st.session_state.quiz_indice -= 1
                st.rerun()
        with col_b:
            rotulo_botao = "Finalizar ✅" if idx == total_perguntas - 1 else "Próxima ➡️"
            if st.button(rotulo_botao, use_container_width=True):
                st.session_state.quiz_respostas[idx] = resposta
                if idx == total_perguntas - 1:
                    st.session_state.quiz_finalizado = True
                else:
                    st.session_state.quiz_indice += 1
                st.rerun()
    else:
        respostas = st.session_state.quiz_respostas
        pontuacao = sum(1 for i, p in enumerate(QUIZ_PERGUNTAS) if respostas.get(i) == p["correta"])
        erros = [p["pergunta"] for i, p in enumerate(QUIZ_PERGUNTAS) if respostas.get(i) != p["correta"]]

        email = st.session_state.get("email")
        if email:
            c.execute("UPDATE usuarios SET nota_quiz=? WHERE email=?", (pontuacao, email))
            conn.commit()
        st.session_state.nota_quiz = pontuacao

        pct = int(100 * pontuacao / total_perguntas)
        cor = "#4CAF50" if pct >= 70 else ("#FFC107" if pct >= 40 else "#F44336")

        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown(f"""
<div class='quiz-score-circle'>
    <div style="font-size:3rem; font-weight:800; color:{cor};">{pontuacao}/{total_perguntas}</div>
    <div style="opacity:0.7;">{pct}% de acerto</div>
</div>
""", unsafe_allow_html=True)
            st.progress(pct / 100)
        with col2:
            if pontuacao == total_perguntas:
                st.balloons()
                st.success("🏆 Excelente! Você dominou o conteúdo!")
            elif pct >= 70:
                st.info("💪 Bom trabalho! Reveja alguns conceitos para aperfeiçoar.")
            else:
                st.warning("📘 Continue estudando! Volte aos módulos e pratique mais.")

        if erros:
            with st.expander("❌ Ver perguntas que você errou"):
                for e in erros:
                    st.write(f"• {e}")
        else:
            st.success("🎉 Você acertou todas as perguntas!")

        st.markdown("---")
        st.info("👉 Complete todos os módulos do curso na aba **👤 Perfil** para desbloquear seu certificado.")
        if st.button("🔁 Refazer o quiz"):
            st.session_state.quiz_indice = 0
            st.session_state.quiz_respostas = {}
            st.session_state.quiz_finalizado = False
            st.rerun()
