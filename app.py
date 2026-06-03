import streamlit as st

# ==============================================================================
# CONFIGURATION ET STYLE DE L'APPLICATION
# ==============================================================================
st.set_page_config(
    page_title="Dashboard Environnemental - CDSG Giono",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Injection CSS pour aérer et styliser les composants
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0F1F15 0%, #050A06 100%);
    }
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
        color: #FFFFFF !important;
        font-family: 'Segoe UI', Roboto, sans-serif;
    }
    /* Espacement et design des blocs de données */
    .data-card {
        background: rgba(255, 255, 255, 0.03);
        border-left: 4px solid #4CAF50;
        padding: 25px;
        border-radius: 0px 12px 12px 0px;
        margin-top: 15px;
        margin-bottom: 30px; /* Grand espacement entre les blocs */
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    /* Cartes de résultats (KPIs) */
    .kpi-card {
        background: rgba(76, 175, 80, 0.08);
        border: 1px solid rgba(76, 175, 80, 0.2);
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        margin-bottom: 20px;
    }
    /* Encadré institutionnel */
    .institution-box {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid #3B82F6;
        padding: 25px;
        border-radius: 12px;
        line-height: 1.6;
    }
    /* Amélioration visuelle des onglets Streamlit */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 8px 8px 0px 0px;
        padding: 10px 20px;
        font-weight: 600;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #4CAF50;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================================================================
# FONCTIONS DE CALCUL (LOGIQUE MÉTIER)
# ==============================================================================
def normaliser_en_kg(poids, unite):
    return poids if unite == "kg" else poids / 1000.0

# ==============================================================================
# STRUCTURE DU DASHBOARD (INTERFACE APPLICATIVE)
# ==============================================================================

# En-tête fixe
st.markdown("#### 🎖️ SYSTÈME DE PILOTAGE ENVIRONNEMENTAL — CADRE CDSG")
st.title("🍏 Objectif Zéro Gaspi | Collège Jean Giono — Orange")
st.markdown("Suivi quantitatif et calcul d'impact — Supervision : M. Thierry Armant")

st.markdown("🔍 *Naviguez à travers les onglets ci-dessous pour consulter ou modifier les indicateurs.*")

# CRÉATION DES ONGLETS POUR ESPACER LE CONTENU
onglet_saisie, onglet_analyse, onglet_cdsg = st.tabs([
    "📥 1. Enregistrement des Pesées", 
    "📊 2. Analyses & Bilan Carbone", 
    "🛡️ 3. Contexte CDSG & ODD 12"
])

# ------------------------------------------------------------------------------
# ONGLET 1 : SAISIE DES DONNÉES (ÉPURÉ EN COLONNES)
# ------------------------------------------------------------------------------
with onglet_saisie:
    st.markdown("### 📋 Formulaire de capture des flux (Données hebdomadaires)")
    st.write("Entrez les mesures effectuées en fin de service pour mettre à jour les graphiques d'impact.")
    
    col_gauche, col_droite = st.columns(2)
    
    with col_gauche:
        # Catégorie 1
        st.markdown('<div class="data-card">', unsafe_allow_html=True)
        st.markdown("#### 🗑️ Biodéchets — Restes de Plats Cuisinés")
        poids_alim = st.number_input("Masse mesurée :", min_value=0.0, value=25.0, step=1.0, key="alim")
        unite_alim = st.selectbox("Unité :", ["kg", "g"], key="u_alim")
        kg_alim = normaliser_en_kg(poids_alim, unite_alim)
        equiv_repas = int(kg_alim / 0.150)
        st.markdown(f"👉 **Équivalence :** Environ `{equiv_repas}` repas complets rejetés.")
        st.markdown('</div>', unsafe_allow_html=True)

        # Catégorie 2
        st.markdown('<div class="data-card">', unsafe_allow_html=True)
        st.markdown("#### 🥖 Reliquats de Pain (Boulangerie)")
        poids_pain = st.number_input("Masse mesurée :", min_value=0.0, value=4.0, step=0.5, key="pain")
        unite_pain = st.selectbox("Unité :", ["kg", "g"], key="u_pain")
        kg_pain = normaliser_en_kg(poids_pain, unite_pain)
        equiv_baguettes = int(kg_pain / 0.250)
        st.markdown(f"👉 **Équivalence :** Environ `{equiv_baguettes}` baguettes perdues.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_droite:
        # Catégorie 3
        st.markdown('<div class="data-card">', unsafe_allow_html=True)
        st.markdown("#### 🍎 Pertes sur Fruits")
        poids_fruits = st.number_input("Masse mesurée :", min_value=0.0, value=2.0, step=0.2, key="fruits")
        unite_fruits = st.selectbox("Unité :", ["kg", "g"], key="u_fruits")
        kg_fruits = normaliser_en_kg(poids_fruits, unite_fruits)
        equiv_fruits = int(kg_fruits / 0.120)
        st.markdown(f"👉 **Équivalence :** Environ `{equiv_fruits}` fruits entiers jetés.")
        st.markdown('</div>', unsafe_allow_html=True)

        # Catégorie 4
        st.markdown('<div class="data-card">', unsafe_allow_html=True)
        st.markdown("#### 🧻 Consommables — Serviettes Papier")
        poids_serviettes = st.number_input("Masse mesurée :", min_value=0.0, value=1.5, step=0.1, key="serviettes")
        unite_serviettes = st.selectbox("Unité :", ["kg", "g"], key="u_serviettes")
        kg_serviettes = normaliser_en_kg(poids_serviettes, unite_serviettes)
        equiv_serviettes = int(kg_serviettes / 0.003)
        st.markdown(f"👉 **Équivalence :** Environ `{equiv_serviettes}` serviettes utilisées.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    # Catégorie 5 (Placée seule en bas pour équilibrer l'espace)
    st.markdown("---")
    st.markdown("#### 📦 Catégorie Complémentaire")
    st.markdown('<div class="data-card" style="max-width: 50%;">', unsafe_allow_html=True)
    poids_emballages = st.number_input("Masse des Emballages (Tout-venant) :", min_value=0.0, value=3.0, step=0.5, key="emballages")
    unite_emballages = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_emballages")
    kg_emballages = normaliser_en_kg(poids_emballages, unite_emballages)
    equiv_emballages = int(kg_emballages / 0.020)
    st.markdown(f"👉 **Équivalence :** Environ `{equiv_emballages}` unités d'emballage indus.")
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# CALCULS TRANSVERSAUX (Effectués en arrière-plan)
# ------------------------------------------------------------------------------
total_masse_kg = kg_alim + kg_pain + kg_fruits + kg_serviettes + kg_emballages
total_unites_nourriture = equiv_repas + equiv_baguettes + equiv_fruits
impact_co2 = total_masse_kg * 2.0
km_voiture_equiv = impact_co2 / 0.120

# ------------------------------------------------------------------------------
# ONGLET 2 : VISUALISATION ET BILAN ENVIRONNEMENTAL
# ------------------------------------------------------------------------------
with onglet_analyse:
    st.markdown("### 📊 Indicateurs de Performance Consolideurs")
    st.write("Données macro-environnementales calculées automatiquement d'après vos saisies de l'onglet 1.")
    
    st.markdown(" ") # Petit espace
    
    kpi1, kpi2, kpi3 = st.columns(3)
    with kpi1:
        st.markdown(f'<div class="kpi-card"><h5>Masse Globale Capturée</h5><h2 style="color: #4CAF50; font-size: 36px;">{total_masse_kg:.2f} kg</h2></div>', unsafe_allow_html=True)
    with kpi2:
        st.markdown(f'<div class="kpi-card"><h5>Ressources Alimentaires Perdues</h5><h2 style="color: #FF9800; font-size: 36px;">{total_unites_nourriture} unités</h2></div>', unsafe_allow_html=True)
    with kpi3:
        st.markdown(f'<div class="kpi-card"><h5>Bilan Carbone Estimé</h5><h2 style="color: #F44336; font-size: 36px;">{impact_co2:.2f} kg CO₂e</h2><p style="font-size: 13px; color: #94A3B8; margin-top: 5px;">Soit {km_voiture_equiv:.0f} km en voiture citadine</p></div>', unsafe_allow_html=True)

    st.markdown(" ")
    st.markdown("#### 🎯 Jauge d'Efficience Environnementale Collective")
    performance_score = max(0.0, min(1.0, (100.0 - total_masse_kg) / 100.0))
    st.progress(performance_score)
    st.caption("💡 **Interprétation :** Plus la jauge progresse vers les 100%, plus la production de déchets est maîtrisée. L'objectif fixé est de rester sous les 30 kg.")

# ------------------------------------------------------------------------------
# ONGLET 3 : CADRE INSTITUTIONNEL (CDSG)
# ------------------------------------------------------------------------------
with onglet_cdsg:
    st.markdown("### 🛡️ Note de Synthèse Pédagogique")
    st.write("Cadre réglementaire et d'étude de l'application.")
    
    st.markdown(
        """
        <div class="institution-box">
            <h4 style="color: #60A5FA; margin-top: 0;">Classe Défense et Sécurité Globales (CDSG)</h4>
            <p>Sous la supervision de <b>M. Thierry Armant</b>, enseignant au <b>Collège Jean G
