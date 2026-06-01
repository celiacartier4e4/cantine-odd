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
        z-index: -1; /* Place l'image derrière le contenu */
    }

    /* 3. Style pour les textes principaux pour qu'ils soient lisibles sur fond foncé */
    h1, h2, h3, h4, h5, h6, .stMarkdown, p, li, label, .stText {
        color: #FFFFFF !important; /* Force le texte en blanc */
    }

    /* 4. Style pour les éléments dans les encadrés jaunes (lisibilité) */
    [style*="background-color: #FFF2CC"] h2,
    [style*="background-color: #FFF2CC"] p,
    [style*="background-color: #FFF2CC"] li,
    [style*="background-color: #FFF2CC"] label {
        color: #31333F !important; /* Texte foncé dans les boîtes jaunes */
    }

    /* 5. Création de la ligne épaisse entre les deux colonnes */
    [data-testid="column"]:nth-child(1) {
        border-right: 5px solid #FFFFFF; /* Ligne blanche */
        padding-right: 30px;
    }
    
    [data-testid="column"]:nth-child(2) {
        padding-left: 30px;
    }

    /* Style pour les encadrés jaunes (réutilisé pour la mission) */
    .mission-box {
        background-color: #FFF2CC;
        border: 2px solid #E0E0E0;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
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
    st.markdown('<div style="background-color: #FFF2CC; border: 1px solid #E0E0E0; padding: 15px; border-radius: 10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.1); margin-bottom: 25px;">', unsafe_allow_html=True)
    st.subheader("🧻 Serviettes en papier")
    poids_serviettes = st.number_input("Ajustez la valeur :", min_value=0.0, value=3.0, step=0.5, key="serviettes")
    unite_serviettes = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_serviettes")
    st.write(f"**Poids enregistré :** {poids_serviettes} {unite_serviettes}")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 5 : Emballages ---
    st.markdown('<div style="background-color: #FFF2CC; border: 1px solid #E0E0E0; padding: 15px; border-radius: 10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.1); margin-bottom: 25px;">', unsafe_allow_html=True)
    st.subheader("📦 Emballages")
    poids_emballages = st.number_input("Ajustez la valeur :", min_value=0.0, value=6.0, step=0.5, key="emballages")
    unite_emballages = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_emballages")
    st.write(f"**Poids enregistré :** {poids_emballages} {unite_emballages}")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 2 : Poubelle à Pain ---
    st.markdown('<div style="background-color: #FFF2CC; border: 1px solid #E0E0E0; padding: 15px; border-radius: 10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.1); margin-bottom: 25px;">', unsafe_allow_html=True)
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
    st.markdown('<div style="background-color: #FFF2CC; border: 1px solid #E0E0E0; padding: 15px; border-radius: 10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.1); margin-bottom: 25px;">', unsafe_allow_html=True)
    st.subheader("🗑️ Déchets Alimentaires")
    poids_alim = st.number_input("Ajustez la valeur :", min_value=0.0, value=42.0, step=0.5, key="alim")
    unite_alim = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_alim")
    st.write(f"**Poids enregistré :** {poids_alim} {unite_alim}")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 3 : Fruits entamés ---
    st.markdown('<div style="background-color: #FFF2CC; border: 1px solid #E0E0E0; padding: 15px; border-radius: 10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.1); margin-bottom: 25px;">', unsafe_allow_html=True)
    st.subheader("🍎 Fruits entamés")
    poids_fruits = st.number_input("Ajustez la valeur :", min_value=0.0, value=5.0, step=0.5, key="fruits")
    unite_fruits = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_fruits")
    st.write(f"**Poids enregistré :** {poids_fruits} {unite_fruits}")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- ENCADRÉ : MISSION ---
    st.markdown(
        """
        <div class="mission-box">
            <h2 style="color: #FF4B4B; margin: 0;">🎯 MISSION</h2>
            <p style="font-size: 22px; font-weight: bold; color: #31333F; margin-bottom: 10px;">Réduire le gaspillage</p>
            <p style="font-size: 14px; color: #666666; font-style: italic; margin: 0; padding-top: 10px; border-top: 1px dashed #D0D0D0;">
                Restes d'assiettes — Objectif : Réduire le gaspillage direct !
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
