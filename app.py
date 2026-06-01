import streamlit as st

# --- STYLE CSS GLOBAL : FOND BLEU NUIT ET ENCADRÉS ROSES ---
st.markdown(
    """
    <style>
    /* 1. Fond du site en bleu nuit profond */
    .stApp {
        background-color: #0A1128;
    }

    /* 2. Terre fixe en arrière-plan */
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

    /* 3. Textes généraux en blanc */
    h1, h2, h3, h4, h5, h6, .stMarkdown, p, li, label, .stText {
        color: #FFFFFF !important;
    }

    /* 4. Textes foncés à l'intérieur des boîtes roses pour le contraste */
    [style*="background-color: #FFB6C1"] h2,
    [style*="background-color: #FFB6C1"] p,
    [style*="background-color: #FFB6C1"] li,
    [style*="background-color: #FFB6C1"] label {
        color: #111111 !important;
    }

    /* 5. Création de la ligne épaisse NOIRE entre les deux colonnes */
    [data-testid="column"]:nth-child(1) {
        border-right: 5px solid #000000; /* Ligne noire */
        padding-right: 30px;
    }
    
    [data-testid="column"]:nth-child(2) {
        padding-left: 30px;
    }

    /* Style spécifique pour la boîte MISSION (en rose) */
    .mission-box {
        background-color: #FFB6C1;
        border: 2px solid #FFFFFF;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 15px rgba(255, 182, 193, 0.4);
        text-align: center;
        margin-bottom: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titre principal
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
    st.markdown('<div style="background-color: #FFB6C1; border: 2px solid #FFFFFF; padding: 15px; border-radius: 10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.2); margin-bottom: 25px;">', unsafe_allow_html=True)
    st.subheader("🧻 Serviettes en papier")
    poids_serviettes = st.number_input("Ajustez la valeur :", min_value=0.0, value=3.0, step=0.5, key="serviettes")
    unite_serviettes = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_serviettes")
    st.write(f"**Poids enregistré :** {poids_serviettes} {unite_serviettes}")
    
    # Équivalence Serviettes (1 serviette = 3g)
    val_serviettes = poids_serviettes if unite_serviettes == "kg" else poids_serviettes / 1000
    nb_serviettes = int(val_serviettes / 0.003)
    st.write(f"💡 *Cela représente environ **{nb_serviettes} serviettes** jetées !*")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 5 : Emballages ---
    st.markdown('<div style="background-color: #FFB6C1; border: 2px solid #FFFFFF; padding: 15px; border-radius: 10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.2); margin-bottom: 25px;">', unsafe_allow_html=True)
    st.subheader("📦 Emballages")
    poids_emballages = st.number_input("Ajustez la valeur :", min_value=0.0, value=6.0, step=0.5, key="emballages")
    unite_emballages = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_emballages")
    st.write(f"**Poids enregistré :** {poids_emballages} {unite_emballages}")
    
    # Équivalence Emballages (1 emballage = 20g)
    val_emballages = poids_emballages if unite_emballages == "kg" else poids_emballages / 1000
    nb_emballages = int(val_emballages / 0.020)
    st.write(f"💡 *Cela représente environ **{nb_emballages} emballages** jetés !*")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 2 : Poubelle à Pain ---
    st.markdown('<div style="background-color: #FFB6C1; border: 2px solid #FFFFFF; padding: 15px; border-radius: 10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.2); margin-bottom: 25px;">', unsafe_allow_html=True)
    st.subheader("🥖 Poubelle à Pain")
    poids_pain = st.number_input("Ajustez la valeur :", min_value=0.0, value=8.0, step=0.5, key="pain")
    unite_pain = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_pain")
    st.write(f"**Poids enregistré :** {poids_pain} {unite_pain}")
    
    # Équivalence Pain (1 baguette = 250g)
    val_pain = poids_pain if unite_pain == "kg" else poids_pain / 1000
    nb_baguettes = int(val_pain / 0.25)
    st.write(f"💡 *Cela représente environ **{nb_baguettes} baguettes** perdues !*")
    st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# COLONNE DROITE
# ==========================================
with col_droite:
    
    # --- CATEGORIE 1 : Déchets Alimentaires ---
    st.markdown('<div style="background-color: #FFB6C1; border: 2px solid #FFFFFF; padding: 15px; border-radius: 10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.2); margin-bottom: 25px;">', unsafe_allow_html=True)
    st.subheader("🗑️ Déchets Alimentaires")
    poids_alim = st.number_input("Ajustez la valeur :", min_value=0.0, value=42.0, step=0.5, key="alim")
    unite_alim = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_alim")
    st.write(f"**Poids enregistré :** {poids_alim} {unite_alim}")
    
    # Équivalence Repas (1 repas = 150g)
    val_alim = poids_alim if unite_alim == "kg" else poids_alim / 1000
    nb_repas = int(val_alim / 0.150)
    st.write(f"💡 *Cela représente environ **{nb_repas} repas complets** jetés !*")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 3 : Fruits entamés ---
    st.markdown('<div style="background-color: #FFB6C1; border: 2px solid #FFFFFF; padding: 15px; border-radius: 10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.2); margin-bottom: 25px;">', unsafe_allow_html=True)
    st.subheader("🍎 Fruits entamés")
    poids_fruits = st.number_input("Ajustez la valeur :", min_value=0.0, value=5.0, step=0.5, key="fruits")
    unite_fruits = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_fruits")
    st.write(f"**Poids enregistré :** {poids_fruits} {unite_fruits}")
    
    # Équivalence Fruits (1 fruit = 120g)
    val_fruits = poids_fruits if unite_fruits == "kg" else poids_fruits / 1000
    nb_fruits = int(val_fruits / 0.120)
    st.write(f"💡 *Cela représente environ **{nb_fruits} fruits entiers** gaspillés !*")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- ENCADRÉ MISSION ---
    st.markdown(
        """
        <div class="mission-box">
            <h2 style="color: #FF4B4B; margin: 0;">🎯 MISSION</h2>
            <p style="font-size: 22px; font-weight: bold; color: #111111; margin-bottom: 10px;">Réduire le gaspillage</p>
            <p style="font-size: 14px; color: #333333; font-style: italic; margin: 0; padding-top: 10px; border-top: 1px dashed #111111;">
                Restes d'assiettes - Objectif : Réduire le gaspillage direct !
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
