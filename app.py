import streamlit as st

# --- STYLE CSS : POP MODERNE & ÉQUILIBRÉ ---
st.markdown(
    """
    <style>
    /* Fond de l'application - Bleu nuit doux */
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

    /* Titre principal stylisé */
    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FFB6C1, #38EF7D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }

    /* Séparation des colonnes par un filet discret */
    [data-testid="column"]:nth-child(1) {
        border-right: 2px dashed rgba(255, 182, 193, 0.3);
        padding-right: 30px;
    }
    
    [data-testid="column"]:nth-child(2) {
        padding-left: 30px;
    }

    /* Cartes de saisie épurées mais colorées */
    .pop-card {
        background: rgba(30, 41, 59, 0.7);
        border: 2px solid #FFB6C1;
        padding: 22px;
        border-radius: 16px;
        margin-bottom: 25px;
        transition: transform 0.2s;
    }
    
    /* Boîte Défi : Habillage dégradé punchy mais propre */
    .challenge-box {
        background: linear-gradient(135deg, #11998E, #38EF7D);
        border: none;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0px 4px 15px rgba(56, 239, 125, 0.2);
        text-align: center;
        margin-bottom: 25px;
    }
    .challenge-box h2, .challenge-box p {
        color: #FFFFFF !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- ENTÊTE ---
st.markdown('<h1 class="main-title">🍏 Mission : Zéro Gaspi Giono</h1>', unsafe_allow_html=True)
st.subheader("Le QG des Éco-Héros du Collège Jean Giono 🚀")
st.write("Remplis les données de la semaine, relève les défis et débloque les badges ! 🏆")

st.markdown("---")

# --- DISPOSITION EN DEUX COLONNES ---
col_gauche, col_droite = st.columns(2)

# ==========================================
# COLONNE GAUCHE : LES PESÉES (INPUTS)
# ==========================================
with col_gauche:
    st.markdown("### 📝 Tes données de la semaine")

    # --- CATEGORIE 1 : Déchets Alimentaires ---
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("🗑️ Les Restes d'Assiettes")
    poids_alim = st.number_input("Poids mesuré :", min_value=0.0, value=42.0, step=1.0, key="alim")
    unite_alim = st.selectbox("Unité :", ["kg", "g"], key="u_alim")
    val_alim_kg = poids_alim if unite_alim == "kg" else poids_alim / 1000
    
    nb_repas = int(val_alim_kg / 0.150)
    if val_alim_kg > 40:
        status_alim = "😰 Ouch ! La poubelle déborde..."
    else:
        status_alim = "⚡ Propre ! On limite le gâchis."
        
    st.write(f"**Statut :** {status_alim}")
    st.info(f"🍔 Ça équivaut à **{nb_repas} repas complets** jetés.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 2 : Poubelle à Pain ---
    st.markdown('<div class="pop-card" style="border-color: #38EF7D;">', unsafe_allow_html=True) # Bordure verte pour varier
    st.subheader("🥖 Le Gâchis de Pain")
    poids_pain = st.number_input("Poids mesuré :", min_value=0.0, value=8.0, step=0.5, key="pain")
    unite_pain = st.selectbox("Unité :", ["kg", "g"], key="u_pain")
    val_pain_kg = poids_pain if unite_pain == "kg" else poids_pain / 1000
    
    nb_baguettes = int(val_pain_kg / 0.25)
    if val_pain_kg > 5:
        status_pain = "⚠️ Alerte overdose de croûtes !"
    else:
        status_pain = "🥖 Parfait, pas une miette ne perd !"

    st.write(f"**Statut :** {status_pain}")
    st.info(f"🥖 De quoi faire environ **{nb_baguettes} baguettes** de boulanger.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 3 : Fruits entamés ---
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("🍎 Les Fruits abandonnés")
    poids_fruits = st.number_input("Poids mesuré :", min_value=0.0, value=5.0, step=0.5, key="fruits")
    unite_fruits = st.selectbox("Unité :", ["kg", "g"], key="u_fruits")
    val_fruits_kg = poids_fruits if unite_fruits == "kg" else poids_fruits / 1000
    
    nb_fruits = int(val_fruits_kg / 0.120)
    st.info(f"🍏 C'est l'équivalent de **{nb_fruits} fruits** à peine croqués.")
    st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# COLONNE DROITE : LE DASHBOARD (RÉSULTATS)
# ==========================================
with col_droite:
    st.markdown("### 🏆 Objectifs & Défis")
    
    # --- ENCADRÉ DÉFI DU MOMENT ---
    st.markdown(
        """
        <div class="challenge-box">
            <h2 style="margin: 0; font-size: 1.4rem;">🎯 DÉFI DE LA SEMAINE</h2>
            <p style="font-size: 18px; font-weight: bold; margin-top: 5px; margin-bottom: 5px;">Opération "Zéro croûte de pain"</p>
            <p style="font-size: 13px; opacity: 0.9; font-style: italic; margin: 0;">
                Si la poubelle à pain passe sous les 5kg, le badge légendaire est débloqué pour tout le collège !
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- ÉQUIVALENCE FUN (SERVIETTES) ---
    st.markdown("🔍 **Le savais-tu ?**")
    poids_serviettes = st.slider("🧻 Serviettes en papier jetées (kg) :", 0.0, 15.0, 3.0)
    nb_serviettes = int(poids_serviettes / 0.003)
    hauteur_tour = (nb_serviettes * 0.1) / 100 
    
    st.write(f"👉 En empilant vos **{nb_serviettes} serviettes**, on obtiendrait une tour de **{hauteur_tour:.1f} mètres** de haut !")
    
    st.markdown("---")

    # --- BADGES ---
    st.markdown("### 🎖️ Vos Badges de la semaine")
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        if val_pain_kg <= 5:
            st.success("🥇 Anti-Gâchis Pain")
        else:
            st.text("🔒 Badge Pain")
            
    with col_b2:
        if val_alim_kg < 40:
            st.success("🌟 Planète Sauvée")
        else:
            st.text("🔒 Badge Assiette Propre")
