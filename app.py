import streamlit as st

# Configuration de la page pour un rendu professionnel
st.set_page_config(
    page_title="CDSG - Objectif Zéro Gaspi", 
    page_icon="🍏", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- STYLE CSS AVANCÉ : LOOK INSTITUTIONNEL ET CITOYEN ---
st.markdown(
    """
    <style>
    /* Fond sombre haut de gamme */
    .stApp {
        background: linear-gradient(135deg, #112211 0%, #050A05 100%);
    }
    
    /* Typographies et couleurs globales */
    h1, h2, h3, h4, h5, h6, .stMarkdown, p, li, label, .stText {
        color: #FFFFFF !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Séparation des sections */
    [data-testid="column"]:nth-child(1) {
        border-right: 2px solid rgba(76, 175, 80, 0.2);
        padding-right: 30px;
    }
    [data-testid="column"]:nth-child(2) {
        padding-left: 30px;
    }
    
    /* Cartes de saisie (Volets) */
    .metric-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(76, 175, 80, 0.3);
        padding: 22px;
        border-radius: 12px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
        margin-bottom: 25px;
    }
    
    /* KPI blocs du haut */
    .kpi-box {
        background: linear-gradient(135deg, #1E4620 0%, #122B14 100%);
        border: 1px solid #4CAF50;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(76, 175, 80, 0.2);
    }
    
    /* Section Mission CDSG */
    .mission-cdsg {
        background: linear-gradient(135deg, #1A365D 0%, #0F172A 100%);
        border: 1px solid #3B82F6;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 20px rgba(59, 130, 246, 0.2);
        text-align: center;
        margin-top: 15px;
    }
    
    /* Badges de conformité */
    .status-ok {
        background-color: #2E7D32;
        color: #FFFFFF !important;
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 13px;
        font-weight: bold;
    }
    .status-alert {
        background-color: #D32F2F;
        color: #FFFFFF !important;
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 13px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- EN-TÊTE OFFICIEL ---
st.markdown("#### 🎖️ PROJET ÉCO-CITOYEN — CLASSE CDSG")
st.title("🍏 Plateforme de Pilotage Éco-Responsable")
st.markdown("##### **Collège Jean Giono (Orange)** — Supervision de l'impact des 700 demi-pensionnaires (ODD 12)")

st.markdown("---")

# --- ZONE CACHÉE : INTERACTION DES DONNÉES (Pour calculs des KPIs en haut) ---
# Nous créons des variables temporaires pour calculer les totaux avant l'affichage visuel
with st.sidebar:
    st.write("🔧 *Paramètres de simulation (Masqués sur l'écran principal)*")

# Pour que l'expérience utilisateur soit parfaite, on organise la page en deux grandes colonnes de saisie
col_gauche, col_droite = st.columns(2)

# ==========================================
# COLONNE GAUCHE : Ressources & Consommables
# ==========================================
with col_gauche:
    st.markdown("### 🥖 Volet A : Suivi des Consommables et Féculents")

    # --- CATEGORIE 2 : Poubelle à Pain ---
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.subheader("🥖 Reliquats de Pain (Boulangerie)")
    poids_pain = st.number_input("Masse totale mesurée :", min_value=0.0, value=4.0, step=0.5, key="pain")
    unite_pain = st.selectbox("Unité :", ["kg", "g"], key="u_pain")
    val_pain = poids_pain if unite_pain == "kg" else poids_pain / 1000
    nb_baguettes = int(val_pain / 0.25)
    st.write(f"📈 **Donnée enregistrée :** {poids_pain} {unite_pain} | *Équivaut à **{nb_baguettes} baguettes** perdues (base 250g).*")
    if nb_baguettes <= 5:
        st.markdown('<span class="status-ok">✔ Seuil Conforme</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="status-alert">⚠️ Seuil Alerte Critique</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 4 : Serviettes en papier ---
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.subheader("🧻 Consommation de Serviettes en Papier")
    poids_serviettes = st.number_input("Masse totale mesurée :", min_value=0.0, value=1.5, step=0.1, key="serviettes")
    unite_serviettes = st.selectbox("Unité :", ["kg", "g"], key="u_serviettes")
    val_serviettes = poids_serviettes if unite_serviettes == "kg" else poids_serviettes / 1000
    nb_serviettes = int(val_serviettes / 0.003)
    st.write(f"📈 **Donnée enregistrée :** {poids_serviettes} {unite_serviettes} | *Équivaut à **{nb_serviettes} serviettes** jetées (base 3g).*")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 5 : Emballages ---
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.subheader("📦 Flux des Emballages Non Recyclés")
    poids_emballages = st.number_input("Masse totale mesurée :", min_value=0.0, value=3.0, step=0.5, key="emballages")
    unite_emballages = st.selectbox("Unité :", ["kg", "g"], key="u_emballages")
    val_emballages = poids_emballages if unite_emballages == "kg" else poids_emballages / 1000
    nb_emballages = int(val_emballages / 0.020)
    st.write(f"📈 **Donnée enregistrée :** {poids_emballages} {unite_emballages} | *Équivaut à **{nb_emballages} emballages indus** (base 20g).*")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# COLONNE DROITE : Composantes des Repas
# ==========================================
with col_droite:
    st.markdown("### 🍽️ Volet B : Restes Alimentaires et Fruits")

    # --- CATEGORIE 1 : Déchets Alimentaires ---
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.subheader("🗑️ Biodéchets - Restes de Plats Cuisinés")
    poids_alim = st.number_input("Masse totale mesurée :", min_value=0.0, value=25.0, step=1.0, key="alim")
    unite_alim = st.selectbox("Unité :", ["kg", "g"], key="u_alim")
    val_alim = poids_alim if unite_alim == "kg" else poids_alim / 1000
    nb_repas = int(val_alim / 0.150)
    st.write(f"📈 **Donnée enregistrée :** {poids_alim} {unite_alim} | *Équivaut à **{nb_repas} repas complets** gaspillés (base 150g).*")
    if nb_repas < 100:
        st.markdown('<span class="status-ok">✔ Objectif National Respecté</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="status-alert">⚠️ Optimisation du service requise</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 3 : Fruits entamés ---
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.subheader("🍎 Pertes sur les Fruits Fruités")
    poids_fruits = st.number_input("Masse totale mesurée :", min_value=0.0, value=2.0, step=0.2, key="fruits")
    unite_fruits = st.selectbox("Unité :", ["kg", "g"], key="u_fruits")
    val_fruits = poids_fruits if unite_fruits == "kg" else poids_fruits / 1000
    nb_fruits = int(val_fruits / 0.120)
    st.write(f"📈 **Donnée enregistrée :** {poids_fruits} {unite_fruits} | *Équivaut à **{nb_fruits} fruits entiers** perdus (base 120g).*")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- ENCADRÉ SPÉCIAL CDSG / CONCOURS NATIONAL ---
    st.markdown(
        """
        <div class="mission-cdsg">
            <h3 style="color: #60A5FA; margin: 0; font-size: 18px;">🛡️ ENGAGEMENT CITOYEN & DÉFENSE GLOBAL</h3>
            <p style="font-size: 14px; color: #E2E8F0; margin-top: 5px; font-weight: bold;">Action de Résilience face au Gaspillage Alimentaire</p>
            <p style="font-size: 13px; color: #94A3B8; font-style: italic; margin: 0; padding-top: 8px; border-top: 1px dashed rgba(255,255,255,0.2);">
                "La sécurité globale passe aussi par la préservation de nos ressources stratégiques et la souveraineté alimentaire."
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- SECTION DES CALCULS ET BILAN DES CONCOURS ---
st.markdown("---")
st.markdown("### 📊 Indicateurs de Synthèse de la Campagne")

total_general_kg = val_pain + val_serviettes + val_emballages + val_alim + val_fruits
total_repas_perdus = nb_repas + nb_baguettes
# Facteur ADEME moyen : 1 kg de biodéchets de self ≈ 2.0 kg d'équivalent CO2 produit (production, transport, cuisson)
co2_impact = total_general_kg * 2.0

# Affichage des 3 compteurs clés de performance (KPI)
kpi1, kpi2, kpi3 = st.columns(3)
with kpi1:
    st.markdown(f'<div class="kpi-box"><h5>Masse Totale Générée</h5><h2 style="color:#4CAF50;">{total_general_kg:.2f} kg</h2></div>', unsafe_allow_html=True)
with kpi2:
    st.markdown(f'<div class="kpi-box"><h5>Équivalence Nutritionnelle</h5><h2 style="color:#FF9800;">{total_repas_perdus} portions</h2></div>', unsafe_allow_html=True)
with kpi3:
    st.markdown(f'<div class="kpi-box"><h5>Empreinte Carbone Générée</h5><h2 style="color:#F44336;">{co2_impact:.2f} kg CO₂e</h2></div>', unsafe_allow_html=True)

# Barre de progression inversée (Scénarisation du score)
st.markdown("#### 🎯 Jauge d'Efficacité Éco-Responsable Collective")
progress_val = max(0.0, min(1.0, (100.0 - total_general_kg) / 100.0))
st.progress(progress_val)
st.caption("💡 **Interprétation pour le jury :** Plus la jauge progresse vers les 100%, plus le collège Jean Giono réduit ses déchets et valide les critères de performance environnementale de l'ODD 12.")
