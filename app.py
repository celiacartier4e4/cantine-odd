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

# --- STYLE CSS : COMPACTAGE MAXIMAL & explosion de COULEURS ---
st.markdown(
    """
    <style>
    /* Supprimer les espaces natifs inutiles de Streamlit */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    
    /* Fond principal */
    .stApp {
        background: linear-gradient(135deg, #F8FAFC 0%, #E2E8F0 100%);
    }

    /* Textes généraux sombres pour contraste max */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stText {
        color: #0F172A !important;
        font-family: 'Segoe UI', Roboto, sans-serif;
    }

    /* Ajustement des espaces entre les inputs Streamlit */
    div[data-testid="stBlock"] {
        gap: 0.5rem !important;
    }

    /* --- CARTES AUX COULEURS VIVES ET FLUSHYS COMPACTES --- */
    .card-base {
        padding: 12px 18px;
        border-radius: 10px;
        margin-bottom: 10px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        border-left: 6px solid rgba(0,0,0,0.2);
    }

    /* Couleurs ultra-flashy */
    .card-gold { background: linear-gradient(135deg, #FFB703 0%, #FB8500 100%); }   /* Orange Mécanique */
    .card-cyan { background: linear-gradient(135deg, #00B4D8 0%, #0077B6 100%); }   /* Bleu Électrique */
    .card-purple { background: linear-gradient(135deg, #9D4EDD 0%, #7B2CBF 100%); } /* Violet Néon */
    .card-green { background: linear-gradient(135deg, #2ECC71 0%, #27AE60 100%); }  /* Vert Toxique */
    .card-red { background: linear-gradient(135deg, #FF4D4D 0%, #D90429 100%); }    /* Rouge Flash */

    /* Forcer le texte lisible à l'intérieur des cartes */
    .card-gold *, .card-cyan * { color: #000000 !important; font-weight: 500; }
    .card-purple *, .card-green *, .card-red * { color: #FFFFFF !important; }
    
    /* Inputs à l'intérieur des cartes */
    .card-base label { font-size: 13px !important; font-weight: bold !important; }

    /* Blocs KPI du bas ultra-flashy */
    .kpi-card {
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        color: white !important;
    }
    .kpi-green { background: #234E40; border: 2px solid #2ECC71; }
    .kpi-orange { background: #4E3E23; border: 2px solid #FFB703; }
    .kpi-red { background: #4E232B; border: 2px solid #FF4D4D; }

    /* Encadré institutionnel CDSG Tricolore / Impactant */
    .institution-box {
        background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
        border: 2px solid #2563EB;
        padding: 12px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .institution-box * { color: #1E40AF !important; }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================================================================
# MOTEUR DE CALCULS TECHNIQUES
# ==============================================================================
def normaliser_en_kg(poids, unite):
    return poids if unite == "kg" else poids / 1000.0

def declencher_mise_a_jour():
    pass

# ==============================================================================
# EN-TÊTE DU DASHBOARD (Très compact)
# ==============================================================================
st.markdown("<p style='margin:0; font-size:12px; font-weight:bold; color:#2563EB !important;'>🎖️ PROJET ÉCO-CITOYEN — CADRE CLASSE CDSG</p>", unsafe_allow_html=True)
st.markdown("<h2 style='margin:0 0 5px 0; padding:0; font-size:26px;'>🍏 Plateforme Réseau de Pilotage Environnemental</h2>", unsafe_allow_html=True)
st.markdown("<p style='margin:0 0 10px 0; font-size:14px;'><b>Collège Jean Giono (Orange)</b> — Impact des 700 demi-pensionnaires | Référent : M. Thierry Armant</p>", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# STRUCTURE EN 3 COLONNES POUR ÉVITER LE SCROLL
# ------------------------------------------------------------------------------
col_gauche, col_milieu, col_droite = st.columns([1, 1, 1.2])

# ==========================================
# COLONNE 1 : Volet A (Consommables / Pain)
# ==========================================
with col_gauche:
    st.markdown("<h4 style='margin:0 0 5px 0; font-size:16px; border-bottom:2px solid #FFB703;'>🥖 Volet A : Reliquats & Papier</h4>", unsafe_allow_html=True)

    # --- Poubelle à Pain ---
    st.markdown('<div class="card-base card-gold">', unsafe_allow_html=True)
    st.markdown("<h5 style='margin:0; font-size:14px;'>Pain perdu (Boulangerie)</h5>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    poids_pain = c1.number_input("Masse :", min_value=0.0, value=4.0, step=0.5, key="pain", label_visibility="collapsed")
    unite_pain = c2.selectbox("Unité :
