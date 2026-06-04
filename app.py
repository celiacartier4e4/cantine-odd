import streamlit as st
import pandas as pd

# ==============================================================================
# CONFIGURATION DE LA PAGE
# ==============================================================================
st.set_page_config(
    page_title="Collège Jean Giono d'Orange - CDSG",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- INJECTION CSS SÉCURISÉE POUR L'ARRIÈRE-PLAN ET LES CARTES COLORÉES ---
css_code = """
<style>
/* Enlever les marges par défaut de Streamlit */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    padding-left: 3rem !important;
    padding-right: 3rem !important;
}

/* Image de fond : Avenue Charles Dardun, Orange */
.stApp {
    background: linear-gradient(rgba(255, 255, 255, 0.1), rgba(15, 23, 42, 0.4)), 
                url('https://images.unsplash.com/photo-1541339907198-e08756dedf3f?q=80&w=1920') no-repeat center center fixed;
    background-size: cover;
}

/* Style des titres principaux */
.main-title {
    color: #0f172a !important;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 42px !important;
    font-weight: bold;
    margin-bottom: 0px !important;
}
.sub-title {
    color: #1e293b !important;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 20px !important;
    margin-top: 0px !important;
    margin-bottom: 25px !important;
}

/* Structure des blocs de saisie colorés */
.card {
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    font-family: 'Segoe UI', Arial, sans-serif;
}
.card-title {
    font-size: 18px !important;
    font-weight: bold !important;
    margin-bottom: 12px !important;
}
.card-analysis {
    font-size: 13px !important;
    margin-top: 10px !important;
    font-weight: 500;
}

/* Couleurs vives des blocs */
.bg-gold { background-color: #ffb703; color: #000000 !important; }
.bg-cyan { background-color: #00f5ff; color: #000000 !important; }
.bg-purple { background-color: #a855f7; color: #ffffff !important; }
.bg-green { background-color: #22c55e; color: #ffffff !important; }
.bg-red { background-color: #ef4444; color: #ffffff !important; }
.bg-dark { background-color: #0f172a; color: #ffffff !important; border: 1px solid #38bdf8; }

/* Panneau de synthèse du bas */
.bottom-panel {
    background-color: #090d16;
    border-radius: 12px;
    padding: 20px;
    margin-top: 30px;
    border: 1px solid #1e293b;
}
.bottom-title {
    color: #ffffff !important;
    font-size: 16px !important;
    font-weight: bold;
}
.kpi-box {
    padding: 10px;
    border-radius: 20px;
    text-align: center;
    font-weight: bold;
    font-size: 14px;
}
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

# ==============================================================================
# EN-TÊTE DE L'APPLICATION
# ==============================================================================
st.markdown('<p class="main-title">Collège Jean Giono d\'Orange</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Projet Éco-Citoyen - CDSG Giono</p>', unsafe_allow_html=True)

# ==============================================================================
# DISPOSITION EN DEUX COLONNES PRINCIPALES
# ==============================================================================
col_gauche, col_droite = st.columns(2)

# --- COLONNE GAUCHE ---
with col_gauche:
    # 1. Reliquats de Pain
    st.markdown('<div class="card bg-gold"><p class="card-title">🥖 Reliquats de Pain (Boulangerie)</p>', unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    poids_pain = c1.number_input("Masse totale mesurée :", min_value=0.0, value=4.0, step=0.5, key="pain", label_visibility="visible")
    unite_pain = c2.selectbox("Unité :", ["kg", "g"], key="u_pain
