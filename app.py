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

# --- STYLE CSS DIRECT ET SÉCURISÉ (ZÉRO TRIPLE GUILLEMETS) ---
style_css = (
    "<style>"
    ".block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; padding-left: 2rem !important; padding-right: 2rem !important; }"
    ".stApp { background: linear-gradient(135deg, #F8FAFC 0%, #E2E8F0 100%); }"
    "h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stText { color: #0F172A !important; font-family: 'Segoe UI', Roboto, sans-serif; }"
    "div[data-testid='stBlock'] { gap: 0.5rem !important; }"
    ".card-base { padding: 12px 18px; border-radius: 10px; margin-bottom: 10px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); border-left: 6px solid rgba(0,0,0,0.2); }"
    ".card-gold { background: linear-gradient(135deg, #FFB703 0%, #FB8500 100%); }"
    ".card-cyan { background: linear-gradient(135deg, #00B4D8 0%, #0077B6 100%); }"
    ".card-purple { background: linear-gradient(135deg, #9D4EDD 0%, #7B2CBF 100%); }"
    ".card-green { background: linear-gradient(135deg, #2ECC71 0%, #27AE60 100%); }"
    ".card-red { background: linear-gradient(135deg, #FF4D4D 0%, #D90429 100%); }"
    ".card-gold *, .card-cyan * { color: #000000 !important; font-weight: 500; }"
    ".card-purple *, .card-green *, .card-red * { color: #FFFFFF !important; }"
    ".card-base label { font-size: 13px !important; font-weight: bold !important; }"
    ".kpi-card { border-radius: 8px; padding: 10px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); color: white !important; }"
    ".kpi-green { background: #234E40; border: 2px solid #2ECC71; }"
    ".kpi-orange { background: #4E3E23; border: 2px solid #FFB703; }"
    ".kpi-red { background: #4E232B; border: 2px solid #FF4D4D; }"
    ".institution-box { background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%); border: 2px solid #2563EB; padding: 12px; border-radius: 10px; margin-bottom: 10px; }"
    ".institution-box * { color: #1E40AF !important; }"
    "</style>"
)
st.markdown(style_css, unsafe_allow_html=True)

# ==============================================================================
# MOTEUR DE CALCULS TECHNIQUES
# ==============================================================================
def normaliser_en_kg(poids, unite):
    return poids if unite == "kg" else poids / 1000.0

