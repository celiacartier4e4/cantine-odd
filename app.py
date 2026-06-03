import streamlit as st

# ==============================================================================
# CONFIGURATION ET THÉMATISATION DE L'APPLICATION
# ==============================================================================
st.set_page_config(
    page_title="Dashboard Éco-Responsable - CDSG Jean Giono",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Injection CSS avancée pour un rendu "Soft Dark / Premium Eco"
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0F1F15 0%, #050A06 100%);
    }
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
        color: #FFFFFF !important;
        font-family: 'Segoe UI', Roboto, Helvetica, sans-serif;
    }
    /* Style des modules de saisie */
    .data-card {
        background: rgba(255, 255, 255, 0.03);
        border-left: 4px solid #4CAF50;
        border-top: 1px solid rgba(255,255,255,0.05);
        border-right: 1px solid rgba(255,255,255,0.05);
        border-bottom: 1px solid rgba(255,255,255,0.05);
        padding: 20px;
        border-radius: 0px 12px 12px 0px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    /* Style des blocs de résultats principaux (KPIs) */
    .kpi-card {
        background: rgba(76, 175, 80, 0.1);
        border: 1px solid rgba(76, 175, 80, 0.3);
        border-radius: 10px;
        padding: 15px;
        text-align: center;
    }
    /* Module institutionnel CDSG */
    .institution-box {
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid #3B82F6;
        padding: 20px;
        border-radius: 12px;
        margin-top: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================================================================
# LOGIQUE MÉTIER & CONVERSIONS DE DONNÉES (MOTEUR DE CALCUL)
# ==============================================================================
def normaliser_en_kg(poids, unite):
    """Convertit instantanément la valeur saisie en kilogrammes."""
    return poids if unite == "kg" else poids / 1000.0

# ==============================================================================
# INTERFACE UTILISATEUR (UI)
# ==============================================================================

# En-tête de l'application
st.markdown("### 🎖️ SYSTÈME DE PILOTAGE ENVIRONNEMENTAL — CADRE CDSG")
st.title("🍏 Objectif Zéro Gaspi | Collège Jean Giono — Orange")
st.markdown(
    "**Outil d'analyse quantitative** développé pour le suivi des 700 demi-pensionnaires. "
    "Conforme aux indicateurs de l'**ODD 12** (Consommation et production responsables)."
)
st.markdown("---")

# ------------------------------------------------------------------------------
# PIÈCE MAÎTRESSE 1 : COLLECTE DES DONNÉES (LES 5 CATÉGORIES RESTRUCTURÉES)
# ------------------------------------------------------------------------------
st.markdown("### 📥 Saisie des Pesées Hebdomadaires")

# Répartition en 3 colonnes asymétriques pour un look "dashboard de contrôle"
col1, col2, col3 = st.columns([1.1, 1.1, 0.8])

with col1:
    # --- CATÉGORIE 1 : Déchets Alimentaires (Restes) ---
    st.markdown('<div class="data-card">', unsafe_allow_html=True)
    st.markdown("#### 🗑️ Biodéchets — Restes de Plats")
    poids_alim = st.number_input("Masse mesurée :", min_value=0.0, value=25.0, step=1.0, key="alim")
    unite_alim = st.selectbox("Unité :", ["kg", "g"], key="u_alim")
    kg_alim = normaliser_en_kg(poids_alim, unite_alim)
    equiv_repas = int(kg_alim / 0.150) # Base : 150g par repas complet
    st.markdown(f"**Équivalence :** Approx. `{equiv_repas}` repas complets rejetés.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATÉGORIE 2 : Poubelle à Pain ---
    st.markdown('<div class="data-card">', unsafe_allow_html=True)
    st.markdown("#### 🥖 Reliquats de Pain")
    poids_pain = st.number_input("Masse mesurée :", min_value=0.0, value=4.0, step=0.5, key="pain")
    unite_pain = st.selectbox("Unité :", ["kg", "g"], key="u_pain")
    kg_pain = normaliser_en_kg(poids_pain, unite_pain)
    equiv_baguettes = int(kg_pain / 0.250) # Base : 250g par baguette
    st.markdown(f"**Équivalence :** Approx. `{equiv_baguettes}` baguettes de 250g perdues.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # --- CATÉGORIE 3 : Fruits entamés ---
    st.markdown('<div class="data-card">', unsafe_allow_html=True)
    st.markdown("#### 🍎 Pertes sur Fruits")
    poids_fruits = st.number_input("Masse mesurée :", min_value=0.0, value=2.0, step=0.2, key="fruits")
    unite_fruits = st.selectbox("Unité :", ["kg", "g"], key="u_fruits")
    kg_fruits = normaliser_en_kg(poids_fruits, unite_fruits)
    equiv_fruits = int(kg_fruits / 0.120) # Base : 120g par fruit
    st.markdown(f"**Équivalence :** Approx. `{equiv_fruits}` fruits entiers gaspillés.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATÉGORIE 4 : Serviettes en papier ---
    st.markdown('<div class="data-card">', unsafe_allow_html=True)
    st.markdown("#### 🧻 Consommables — Serviettes Papier")
    poids_serviettes = st.number_input("Masse mesurée :", min_value=0.0, value=1.5, step=0.1, key="serviettes")
    unite_serviettes = st.selectbox("Unité :", ["kg", "g"], key="u_serviettes")
    kg_serviettes = normaliser_en_kg(poids_serviettes, unite_serviettes)
    equiv_serviettes = int(kg_serviettes / 0.003) # Base : 3g par serviette
    st.markdown(f"**Équivalence :** Approx. `{equiv_serviettes}` serviettes consommées.")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    # --- CATÉGORIE 5 : Emballages ---
    st.markdown('<div class="data-card">', unsafe_allow_html=True)
    st.markdown("#### 📦 Flux des Emballages (Tout-venant)")
    poids_emballages = st.number_input("Masse mesurée :", min_value=0.0, value=3.0, step=0.5, key="emballages")
    unite_emballages = st.selectbox("Unité :", ["kg", "g"], key="u_emballages")
    kg_emballages = normaliser_en_kg(poids_emballages, unite_emballages)
    equiv_emballages = int(kg_emballages / 0.020) # Base : 20g par emballage
    st.markdown(f"**Équivalence :** Approx. `{equiv_emballages}` unités jetées.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Note institutionnelle fixe
    st.markdown(
        """
        <div class="institution-box">
            <h5 style="color: #60A5FA; margin-0; font-size: 14px;">🛡️ CONTEXTE DEFENSE GLOBAL</h5>
            <p style="font-size: 12px; color: #94A3B8; margin: 5px 0 0 0; line-height: 1.4;">
                Sous la direction de <b>M. Thierry Armant</b>, la classe CDSG analyse la résilience du collège face aux enjeux de souveraineté alimentaire.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------------------------------------------------------------------
# PIÈCE MAÎTRESSE 2 : MÉTRIQUES DE SYNTHÈSE ET CALCULS AVANCÉS (ADEME)
# ------------------------------------------------------------------------------
st.markdown("---")
st.markdown("### 📊 Indicateurs Majeurs d'Impact")

# Calculs globaux consolidés
total_masse_kg = kg_alim + kg_pain + kg_fruits + kg_serviettes + kg_emballages
total_unites_nourriture = equiv_repas + equiv_baguettes + equiv_fruits

# Facteur carbone moyen ADEME : 1kg de gaspillage en restauration scolaire génère environ 2.0 kg CO2 équivalent (production + transport + fin de vie)
impact_co2 = total_masse_kg * 2.0
# Équivalence routière : une voiture moyenne émet environ 0.120 kg CO2 par km (2026 standards)
km_voiture_equiv = impact_co2 / 0.120

kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

with kpi_col1:
    st.markdown(
        f'<div class="kpi-card"><h5>Masse Globale Capturée</h5>'
        f'<h2 style="color: #4CAF50; margin: 5px 0 0 0;">{total_masse_kg:.2f} kg</h2></div>', 
        unsafe_allow_html=True
    )

with kpi_col2:
    st.markdown(
        f'<div class="kpi-card"><h5>Volume de Gaspillage Direct</h5>'
        f'<h2 style="color: #FF9800; margin: 5px 0 0 0;">{total_unites_nourriture} portions</h2></div>', 
        unsafe_allow_html=True
    )

with kpi_col3:
    st.markdown(
        f'<div class="kpi-card"><h5>Bilan Carbone Associé</h5>'
        f'<h2 style="color: #F44336; margin: 5px 0 0 0;">{impact_co2:.2f} kg CO₂e</h2>'
        f'<p style="font-size: 12px; color: #94A3B8; margin: 4px 0 0 0;">Soit {km_voiture_equiv:.0f} km parcourus en voiture citadine</p></div>', 
        unsafe_allow_html=True
    )

# Jauge d'évaluation finale
st.markdown("#### 🎯 Jauge d'Efficience Environnementale")
# Calcul inversé : moins il y a de déchets, plus la barre est remplie (Objectif théorique max : 100 kg)
performance_score = max(0.0, min(1.0, (100.0 - total_masse_kg) / 100.0))
st.progress(performance_score)
st.caption(
    "**Note de performance :** Cet indicateur synthétise l'efficacité globale du plan d'action mené par le collège Jean Giono. "
    "L'objectif validé par la CDSG est le maintien sous le seuil critique des 30,00 kg hebdomadaires."
)
