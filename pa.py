import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Threat Modeling Dashboard", layout="wide")

# =========================
# MENU
# =========================
aba = st.sidebar.radio("Navegação", ["📚 Teoria", "📊 Dashboard", "🧪 Prática"])

# =========================
# 📚 ABA TEORIA
# =========================
if aba == "📚 Teoria":

    st.title("🔐 Modelagem de Ameaças e Métricas de Segurança")

    st.header("1. Introdução")
    st.write("""
A crescente digitalização de serviços e sistemas torna a segurança da informação um fator crítico.
A modelagem de ameaças é uma abordagem proativa que permite antecipar ataques.
""")

    st.header("2. Conceito de Modelagem de Ameaça")
    st.write("""
Responde quatro perguntas:
- O que estamos construindo?
- O que pode dar errado?
- O que vamos fazer?
- Fizemos bem?
""")

    st.header("3. Metodologias")

    st.subheader("STRIDE")
    st.write("""
- Spoofing
- Tampering
- Repudiation
- Information Disclosure
- Denial of Service
- Elevation of Privilege
""")

    st.subheader("DREAD")
    st.write("""
- Damage
- Reproducibility
- Exploitability
- Affected Users
- Discoverability
""")

    st.subheader("PASTA")
    st.write("Foco em negócio, impacto financeiro e simulação de ataques.")

    st.header("4. Risco")
    st.latex("Risco = Impacto \\times Probabilidade")

    st.header("5. Métricas")

    st.subheader("Risco")
    st.write("- Risco médio\n- Top riscos\n- Distribuição")

    st.subheader("Vulnerabilidade")
    st.latex("MTTR = \\frac{\\sum Tempo\\ de\\ Correção}{Número\\ de\\ Incidentes}")

    st.subheader("Resposta")
    st.write("- MTTD\n- MTTR\n- Incidentes")

    st.subheader("Controle")
    st.write("- % mitigado\n- cobertura")

    st.header("6. Dashboards")
    st.write("""
KPIs, gráficos, heatmaps e séries temporais ajudam na decisão.
""")

    st.header("7. Ferramentas")
    st.write("Streamlit permite dashboards interativos com Python.")

    st.header("8. Normas")
    st.write("""
- ISO 27001
- OWASP
- NIST
""")

    st.header("9. Benefícios")
    st.write("""
- Redução de custos
- Segurança desde o design
- Priorização eficiente
""")

    st.header("10. Desafios")
    st.write("""
- Complexidade
- Atualização constante
- Conhecimento técnico
""")

    st.header("11. Conclusão")
    st.write("""
A modelagem de ameaças + métricas + dashboards melhora a segurança e tomada de decisão.
""")

# =========================
# 📊 ABA DASHBOARD
# =========================
elif aba == "📊 Dashboard":

    st.title("📊 Dashboard de Ameaças")

    df = pd.read_csv("data.csv")
    df["risco"] = df["impacto"] * df["probabilidade"]

    # filtros
    sistema = st.sidebar.multiselect("Sistema", df["sistema"].unique(), default=df["sistema"].unique())
    df = df[df["sistema"].isin(sistema)]

    # KPIs
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Ameaças", len(df))
    col2.metric("Risco Médio", round(df["risco"].mean(), 2))
    col3.metric("Maior Risco", df["risco"].max())

    # gráficos
    fig1 = px.pie(df, names="STRIDE", title="Distribuição STRIDE")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.bar(df, x="ameaca", y="risco", color="STRIDE", title="Risco por Ameaça")
    st.plotly_chart(fig2, use_container_width=True)

    df["data"] = pd.to_datetime(df["data"])
    fig3 = px.line(df, x="data", y="risco", color="sistema", title="Evolução do Risco")
    st.plotly_chart(fig3, use_container_width=True)

# =========================
# 🧪 ABA PRÁTICA
# =========================
elif aba == "🧪 Prática":

    st.title("🧪 Exemplo Prático de Modelagem de Ameaça")

    st.subheader("Sistema: Login de Usuário")

    st.write("""
Vamos simular uma análise real usando STRIDE e cálculo de risco.
""")

    exemplo = pd.DataFrame({
        "Ameaça": ["Roubo de senha", "Ataque de força bruta", "Session hijacking"],
        "STRIDE": ["Spoofing", "DoS", "Elevation"],
        "Impacto": [9, 7, 8],
        "Probabilidade": [8, 9, 6]
    })

    exemplo["Risco"] = exemplo["Impacto"] * exemplo["Probabilidade"]

    st.dataframe(exemplo)

    st.subheader("Análise")

    st.write("""
- Roubo de senha → risco alto → precisa MFA
- Força bruta → implementar bloqueio
- Session hijacking → usar HTTPS + tokens seguros
""")

    st.bar_chart(exemplo.set_index("Ameaça")["Risco"])

    st.subheader("Classificação automática")

    def classificar(r):
        if r > 70:
            return "Alto"
        elif r > 40:
            return "Médio"
        return "Baixo"

    exemplo["Nível"] = exemplo["Risco"].apply(classificar)

    st.dataframe(exemplo)

    st.success("Esse é exatamente o tipo de análise usada em empresas.")