# ==============================================================================
# EN-TÊTE DU DASHBOARD (Condensé)
# ==============================================================================
st.markdown("<p style='margin:0; font-size:12px; font-weight:bold; color:#2563EB !important;'>🎖️ PROJET ÉCO-CITOYEN — CADRE CLASSE CDSG</p>", unsafe_allow_html=True)
st.markdown("<h2 style='margin:0 0 5px 0; padding:0; font-size:26px;'>🍏 Plateforme Réseau de Pilotage Environnemental</h2>", unsafe_allow_html=True)
st.markdown("<p style='margin:0 0 10px 0; font-size:14px;'><b>Collège Jean Giono (Orange)</b> — Impact des 700 demi-pensionnaires | Référent : M. Thierry Armant</p>", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# STRUCTURE EN 3 COLONNES VISUELLES (Évite le défilement vertical)
# ------------------------------------------------------------------------------
col_gauche, col_milieu, col_droite = st.columns([1, 1, 1.2])

# ==========================================
# COLONNE 1 : Volet A (Reliquats & Papier)
# ==========================================
with col_gauche:
    st.markdown("<h4 style='margin:0 0 5px 0; font-size:16px; border-bottom:2px solid #FFB703;'>🥖 Volet A : Reliquats & Papier</h4>", unsafe_allow_html=True)

    # --- Poubelle à Pain ---
    st.markdown('<div class="card-base card-gold">', unsafe_allow_html=True)
    st.markdown("<h5 style='margin:0; font-size:14px;'>Pain perdu (Boulangerie)</h5>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    poids_pain = c1.number_input("Masse :", min_value=0.0, value=4.0, step=0.5, key="pain", label_visibility="collapsed")
    unite_pain = c2.selectbox("Unité :", ["kg", "g"], key="u_pain", label_visibility="collapsed")
    kg_pain = normaliser_en_kg(poids_pain, unite_pain)
    st.markdown(f"<p style='margin:2px 0 0 0; font-size:12px;'>📊 Équiv: <b>{int(kg_pain / 0.250)} baguettes</b></p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Serviettes en papier ---
    st.markdown('<div class="card-base card-cyan">', unsafe_allow_html=True)
    st.markdown("<h5 style='margin:0; font-size:14px;'>Serviettes en Papier</h5>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    poids_serviettes = c1.number_input("Masse :", min_value=0.0, value=1.5, step=0.1, key="serviettes", label_visibility="collapsed")
    unite_serviettes = c2.selectbox("Unité :", ["kg", "g"], key="u_serviettes", label_visibility="collapsed")
    kg_serviettes = normaliser_en_kg(poids_serviettes, unite_serviettes)
    st.markdown(f"<p style='margin:2px 0 0 0; font-size:12px;'>📊 Équiv: <b>{int(kg_serviettes / 0.003)} jetées</b></p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# COLONNE 2 : Volet B (Biodéchets & Emballages)
# ==========================================
with col_milieu:
    st.markdown("<h4 style='margin:0 0 5px 0; font-size:16px; border-bottom:2px solid #2ECC71;'>🗑️ Volet B : Restes de Repas</h4>", unsafe_allow_html=True)

    # --- Déchets Alimentaires ---
    st.markdown('<div class="card-base card-green">', unsafe_allow_html=True)
    st.markdown("<h5 style='margin:0; font-size:14px;'>Biodéchets (Plats cuisinés)</h5>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    poids_alim = c1.number_input("Masse :", min_value=0.0, value=25.0, step=1.0, key="alim", label_visibility="collapsed")
    unite_alim = c2.selectbox("Unité :", ["kg", "g"], key="u_alim", label_visibility="collapsed")
    kg_alim = normaliser_en_kg(poids_alim, unite_alim)
    st.markdown(f"<p style='margin:2px 0 0 0; font-size:12px;'>📊 Équiv: <b>{int(kg_alim / 0.150)} repas rejetés</b></p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Fruits entamés ---
    st.markdown('<div class="card-base card-red">', unsafe_allow_html=True)
    st.markdown("<h5 style='margin:0; font-size:14px;'>Pertes sur les Fruits</h5>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    poids_fruits = c1.number_input("Masse :", min_value=0.0, value=2.0, step=0.2, key="fruits", label_visibility="collapsed")
    unite_fruits = c2.selectbox("Unité :", ["kg", "g"], key="u_fruits", label_visibility="collapsed")
    kg_fruits = normaliser_en_kg(poids_fruits, unite_fruits)
    st.markdown(f"<p style='margin:2px 0 0 0; font-size:12px;'>📊 Équiv: <b>{int(kg_fruits / 0.120)} fruits gaspillés</b></p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Flux des Emballages ---
    st.markdown('<div class="card-base card-purple">', unsafe_allow_html=True)
    st.markdown("<h5 style='margin:0; font-size:14px;'>Emballages Non Recyclés</h5>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    poids_emballages = c1.number_input("Masse :", min_value=0.0, value=3.0, step=0.5, key="emballages", label_visibility="collapsed")
    unite_emballages = c2.selectbox("Unité :", ["kg", "g"], key="u_emballages", label_visibility="collapsed")
    kg_emballages = normaliser_en_kg(poids_emballages, unite_emballages)
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# COLONNE 3 : Contexte CDSG & Grilles Historiques
# ==========================================
with col_droite:
    st.markdown("<h4 style='margin:0 0 5px 0; font-size:16px; border-bottom:2px solid #2563EB;'>📋 Suivi Temporel & Cadre</h4>", unsafe_allow_html=True)
    
    # Bloc institutionnel compact
    st.markdown('<div class="institution-box"><p style="font-size: 11px; margin: 0; line-height:1.3;"><b>🛡️ CADRE CLASSE DÉFENSE (CDSG) :</b> Analyse de résilience locale face au gaspillage de ressources stratégiques au <b>Collège Jean Giono</b> (ODD 12 ONU).</p></div>', unsafe_allow_html=True)

    # Tableaux éditables empilés à hauteur restreinte
    st.markdown("<p style='margin:2px 0; font-size:12px; font-weight:bold;'>🗓️ Bilan
