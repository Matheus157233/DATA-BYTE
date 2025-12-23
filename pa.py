import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# ============================================================
# CONFIGURAÇÃO
# ============================================================
st.set_page_config(
    page_title="International Data Science Project",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# ESTADOS
# ============================================================
if "logged" not in st.session_state:
    st.session_state.logged = False

if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "lang" not in st.session_state:
    st.session_state.lang = "PT"

# ============================================================
# LOGIN
# ============================================================
if not st.session_state.logged:
    st.title("🔐 Login")
    name = st.text_input("Digite seu nome / Enter your name")
    if st.button("Entrar / Login") and name:
        st.session_state.user = name
        st.session_state.logged = True
        st.rerun()
    st.stop()

# ============================================================
# SIDEBAR CONFIG
# ============================================================
st.sidebar.title("⚙️ Settings")

theme = st.sidebar.toggle("🌙 Dark Mode", value=st.session_state.theme == "dark")
st.session_state.theme = "dark" if theme else "light"

lang = st.sidebar.selectbox("🌎 Language", ["Português", "English"])
st.session_state.lang = "PT" if lang == "Português" else "EN"

st.sidebar.markdown("---")

# ============================================================
# CSS
# ============================================================
if st.session_state.theme == "dark":
    bg, card, text = "#0e1117", "#161b22", "#ffffff"
else:
    bg, card, text = "#ffffff", "#f1f3f6", "#000000"

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
    text-align:center;
    font-size:40px;
    font-weight:bold;
}}
</style>
""", unsafe_allow_html=True)

# ============================================================
# TEXTOS
# ============================================================
T = {
    "PT": ["Início", "Teoria Acadêmica", "Limpeza de CSV", "Estatística", "Laboratório", "Certificado", "Sobre o Autor"],
    "EN": ["Home", "Academic Theory", "CSV Cleaning", "Statistics", "Lab", "Certificate", "About the Author"]
}

menu = st.sidebar.radio("📚 Menu", T[st.session_state.lang])

# ============================================================
# HOME
# ============================================================
if menu in ["Início", "Home"]:
    st.markdown("<div class='title'>International Data Science Project</div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="section">
    Projeto educacional desenvolvido para demonstrar domínio em Ciência de Dados,
    estatística, programação e análise crítica de dados.
    <br><br>
    Usuário logado: <strong>{st.session_state.user}</strong>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# THEORY
# ============================================================
elif menu in ["Teoria Acadêmica", "Academic Theory"]:
    st.title("📘 Data Science – Academic Overview")
    st.markdown("""
    <div class="section">
    Data Science is an interdisciplinary field that combines statistics,
    computer science and domain knowledge to extract insights from structured
    and unstructured data.

    It plays a central role in decision-making processes across industries,
    including finance, healthcare, technology and public policy.
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# CSV CLEANING
# ============================================================
elif menu in ["Limpeza de CSV", "CSV Cleaning"]:
    st.title("🧹 CSV Analysis & Cleaning")

    file = st.file_uploader("Upload CSV", type=["csv"])
    if file:
        df = pd.read_csv(file)
        st.subheader("📄 Raw Data")
        st.dataframe(df.head())

        df_clean = df.dropna()
        st.subheader("✅ Cleaned Data")
        st.dataframe(df_clean.head())

        csv = df_clean.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Clean CSV", csv, "clean_data.csv", "text/csv")

# ============================================================
# STATISTICS
# ============================================================
elif menu in ["Estatística", "Statistics"]:
    st.title("📊 Descriptive Statistics")
    data = pd.DataFrame({"Values": np.random.randint(0, 100, 50)})
    st.dataframe(data)

    st.markdown(f"""
    <div class="section">
    Mean: {data['Values'].mean():.2f}<br>
    Median: {data['Values'].median()}<br>
    Std Dev: {data['Values'].std():.2f}
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# LAB
# ============================================================
elif menu in ["Laboratório", "Lab"]:
    st.title("⚙️ Interactive Lab")
    rows = st.slider("Rows", 10, 100, 30)
    df = pd.DataFrame({
        "Feature_A": np.random.randn(rows),
        "Feature_B": np.random.rand(rows),
        "Target": np.random.randint(0, 2, rows)
    })
    st.dataframe(df)
    st.line_chart(df)

# ============================================================
# CERTIFICATE
# ============================================================
elif menu in ["Certificado", "Certificate"]:
    st.title("🎓 Certificate Generator")

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(300, 750, "Certificate of Completion")
    c.setFont("Helvetica", 14)
    c.drawCentredString(300, 700, f"This certifies that {st.session_state.user}")
    c.drawCentredString(300, 670, "has completed the Data Science Project")
    c.drawCentredString(300, 640, datetime.now().strftime("%Y-%m-%d"))
    c.showPage()
    c.save()

    st.download_button(
        "📄 Download Certificate (PDF)",
        buffer.getvalue(),
        file_name="certificate.pdf",
        mime="application/pdf"
    )

# ============================================================
# ABOUT
# ============================================================
elif menu in ["Sobre o Autor", "About the Author"]:
    st.title("👤 About the Author")
    st.markdown("""
    <div class="section">
    Hi, my name is <strong>Matheus</strong>, a Brazilian technical high school student
    focused on Data Science.

    This project represents my commitment to academic excellence, international
    education standards and continuous learning.

    My long-term goal is to pursue higher education abroad and build a career
    in data-driven decision making.
    </div>
    """, unsafe_allow_html=True)
