import streamlit as st

# --- STYLE CSS : DESIGN CAPTIVANT & POP MODERNE ---
st.markdown(
    """
    <style>
    /* Fond de l'application - Bleu nuit profond */
    .stApp {
        background-color: #0F172A;
    }

    /* Arrière-plan Terre très discret */
    [data-testid="stAppViewContainer"]::before {
        content: "";
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 100vw;
        height: 100vh;
        background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/The_Earth_seen_from_Apollo_17.jpg/800px-The_Earth_seen_from_Apollo_17.jpg");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        opacity: 0.08;
        z-index: -1;
    }

    /* Typographie globale */
    h1, h2, h3, h4, h5, h6, .stMarkdown, p, li, label, .stText {
        color: #F8FAFC !important;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    /* Grand Titre en dégradé Flashy/Propre */
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FFB6C1, #38EF7D, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
        text-align: center;
    }

    /* Sous-titre animé ou mis en valeur */
    .subtitle {
        font-size: 1.2rem;
        text-align: center;
        color: #94A3B8 !important;
        margin-bottom: 30px;
    }

    /* Séparation des colonnes par un filet discret */
    [data-testid="column"]:nth-child(1) {
        border-right: 2px dashed rgba(255, 182, 193, 0.2);
        padding-right: 30px;
    }
    
    [data-testid="column"]:nth-child(2) {
        padding-left: 30px;
    }

    /* Cartes de saisie avec effet de survol (Hover) */
    .pop-card {
        background: rgba(30, 41, 59, 0.7);
        border: 2px solid rgba(255, 182, 193, 0.4);
        padding: 22px;
        border-radius: 16px;
        margin-bottom: 25px;
        transition: all 0.3s ease;
    }
    .pop-card:hover {
        transform: translateY(-5px);
        border-color: #FFB6C1;
        box-shadow: 0px 8px 20px rgba(255, 182, 193, 0.15);
    }
    
    /* Version de carte avec bordure verte */
    .pop-card-green {
        background: rgba(30, 41, 59, 0.7);
        border: 2px solid rgba(56, 239, 125, 0.4);
        padding: 22px;
        border-radius: 16px;
        margin-bottom: 25px;
        transition: all 0.3s ease;
    }
    .pop-card-green:hover {
        transform: translateY(-5px);
        border-color: #38EF7D;
        box-shadow: 0px 8px 20px rgba(56, 239, 125, 0.15);
    }

    /* Boîte Défi : Look bannière d'événement */
    .challenge-box {
        background: linear-gradient(135deg, #11998E, #38EF7D);
        border: none;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0px 4px 20px rgba(56, 239, 125, 0.25);
        text-align: center;
        margin-bottom: 25px;
    }
    .challenge-box h2, .challenge-box p {
        color: #FFFFFF !important;
    }

    /* Conteneur pour la barre de progression custom */
    .progress-text {
        display: flex;
        justify-content: space-between;
        font-size: 0.9rem;
        margin-bottom: 5px;
        color: #94A3B8 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- ENTÊTE ---
st.markdown('<h1 class="main-title">🚀 Mission : Zéro Gaspi Giono</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Le QG secret des Éco-Héros du Collège Jean Giono • ODD 12</p>', unsafe_allow_html=True)

# --- BARRE DE PROGRESSION GLOBALE (COMMUNAUTÉ) ---
# Un élément visuel fort dès l'entrée pour montrer l'effort collectif
st.markdown('### 🌍 Objectif Collectif du Collège')
st.markdown('<div class="progress-text"><span>Avancement de la mission</span><span>75% Réussi</span></div>', unsafe_allow_html=True)
st.progress(0.75)
