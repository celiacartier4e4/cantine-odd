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

# --- STYLE CSS : COMPACTAGE MAXIMAL & EXPLOSION DE COULEURS ---
st.markdown(
    '''
    <style>
    /* Supprimer les espaces natifs inutiles de Streamlit pour forcer le single-page */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    
    /* Fond de page professionnel et lumineux */
    .stApp {
        background: linear-gradient(135deg, #F8FAFC 0%, #E2E8F0 100%);
    }

    /* Textes généraux sombres pour un contraste maximal */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stText {
        color: #0F172A !important;
        font-family: 'Segoe UI', Roboto, sans-serif;
    }

    /* Optimisation des espacements des blocs */
    div[data-testid="stBlock"] {
        gap: 0.5rem !important;
    }

    /* --- CARTES AUX COULEURS VIVES ET FLUSHYS --- */
    .card-base {
        padding: 12px 18px;
        border-radius: 10px;
        margin-bottom: 10px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        border-left: 6px solid rgba(0,0,0,0.2);
    }

    /* Dégradés ultra-vifs pour attirer l'œil du jury */
    .card-gold { background: linear-gradient(135deg, #FFB703 0%, #FB8500 100%); }
    .card-cyan { background: linear-gradient(135deg, #00B4D8 0%, #0077B6 100%); }
    .card-purple { background: linear-gradient(135deg, #9D4EDD 0%, #7B2CBF 100%); }
    .card-green { background: linear-gradient(135deg, #2ECC71 0%, #27AE60 100%); }
    .card-red { background: linear-gradient(135deg, #FF4D4D 0%, #D90429 100%); }

    /* Forcer la lisibilité des textes selon le fond */
    .card-gold *, .card-cyan * { color: #000000 !important; font-weight: 500; }
    .card-purple *, .card-green *, .card-red * { color: #FFFFFF !important; }
    
    .card-base label { font-size: 13px !important; font-weight: bold !important; }

    /* Blocs indicateurs du bas (KPIs) stylisés et colorés */
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

    /* Encadré institutionnel CDSG bleu républicain */
    .institution-box {
        background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
        border: 2px solid #2563EB;
        padding: 12px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .institution-box * { color: #1E40AF !important; }
    </style>
    ''',
    unsafe_allow_html=True
)

# ==============================================================================
# MOTEUR DE CALCULS TECHNIQUES
# ==============================================================================
def normaliser_en_kg(p
