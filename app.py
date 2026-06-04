import streamlit as st
import plotly.graph_objects as go

# ==============================================================================
# CONFIGURATION DE LA PAGE
# ==============================================================================
st.set_page_config(
    page_title="Dashboard Éco-Citoyen - CDSG Giono",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- STYLE CSS : COULEURS VIVES, LUMINEUSES ET CONTRASTÉES ---
st.markdown(
    """
    <style>
    /* Fond principal clair et ultra lumineux */
    .stApp {
        background: linear-gradient(135deg, #F0F4F8 0%, #E2E8F0 100%);
    }

    /* Textes généraux en bleu nuit très foncé pour un contraste maximal */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stText {
        color: #0F172A !important;
        font-family: 'Segoe UI', Roboto, Helvetica, sans-serif;
    }

    /* Séparation centrale des colonnes */
    [data-testid="column"]:nth-child(1) {
        border-right: 2px dashed #94A3B8;
        padding-right: 40px;
    }
    [data-testid="column"]:nth-child(2) {
        padding-left: 40px;
    }

    /* --- CARTES AUX COULEURS VIVES ET FLUSHYS --- */
    .card-base {
        padding: 20px;
        border-radius: 14px;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
        border: 2px solid #FFFFFF;
    }

    /* Fonds colorés vifs avec textes adaptés pour rester lisibles */
    .card-green { background-color: #2ECC71; }   /* Vert néon */
    .card-gold { background-color: #FFB703; }    /* Jaune/Orange vif */
    .card-red { background-color: #FF4D4D; }     /* Rouge flashy */
    .card-cyan { background-color: #00B4D8; }    /* Cyan électrique */
    .card-purple { background-color: #9D4EDD; }  /* Violet fluo */

    /* Forcer le texte en blanc ou noir à l'intérieur des cartes */
    .card-gold *, .card-cyan * { color: #000000 !important; }
    .card-purple *, .card-green *, .card-red * { color: #FFFFFF !important; }

    /* Blocs indicateurs de performance du bas (KPIs) */
    .kpi-card {
        background: #FFFFFF;
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #E2E8F0;
    }

    /* Encadré institutionnel CDSG */
    .institution-box {
        background: #E0F2FE;
        border: 2px solid #3B82F6;
        padding: 22px;
        border-radius: 12px;
        margin-bottom: 35px;
    }
    .institution-box * {
        color: #1E3A8A !important;
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

def declencher_mise_a_jour():
    pass

# ==============================================================================
# EN-TÊTE DU DASHBOARD
# ==============================================================================
st.markdown("#### 🎖️ PROJET ÉCO-CITOYEN — CADRE CLASSE CDSG")
st.title("🍏 Plateforme de Pilotage Environnemental")
st.markdown("##### **Collège Jean Giono (Orange)** — Impact des 700 demi-pensionnaires | Référent : M. Thierry Armant")
st.markdown("---")

# ------------------------------------------------------------------------------
# INTERFACE EN DEUX GRANDES COLONNES
# ------------------------------------------------------------------------------
col_gauche, col_droite = st.columns([1.3, 1])

# ==========================================
# COLONNE DROITE : Saisie de toutes les catégories (Empilées)
# ==========================================
with col_droite:
    st.markdown("### 📋 Formulaire de Saisie des Déchets")
    st.write(" ")
    
    # --- CATEGORIE 1 : Biodéchets ---
    st.markdown('<div class="card-base card-green">', unsafe_allow_html=True)
    st.markdown("#### 🗑️ Biodéchets — Restes de Plats Cuisinés")
    poids_alim = st.number_input("Masse totale mesurée :", min_value=0.0, value=25.0, step=1.0, key="alim", on_change=declencher_mise_a_jour)
    unite_alim = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_alim")
    kg_alim = normaliser_en_kg(poids_alim, unite_alim)
    equiv_repas = int(kg_alim / 0.150)
    st.markdown(f"📊 **Analyse d'équivalence :** Environ **{equiv_repas} repas complets** rejetés.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 2 : Poubelle à Pain ---
    st.markdown('<div class="card-base card-gold">', unsafe_allow_html=True)
    st.markdown("#### 🥖 Reliquats de Pain (Boulangerie)")
    poids_pain = st.number_input("Masse totale mesurée :", min_value=0.0, value=4.0, step=0.5, key="pain", on_change=declencher_mise_a_jour)
    unite_pain = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_pain")
    kg_pain = normaliser_en_kg(poids_pain, unite_pain)
    equiv_baguettes = int(kg_pain / 0.250)
    st.markdown(f"📊 **Analyse d'équivalence :** Environ **{equiv_baguettes} baguettes** de 250g perdues.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 3 : Fruits entamés ---
    st.markdown('<div class="card-base card-red">', unsafe_allow_html=True)
    st.markdown("#### 🍎 Pertes sur les Fruits")
    poids_fruits = st.number_input("Masse totale mesurée :", min_value=0.0, value=2.0, step=0.2, key="fruits", on_change=declencher_mise_a_jour)
    unite_fruits = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_fruits")
    kg_fruits = normaliser_en_kg(poids_fruits, unite_fruits)
    equiv_fruits = int(kg_fruits / 0.120)
    st.markdown(f"📊 **Analyse d'équivalence :** Environ **{equiv_fruits} fruits entiers** gaspillés.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 4 : Serviettes en papier ---
    st.markdown('<div class="card-base card-cyan">', unsafe_allow_html=True)
    st.markdown("#### 🧻 Consommation de Serviettes en Papier")
    poids_serviettes = st.number_input("Masse totale mesurée :", min_value=0.0, value=1.5, step=0.1, key="serviettes", on_change=declencher_mise_a_jour)
    unite_serviettes = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_serviettes")
    kg_serviettes = normaliser_en_kg(poids_serviettes, unite_serviettes)
    equiv_serviettes = int(kg_serviettes / 0.003)
    st.markdown(f"📊 **Analyse d'équivalence :** Environ **{equiv_serviettes} unités** de serviettes jetées.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIE 5 : Emballages ---
    st.markdown('<div class="card-base card-purple">', unsafe_allow_html=True)
    st.markdown("#### 📦 Flux des Emballages Non Recyclés")
    poids_emballages = st.number_input("Masse totale mesurée :", min_value=0.0, value=3.0, step=0.5, key="emballages", on_change=declencher_mise_a_jour)
    unite_emballages = st.selectbox("Unité de mesure :", ["kg", "g"], key="u_emballages")
    kg_emballages = normaliser_en_kg(poids_emballages, unite_emballages)
    equiv_emballages = int(kg_emballages / 0.020)
    st.markdown(f"📊 **Analyse d'équivalence :** Environ **{equiv_emballages} unités** d'emballage indus.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- BLOC INSTITUTIONNEL CDSG ---
    st.markdown(
        """
        <div class="institution-box">
        <h4>🛡️ CONTEXTE CLASSE DÉFENSE ET SÉCURITÉ GLOBALES</h4>
        <p style="font-size: 14px; line-height: 1.5; margin-bottom: 0;">
        Cette plateforme de modélisation quantitative, supervisée par <b>M. Thierry Armant</b> au <b>Collège Jean Giono</b>,
        analyse la résilience locale face au gaspillage de ressources stratégiques, répondant directement aux exigences de l'<b>ODD 12</b> de l'ONU.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================
# COLONNE GAUCHE : Graphique en Cercle Dynamique
# ==========================================
with col_gauche:
    st.markdown("### 📊 Répartition en Temps Réel de la Masse des Déchets")
    st.write(" ")
    
    labels = ["Biodéchets", "Pain", "Fruits", "Serviettes", "Emballages"]
    valeurs = [kg_alim, kg_pain, kg_fruits, kg_serviettes, kg_emballages]
    couleurs = ["#2ECC71", "#FFB703", "#FF4D4D", "#00B4D8", "#9D4EDD"]
    
    if sum(valeurs) == 0:
        valeurs = [1, 1, 1, 1, 1]
        labels = ["En attente de saisie...", "", "", "", ""]
        couleurs = ["#94A3B8", "#94A3B8", "#94A3B8", "#94A3B8", "#94A3B8"]

    fig = go.Figure(data=[go.Pie(
        labels=labels, 
        values=valeurs, 
        hole=0.45,
        marker=dict(colors=couleurs, line=dict(color='#FFFFFF', width=2)),
        textinfo='percent+label',
        insidetextorientation='horizontal',
        textfont=dict(size=14, color='#0F172A')
    )])
    
    fig.update_layout(
        showlegend=False,
        margin=dict(t=0, b=0, l=0, r=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=550
    )
    
    st.plotly_chart(fig, use_container_width=True, key="pie_chart_eco")

# ------------------------------------------------------------------------------
# SYNTHÈSE GLOBALE ET RÉSULTATS (EN BAS DE PAGE)
# ------------------------------------------------------------------------------
st.markdown("---")
st.markdown("### 📊 Indicateurs Centraux de Performance de la Campagne")

total_masse_kg = kg_alim + kg_pain + kg_fruits + kg_serviettes + kg_emballages
total_portions_perdues = equiv_repas + equiv_baguettes + equiv_fruits
impact_co2 = total_masse_kg * 2.0
km_voiture_equiv = impact_co2 / 0.120

kpi1, kpi2, kpi3 = st.columns(3)
with kpi1:
    st.markdown(f'<div class="kpi-card"><h5>Masse Globale Capturée</h5><h2 style="color: #2ECC71; font-size: 34px; margin: 5px 0 0 0;">{total_masse_kg:.2f} kg</h2></div>', unsafe_allow_html=True)
with kpi2:
    st.markdown(f'<div class="kpi-card"><h5>Volume de Gaspillage Alimentaire</h5><h2 style="color: #FFB703; font-size: 34px; margin: 5px 0 0 0;">{total_portions_perdues} portions</h2></div>', unsafe_allow_html=True)
with kpi3:
    st.markdown(f'<div class="kpi-card"><h5>Bilan Carbone Associé</h5><h2 style="color: #FF4D4D; font-size: 34px; margin: 5px 0 0 0;">{impact_co2:.2f} kg CO₂e</h2><p style="font-size: 12px; color: #64748B; margin: 2px 0 0 0;">Soit équivalent à {km_voiture_equiv:.0f} km en voiture</p></div>', unsafe_allow_html=True)

st.markdown(" ")
st.markdown("#### 🎯 Jauge d'Efficience Collective")
performance_score = max(0.0, min(1.0, (100.0 - total_masse_kg) / 100.0))
st.progress(performance_score)
st.caption("💡 **Indicateur d'analyse pour le jury :** Plus la jauge tend vers 100%, plus la production de déchets est optimisée au collège Jean Giono (seuil visé : < 30 kg).")
