import streamlit as st
import pandas as pd

# ==========================================
# CONFIGURATION DE LA PAGE
# ==========================================
st.set_page_config(
    page_title="Giono - CDSG",
    page_icon="🍏",
    layout="wide"
)

# --- URL DE TON IMAGE DE FOND EXTRAITE ET DÉCOUPÉE ---
u_base = "https://provence-alpes-cotedazur.com/"
u_code = "app/uploads/crt-paca/2020/12/thumbs/"
u_file = "orange-f-2018-14945-1920x960.jpg"
fond_ecran = u_base + u_code + u_file

# --- INJECTION DU STYLE GLOSSY (GLASSMORPHISM) ---
design_global = [
    "<style>",
    "[data-testid='stApp'] {",
    f"background-image: linear-gradient(rgba(15,23,42,0.45), rgba(15,23,42,0.65)), url('{fond_ecran}') !important;",
    "background-size: cover !important;",
    "background-position: center !important;",
    "background-attachment: fixed !important;",
    "}",
    "[data-testid='stHeader'], [data-testid='stAppViewContainer'] {",
    "background: transparent !important;",
    "}",
    "h1, h2, h3, h4, h5, h6, p, label, span, div, text {",
    "color: #ffffff !important;",
    "text-shadow: 1px 1px 3px rgba(0,0,0,0.8) !important;",
    "}",
    "div[data-testid='stVerticalBlockBorderWrapper'] > div {",
    "background: linear-gradient(135deg, rgba(255,255,255,0.12), rgba(255,255,255,0.03)) !important;",
    "backdrop-filter: blur(10px) !important;",
    "-webkit-backdrop-filter: blur(10px) !important;",
    "border: 1px solid rgba(255, 255, 255, 0.25) !important;",
    "box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;",
    "border-radius: 12px !important;",
    "padding: 18px !important;",
    "}",
    "div[data-testid='stWidgetLabel'] p {",
    "color: #ffffff !important;",
    "font-weight: bold !important;",
    "}",
    "</style>"
]
st.markdown("\n".join(design_global), unsafe_allow_html=True)

# ==========================================
# EN-TÊTE DE LA PAGE
# ==========================================
st.title("Collège Jean Giono d'Orange")
st.subheader("Projet Éco-Citoyen - CLASSE DÉFENSE (CDSG Giono)")

# ==========================================
# ESPACE DE SAISIE EN 2 COLONNES
# ==========================================
col_gauche, col_droite = st.columns(2)

with col_gauche:
    with st.container(border=True):
        st.write("### 🥖 Reliquats de Pain (Boulangerie)")
        p_pain = st.number_input("Masse mesurée (kg) :", 0.0, 100.0, 4.0, 0.5, key="pain")
        st.write(f"Équivalent : {int(p_pain / 0.25)} baguettes perdues.")

    with st.container(border=True):
        st.write("### 🧻 Serviettes en Papier")
        p_serv = st.number_input("Masse mesurée (kg) :", 0.0, 100.0, 1.5, 0.1, key="serviettes")
        st.write(f"Équivalent : {int(p_serv / 0.003)} serviettes jetées.")

    with st.container(border=True):
        st.write("### 📦 Emballages Non Recyclés")
        p_emb = st.number_input("Masse mesurée (kg) :", 0.0, 100.0, 3.0, 0.5, key="emballages")
        st.write(f"Équivalent : {int(p_emb / 0.02)} emballages jetés.")

with col_droite:
    with st.container(border=True):
        st.write("### 🗑️ Biodéchets — Restes Cuisinés")
        p_bio = st.number_input("Masse mesurée (kg) :", 0.0, 100.0, 25.0, 1.0, key="biodechets")
        st.write(f"Équivalent : {int(p_bio / 0.15)} repas jetés.")

    with st.container(border=True):
        st.write("### 🍎 Pertes sur les Fruits")
        p_frt = st.number_input("Masse mesurée (kg) :", 0.0, 100.0, 2.0, 0.2, key="fruits")
        st.write(f"Équivalent : {int(p_frt / 0.12)} fruits gaspillés.")

    with st
