import streamlit as st
import sqlite3
import pandas as pd
import re

# ------------------------
# Banco de dados
# ------------------------
conn = sqlite3.connect("cadastro.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    cpf TEXT
)
""")

# ------------------------
# Funções
# ------------------------
def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validar_cpf(cpf):
    return len(cpf) == 11 and cpf.isdigit()

def buscar_usuarios(nome_busca=""):
    if nome_busca:
        c.execute("SELECT * FROM usuarios WHERE nome LIKE ?", ('%' + nome_busca + '%',))
    else:
        c.execute("SELECT * FROM usuarios")
    return c.fetchall()

# ------------------------
# Interface
# ------------------------
st.title("📋 Sistema de Cadastro")

aba = st.sidebar.selectbox("Menu", ["Cadastrar", "Visualizar"])

# ------------------------
# CADASTRO
# ------------------------
if aba == "Cadastrar":
    st.subheader("➕ Novo Usuário")

    nome = st.text_input("Nome")
    email = st.text_input("Gmail")
    cpf = st.text_input("CPF")

    if st.button("Salvar"):
        if not nome or not email or not cpf:
            st.warning("Preencha todos os campos!")
        elif not validar_email(email):
            st.error("Email inválido!")
        elif not validar_cpf(cpf):
            st.error("CPF deve ter 11 números!")
        else:
            c.execute("INSERT INTO usuarios (nome, email, cpf) VALUES (?, ?, ?)", (nome, email, cpf))
            conn.commit()
            st.success("Usuário cadastrado!")

# ------------------------
# VISUALIZAÇÃO + CRUD
# ------------------------
if aba == "Visualizar":
    st.subheader("📊 Usuários")

    busca = st.text_input("🔍 Buscar por nome")

    dados = buscar_usuarios(busca)

    df = pd.DataFrame(dados, columns=["ID", "Nome", "Email", "CPF"])

    st.dataframe(df, use_container_width=True)

    # ------------------------
    # EDITAR
    # ------------------------
    st.subheader("✏️ Editar Usuário")

    id_edit = st.number_input("ID do usuário", min_value=1, step=1)

    novo_nome = st.text_input("Novo nome")
    novo_email = st.text_input("Novo email")
    novo_cpf = st.text_input("Novo CPF")

    if st.button("Atualizar"):
        if novo_email and not validar_email(novo_email):
            st.error("Email inválido!")
        elif novo_cpf and not validar_cpf(novo_cpf):
            st.error("CPF inválido!")
        else:
            c.execute("""
                UPDATE usuarios 
                SET nome = COALESCE(?, nome),
                    email = COALESCE(?, email),
                    cpf = COALESCE(?, cpf)
                WHERE id = ?
            """, (novo_nome, novo_email, novo_cpf, id_edit))
            conn.commit()
            st.success("Usuário atualizado!")

    # ------------------------
    # DELETAR
    # ------------------------
    st.subheader("❌ Deletar Usuário")

    id_delete = st.number_input("ID para deletar", min_value=1, step=1, key="delete")

    if st.button("Deletar"):
        c.execute("DELETE FROM usuarios WHERE id = ?", (id_delete,))
        conn.commit()
        st.warning("Usuário deletado!")
