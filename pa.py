import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Threat Modeling Dashboard", layout="wide")

# =========================
# MENU
# =========================
aba = st.sidebar.radio("Navegação", ["📚 Teoria", "📊 Dashboard", "🧪 Prática", "🎥 Vídeos"])

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
    st.write("KPIs, gráficos, heatmaps e séries temporais ajudam na decisão.")

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

    st.header("12. Aprofundamento Técnico")

    st.write("""
### 🔍 Fluxo de Modelagem de Ameaças

1. Identificação de ativos  
2. Mapeamento de fluxos de dados  
3. Identificação de ameaças (STRIDE)  
4. Análise de risco (DREAD)  
5. Definição de contramedidas  
""")

    st.write("""
### 🧱 Conceitos importantes

- Superfície de ataque  
- Ativos  
- Trust Boundaries  
""")

    st.write("""
### 🔐 Security by Design

A segurança deve ser construída desde o início do sistema.
""")

# =========================
# 📊 ABA DASHBOARD
# =========================
elif aba == "📊 Dashboard":

    st.title("📊 Dashboard de Ameaças")

    # fallback caso não exista CSV
    try:
        df = pd.read_csv("data.csv")
    except:
        df = pd.DataFrame({
            "sistema": ["Login", "API", "Banco", "Frontend", "Admin"],
            "ameaca": ["Spoofing", "DoS", "Tampering", "Info Leak", "EoP"],
            "STRIDE": ["Spoofing", "Denial of Service", "Tampering", "Information Disclosure", "Elevation of Privilege"],
            "impacto": [9, 7, 8, 6, 9],
            "probabilidade": [8, 9, 7, 6, 7],
            "data": ["2026-05-01", "2026-05-02", "2026-05-03", "2026-05-04", "2026-05-05"]
        })

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

    st.subheader("📋 Dados")
    st.dataframe(df)

# =========================
# 🧪 ABA PRÁTICA
# =========================
elif aba == "🧪 Prática":

    st.title("🧪 Exemplo Prático")

    exemplo = pd.DataFrame({
        "Ameaça": ["Roubo de senha", "Força bruta", "Session hijacking"],
        "STRIDE": ["Spoofing", "DoS", "Elevation"],
        "Impacto": [9, 7, 8],
        "Probabilidade": [8, 9, 6]
    })

    exemplo["Risco"] = exemplo["Impacto"] * exemplo["Probabilidade"]

    st.dataframe(exemplo)

    st.bar_chart(exemplo.set_index("Ameaça")["Risco"])

    def classificar(r):
        if r > 70:
            return "Alto"
        elif r > 40:
            return "Médio"
        return "Baixo"

    exemplo["Nível"] = exemplo["Risco"].apply(classificar)

    st.dataframe(exemplo)

    st.write("""
Análise:
- Roubo de senha → usar MFA  
- Força bruta → bloquear tentativas  
- Session hijacking → HTTPS e tokens  
""")

# =========================
# 🎥 ABA VÍDEOS
# =========================
elif aba == "🎥 Vídeos":

    st.title("🎥 Vídeos Explicativos (Português)")

    st.write("Conteúdos curtos para entender threat modeling na prática.")

    st.subheader("🔐 O que é Modelagem de Ameaças")
    st.video("https://youtu.be/UWDqnhJsafY?si=2IJDvl8XNQgbqJTz")

    st.subheader("🧠 STRIDE explicado")
    st.video("https://www.youtube.com/watch?v=rEnJYNkUde0")

    st.subheader("📊 Análise de risco (DREAD)")
    st.video("https://youtu.be/R2NBddNL9Ic?si=OR6YCFRVvXPfFM4A")
    
    st.divider()

    st.subheader("📌 O que aprender com esses vídeos")
    st.write("""
- Identificar ameaças com STRIDE  
- Priorizar riscos com DREAD  
- Aplicar segurança na prática  
- Pensar como um analista de segurança  
""")
