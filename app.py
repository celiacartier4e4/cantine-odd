import streamlit as st

# ==============================================================================
# CONFIGURATION DE LA PAGE
# ==============================================================================
st.set_page_config(
    page_title="Dashboard Environnemental - CDSG Giono",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ARCHITECTURE DESIGN : PALETTE DE COULEURS DYNAMIQUE ---
st.markdown(
    """
    <style>
    /* Fond bleu-gris métallique pour éclaircir le site */
    .stApp {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
    }
    
    /* Typographies générales claires */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
        color: #FFFFFF !important;
        font-family: 'Segoe UI', Roboto, Helvetica, sans-serif;
    }
    
    /* Séparation centrale des colonnes par pointillés discrets */
    [data-testid="column"]:nth-child(1) {
        border-right: 1px dashed rgba(255, 255, 255, 0.2);
        padding-right: 40px;
    }
    [data-testid="column"]:nth-child(2) {
        padding-left: 40px;
    }
    
    /* --- STRUCTURE DES CARTES COLORÉES AVEC GRAND ESPACEMENT --- */
    .card-base {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 40px; /* Grand espacement pour aérer */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    }
    
    /* Variantes de couleurs de bordures gauches (Indicateurs visuels forts) */
    .card-green { border-left: 6px solid #10B981; }  /* Biodéchets */
    .card-gold { border-left: 6px solid #F59E0B; }   /* Pain */
    .card-red { border-left: 6px solid #EF4444; }    /* Fruits */
    .card-cyan { border-left: 6px solid #06B6D4; }   /* Serviettes */
    .card-purple { border-left: 6px solid #8B5CF6; } /* Emballages */
    
    /* Blocs indicateurs de performance du bas (KPIs) */
    .kpi-card {
        background: rgba(255, 255, 255, 0.06);
        border-top: 3px solid #10B981;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Encadré institutionnel CDSG */
    .institution-box {
        background: rgba(59, 130, 246, 0.1);
        border: 1px solid rgba(59, 130, 246, 0.3);
        border-left: 6px solid #3B82F6;
        padding: 22px;
        border-radius: 10px;
        margin-bottom: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================================================================
# MOTEUR DE CALCULS TECHNIQUES
# ==============================================================================
def normaliser_en_kg(poids, unite):
    return poids if unite == "kg" else poids / 1000.0

# ==============================================================================
# EN-TÊTE DU DASHBOARD
# ==============================================================================
st.markdown("#### 🎖️ PROJET ÉCO-CITOYEN — CADRE CDSG")
st.title("🍏 Plateforme de Pilotage Environnemental")
st.markdown("##### **Collège Jean Giono (Orange)** — Supervision de l'impact des 700 demi-pensionnaires | Référent : M. Thierry Armant")
st.markdown("---")

# ------------------------------------------------------------------------------
# INTERFACE EN DEUX GRANDES COLONNES
# ------------------------------------------------------------------------------
col_gauche, col_droite = st.columns(2)

# ==========================================
# COLONNE GAUCHE : Boulangerie & Consommables
# ==========================================
with col_gauche:
    st.markdown("### 📋 Volet A : Suivi des Consommables et Féculents")
    st.write(" ") 

    # --- CATEGORIE 2 : Poubelle à Pain ---
    st.markdown('<div class="card-base card-gold">', unsafe_allow_html=True)
    st.markdown("#### 🥖 <span style='color:#F59E0B;'>Reliquats de Pain (Boulangerie)</span>", unsafe_allow_html=True)
    poids_pain = st.number_input("Masse totale mesurée :", min_value=0.0, value=4.0, step=0.5, key="pain")
    unite_pain = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_pain")
    kg_pain = normaliser_en_kg(poids_pain, unite_pain)
    equiv_baguettes = int(kg_pain / 0.250)
    st.markdown(f"📊 **Analyse d'équivalence :** Environ `{equiv_baguettes}` baguettes de 250g perdues.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 4 : Serviettes en papier ---
    st.markdown('<div class="card-base card-cyan">', unsafe_allow_html=True)
    st.markdown("#### 🧻 <span style='color:#06B6D4;'>Consommation de Serviettes en Papier</span>", unsafe_allow_html=True)
    poids_serviettes = st.number_input("Masse totale mesurée :", min_value=0.0, value=1.5, step=0.1, key="serviettes")
    unite_serviettes = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_serviettes")
    kg_serviettes = normaliser_en_kg(poids_serviettes, unite_serviettes)
    equiv_serviettes = int(kg_serviettes / 0.003)
    st.markdown(f"📊 **Analyse d'équivalence :** Environ `{equiv_serviettes}` unités de serviettes jetées.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 5 : Emballages ---
    st.markdown('<div class="card-base card-purple">', unsafe_allow_html=True)
    st.markdown("#### 📦 <span style='color:#8B5CF6;'>Flux des Emballages Non Recyclés</span>", unsafe_allow_html=True)
    poids_emballages = st.number_input("Masse totale mesurée :", min_value=0.0, value=3.0, step=0.5, key="emballages")
    unite_emballages = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_emballages")
    kg_emballages = normaliser_en_kg(poids_emballages, unite_emballages)
    equiv_emballages = int(kg_emballages / 0.020)
    st.markdown(f"📊 **Analyse d'équivalence :** Environ `{equiv_emballages}` unités d'emballage indus.")
    st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# COLONNE DROITE : Alimentation & Contexte
# ==========================================
with col_droite:
    st.markdown("### 🍽️ Volet B : Restes Alimentaires et Cadre d'Étude")
    st.write(" ") 

    # --- CATEGORIE 1 : Déchets Alimentaires (Restes de repas) ---
    st.markdown('<div class="card-base card-green">', unsafe_allow_html=True)
    st.markdown("#### 🗑️ <span style='color:#10B981;'>Biodéchets — Restes de Plats Cuisinés</span>", unsafe_allow_html=True)
    poids_alim = st.number_input("Masse totale mesurée :", min_value=0.0, value=25.0, step=1.0, key="alim")
    unite_alim = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_alim")
    kg_alim = normaliser_en_kg(poids_alim, unite_alim)
    equiv_repas = int(kg_alim / 0.150)
    st.markdown(f"📊 **Analyse d'équivalence :** Environ `{equiv_repas}` repas complets rejetés.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 3 : Fruits entamés ---
    st.markdown('<div class="card-base card-red">', unsafe_allow_html=True)
    st.markdown("#### 🍎 <span style='color:#EF4444;'>Pertes sur les Fruits</span>", unsafe_allow_html=True)
    poids_fruits = st.number_input("Masse totale mesurée :", min_value=0.0, value=2.0, step=0.2, key="fruits")
    unite_fruits = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_fruits")
    kg_fruits = normaliser_en_kg(poids_fruits, unite_fruits)
    equiv_fruits = int(kg_fruits / 0.120)
    st.markdown(f"📊 **Analyse d'équivalence :** Environ `{equiv_fruits}` fruits entiers gaspillés.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- BLOC INSTITUTIONNEL CDSG ---
    st.markdown(
        """
        <div class="institution-box">
            <h4 style="color: #60A5FA; margin-top: 0; font-size: 16px;">🛡️ CONTEXTE CLASSE DÉFENSE ET SÉCURITÉ GLOBALES</h4>
            <p style="font-size: 13px; color: #E2E8F0; line-height: 1.5; margin-bottom: 0;">
                Cette plateforme de modélisation quantitative, supervisée par <b>M. Thierry Armant</b> au <b>Collège Jean Giono</b>, 
                analyse la résilience locale face au gaspillage de ressources stratégiques, répondant directement aux exigences de l'<b>ODD 12</b> de l'ONU.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ------------------------------------------------------------------------------
# SYNTHÈSE GLOBALE ET RÉSULTATS (EN BAS DE PAGE)
# ------------------------------------------------------------------------------
st.markdown("---")
st.markdown("### 📊 Indicateurs Centraux de Performance de la Campagne")

# Consolidation des variables
total_masse_kg = kg_alim + kg_pain + kg_fruits + kg_serviettes + kg_emballages
total_portions_perdues = equiv_repas + equiv_baguettes + equiv_fruits
impact_co2 = total_masse_kg * 2.0  
km_voiture_equiv = impact_co2 / 0.120

# Cartes KPI
kpi1, kpi2, kpi3 = st.columns(3)
with kpi1:
    st.markdown(f'<div class="kpi-card"><h5>Masse Globale Capturée</h5><h2 style="color: #10B981; font-size: 32px; margin: 5px 0 0 0;">{total_masse_kg:.2f} kg</h2></div>', unsafe_allow_html=True)
with kpi2:
    st.markdown(f'<div class="kpi-card"><h5>Volume de Gaspillage Alimentaire</h5><h2 style="color: #F59E0B; font-size: 32px; margin: 5px 0 0 0;">{total_portions_perdues} portions</h2></div>', unsafe_allow_html=True)
with kpi3:
    st.markdown(f'<div class="kpi-card"><h5>Bilan Carbone Associé</h5><h2 style="color: #EF4444; font-size: 32px; margin: 5px 0 0 0;">{impact_co2:.2f} kg CO₂e</h2><p style="font-size: 11px; color: #9CA3AF; margin: 2px 0 0 0;">Soit équivalent à {km_voiture_equiv:.0f} km en voiture</p></div>', unsafe_allow_html=True)

# Barre d'évaluation finale
st.markdown(" ")
st.markdown("#### 🎯 Jauge d'Efficience Collective")
performance_score = max(0.0, min(1.0, (100.0 - total_masse_kg) / 100.0))
st.progress(performance_score)
st.caption("💡 **Indicateur d'analyse pour le jury :** Plus la jauge tend vers 100%, plus la production de déchets est optimisée au collège Jean Giono (seuil visé : < 30 kg).")
