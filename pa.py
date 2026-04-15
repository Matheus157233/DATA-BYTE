# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

import streamlit as st

import pandas as pd

import folium

from streamlit_folium import st_folium

import requests

from sqlalchemy import text

@st.cache_data

def carregar_geojson():

    st.set_page_config(page_title="Brasil BI: Regional & CRUD", layout="wide",

    page_icon="🇧🇷")

    conn = st.connection("sql", url="sqlite:///database_final_v3.db")

    def carregar_geojson(url = ("https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson%22)):

    return requests.get(url).geojson()

    def inicializar_banco():

    with conn.session as s:

    s.execute(text("""

    CREATE TABLE IF NOT EXISTS populacao (

                    id 

    INTEGER PRIMARY KEY AUTOINCREMENT,

                    uf 

    TEXT NOT NULL,

                    regiao 

    TEXT NOT NULL,

                    habitantes INTEGER NOT NULL

                )

    """))

    check = s.execute(text("SELECT COUNT(*) FROM populacao")).fetchone()

    if check[0] == 0:

    dados = [

    6

    ("São Paulo", "Sudeste", 45919049), ("Minas Gerais",

    "Sudeste", 20538718),

    ("Rio de Janeiro", "Sudeste", 16054524), ("Bahia", "Nordeste",

    14136417,

    10880506,

    8791688,

    7609601,

    3941175),

    ("Paraná", "Sul", 11443208), ("Rio Grande do Sul", "Sul",

    ("Pernambuco", "Nordeste", 9058155), ("Ceará", "Nordeste",

    ("Pará", "Norte", 8116132), ("Santa Catarina", "Sul",

    ("Goiás", "Centro-Oeste", 7056495), ("Amazonas", "Norte",

    ("Distrito Federal", "Centro-Oeste", 2817068), ("Espírito Santo", "Sudeste", 3833486)

    for uf, reg, hab in dados:

    s.execute(text("INSERT INTO populacao (uf, regiao, habitantesVALUES (:u, :r, :h)"), 

    {"u": uf, "r": reg, "h": hab})

    s.commit()

    inicializar_banco()

    geojson_data = carregar_geojson()

 
