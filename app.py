import streamlit as st

# ==============================================================================
# CONFIGURATION DE LA PAGE
# ==============================================================================
st.set_page_config(
    page_title="Dashboard Éco-Citoyen - CDSG Giono",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- STYLE CSS NETTOYÉ ---
st.markdown(
    """
    <style>
    /* Fond principal clair et lumineux */
    .stApp {
        background: linear-gradient(135deg, #F0F4F8 0%, #E2E8F0 100%);
    }

    /* Textes généraux en bleu nuit très foncé */
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

    /* CARTES AUX COULEURS VIVES */
    .card-base {
        padding: 25px;
        border-radius: 14px;
        margin-bottom: 35px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
        border: 2px solid #FFFFFF;
    }

    .card-gold { background-color: #FFB703; }
    .card-cyan { background-color: #00B4D8; }
    .card-purple { background-color: #9D4EDD; }
    .card-green { background-color: #2ECC71; }
    .card-red { background-color: #FF4D4D; }

    .card-gold *, .card-cyan * { color: #000000 !important; }
    .card-purple *, .card-green *, .card-red * { color: #FFFFFF !important; }

    .kpi-card {
        background: #FFFFFF;
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #E2E8F0;
    }

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

    /* STYLE DE LA JAUGE MULTICOLORE */
    .progress-container-multi {
        width: 100%;
        background-color: #E2E8F0;
        border-radius: 25px;
        display: flex;
        overflow: hidden;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.1);
        margin-top: 15px;
        margin-bottom: 5px;
        border: 1px solid #CBD5E1;
    }
    .progress-segment {
        height: 35px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        font-size: 13px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.4);
    }
    .segment-text-black {
        color: #000000 !important;
        text-shadow: none !important;
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
col_gauche, col_droite = st.columns(2)

# ==========================================
# COLONNE GAUCHE : Volet A (Suivi Consommables)
# ==========================================
with col_gauche:
    st.markdown("### 📋 Volet A : Suivi des Consommables et Féculents")
    st.write(" ")
    
    # --- CATEGORIE : Poubelle à Pain (JAUNE) ---
    st.markdown('<div class="card-base card-gold">', unsafe_allow_html=True)
    st.markdown("#### 🥖 Reliquats de Pain (Boulangerie)")
    poids_pain = st.number_input("Masse totale mesurée :", min_value=0.0, value=4.0, step=0.5, key="pain")
    unite_pain = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_pain")
    kg_pain = normaliser_en_kg(poids_pain, unite_pain)
    equiv_baguettes = int(kg_pain / 0.250)
    st.markdown(f"📊 **Analyse d'équivalence :** Environ **{equiv_baguettes} baguettes** de 250g perdues.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE : Serviettes en papier (CYAN) ---
    st.markdown('<div class="card-base card-cyan">', unsafe_allow_html=True)
    st.markdown("#### 🧻 Consommation de Serviettes en Papier")
    poids_serviettes = st.number_input("Masse totale mesurée :", min_value=0.0, value=1.5, step=0.1, key="serviettes")
    unite_serviettes = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_serviettes")
    kg_serviettes = normaliser_en_kg(poids_serviettes, unite_serviettes)
    equiv_serviettes = int(kg_serviettes / 0.003)
    st.markdown(f"📊 **Analyse d'équivalence :** Environ **{equiv_serviettes} unités** de serviettes jetées.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE : Emballages (VIOLET) ---
    st.markdown('<div class="card-base card-purple">', unsafe_allow_html=True)
    st.markdown("#### 📦 Flux des Emballages Non Recyclés")
    poids_emballages = st.number_input("Masse totale mesurée :", min_value=0.0, value=3.0, step=0.5, key="emballages")
    unite_emballages = st.selectbox("Unité de mesure :",
