import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Objectif Zéro Gaspi", page_icon="🍏", layout="wide")

# --- STYLE CSS REVISITÉ : FRAIS, MODERNE ET FUN ---
st.markdown(
    """
    <style>
    /* Fond dégradé vert éco/dynamique */
    .stApp {
        background: linear-gradient(135deg, #1E3F20 0%, #0D2010 100%);
    }
    
    /* Textes généraux en blanc */
    h1, h2, h3, h4, h5, h6, .stMarkdown, p, li, label, .stText {
        color: #FFFFFF !important;
    }
    
    /* Ligne de séparation stylisée entre les colonnes */
    [data-testid="column"]:nth-child(1) {
        border-right: 3px dashed #4CAF50;
        padding-right: 30px;
    }
    [data-testid="column"]:nth-child(2) {
        padding-left: 30px;
    }
    
    /* Style des cartes de catégories */
    .card {
        background-color: rgba(255, 255, 255, 0.1);
        border: 2px solid #4CAF50;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.3);
        margin-bottom: 25px;
        transition: transform 0.2s;
    }
    .card:hover {
        transform: scale(1.02);
        border-color: #81C784;
    }
    
    /* Boîte Mission Spéciale */
    .mission-box {
        background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%);
        border: none;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 8px 25px rgba(255, 152, 0, 0.4);
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* Badges de score */
    .badge-good {
        background-color: #2E7D32;
        color: #E8F5E9 !important;
        padding: 5px 10px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 14px;
        display: inline-block;
        margin-top: 10px;
    }
    .badge-warning {
        background-color: #C62828;
        color: #FFEBEE !important;
        padding: 5px 10px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 14px;
        display: inline-block;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- EN-TÊTE DYNAMIQUE ---
st.title("🍏 Objectif Zéro Gaspi — Collège Jean Giono ⚡")
st.subheader("🏆 Le QG des 700 éco-aventuriers du self (ODD 12)")

st.info("🎯 **Le défi de la semaine :** Entre les pesées réelles de ton plateau et regarde l'impact en direct sur la planète !")

st.markdown("---")

# Création des deux colonnes
col_gauche, col_droite = st.columns(2)

# ==========================================
# COLONNE GAUCHE
# ==========================================
with col_gauche:
    st.markdown("### 📥 Section : Recyclage & Amuse-bouches")

    # --- CATEGORIE 2 : Poubelle à Pain ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🥖 Le Gang des Baguettes")
    poids_pain = st.number_input("Poids du pain gaspillé :", min_value=0.0, value=4.0, step=0.5, key="pain")
    unite_pain = st.selectbox("Unité :", ["kg", "g"], key="u_pain")
    
    val_pain = poids_pain if unite_pain == "kg" else poids_pain / 1000
    nb_baguettes = int(val_pain / 0.25)
    
    st.write(f"👉 **Total :** {poids_pain} {unite_pain}")
    st.write(f"💥 *Aïe ! Ça fait quand même **{nb_baguettes} baguettes** jetées à la poubelle...*")
    
    # Badge dynamique de jeu
    if nb_baguettes <= 5:
        st.markdown('<span class="badge-good">🏅 Statut : Maîtres Boulangers (Excellent !)</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="badge-warning">🚨 Statut : Alerte miettes ! On ralentit sur le gâchis.</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 4 : Serviettes en papier ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧻 Défi Serviettes")
    poids_serviettes = st.number_input("Poids des serviettes :", min_value=0.0, value=1.5, step=0.1, key="serviettes")
    unite_serviettes = st.selectbox("Unité :", ["kg", "g"], key="u_serviettes")
    
    val_serviettes = poids_serviettes if unite_serviettes == "kg" else poids_serviettes / 1000
    nb_serviettes = int(val_serviettes / 0.003)
    
    st.write(f"👉 **Total :** {poids_serviettes} {unite_serviettes}")
    st.write(f"🌲 *C'est l'équivalent de **{nb_serviettes} serviettes** utilisées pour rien.*")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 5 : Emballages ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📦 Opération Anti-Plastoc")
    poids_emballages = st.number_input("Poids des emballages :", min_value=0.0, value=3.0, step=0.5, key="emballages")
    unite_emballages = st.selectbox("Unité :", ["kg", "g"], key="u_emballages")
    
    val_emballages = poids_emballages if unite_emballages == "kg" else poids_emballages / 1000
    nb_emballages = int(val_emballages / 0.020)
    
    st.write(f"👉 **Total :** {poids_emballages} {unite_emballages}")
    st.write(f"🗑️ *Environ **{nb_emballages} emballages** plastiques ou cartons.*")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# COLONNE DROITE
# ==========================================
with col_droite:
    st.markdown("### 🍗 Section : Le Gros des Assiettes")

    # --- CATEGORIE 1 : Déchets Alimentaires ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🗑️ Le Reste des Plats")
    poids_alim = st.number_input("Poids des restes de repas :", min_value=0.0, value=25.0, step=1.0, key="alim")
    unite_alim = st.selectbox("Unité :", ["kg", "g"], key="u_alim")
    
    val_alim = poids_alim if unite_alim == "kg" else poids_alim / 1000
    nb_repas = int(val_alim / 0.150)
    
    st.write(f"👉 **Total :** {poids_alim} {unite_alim}")
    st.write(f"🍽️ *Ouch ! Ça représente **{nb_repas} repas complets** qui finissent à la benne.*")
    
    if nb_repas < 100:
        st.markdown('<span class="badge-good">🚀 Record en vue ! L\'assiette est presque vide.</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="badge-warning">👀 Mission : Finis ton assiette au prochain service !</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 3 : Fruits entamés ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🍎 Les Fruits Abandonnés")
    poids_fruits = st.number_input("Poids des fruits jetés :", min_value=0.0, value=2.0, step=0.2, key="fruits")
    unite_fruits = st.selectbox("Unité :", ["kg", "g"], key="u_fruits")
    
    val_fruits = poids_fruits if unite_fruits == "kg" else poids_fruits / 1000
    nb_fruits = int(val_fruits / 0.120)
    
    st.write(f"👉 **Total :** {poids_fruits} {unite_fruits}")
    st.write(f"🦔 *C'est l'équivalent de **{nb_fruits} fruits entiers** gaspillés.*")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- ENCADRÉ MISSION EN FLAMMES ---
    st.markdown(
        """
        <div class="mission-box">
            <h2 style="color: #FFFFFF; margin: 0; font-size: 28px;">🎯 VOTRE MISSION 🔥</h2>
            <p style="font-size: 18px; font-weight: bold; color: #FFFFFF; margin-top: 5px;">Débloquer le badge "Zéro Gâchis du Chef"</p>
            <p style="font-size: 14px; color: #FFF3E0; font-style: italic; margin: 0; padding-top: 10px; border-top: 1px dashed #FFFFFF;">
                L'objectif final : Diviser par deux le poids des poubelles d'ici la fin du mois ! On compte sur vous.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- CALCUL DE LA BARRE DE PROGRESSION GLOBALE ---
total_general_kg = val_pain + val_serviettes + val_emballages + val_alim + val_fruits
st.markdown("---")
st.markdown(f"### 📈 Score Éco-Responsable Global : `{total_general_kg:.2f} kg` de déchets cette semaine")

# Plus le score est bas, plus la barre se remplit vers le succès !
# Imaginons un objectif max de 100kg à ne pas dépasser
progress_val = max(0.0, min(1.0, (100.0 - total_general_kg) / 100.0))
st.progress(progress_val)
st.caption("💡 *Plus la barre est pleine, plus on est proches de sauver la planète ! (Objectif : Moins de 30kg au total)*")
