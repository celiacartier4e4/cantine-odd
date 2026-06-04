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

    /* Fonds colorés vifs pour chaque catégorie */
    .card-gold { background-color: #FFB703; } /* Jaune/Orange */
    .card-cyan { background-color: #00B4D8; } /* Cyan */
    .card-purple { background-color: #9D4EDD; } /* Violet */
    .card-green { background-color: #2ECC71; } /* Vert */
    .card-red { background-color: #FF4D4D; } /* Rouge */

    /* Forcer le texte lisible à l'intérieur des cartes */
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

    /* --- STYLE DE LA JAUGE MULTICOLORE PERSONNALISÉE --- */
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
        transition: width 0.5s ease-in-out;
        display: flex
