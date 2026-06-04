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

# --- STYLE CSS : COULEURS VIVES, LUMINEUSES ET CONTRASTÉES ---
st.markdown(
    """
    <style>
    /* Fond principal clair et ultra lumineux */
    .stApp {
        background: linear-gradient(135deg, #F0F4F8 0%, #E2E8F0 100%);
    }

    /* Textes généraux en bleu nuit très foncé pour un contraste maximal */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stText {
        color: #0F172A !important;
        font-family: 'Segoe UI', Roboto, Helvetica, sans-serif;
    }

    /* Séparation centrale des colonnes */
    [data-testid="column"]:nth-child(1) {
        border-right: 2px dashed #94A3B8;
        padding-right: 40px;
    }
    [data-testid="column"]:nth-child(2) {
        padding-left: 40px;
    }

    /* --- CARTES AUX COULEURS VIVES ET FLUSHYS --- */
    .card-base {
        padding: 25px;
        border-radius: 14px;
        margin-bottom: 35px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
        border: 2px solid #FFFFFF;
    }

    /* Fonds colorés vifs avec textes adaptés pour rester lisibles */
    .card-gold { background-color: #FFB703; } /* Jaune/Orange vif */
    .card-cyan { background-color: #00B4D8; } /* Cyan électrique */
    .card-purple { background-color: #9D4EDD; } /* Violet fluo */
    .card-green { background-color: #2ECC71; } /* Vert néon */
    .card-red { background-color: #FF4D4D; } /* Rouge flashy */

    /* Forcer le texte en blanc ou noir à l'intérieur des cartes */
    .card-gold *, .card-cyan * { color: #000000 !important; }
    .card-purple *, .card-green *, .card-red * { color: #FFFFFF !important; }

    /* Blocs indicateurs de performance du bas (KPIs) */
    .kpi-card {
        background: #FFFFFF;
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #E2E8F0;
    }

    /* Encadré institutionnel CDSG */
    .institution-box {
        background: #E0F2FE;
        border: 2px solid #3B82F6;
        padding: 22px;
        border-radius: 12px;
        margin-bottom: 35px;
    }
    .institution-box * {
        color: #1E3A8A !important;
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

# ------------------------------------------------------------------------------
# INTERFACE EN DEUX GRANDES COLONNES
# ------------------------------------------------------------------------------
col_gauche, col_droite = st.columns([1.3, 1])

# Création d'une zone tampon pour injecter le graphique à gauche plus tard dans le script
with col_gauche:
    st.markdown("### 📊 Répartition de la Masse des Déchets (kg)")
    st.write(" ")
    emplacement_graphique = st.container()

# ==========================================
# COLONNE DROITE : Saisie de toutes les catégories (Empilées)
# ==========================================
with col_droite:
    st.markdown("### 📋 Formulaire de Saisie des Déchets")
    st.write(" ")
    
    # --- CATEGORIE 1 : Biodéchets ---
    st.markdown('<div class="card-base card-green">', unsafe_allow_html=True)
    st.markdown("#### 🗑️ Biodéchets — Restes de Plats Cuisinés")
    poids_alim = st.number_input("Masse totale mesurée :", min_value=0.0, value=25.0, step=1.0, key="alim")
    unite_alim = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_alim")
    kg_alim = normaliser_en_kg(poids_alim, unite_alim)
    equiv_repas = int(kg_alim / 0.150)
    st.markdown(f"📊 **Analyse d'équivalence :** Environ **{equiv_repas} repas complets** rejetés.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 2 : Poubelle à Pain ---
    st.markdown('<div class="card-base card-gold">', unsafe_allow_html=True)
    st.markdown("#### 🥖 Reliquats de Pain (Boulangerie)")
    poids_pain = st.number_input("Masse totale mesurée :", min_value=0.0, value=4.0, step=0.5, key="pain")
    unite_pain = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_pain")
    kg_pain = normaliser_en_kg(poids_pain, unite_pain)
    equiv_baguettes = int(kg_pain / 0.250)
    st.markdown(f"📊 **Analyse d'équivalence :** Environ **{equiv_baguettes} baguettes** de 250g perdues.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 3 : Fruits entamés ---
    st.markdown('<div class="card-base card-red">', unsafe_allow_html=True)
    st.markdown("#### 🍎 Pertes sur les Fruits")
    poids_fruits = st.number_input("Masse totale mesurée :", min_value=0.0, value=2.0, step=0.2, key="fruits")
    unite_fruits = st.selectbox("Unité de mesure :",
