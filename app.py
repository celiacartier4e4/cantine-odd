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

# --- URL DU THÉÂTRE ANTIQUE D'ORANGE ---
u_base = "https://images.unsplash.com/"
u_code = "photo-1600021319323-b6c86725227d"
u_param = "?q=80&w=1920"
fond_ecran = u_base + u_code + u_param

# --- INJECTION DU STYLE POUR TRANSPARENCE ET IMAGE DE FOND ---
design_global = [
    "<style>",
    "[data-testid='stApp'] {",
    f"background-image: linear-gradient(rgba(15,23,42,0.55), rgba(15,23,42,0.8)), url('{fond_ecran}') !important;",
    "background-size: cover !important;",
    "background-position: center !important;",
    "background-attachment: fixed !important;",
    "}",
    "[data-testid='stHeader'], [data-testid='stAppViewContainer'] {",
    "background: transparent !important;",
    "}",
    "h1, h2, h3, h4, h5, h6, p, label, span, div, text {",
    "color: #ffffff !important;",
    "text-shadow: 1px 1px 3px rgba(0,0,0,0.9) !important;",
    "}",
    "div[data-testid='stVerticalBlockBorderWrapper'] > div {",
    "background-color: rgba(15, 23, 42, 0.85) !important;",
    "border: 1px solid #38bdf8 !important;",
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
        p_frt = st.number_input("Masse mesurée (kg) :", 0.0, 100.0, 2.0, 0.
