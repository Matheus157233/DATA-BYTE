# ========================= DATASTART PRO MAX =========================
# Plataforma completa de Ciência de Dados (versão absurda)

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import random
import time
from datetime import datetime

# ========================= CONFIG =========================
st.set_page_config(page_title="DataStart PRO MAX", layout="wide")

# ========================= SESSION STATE =========================
def init_state():
    defaults = {
        "xp": 0,
        "level": 1,
        "badges": [],
        "progress": {i: False for i in range(1,8)},
        "history": [],
        "username": "Aluno",
        "theme": "dark"
    }
    for k,v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ========================= STYLE =========================
st.markdown("""
<style>
body {background-color:#0e1117; color:white;}
.block-container {padding:2rem;}
.card {
    background: linear-gradient(145deg,#1f2230,#161822);
    padding:25px;
    border-radius:20px;
    margin-bottom:15px;
    box-shadow:0 0 25px rgba(0,0,0,0.6);
    transition:0.3s;
}
.card:hover {transform:scale(1.03);}
.title {font-size:45px;font-weight:bold;}
.subtitle {color:#aaa;}
.badge {background:#ff4b4b;padding:5px 10px;border-radius:10px;}
</style>
""", unsafe_allow_html=True)

# ========================= SYSTEMS =========================
def add_xp(amount):
    st.session_state.xp += amount
    st.session_state.history.append((datetime.now(), amount))
    if st.session_state.xp >= st.session_state.level * 100:
        st.session_state.level += 1
        st.success("🔥 LEVEL UP!")
        unlock_badge("Level Up")

def unlock_badge(name):
    if name not in st.session_state.badges:
        st.session_state.badges.append(name)
        st.success(f"🏆 Nova conquista: {name}")

# ========================= SIDEBAR =========================
st.sidebar.title("🚀 DataStart PRO MAX")
menu = st.sidebar.radio("Menu",[
    "🏠 Home","📚 Jornada","🧠 Lógica","🐍 Python","📊 Dados",
    "📈 Dashboard","🤖 IA","🎮 Gamificação","🏁 Projeto Final"
])

st.sidebar.markdown(f"XP: {st.session_state.xp}")
st.sidebar.markdown(f"Level: {st.session_state.level}")
st.sidebar.markdown("---")

# ========================= HOME =========================
if menu == "🏠 Home":
    st.markdown('<div class="title">DataStart PRO MAX 🚀</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Plataforma completa e profissional</div>', unsafe_allow_html=True)

    col1,col2,col3 = st.columns(3)
    col1.metric("XP", st.session_state.xp)
    col2.metric("Level", st.session_state.level)
    col3.metric("Badges", len(st.session_state.badges))

    progress_total = sum(st.session_state.progress.values())/7
    st.progress(progress_total)

    st.markdown("### 🏆 Conquistas")
    for b in st.session_state.badges:
        st.markdown(f"<span class='badge'>{b}</span>", unsafe_allow_html=True)

# ========================= JORNADA =========================
elif menu == "📚 Jornada":
    st.title("📚 Jornada Completa")
    for i in range(1,8):
        col1,col2 = st.columns([4,1])
        with col1:
            st.markdown(f"<div class='card'>Módulo {i}</div>", unsafe_allow_html=True)
        with col2:
            if st.button(f"Concluir {i}"):
                st.session_state.progress[i]=True
                add_xp(50)
                if i==7: unlock_badge("Curso Completo")

# ========================= LOGICA =========================
elif menu == "🧠 Lógica":
    st.title("🧠 Desafios")
    perguntas = [
        ("2,4,8,16,?","32"),
        ("1,3,9,27,?","81"),
        ("5,10,20,40,?","80")
    ]
    p = random.choice(perguntas)
    resp = st.text_input(p[0])
    if resp == p[1]:
        st.success("Acertou!")
        add_xp(20)

# ========================= PYTHON =========================
elif menu == "🐍 Python":
    st.title("🐍 IDE Python")
    code = st.text_area("Código:", "print('Hello Data')", height=200)
    if st.button("Executar"):
        try:
            exec(code)
            add_xp(10)
        except Exception as e:
            st.error(e)

# ========================= DADOS =========================
elif menu == "📊 Dados":
    st.title("📊 Laboratório de Dados")
    file = st.file_uploader("CSV")
    if file:
        df = pd.read_csv(file)
        st.dataframe(df)

        st.write("### Estatísticas")
        st.write(df.describe())

        coluna = st.selectbox("Coluna", df.columns)
        st.write("Média:", df[coluna].mean())

        add_xp(30)
        unlock_badge("Analista")

# ========================= DASHBOARD =========================
elif menu == "📈 Dashboard":
    st.title("📈 Dashboard Interativo")
    df = px.data.iris()

    col = st.selectbox("Coluna", df.columns)
    fig = px.histogram(df, x=col)
    st.plotly_chart(fig)

    fig2 = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    st.plotly_chart(fig2)

    add_xp(15)

# ========================= IA =========================
elif menu == "🤖 IA":
    st.title("🤖 Simulação Inteligente")
    x = st.slider("Entrada",0,100)
    y = x*2 + random.randint(-5,5)
    st.write("Previsão:", y)

    if y > 150:
        unlock_badge("IA Master")

    add_xp(25)

# ========================= GAMIFICAÇÃO =========================
elif menu == "🎮 Gamificação":
    st.title("🎮 Sistema de XP")
    st.write("Histórico de XP:")
    for h in st.session_state.history:
        st.write(h)

    st.write("Badges:")
    st.write(st.session_state.badges)

# ========================= PROJETO FINAL =========================
elif menu == "🏁 Projeto Final":
    st.title("🏁 Projeto Final")
    file = st.file_uploader("Dataset")
    if file:
        df = pd.read_csv(file)
        st.dataframe(df)

        fig = px.histogram(df)
        st.plotly_chart(fig)

        fig2 = px.box(df)
        st.plotly_chart(fig2)

        st.success("Projeto concluído!")
        add_xp(100)
        unlock_badge("Cientista de Dados")

# ========================= FOOTER =========================
st.markdown("---")
st.markdown("🚀 Plataforma desenvolvida para impressionar")
