import streamlit as st
import pandas as pd
import numpy as np

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(
    page_title="Data Science Project | Matheus",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# ESTADOS GLOBAIS
# ============================================================
if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "lang" not in st.session_state:
    st.session_state.lang = "PT"

# ============================================================
# SIDEBAR – CONTROLES GERAIS
# ============================================================
st.sidebar.title("⚙️ Configurações")

# Tema
theme_toggle = st.sidebar.toggle("🌙 Modo Escuro", value=st.session_state.theme == "dark")
st.session_state.theme = "dark" if theme_toggle else "light"

# Idioma
lang = st.sidebar.selectbox("🌎 Language / Idioma", ["Português", "English"])
st.session_state.lang = "PT" if lang == "Português" else "EN"

st.sidebar.markdown("---")

# ============================================================
# CSS DINÂMICO
# ============================================================
if st.session_state.theme == "dark":
    bg = "#0e1117"
    text = "#ffffff"
    card = "#161b22"
else:
    bg = "#ffffff"
    text = "#000000"
    card = "#f1f3f6"

st.markdown(f"""
<style>
body {{
    background-color: {bg};
    color: {text};
}}
.section {{
    background-color: {card};
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 20px;
}}
.title {{
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}}
.subtitle {{
    text-align: center;
    font-size: 18px;
    opacity: 0.8;
}}
</style>
""", unsafe_allow_html=True)

# ============================================================
# TEXTOS (PT / EN)
# ============================================================
T = {
    "PT": {
        "home": "Início",
        "what": "O que é Ciência de Dados?",
        "clean": "Análise e Limpeza de CSV",
        "stats": "Estatística",
        "lab": "Laboratório Interativo",
        "about": "Sobre o Autor"
    },
    "EN": {
        "home": "Home",
        "what": "What is Data Science?",
        "clean": "CSV Analysis & Cleaning",
        "stats": "Statistics",
        "lab": "Interactive Lab",
        "about": "About the Author"
    }
}

# ============================================================
# MENU
# ============================================================
menu = st.sidebar.radio(
    "📚 Menu",
    [
        T[st.session_state.lang]["home"],
        T[st.session_state.lang]["what"],
        T[st.session_state.lang]["clean"],
        T[st.session_state.lang]["stats"],
        T[st.session_state.lang]["lab"],
        T[st.session_state.lang]["about"]
    ]
)

# ============================================================
# HOME
# ============================================================
if menu == T[st.session_state.lang]["home"]:
    st.markdown("<div class='title'>Data Science Educational Project</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Theory, practice and real data analysis</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section">
    Este projeto foi desenvolvido para apresentar conceitos fundamentais de
    Ciência de Dados de forma clara, prática e profissional.
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# WHAT IS DATA SCIENCE
# ============================================================
elif menu == T[st.session_state.lang]["what"]:
    st.title("📘 Data Science")

    st.markdown("""
    <div class="section">
    Ciência de Dados é a área que combina <strong>estatística, programação e análise</strong>
    para extrair conhecimento a partir de dados.
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# CSV CLEANING
# ============================================================
elif menu == T[st.session_state.lang]["clean"]:
    st.title("🧹 CSV Analysis & Cleaning")

    uploaded = st.file_uploader("📤 Upload CSV", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)

        st.subheader("📄 Dados Originais")
        st.dataframe(df.head())

        df_clean = df.copy()
        df_clean = df_clean.dropna()

        st.subheader("✅ Dados Tratados")
        st.dataframe(df_clean.head())

        # DOWNLOAD DO CSV TRATADO
        csv_download = df_clean.to_csv(index=False).encode("utf-8")
        st.download_button(
            "📥 Baixar CSV Tratado",
            data=csv_download,
            file_name="dados_tratados.csv",
            mime="text/csv"
        )

# ============================================================
# STATISTICS
# ============================================================
elif menu == T[st.session_state.lang]["stats"]:
    st.title("📊 Estatística Descritiva")

    data = pd.DataFrame({
        "Valores": np.random.randint(10, 100, 50)
    })

    st.dataframe(data)

    st.markdown(f"""
    <div class="section">
    <ul>
        <li><strong>Média:</strong> {data['Valores'].mean():.2f}</li>
        <li><strong>Mediana:</strong> {data['Valores'].median()}</li>
        <li><strong>Desvio Padrão:</strong> {data['Valores'].std():.2f}</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# INTERACTIVE LAB
# ============================================================
elif menu == T[st.session_state.lang]["lab"]:
    st.title("⚙️ Interactive Lab")

    rows = st.slider("Linhas", 5, 100, 20)

    df = pd.DataFrame({
        "A": np.random.randn(rows),
        "B": np.random.rand(rows),
        "C": np.random.randint(0, 100, rows)
    })

    st.dataframe(df)
    st.line_chart(df)

# ============================================================
# ABOUT THE AUTHOR
# ============================================================
elif menu == T[st.session_state.lang]["about"]:
    st.title("👤 About the Author")

    st.markdown("""
    <div class="section">
    <p>
    Hi, my name is <strong>Matheus</strong>. I am 16 years old and I live in São Paulo, Brazil.
    </p>

    <p>
    I am currently a technical high school student focused on Data Science.
    This project was developed independently as part of my academic journey.
    </p>

    <p>
    I am interested in Data Science because I study this field daily and enjoy
    working with data analysis, statistics and programming.
    </p>

    <p>
    My goal is to pursue higher education in Data Science and build an international
    academic and professional career.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.success("🚀 Project built with dedication and long-term vision.")
