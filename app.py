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
        transform: translate(-50%, -50%);
        width: 100vw;
        height: 100vh;
        background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/The_Earth_seen_from_Apollo_17.jpg/800px-The_Earth_seen_from_Apollo_17.jpg");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        opacity: 0.18;
        z-index: -1;
    }

    /* 3. Style pour les textes principaux pour qu'ils soient lisibles sur fond foncé */
    h1, h2, h3, h4, h5, h6, .stMarkdown, p, li, label, .stText {
        color: #FFFFFF !important;
    }

    /* 4. Style pour les éléments dans les encadrés jaunes foncés (lisibilité) */
    [style*="background-color: #FFD700"] h2,
    [style*="background-color: #FFD700"] p,
    [style*="background-color: #FFD700"] li,
    [style*="background-color: #FFD700"] label {
        color: #111111 !important;
    }

    /* 5. Création de la ligne épaisse entre les deux colonnes */
    [data-testid="column"]:nth-child(1) {
        border-right: 5px solid #FFFFFF;
        padding-right: 30px;
    }
    
    [data-testid="column"]:nth-child(2) {
        padding-left: 30px;
    }

    /* Style pour les encadrés jaunes (réutilisé pour la mission) */
    .mission-box {
        background-color: #FFD700;
        border: 2px solid #FFFFFF;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 15px rgba(255,215,0,0.3);
        text-align: center;
        margin-bottom: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titre principal de la page
st.title("🍏 Objectif Zéro Gaspi - Collège Jean Giono 🍎")
st.subheader("Suivi des déchets pour 700 demi-pensionnaires (ODD 12)")

st.write("""
**À vous de jouer !** Utilisez les flèches pour augmenter ou diminuer le chiffre, puis choisissez l'unité (g ou kg).
""")

st.markdown("### 📊 Nos Pesées Hebdomadaires")

# Création des deux colonnes
col_gauche, col_droite = st.columns(2)

# ==========================================
# COLONNE GAUCHE
# ==========================================
with col_gauche:
    
    # --- CATEGORIE 4 : Serviettes en papier ---
    st.markdown('<div style="background-color: #FFD700; border: 2px solid #FFFFFF; padding: 15px; border-radius: 10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.2); margin-bottom: 25px;">', unsafe_allow_html=True)
    st.subheader("🧻 Serviettes en papier")
    poids_serviettes = st.number_input("Ajustez la valeur :", min_value=0.0, value=3.0, step=0.5, key="serviettes")
    unite_serviettes = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_serviettes")
    st.write(f"**Poids enregistré :** {poids_serviettes} {unite_serviettes}")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 5 : Emballages ---
    st.markdown('<div style="background-color: #FFD700; border: 2px solid #FFFFFF; padding: 15px; border-radius: 10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.2); margin-bottom: 25px;">', unsafe_allow_html=True)
    st.subheader("📦 Emballages")
    poids_emballages = st.number_input("Ajustez la valeur :", min_value=0.0, value=6.0, step=0.5, key="emballages")
    unite_emballages = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_emballages")
    st.write(f"**Poids enregistré :** {poids_emballages} {unite_emballages}")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 2 : Poubelle à Pain ---
    st.markdown('<div style="background-color: #FFD700; border: 2px solid #FFFFFF; padding: 15px; border-radius: 10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.2); margin-bottom: 25px;">', unsafe_allow_html=True)
    st.subheader("🥖 Poubelle à Pain")
    poids_pain = st.number_input("Ajustez la valeur :", min_value=0.0, value=8.0, step=0.5, key="pain")
    unite_pain = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_pain")
    st.write(f"**Poids enregistré :** {poids_pain} {unite_pain}")

    # Calcul automatique du nombre de baguettes
    valeur_pain = poids_pain
    if unite_pain == "g":
        valeur_pain = valeur_pain / 1000
    nb_baguettes = int(valeur_pain / 0.25)
    st.write(f"💡 *Cela représente environ **{nb_baguettes} baguettes** perdues !*")
    st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# COLONNE DROITE
# ==========================================
with col_droite:
    
    # --- CATEGORIE 1 : Déchets Alimentaires ---
    st.markdown('<div style="background-color: #FFD700; border: 2px solid #FFFFFF; padding: 15px; border-radius: 10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.2); margin-bottom: 25px;">', unsafe_allow_html=True)
    st.subheader("🗑️ Déchets Alimentaires")
    poids_alim = st.number_input("Ajustez la valeur :", min_value=0.0, value=42.0, step=0.5, key="alim")
    unite_alim = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_alim")
    st.write(f"**Poids enregistré :** {poids_alim} {unite_alim}")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 3 : Fruits entamés ---
    st.markdown('<div style="background-color: #FFD700; border: 2px solid #FFFFFF; padding: 15px; border-radius: 10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.2); margin
