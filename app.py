import streamlit as st

# --- STYLE CSS GLOBAL : FOND BLEU NUIT PROFOND ET TERRE FIXE ---
st.markdown(
    """
    <style>
    /* 1. Définit le fond de tout le site en bleu nuit très foncé */
    .stApp {
        background-color: #0A1128; /* Bleu nuit espace profond */
    }

    /* 2. Ajoute la Terre fixe en arrière-plan */
    [data-testid="stAppViewContainer"]::before {
        content: "";
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%); /* Centre parfaitement */
        width: 100vw; /* Utilise toute la largeur visible */
        height: 100vh; /* Utilise toute la hauteur visible */
        background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/The_Earth_seen_from_Apollo_17.jpg/800px-The_Earth_seen_from_Apollo_17.jpg");
        background-size: contain; /* Adapte l'image sans la recadrer */
        background-repeat: no-repeat;
        background-position: center;
        opacity: 0.18; /* Subtile pour préserver la lisibilité */
        z-index: -1; /*
