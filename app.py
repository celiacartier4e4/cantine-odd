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

# --- STYLE CSS SÉCURISÉ (CONCATÉNATION SANS TRIPLES GUILLEMETS) ---
css_lines = [
    "<style>",
    ".block-container { padding-top: 1.5rem !important; padding-bottom: 1.5rem !important; padding-left: 5rem !important; padding-right: 5rem !important; }",
    ".stApp { background: linear-gradient(rgba(255, 255, 255, 0.15), rgba(15, 23, 42, 0.85)), url('https://images.unsplash.com/photo-1541339907198-e08756dedf3f?q=80&w=1920&auto=format&fit=crop') no-repeat center center fixed; background-size: cover; }",
    "h1, h2, h3, h4, h5, h6, .stMarkdown, .stText { color: #FFFFFF !important; font-family: 'Segoe UI', Roboto, sans-serif; text-shadow: 1px 1px 4px rgba(0,0,0,0.8); }",
    "label, div[data-testid='stWidgetLabel'] p { color: #FFFFFF !important; font-weight: bold !important; text-shadow: 1px 1px 3px rgba(0,0,0,0.9); }",
    ".card-base { padding: 16px; border-radius: 12px; margin-bottom: 14px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); border-left: 8px solid rgba(0,0,0,0.3); }",
    ".card-green { background: linear-gradient(135deg, #00FF66 0%, #009933 100%); }",
    ".card-gold { background: linear-gradient(135deg, #FFCC00 0%, #FF6600 100%); }",
    ".card-red { background: linear-gradient(135deg, #FF3333 0%, #990000 100%); }",
    ".card-cyan { background: linear-gradient(135deg, #00FFFF 0%, #006699 100%); }",
    ".card-purple { background: linear-gradient(135deg, #CC33FF 0%, #660099 100%); }",
    ".card-green *, .card-red *, .card-purple * { color: #FFFFFF !important; }",
    ".card-gold *, .card-cyan * { color: #000000 !important; font-weight: bold; text-shadow: none !important; }",
    ".institution-box { background: rgba(30, 41, 59, 0.85); border: 2px solid #38BDF8; padding: 14px; border-radius: 10px; margin-bottom: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.4); }",
    ".kpi-card { border-radius: 8px; padding: 12px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.3); color: white !important; }",
    ".kpi-green { background: rgba(16, 185, 129, 0.9); border: 2px solid #00FF66; }",
    ".kpi-orange { background: rgba(245, 158, 11, 0.9); border: 2px solid #FFCC00; }",
    ".kpi-red { background: rgba(239, 68, 68, 0.9); border: 2px solid #FF3333; }",
    "div [data-testid='stProgressBar'] > div > div { background-image: linear-gradient(to right, #FF3333, #FFCC00, #00FF66) !important; }",
    "</style>"
]
st.markdown("".join(css_lines), unsafe_allow_html=True)

# ==============================================================================
# MOTEUR DE CALCULS TECHNIQUES
# ==============================================================================
def normaliser_en_kg(poids, unite):
    return poids if unite == "kg" else poids / 1000.0

# ==============================================================================
# EN-TÊTE DU DASHBOARD
# ==============================================================================
st.markdown("<p style='margin:0; font-size:13px; font-weight:bold; color:#38BDF8 !important;'>🎖️ PROJET ÉCO-CITOYEN — CADRE CLASSE CDSG</p>", unsafe_allow_html=True)
st.markdown("<h1 style='margin:0 0 5px 0; padding:0; font-size:32px;'>🍏 Plateforme Réseau de Pilotage Environnemental</h1>", unsafe_allow_html=True)
st.markdown("<p style='margin:0 0 20px 0; font-size:15px;'><b>Collège Jean Giono</b> — Avenue Charles Dardun, 84100 Orange<br>Impact des 700 demi-pensionnaires | Référent : M. Thierry Armant</p>", unsafe_allow_html=True)

# ==============================================================================
# CONTEXTE CDSG
# ==============================================================================
st.markdown(
    "<div class='institution-box'>"
    "<h5 style='margin:0 0 4px 0; font-size:14px; font-weight:bold; color:#38BDF8 !important;'>🛡️ CONTEXTE CLASSE DÉFENSE (CDSG)</h5>"
    "<p style='font-size: 12px; margin: 0; line-height:1.4; color:#E2E8F0 !important;'>"
    "Modélisation quantitative de résilience locale face au gaspillage de ressources stratégiques. "
    "Ce module de suivi s'inscrit directement dans les objectifs de l'<b>ODD 12</b> de l'ONU."
    "</p></div>", 
    unsafe_allow_html=True
)

# ==============================================================================
# ZONE DE SAIS
