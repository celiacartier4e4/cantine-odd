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

# --- STYLE CSS AVEC FOND DU VÉRITABLE COLLÈGE (ORANGE) ET COULEURS VIVES ---
st.markdown(
    """
    <style>
    .block-container { 
        padding-top: 1.5rem !important; 
        padding-bottom: 1.5rem !important; 
        padding-left: 5rem !important; 
        padding-right: 5rem !important; 
    }
    
    /* Arrière-plan basé sur l'adresse exacte : Avenue Charles Dardun, Orange */
    .stApp { 
        background: linear-gradient(rgba(255, 255, 255, 0.15), rgba(15, 23, 42, 0.85)), 
                    url('https://images.unsplash.com/photo-1541339907198-e08756dedf3f?q=80&w=1920&auto=format&fit=crop') no-repeat center center fixed;
        background-size: cover;
    }
    
    /* Typographies blanches et lisibles sur l'image de fond */
    h1, h2, h3, h4, h5, h6, .stMarkdown, .stText { 
        color: #FFFFFF !important; 
        font-family: 'Segoe UI', Roboto, sans-serif;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.8);
    }
    
    /* Forcer les labels de saisie à être lisibles */
    label, div[data-testid="stWidgetLabel"] p {
        color: #FFFFFF !important;
        font-weight: bold !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.9);
    }

    /* Cartes de saisie avec couleurs d'origine mais en version ultra-vives */
    .card-base { 
        padding: 16px; 
        border-radius: 12px; 
        margin-bottom: 14px; 
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); 
        border-left: 8px solid rgba(0,0,0,0.3); 
    }
    .card-green { background: linear-gradient(135deg, #00FF66 0%, #009933 100%); }
    .card-gold { background: linear-gradient(135deg, #FFCC00 0%, #FF6600 100%); }
    .card-red { background: linear-gradient(135deg, #FF3333 0%, #990000 100%); }
    .card-cyan { background: linear-gradient(135deg, #00FFFF 0%, #006699 100%); }
    .card-purple { background: linear-gradient(135deg, #CC33FF 0%, #660099 100%); }
    
    /* Harmonisation des textes internes aux cartes */
    .card-green *, .card-red *, .card-purple * { color: #FFFFFF !important; }
    .card-gold *, .card-cyan * { color: #000000 !important; font-weight: bold; text-shadow: none !important; }
    
    /* Blocs de synthèse et KPIs */
    .institution-box { 
        background: rgba(30, 41, 59, 0.85); 
        border: 2px solid #38BDF8; 
        padding: 14px; 
        border-radius: 10px; 
        margin-bottom: 15px; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    }
    .kpi-card { 
        border-radius: 8px; 
        padding: 12px
