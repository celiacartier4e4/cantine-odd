import streamlit as st
import pandas as pd

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

    /* --- CARTES AUX COULEURS VIVES --- */
    .card-base {
        padding: 20px;
        border-radius: 14px;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
        border: 2px solid #FFFFFF;
    }

    /* Fonds colorés vifs */
    .card-green { background-color: #2ECC71; }   /* Vert */
    .card-gold { background-color: #FFB703; }    /* Jaune/Orange */
    .card-red { background-color: #FF4D4D; }     /* Rouge */
    .card-cyan { background-color: #00B4D8; }    /* Cyan */
    .card-purple { background-color: #9D4EDD; }  /* Violet */

    /* Forcer la lisibilité du texte */
    .card-gold *, .card-cyan * { color: #000000 !important; }
    .card-purple *, .card-green *, .card-red * { color: #FFFFFF !important; }

    /* Blocs indicateurs du bas (KPIs) */
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

# ==============================================================================
# ÉTAPE 1 : CRÉATION SECRÈTE DES FORMULAIRES DE SAISIE POUR OBTENIR LES VARIABLES
# ==============================================================================
# Pour que le graphique à gauche connaisse les valeurs sans bugger, on crée temporairement 
# les éléments de saisie dans des variables globales en utilisant des "st.sidebar" invisibles 
# ou des conteneurs, mais pour garder la structure exacte demandée (Saisie à droite), 
# on va utiliser des conteneurs vides Streamlit (`st.empty()`).

# On prépare les emplacements à droite dans le code pour les forcer à s'exécuter en premier !
inputs_data = {}

# ==============================================================================
# ÉTAPE 2 : DISTRIBUTION DE L'INTERFACE EN DEUX COLONNES
# ==============================================================================
col_gauche, col_droite = st.columns([1.3, 1])

# --- ON REMPLIT LA COLONNE DROITE EN PREMIER POUR LE MOTEUR PYTHON ---
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

# --- MAINTENANT ON REMPLIT LA COLONNE GAUCHE (Le graphique possède enfin ses variables !) ---
with col_gauche:
    st.markdown("### 📊 Répartition en Temps Réel de la Masse des Déchets")
    st.write(" ")
    
    # Création sécurisée du tableau de données pour le graphique
    total_somme = kg_alim + kg_pain + kg_fruits + kg_serviettes + kg_emballages
    
    if total_somme == 0:
        # Évite le crash si toutes les valeurs valent 0
        donnees_graphique = pd.DataFrame({
            "Catégories": ["En attente de données..."],
            "Masse (kg)": [1.0],
            "Couleur": ["#94A3B8"]
        })
        color_scale = {"domain": ["En attente de données..."], "range": ["#94A3B8"]}
    else:
        donnees_graphique = pd.DataFrame({
            "Catégories": ["Biodéchets 🗑️", "Pain 🥖", "Fruits 🍎", "Serviettes 🧻", "Emballages 📦"],
            "Masse (kg)": [kg_alim, kg_pain, kg_fruits, kg_serviettes, kg_emballages]
        })
        color_scale = {
            "domain": ["Biodéchets 🗑️", "Pain 🥖", "Fruits 🍎", "Serviettes 🧻", "Emballages 📦"],
            "range": ["#2ECC71", "#FFB703", "#FF4D4D", "#00B4D8", "#9D4EDD"]
        }
    
    # Affichage du graphique en forme de cercle parfait (Donut)
    st.vega_lite_chart(donnees_graphique, {
        "width": "container",
        "height": 550,
        "mark": {"type": "arc", "innerRadius": 100, "stroke": "#fff", "strokeWidth": 3},
        "encoding": {
            "theta": {"field": "Masse (kg)", "type": "quantitative"},
            "color": {
                "field": "Catégories", 
                "type": "nominal",
                "scale": color_scale,
                "legend": {"orient": "bottom", "labelFontSize": 15, "titleFontSize": 15, "offset": 20}
            },
            "tooltip":
