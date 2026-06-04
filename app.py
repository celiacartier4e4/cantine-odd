import streamlit as st
import pandas as pd

# ==============================================================================
# CONFIGURATION DE LA PAGE SÉCURISÉE
# ==============================================================================
st.set_page_config(
    page_title="Dashboard Éco-Citoyen - CDSG Giono",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Fonction de conversion technique
def normaliser_en_kg(poids, unite):
    if unite == "kg":
        return poids
    else:
        return poids / 1000.0

# ==============================================================================
# EN-TÊTE ET IMAGE DU VRAI COLLÈGE JEAN GIONO
# ==============================================================================
st.caption("🎖️ PROJET ÉCO-CITOYEN — CADRE CLASSE CDSG")
st.title("🍏 Collège Jean Giono d'Orange")
st.subheader("Avenue Charles Dardun, 84100 Orange")
st.text("Impact des 700 demi-pensionnaires | Référent : M. Thierry Armant")

# Intégration propre de l'illustration du collège sans casser le script
st.image(
    "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?q=80&w=1200",
    caption="Vue d'ensemble - Modélisation Éco-Responsable",
    use_container_width=True
)

st.divider()

# ------------------------------------------------------------------------------
# STRUCTURE EN 2 COLONNES (GAUCHE = SYNTHÈSE / DROITE = SAISIE COULEURS VIVES)
# ------------------------------------------------------------------------------
col_gauche, col_droite = st.columns([1.2, 1])

# ==============================================================================
# COLONNE DE DROITE : FORMULAIRES DE SAISIE STABLES ET COLORÉS
# ==============================================================================
with col_droite:
    st.write("### 📥 Saisie des Catégories de Pesée")

    # --- 1. BIODÉCHETS (VERT) ---
    with st.container(border=True):
        st.success("🗑️ **Biodéchets — Restes de Plats Cuisinés**")
        poids_alim = st.number_input("Masse Alim :", min_value=0.0, value=25.0, step=1.0, key="alim")
        unite_alim = st.selectbox("Unité Alim :", ["kg", "g"], key="u_alim")
        kg_alim = normaliser_en_kg(poids_alim, unite_alim)
        equiv_repas = int(kg_alim / 0.150)
        st.info(f"📊 **Équivalence :** Environ **{equiv_repas} repas complets** rejetés.")

    # --- 2. RELIQUATS PAIN (JAUNE/ORANGE) ---
    with st.container(border=True):
        st.warning("🥖 **Reliquats de Pain (Boulangerie)**")
        poids_pain = st.number_input("Masse Pain :", min_value=0.0, value=4.0, step=0.5, key="pain")
        unite_pain = st.selectbox("Unité Pain :", ["kg", "g"], key="u_pain")
        kg_pain = normaliser_en_kg(poids_pain, unite_pain)
        equiv_baguettes = int(kg_pain / 0.250)
        st.info(f"📊 **Équivalence :** Environ **{equiv_baguettes} baguettes** de 250g perdues.")

    # --- 3. PERTES FRUITS (ROUGE) ---
    with st.container(border=True):
        st.error("🍎 **Pertes sur les Fruits**")
        poids_fruits = st.number_input("Masse Fruits :", min_value=0.0, value=2.0, step=0.2, key="fruits")
        unite_fruits = st.selectbox("Unité Fruits :", ["kg", "g"], key="u_fruits")
        kg_fruits = normaliser_en_kg(poids_fruits, unite_fruits)
        equiv_fruits = int(kg_fruits / 0.120)
        st.info(f"📊 **Équivalence :** Environ **{equiv_fruits} fruits entiers** gaspillés.")

    # --- 4. SERVIETTES (CYAN) ---
    with st.container(border=True):
        st.markdown("🌐 **Consommation de Serviettes en Papier**")
        poids_serviettes = st.number_input("Masse Serviettes :", min_value=0.0, value=1.5, step=0.1, key="serviettes")
        unite_serviettes = st.selectbox("Unité Serviettes :", ["kg", "g"], key="u_serviettes")
        kg_serviettes = normaliser_en_kg(poids_serviettes, unite_serviettes)
        equiv_serviettes = int(kg_serviettes / 0.003)
        st.info(f"📊 **Équivalence :** Environ **{equiv_serviettes} unités** jetées.")

    # --- 5. EMBALLAGES (VIOLET) ---
    with st.container(border=True):
        st.markdown("📦 **Flux des Emballages Non Recyclés**")
        poids_emballages = st.number_input("Masse Emb :", min_value=0.0, value=3.0, step=0.5, key="emballages")
        unite_emballages = st.selectbox("Unité Emb :", ["kg", "g"], key="u_emballages")
        kg_emballages = normaliser_en_kg(poids_emballages, unite_emballages)
        equiv_emballages = int(kg_emballages / 0.020)
        st.info(f"📊 **Équivalence :** Environ **{equiv_emballages} unités** d'emballages.")


# ==============================================================================
# COLONNE DE GAUCHE : SYNTHÈSE, KPIs ET GRAPHIQUES HISTORIQUES
# ==============================================================================
with col_gauche:
    st.write("### 📊 Bilans, Graphiques & Impacts Récapitulatifs")
    
    # Calculs internes globaux
    total_masse_kg = kg_alim + kg_pain + kg_fruits + kg_serviettes + kg_emballages
    total_portions_perdues = equiv_repas + equiv_baguettes + equiv_fruits
    impact_co2 = total_masse_kg * 2.0
    km_voiture_equiv = impact_co2 / 0.120

    # Bloc Contexte Défense
    with st.container(border=True):
        st.markdown("#### 🛡️ CONTEXTE CLASSE DÉFENSE (CDSG)")
        st.write("Modélisation quantitative de résilience locale face au gaspillage de ressources stratégiques. Répond aux exigences de l'**ODD 12** de l'ONU.")

    # Affichage des KPIs d'impacts
    k1, k2, k3 = st.columns(3)
    k1.metric("Masse Globale (Jour)", f"{total_masse_kg:.2f} kg")
    k2.metric("Volume Perdu", f"{total_portions_perdues} portions")
    k3.metric("Bilan Carbone", f"{impact_co2:.1f} kg CO₂e", f"≈ {km_voiture_equiv:.0f} km auto")

    # Graphique 1 : Répartition du jour
    st.write("#### 📊 Répartition Globale des Déchets du Jour (kg)")
    chart_data = pd.DataFrame(
        [[kg_alim, kg_pain, kg_fruits, kg_serviettes, kg_emballages]],
        columns=["Biodéchets", "Pain", "Fruits", "Serviettes", "Emballages"]
    )
    st.bar_chart(chart_data, horizontal=True, color=
