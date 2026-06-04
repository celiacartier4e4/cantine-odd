import streamlit as st
import pandas as pd

# ==============================================================================
# CONFIGURATION DE LA PAGE
# ==============================================================================
st.set_page_config(
    page_title="Dashboard Éco-Citoyen - CDSG Giono",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- STYLE CSS DIRECT ET SÉCURISÉ (CHAÎNE CONTINUE CONCATÉNÉE) ---
style_css = (
    "<style>"
    ".block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; padding-left: 2rem !important; padding-right: 2rem !important; }"
    ".stApp { background: linear-gradient(135deg, #F8FAFC 0%, #E2E8F0 100%); }"
    "h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stText { color: #0F172A !important; font-family: 'Segoe UI', Roboto, sans-serif; }"
    "div[data-testid='stBlock'] { gap: 0.4rem !important; }"
    ".card-base { padding: 10px 14px; border-radius: 8px; margin-bottom: 8px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08); border-left: 6px solid rgba(0,0,0,0.2); }"
    ".card-gold { background: linear-gradient(135deg, #FFB703 0%, #FB8500 100%); }"
    ".card-cyan { background: linear-gradient(135deg, #00B4D8 0%, #0077B6 100%); }"
    ".card-purple { background: linear-gradient(135deg, #9D4EDD 0%, #7B2CBF 100%); }"
    ".card-green { background: linear-gradient(135deg, #2ECC71 0%, #27AE60 100%); }"
    ".card-red { background: linear-gradient(135deg, #FF4D4D 0%, #D90429 100%); }"
    ".card-gold *, .card-cyan * { color: #000000 !important; font-weight: 500; }"
    ".card-purple *, .card-green *, .card-red * { color: #FFFFFF !important; }"
    ".card-base label { font-size: 12px !important; font-weight: bold !important; }"
    ".kpi-card { border-radius: 6px; padding: 8px; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.05); color: white !important; }"
    ".kpi-green { background: #234E40; border: 1.5px solid #2ECC71; }"
    ".kpi-orange { background: #4E3E23; border: 1.5px solid #FFB703; }"
    ".kpi-red { background: #4E232B; border: 1.5px solid #FF4D4D; }"
    ".institution-box { background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%); border: 1.5px solid #2563EB; padding: 10px; border-radius: 8px; margin-bottom: 8px; }"
    ".institution-box * { color: #1E40AF !important; }"
    "/* Dégradé flashy pour la jauge de progression */"
    "div [data-testid='stProgressBar'] > div > div { background-image: linear-gradient(to right, #FF4D4D, #FFB703, #2ECC71) !important; }"
    "</style>"
)
st.markdown(style_css, unsafe_allow_html=True)

# ==============================================================================
# MOTEUR DE CALCULS TECHNIQUES
# ==============================================================================
def normaliser_en_kg(poids, unite):
    return poids if unite == "kg" else poids / 1000.0

# ==============================================================================
# EN-TÊTE DU DASHBOARD
# ==============================================================================
st.markdown("<p style='margin:0; font-size:11px; font-weight:bold; color:#2563EB !important;'>🎖️ PROJET ÉCO-CITOYEN — CADRE CLASSE CDSG</p>", unsafe_allow_html=True)
st.markdown("<h2 style='margin:0 0 5px 0; padding:0; font-size:24px;'>🍏 Plateforme Réseau de Pilotage Environnemental</h2>", unsafe_allow_html=True)
st.markdown("<p style='margin:0 0 10px 0; font-size:13px;'><b>Collège Jean Giono (Orange)</b> — Impact des 700 demi-pensionnaires | Référent : M. Thierry Armant</p>", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# INITIALISATION DES VARIABLES DE SAISIE POUR ÉVITER LES ERREURS DE LECTURE
# ------------------------------------------------------------------------------
if "p_pain" not in st.session_state: st.session_state["p_pain"] = 4.0
if "p_serv" not in st.session_state: st.session_state["p_serv"] = 1.5
if "p_alim" not in st.session_state: st.session_state["p_alim"] = 25.0
if "p_frut" not in st.session_state: st.session_state["p_frut"] = 2.0
if "p_emb" not in st.session_state: st.session_state["p_emb"] = 3.0

# ------------------------------------------------------------------------------
# STRUCTURE EN 2 GRANDES COLONNES (GAUCHE = RECAPS VISUELS / DROITE = SAISIES SÉCURISÉES)
# ------------------------------------------------------------------------------
col_gauche_bilan, col_droite_saisie = st.columns([1.2, 1])

# =
