import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Objectif Zéro Gaspi", page_icon="🍏", layout="wide")

# --- STYLE CSS REVISITÉ : ÉCO-RESPONSABLE ET MODERNE ---
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
    
    /* Boîte Mission Citoyenne */
    .mission-box {
        background: linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%);
        border: 2px solid #81C784;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 8px 25px rgba(76, 175, 80, 0.3);
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
        background-color: #E65100;
        color: #FFF3E0 !important;
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

# --- EN-TÊTE ---
st.title("🍏 Objectif Zéro Gaspi — Collège Jean Giono ⚡")
st.subheader("🏆 Suivi participatif des 700 demi-pensionnaires (ODD 12)")

st.info("🎯 **Principe :** Saisissez les pesées de la semaine pour mesurer notre impact environnemental en temps réel et ajuster nos actions !")

st.markdown("---")

# Création des deux colonnes
col_gauche, col_droite = st.columns(2)

# ==========================================
# COLONNE GAUCHE : Ressources & Consommables
# ==========================================
with col_gauche:
    st.markdown("### 📋 Volet 1 : Boulangerie et Consommables")

    # --- CATEGORIE 2 : Poubelle à Pain ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🥖 Gaspillage de Pain")
    poids_pain = st.number_input("Masse de pain non consommée :", min_value=0.0, value=4.0, step=0.5, key="pain")
    unite_pain = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_pain")
    
    val_pain = poids_pain if unite_pain == "kg" else poids_pain / 1000
    nb_baguettes = int(val_pain / 0.25)
    
    st.write(f"👉 **Total enregistré :** {poids_pain} {unite_pain}")
    st.write(f"💡 *Équivalence : Cela représente environ **{nb_baguettes} baguettes** de 250g.*")
    
    # Badge dynamique
    if nb_baguettes <= 5:
        st.markdown('<span class="badge-good">🏅 Objectif Atteint : Consommation maîtrisée !</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="badge-warning">⚠️ Vigilance : Encourageons le juste choix des portions.</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 4 : Serviettes en papier ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧻 Consommation de Serviettes Papier")
    poids_serviettes = st.number_input("Masse de serviettes jetées :", min_value=0.0, value=1.5, step=0.1, key="serviettes")
    unite_serviettes = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_serviettes")
    
    val_serviettes = poids_serviettes if unite_serviettes == "kg" else poids_serviettes / 1000
    nb_serviettes = int(val_serviettes / 0.003)
    
    st.write(f"👉 **Total enregistré :** {poids_serviettes} {unite_serviettes}")
    st.write(f"🌲 *Équivalence : Environ **{nb_serviettes} serviettes** jetées.*")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 5 : Emballages ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📦 Tri des Emballages")
    poids_emballages = st.number_input("Masse d'emballages jetés :", min_value=0.0, value=3.0, step=0.5, key="emballages")
    unite_emballages = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_emballages")
    
    val_emballages = poids_emballages if unite_emballages == "kg" else poids_emballages / 1000
    nb_emballages = int(val_emballages / 0.020)
    
    st.write(f"👉 **Total enregistré :** {poids_emballages} {unite_emballages}")
    st.write(f"🗑️ *Équivalence : Environ **{nb_emballages} unités d'emballage**.*")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# COLONNE DROITE : Composantes des Repas
# ==========================================
with col_droite:
    st.markdown("### 🍽️ Volet 2 : Restes de Plats et Aliments")

    # --- CATEGORIE 1 : Déchets Alimentaires ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🗑️ Restes de Plats Cuisinés")
    poids_alim = st.number_input("Masse des restes d'assiettes :", min_value=0.0, value=25.0, step=1.0, key="alim")
    unite_alim = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_alim")
    
    val_alim = poids_alim if unite_alim == "kg" else poids_alim / 1000
    nb_repas = int(val_alim / 0.150)
    
    st.write(f"👉 **Total enregistré :** {poids_alim} {unite_alim}")
    st.write(f"🍽️ *Équivalence : Cela correspond à environ **{nb_repas} repas complets**.*")
    
    if nb_repas < 100:
        st.markdown('<span class="badge-good">🚀 Performance : Excellente tendance à la baisse !</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="badge-warning">🔍 Action requise : Sensibilisons sur le gaspillage direct.</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 3 : Fruits entamés ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🍎 Pertes sur les Fruits")
    poids_fruits = st.number_input("Masse de fruits non consommés :", min_value=0.0, value=2.0, step=0.2, key="fruits")
    unite_fruits = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_fruits")
    
    val_fruits = poids_fruits if unite_fruits == "kg" else poids_fruits / 1000
    nb_fruits = int(val_fruits / 0.120)
    
    st.write(f"👉 **Total enregistré :** {poids_fruits} {unite_fruits}")
    st.write(f"🍏 *Équivalence : Environ **{nb_fruits} fruits entiers** gaspillés.*")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- ENCADRÉ MISSION SÉRIEUX MAIS ENGAGEANT ---
    st.markdown(
        """
        <div class="mission-box">
            <h2 style="color: #FFFFFF; margin: 0; font-size: 24px;">🎯 NOTRE PROJET ÉCO-CITOYEN</h2>
            <p style="font-size: 16px; font-weight: bold; color: #E8F5E9; margin-top: 5px;">Débloquer la mention officielle "Établissement Durable"</p>
            <p style="font-size: 14px; color: #C8E6C9; font-style: italic; margin: 0; padding-top: 10px; border-top: 1px dashed #FFFFFF;">
                Notre plan d'action : Réduire de 50% la masse globale de nos déchets d'ici la fin du trimestre.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- CALCUL DE LA BARRE DE PROGRESSION GLOBALE ---
total_general_kg = val_pain + val_serviettes + val_emballages + val_alim + val_fruits
st.markdown("---")
st.markdown(f"### 📈 Bilan Environnemental Global : `{total_general_kg:.2f} kg` de déchets mesurés")

# Calcul de progression éco-responsable
progress_val = max(0.0, min(1.0, (100.0 - total_general_kg) / 100.0))
st.progress(progress_val)
st.caption("💡 *Indicateur d'efficacité : Plus la barre se rapproche des 100%, plus nos actions collectives portent leurs fruits !*")
