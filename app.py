import streamlit as st

# --- STYLE CSS : LOOK GAMING & CONTRASTE OPTIMISÉ ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0A1128;
    }

    /* Image de la Terre en fond discret */
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
        opacity: 0.12;
        z-index: -1;
    }

    /* Textes généraux en blanc */
    h1, h2, h3, h4, h5, h6, .stMarkdown, p, li, label, .stText {
        color: #FFFFFF !important;
    }

    /* Ligne de séparation au milieu */
    [data-testid="column"]:nth-child(1) {
        border-right: 3px dashed #FFB6C1;
        padding-right: 30px;
    }
    
    [data-testid="column"]:nth-child(2) {
        padding-left: 30px;
    }

    /* Cartes de saisie style "Gaming/Cyber" */
    .game-card {
        background: rgba(255, 182, 193, 0.15);
        border: 2px solid #FFB6C1;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 0px 15px rgba(255, 182, 193, 0.2);
        margin-bottom: 25px;
    }

    /* Boîte Mission Flashy */
    .mission-box {
        background: linear-gradient(135deg, #FF4B4B, #FF8585);
        border: 2px solid #FFFFFF;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(255, 75, 75, 0.4);
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* Grand Score de l'école */
    .score-banner {
        background: linear-gradient(135deg, #11998e, #38ef7d);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: white !important;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- ENTÊTE ---
st.title("🎮 Mission : Zéro Gaspi Giono")
st.subheader("Le QG des Éco-Héros du Collège Jean Giono 🚀")
st.write("Chaque pesée enregistrée change le score de la communauté. Remplis les données de la semaine et décroche les badges ! :trophy:")

# --- INITIALISATION DES VARIABLES DE CALCUL DU SCORE ---
# On va calculer un score global de réduction fictif basé sur les entrées de l'utilisateur
score_total = 1000

# --- DISPOSITION EN DEUX COLONNES ---
col_gauche, col_droite = st.columns(2)

# ==========================================
# COLONNE GAUCHE : LES PESÉES (INPUTS)
# ==========================================
with col_gauche:
    st.markdown("### 📝 Entre tes données de la semaine")

    # --- CATEGORIE 1 : Déchets Alimentaires ---
    st.markdown('<div class="game-card">', unsafe_allow_html=True)
    st.subheader("🗑️ Les Restes d'Assiettes")
    poids_alim = st.number_input("Poids mesuré :", min_value=0.0, value=42.0, step=1.0, key="alim")
    unite_alim = st.selectbox("Unité :", ["kg", "g"], key="u_alim")
    val_alim_kg = poids_alim if unite_alim == "kg" else poids_alim / 1000
    
    # Feedback visuel et fun
    nb_repas = int(val_alim_kg / 0.150)
    if val_alim_kg > 40:
        status_alim = "😰 Aïe ! C'est critique..."
        score_total -= 300
    else:
        status_alim = "⚡ Pas mal, on limite la casse !"
        score_total += 100
        
    st.write(f"**Impact :** {status_alim}")
    st.info(f"🍔 Ça équivaut à **{nb_repas} repas entiers** jetés à la poubelle.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 2 : Poubelle à Pain ---
    st.markdown('<div class="game-card">', unsafe_allow_html=True)
    st.subheader("🥖 Le Gâchis de Pain")
    poids_pain = st.number_input("Poids mesuré :", min_value=0.0, value=8.0, step=0.5, key="pain")
    unite_pain = st.selectbox("Unité :", ["kg", "g"], key="u_pain")
    val_pain_kg = poids_pain if unite_pain == "kg" else poids_pain / 1000
    
    nb_baguettes = int(val_pain_kg / 0.25)
    if val_pain_kg > 5:
        status_pain = "⚠️ Alerte overdose de croûtes !"
        score_total -= 150
    else:
        status_pain = "🥖 Champion de la miche !"
        score_total += 150

    st.write(f"**Impact :** {status_pain}")
    st.info(f"🥖 On a gaspillé de quoi faire **{nb_baguettes} baguettes** de boulanger.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 3 : Fruits entamés ---
    st.markdown('<div class="game-card">', unsafe_allow_html=True)
    st.subheader("🍎 Les Fruits abandonnés")
    poids_fruits = st.number_input("Poids mesuré :", min_value=0.0, value=5.0, step=0.5, key="fruits")
    unite_fruits = st.selectbox("Unité :", ["kg", "g"], key="u_fruits")
    val_fruits_kg = poids_fruits if unite_fruits == "kg" else poids_fruits / 1000
    
    nb_fruits = int(val_fruits_kg / 0.120)
    st.info(f"🍏 C'est l'équivalent de **{nb_fruits} fruits** à peine croqués.")
    st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# COLONNE DROITE : LE DASHBOARD GAMING (RÉSULTATS)
# ==========================================
with col_droite:
    st.markdown("### 🏆 Tableau des Éco-Scores")
    
    # Affichage du Score Éco-Héros Dynamique
    if score_total < 600:
        color_score = "🔴"
        rang = "Apprenti Gaspi"
    elif score_total < 900:
        color_score = "🟡"
        rang = "Gardien du Resto"
    else:
        color_score = "🟢"
        rang = "Maître Éco-Héros 👑"

    st.markdown(f"""
    <div class="score-banner">
        {color_score} Score Global : {score_total} XP<br>
        <span style="font-size: 16px; font-weight: normal;">Rang actuel : {rang}</span>
    </div>
    """, unsafe_allow_html=True)

    # --- ENCADRÉ MISSION DU JOUR ---
    st.markdown(
        """
        <div class="mission-box">
            <h2 style="color: #FFFFFF; margin: 0;">🎯 DEFIS DU MOMENT</h2>
            <p style="font-size: 18px; font-weight: bold; margin-bottom: 5px;">Opération "Zéro croûte de pain"</p>
            <p style="font-size: 13px; color: #FFFFFF; opacity: 0.9; font-style: italic; margin: 0;">
                Si la poubelle à pain descend sous les 3kg cette semaine, tout le collège débloque le badge légendaire !
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- AUTRES DECHETS FUNS ---
    st.markdown("🔍 **Zoom sur le reste du self :**")
    
    # Serviettes
    poids_serviettes = st.slider("🧻 Serviettes jetées (kg) :", 0.0, 15.0, 3.0)
    nb_serviettes = int(poids_serviettes / 0.003)
    # 3g par serviette pliée fait environ 0.1 cm d'épaisseur -> calcul fun de hauteur
    hauteur_tour = (nb_serviettes * 0.1) / 100 
    st.write(f"👉 *Empilées, vos {nb_serviettes} serviettes formeraient une tour de **{hauteur_tour:.1f} mètres** de haut !*")
    
    st.markdown("---")

    # Badges à collectionner
    st.markdown("### 🎖️ Badges de la semaine")
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        if val_pain_kg <= 4:
            st.success("🥇 Anti-Gâchis Pain")
        else:
            st.text("🔒 Badge Pain Verrouillé")
            
    with col_b2:
        if val_alim_kg < 30:
            st.success("🌟 Planète Sauvée")
        else:
            st.text("🔒 Badge Assiette Propre")
