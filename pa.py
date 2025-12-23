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
# CSS PERSONALIZADO
# ============================================================
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #1f77b4;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555;
}
.section {
    background-color: #f8f9fa;
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# MENU LATERAL
# ============================================================
st.sidebar.title("📚 Navigation")
menu = st.sidebar.radio(
    "Choose a section:",
    [
        "🏠 Home",
        "📘 What is Data Science?",
        "🧹 Data Cleaning & Analysis",
        "📊 Statistics & Insights",
        "⚙️ Interactive Lab",
        "👤 About the Author"
    ]
)

# ============================================================
# HOME
# ============================================================
if menu == "🏠 Home":
    st.markdown("<div class='main-title'>Data Science Educational Project</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>From theory to practice — an interactive learning experience</div>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div class="section">
    <h3>🎯 Project Objective</h3>
    <p>
    This project was developed to present the fundamentals of Data Science in a clear,
    interactive and educational way. It combines theory, statistics and real data analysis
    using Python.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section">
    <h3>🛠 Tools Used</h3>
    <ul>
        <li>Python</li>
        <li>Pandas & NumPy</li>
        <li>Streamlit</li>
        <li>CSV data processing</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# WHAT IS DATA SCIENCE
# ============================================================
elif menu == "📘 What is Data Science?":
    st.title("📘 What is Data Science?")

    st.markdown("""
    <div class="section">
    <p>
    Data Science is an interdisciplinary field that combines <strong>statistics,
    programming, and domain knowledge</strong> to extract meaningful insights from data.
    </p>

    <p>
    It is widely used in areas such as:
    </p>
    <ul>
        <li>Business and Marketing</li>
        <li>Finance</li>
        <li>Healthcare</li>
        <li>Technology and Artificial Intelligence</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section">
    <h4>📌 Why Data Science matters?</h4>
    <p>
    Companies and institutions rely on data-driven decisions. Data Science allows
    professionals to transform raw data into strategic information.
    </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# DATA CLEANING
# ============================================================
elif menu == "🧹 Data Cleaning & Analysis":
    st.title("🧹 Data Cleaning & Analysis")

    st.markdown("""
    <div class="section">
    <p>
    Real-world data is often messy. Data cleaning is a crucial step to ensure accurate
    analysis and reliable results.
    </p>
    <ul>
        <li>Handling missing values</li>
        <li>Correcting data types</li>
        <li>Removing inconsistencies</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    uploaded = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)

        st.subheader("🔍 Raw Data")
        st.dataframe(df.head())

        st.subheader("🧼 Cleaned Data (Example)")
        df_clean = df.dropna()
        st.dataframe(df_clean.head())

# ============================================================
# STATISTICS
# ============================================================
elif menu == "📊 Statistics & Insights":
    st.title("📊 Statistics & Insights")

    st.markdown("""
    <div class="section">
    <p>
    Descriptive statistics help us understand the structure and distribution of data.
    </p>
    </div>
    """, unsafe_allow_html=True)

    data = pd.DataFrame({
        "Scores": np.random.randint(50, 100, 30)
    })

    st.dataframe(data)

    st.markdown("""
    <div class="section">
    <ul>
        <li><strong>Mean:</strong> {}</li>
        <li><strong>Median:</strong> {}</li>
        <li><strong>Standard Deviation:</strong> {:.2f}</li>
    </ul>
    </div>
    """.format(
        data["Scores"].mean(),
        data["Scores"].median(),
        data["Scores"].std()
    ), unsafe_allow_html=True)

# ============================================================
# INTERACTIVE LAB
# ============================================================
elif menu == "⚙️ Interactive Lab":
    st.title("⚙️ Interactive Data Science Lab")

    st.markdown("""
    <div class="section">
    <p>
    This section allows users to interact with data and observe results in real time.
    </p>
    </div>
    """, unsafe_allow_html=True)

    rows = st.slider("Number of rows", 5, 100, 20)
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
elif menu == "👤 About the Author":
    st.title("👤 About the Author")

    st.markdown("""
    <div class="section">
    <p>
    Hi! My name is <strong>Matheus</strong>, I am 16 years old and I live in São Paulo, Brazil.
    </p>

    <p>
    This project was developed independently as part of my technical high school studies.
    Its main objective is to present Data Science concepts in a practical and accessible way.
    </p>

    <p>
    I am interested in Data Science because I study this field every day at school and enjoy
    working with data. I plan to study Data Science in the future, as it is an area with strong
    growth and great potential to impact different industries.
    </p>

    <p>
    Through this project, I aim to improve my technical skills and take my first steps toward
    an international academic and professional career.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.success("🚀 Project developed with dedication, curiosity and passion for learning.")
