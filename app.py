import streamlit as st
import pandas as pd

# ==========================================
# CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Giono - CDSG",
    page_icon="🍏",
    layout="wide"
)

# --- URL DECOUPÉE DU THÉÂTRE ANTIQUE D'ORANGE ---
u1 = "https://images.unsplash.com/"
u2 = "photo-1600021319323-b6c86725227d"
u3 = "?q=80&w=1920"
img_url = u1 + u2 + u3

# --- INJECTION DU DESIGN AVEC TEXTES BLANCS ---
css = [
    "<style>",
    ".stApp {",
    "background: linear-gradient(",
    "rgba(15,23,42,0.4),",
    "rgba(15,23,42,0.7)),",
    f"url('{img_url}');",
    "background-size: cover;",
    "background-position: center;",
    "background-attachment: fixed;",
    "}",
    # Force TOUS les textes du site en blanc
    "h1, h2, h3, h4, h5, h6, p, label, span, div {",
    "color: #ffffff !important;",
    "text-shadow: 1px 1px 3px rgba(0,0,0,0.9);",
    "}",
    # Conteneurs de saisie en fond sombre transparent
    "div[data-testid='stContainer'] {",
    "background-color: rgba(15, 23, 42, 0.85) !important;",
    "border: 1px solid #38bdf8 !important;",
    "border-radius: 12px;",
    "padding: 20px;",
    "}",
    # Textes des étiquettes de saisie en blanc
    "div[data-testid='stWidgetLabel'] p {",
    "color: #ffffff !important;",
    "font-weight: bold !important;",
    "}",
    "</style>"
]
st.markdown("\n".join(css), unsafe_allow_html=True)

# ==========================================
# EN-TÊTE
# ==========================================
st.markdown("<h1>Collège Jean Giono d'Orange</h1>", unsafe_allow_html=True)
st.markdown("<h3>Projet Éco-Citoyen - CDSG Giono</h3>", unsafe_allow_html=True)

# ==========================================
# COLONNES DE SAISIE (STRUCTURE PHOTO)
# ==========================================
col_g, col_d = st.columns(2)

with col_g:
    with st.container(border=True):
        st.markdown("<h3 style='color:#ffb703 !important;'>🥖 Reliquats de Pain (Boulangerie)</h3>", unsafe_allow_html=True)
        p_pain = st.number_input("Masse (kg) :", 0.0, 100.0, 4.0, 0.5)
        st.write(f"Equiv: {int(p_pain / 0.25)} baguettes de 250g perdues.")

    with st.container(border=True):
        st.markdown("<h3 style='color:#00f5ff !important;'>🧻 Serviettes en Papier</h3>", unsafe_allow_html=True)
        p_serv = st.number_input("Masse (kg) :", 0.0, 100.0, 1.5, 0.1)
        st.write(f"Equiv: {int(p_serv / 0.003)} serviettes jetées.")

    with st.container(border=True):
        st.markdown("<h3 style='color:#a855f7 !important;'>📦 Emballages Non Recyclés</h3>", unsafe_allow_html=True)
        p_emb = st.number_input("Masse (kg) :", 0.0, 100.0, 3.0, 0.5)
        st.write(f"Equiv: {int(p_emb / 0.02)} emballages industriels.")

with col_d:
    with st.container(border=True):
        st.markdown("<h3 style='color:#22c55e !important;'>🗑️ Biodéchets — Restes Cuisinés</h3>", unsafe_allow_html=True)
        p_bio = st.number_input("Masse (kg) :", 0.0, 100.0, 25.0, 1.0)
        st.
