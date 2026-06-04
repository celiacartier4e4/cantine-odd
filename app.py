import streamlit as st
import pandas as pd

# ==============================================================================
# CONFIGURATION DE LA PAGE
# ==============================================================================
st.set_page_config(
    page_title="Collège Jean Giono - CDSG",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- INJECTION DU DESIGN ET DE L'ARRIÈRE-PLAN (LIGNES COURTES ANTI-COUPURE) ---
css_style = [
    "<style>",
    ".block-container { padding: 1.5rem 3rem !important; }",
    ".stApp { background: linear-gradient(rgba(255,255,255,0.1), ",
    "rgba(15,23,42,0.4)), url('https://images.unsplash.com/photo-1541339907198-e08756dedf3f?q=80&w=1920') ",
    "no-repeat center center fixed; background-size: cover; }",
    ".main-title { color: #0f172a !important; font-family: sans-serif; ",
    "font-size: 42px !important; font-weight: bold; margin: 0 !important; }",
    ".sub-title { color: #1e293b !important; font-family: sans-serif; ",
    "font-size: 20px !important; margin: 0 0 20px 0 !important; }",
    ".card { padding: 15px 20px; border-radius: 12px; margin-bottom: 15px; ",
    "box-shadow: 0 4px 10px rgba(0,0,0,0.15); font-family: sans-serif; }",
    ".card-title { font-size: 16px !important; font-weight: bold !important; ",
    "margin-bottom: 8px !important; }",
    ".card-analysis { font-size: 12px !important; margin-top: 8px !important; ",
    "font-weight: 500; }",
    ".bg-gold { background-color: #ffb703; color: #000000 !important; }",
    ".bg-cyan { background-color: #00f5ff; color: #000000 !important; }",
    ".bg-purple { background-color: #a855f7; color: #ffffff !important; }",
    ".bg-green { background-color: #22c55e; color: #ffffff !important; }",
    ".bg-red { background-color: #ef4444; color: #ffffff !important; }",
    ".bg-dark { background-color: #0f172a; color: #ffffff !important; ",
    "border: 1px solid #38bdf8; }",
    ".bottom-panel { background-color: #090d16; border-radius: 12px; ",
    "padding: 20px; margin-top: 25px; border: 1px solid #1e293b; }",
    ".bottom-title { color: #ffffff !important; font-size: 15px !important; ",
    "font-weight: bold; margin-bottom: 10px !important; }",
    ".kpi-box { padding: 8px; border-radius: 20px; text-align: center; ",
    "font-weight: bold; font-size: 13px; margin-bottom: 8px; }",
    "div[data-testid='stWidgetLabel'] p { color: inherit !important; font-weight: bold; }",
    "</style>"
]
st.markdown("\n".join(css_style), unsafe_allow_html=True)

# ==============================================================================
# EN-TÊTE DU COLLÈGE
# ==============================================================================
st.markdown('<p class="main-title">Collège Jean Giono d\'Orange</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Projet Éco-Citoyen - CDSG Giono</p>', unsafe_allow_html=True)

# ==============================================================================
# MISE EN PAGE : DOUBLE COLONNE DE BLOCS (COMME SUR LA PHOTO)
# ==============================================================================
col_gauche, col_droite = st.columns(2)

with col_gauche:
    # 1. Reliquats de Pain
    st.markdown('<div class="card bg-gold"><p class="card-title">🥖 Reliquats de Pain (Boulangerie)</p>', unsafe_allow_html
