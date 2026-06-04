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

# --- STYLE CSS (SÉCURISÉ & OPTIMISÉ POUR LE CONTRASTE) ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #F8FAFC 0%, #E2E8F0 100%);
    }
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
        color: #0F172A !important;
        font-family: 'Segoe UI', Roboto, sans-serif;
    }
    .category-box {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #3B82F6;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .institution-box {
        background: #EFF6FF;
        border: 2px solid #3B82F6;
        padding: 20px;
        border-radius: 12px;
        margin-top: 10px;
    }
    .institution-box * {
        color: #1E40AF !important;
    }
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
# EN-TÊTE DU DASHBOARD
# ==============================================================================
st.markdown("#### 🎖️ PROJET ÉCO-CITOYEN — CADRE CLASSE CDSG")
st.title("🍏 Plateforme de Pilotage Environnemental")
st.markdown("##### **Collège Jean Giono (Orange)** — Impact des 700 demi-pensionnaires | Référent : M. Thierry Armant")
st.markdown("---")

# ==============================================================================
# ETAPE 1 : ZONE DE SAISIE DES DONNÉES (2 COLONNES)
# ==============================================================================
col_gauche, col_droite = st.columns(2)

# --- COLONNE GAUCHE : Volet A (Consommables & Féculents) ---
with col_gauche:
    st.markdown("### 📋 Volet A : Suivi des Consommables et Féculents")
    
    # Catégorie : Pain
    st.markdown('<div class="category-box" style="border-left-color: #FFB703;">', unsafe_allow_html=True)
    st.markdown("#### 🥖 Reliquats de Pain (Boulangerie)")
    poids_pain = st.number_input("Masse mesurée :", min_value=0.0, value=4.0, step=0.5, key="pain", on_change=declencher_mise_a_jour)
    unite_pain = st.selectbox("Unité :", ["kg", "g"], key="u_pain")
    kg_pain = normaliser_en_kg(poids_pain, unite_pain)
    equiv_baguettes = int(kg_pain / 0.250)
    st.markdown(f"💡 *Équivalence : environ **{equiv_baguettes} baguettes** perdues.*")
    st.markdown('</div>', unsafe_allow_html=True)

    # Catégorie : Serviettes
    st.markdown('<div class="category-box" style="border-left-color: #00B4D8;">', unsafe_allow_html=True)
    st.markdown("#### 🧻 Consommation de Serviettes en Papier")
    poids_serviettes = st.number_input("Masse mesurée :", min_value=0.0, value=1.5, step=0.1, key="servi
