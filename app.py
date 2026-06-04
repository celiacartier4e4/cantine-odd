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

# --- STYLE CSS MULTI-LIGNES VALIDE ET SÉCURISÉ ---
st.markdown(
    """
    <style>
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; padding-left: 2rem !important; padding-right: 2rem !important; }
    .stApp { background: linear-gradient(135deg, #F8FAFC 0%, #E2E8F0 100%); }
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stText { color: #0F172A !important; font-family: 'Segoe UI', Roboto, sans-serif; }
    div[data-testid='stBlock'] { gap: 0.4rem !important; }
    .card-base { padding: 10px 14px; border-radius: 8px; margin-bottom: 8px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08); border-left: 6px solid rgba(0,0,0,0.2); }
    .card-gold { background: linear-gradient(135deg, #FFB703 0%, #FB8500 100%); }
    .card-cyan { background: linear-gradient(135deg, #00B4D8 0%, #0077B6 100%); }
    .card-purple { background: linear-gradient(135deg, #9D4EDD 0%, #7B2CBF 100%); }
    .card-green { background: linear-gradient(135deg, #2ECC71 0%, #27AE60 100%); }
    .card-red { background: linear-gradient(135deg, #FF4D4D 0%, #D90429 100%); }
    .card-gold *, .card-cyan * { color: #000000 !important; font-weight: 500; }
    .card-purple *, .card-green *, .card-red * { color: #FFFFFF !important; }
    .card-base label { font-size: 12px !important; font-weight: bold !important; }
    .kpi-card { border-radius: 6px; padding: 8px; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.05); color: white !important; }
    .kpi-green { background: #234E40; border: 1.5px solid #2ECC71; }
    .kpi-orange { background: #4E3E23; border: 1.5px solid #FFB703; }
    .kpi-red { background: #4E232B; border: 1.5px solid #FF4D4D; }
    .institution-box { background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%); border: 1.5px solid #2563EB; padding: 10px; border-radius: 8px; margin-bottom: 8px; }
    .institution-box * { color: #1E40AF !important; }
    div [data-testid='stProgressBar'] > div > div { background-image: linear-gradient(to right, #FF4D4D, #FFB703, #2ECC71) !important; }
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
st.markdown("<p style='margin:0; font-size:11px; font-weight:bold; color:#2563EB !important;'>🎖️ PROJET ÉCO-CITOYEN — CADRE CLASSE CDSG</p>", unsafe_allow_html=True)
st.markdown("<h2 style='margin:0 0 5px 0; padding:0; font-size:24px;'>🍏 Plateforme Réseau de Pilotage Environnemental</h2>", unsafe_allow_html=True)
st.markdown("<p style='margin:0 0 10px 0; font-size:13px;'><b>Collège Jean Giono (Orange)</b> — Impact des 700 demi-pensionnaires | Référent : M. Thierry Armant</p>", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# STRUCTURE EN 2 COLONNES PRINCIPALES
# ------------------------------------------------------------------------------
col_gauche_bilan, col_droite_saisie = st.columns([1.2, 1])

# ==============================================================================
# COLONNE DE DROITE : BLOC DE SAISIE DES CATEGORIES (AVEC LES EQUIVALENCES)
# ==============================================================================
with col_droite_saisie:
    st.markdown("<h4 style='margin:0 0 5px 0; font-size:15px; border-bottom:2px solid #64748B;'>📥 Saisie des Catégories de Pesée</h4>", unsafe_allow_html=True)

    # --- 1. BIODÉCHETS ---
    st.markdown('<div class="card-base card-green">', unsafe_allow_html=True)
    st.markdown("<h5 style='margin:0; font-size:13px;'>🗑️ Biodéchets — Restes de Plats Cuisinés</h5>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    poids_alim = c1.number_input("Masse Alim :", min_value=0.0, value=25.0, step=1.0, key="alim", label_visibility="collapsed")
    unite_alim = c2.selectbox("Unité Alim :", ["kg", "g"], key="u_alim", label_visibility="collapsed")
    kg_alim = normaliser_en_kg(poids_alim, unite_alim)
    equiv_repas = int(kg_alim / 0.150)
    st.markdown(f"<p style='margin:2px 0 0 0; font-size:11px;'>📊 <b>Analyse d'équivalence :</b> Environ <b>{equiv_repas} repas complets</b> rejetés.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 2. RELIQUATS PAIN ---
    st.markdown('<div class="card-base card-gold">', unsafe_allow_html=True)
    st.markdown("<h5 style='margin:0; font-size:13px;'>🥖 Reliquats de Pain (Boulangerie)</h5>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    poids_pain = c1.number_input("Masse Pain :", min_value=0.0, value=4.0, step=0.5, key="pain", label_visibility="collapsed")
    unite_pain = c2.selectbox("Unité Pain :", ["kg", "g"], key="u_pain", label_visibility="collapsed")
    kg_pain = normaliser_en_kg(poids_pain, unite_pain)
    equiv_baguettes = int(kg_pain / 0.250)
    st.markdown(f"<p style='margin:2px 0 0 0; font-size:11px;'>📊 <b>Analyse d'équivalence :</b> Environ <b>{equiv_baguettes} baguettes</b> de 250g perdues.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 3. PERTES FRUITS ---
    st.markdown('<div class="card-base card-red">', unsafe_allow_html=True)
    st.markdown("<h5 style='margin:0; font-size:13px;'>🍎 Pertes sur les Fruits</h5>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    poids_fruits = c1.number_input("Masse Fruits :", min_value=0.0, value=2.0, step=0.2, key="fruits", label_visibility="collapsed")
    unite_fruits = c2.selectbox("Unité Fruits :", ["kg", "g"], key="u_fruits", label_visibility="collapsed")
    kg_fruits = normaliser_en_kg(poids_fruits, unite_fruits)
    equiv_fruits = int(kg_fruits / 0.120)
    st.markdown(f"<p style='margin:2px 0 0 0; font-size:11px;'>📊 <b>Analyse d'équivalence :</b> Environ <b>{equiv_fruits} fruits entiers</b> gaspillés.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 4. SERVIETTES ---
    st.markdown('<div class="card-base card-cyan">', unsafe_allow_html=True)
    st.markdown("<h5 style='margin:0; font-size:13px;'>🧻 Consommation de Serviettes en Papier</h5>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    poids_serviettes = c1.number_input("Masse Serviettes :", min_value=0.0, value=1.5, step=0.1, key="serviettes", label_visibility="collapsed")
    unite_serviettes = c2.selectbox("Unité Serviettes :", ["kg", "g"], key="u_serviettes", label_visibility="collapsed")
    kg_serviettes = normaliser_en_kg(poids_serviettes, unite_serviettes)
    equiv_serviettes = int(kg_serviettes / 0.003)
    st.markdown(f"<p style='margin:2px 0 0 0; font-size:11px;'>📊 <b>Analyse d'équivalence :</b> Environ <b>{equiv_serviettes} unités</b> de serviettes jetées.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 5. EMBALLAGES ---
    st.markdown('<div class="card-base card-purple">', unsafe_allow_html=True)
    st.markdown("<h5 style='margin:0; font-size:13px;'>📦 Flux des Emballages Non Recyclés</h5>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    poids_emballages = c1.number_input("Masse Emb :", min_value=0.0, value=3.0, step=0.5, key="emballages", label_visibility="collapsed")
    unite_emballages = c2.selectbox("Unité Emb :", ["kg", "g"], key="u_emballages", label_visibility="collapsed")
    kg_emballages = normaliser_en_kg(poids_emballages, unite_emballages)
    equiv_emballages = int(kg_emballages / 0.020)
    st.markdown(f"<p style='margin:2px 0 0 0; font-size:11px;'>📊 <b>Analyse d'équivalence :</b> Environ <b>{equiv_emballages} unités</b> d'emballage indus.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ==============================================================================
# COLONNE DE GAUCHE : TOUS LES GRAPHIQUES (JOUR, SEMAINE, ANNÉE)
# ==============================================================================
with col_gauche_bilan:
    st.markdown("<h4 style='margin:0 0 5px 0; font-size:15px; border-bottom:2px solid #2563EB;'>📊 Bilans, Graphiques & Impacts Récapitulatifs</h4>", unsafe_allow_html=True)
    
    # --- CALCULS GLOBAUX ---
    total_masse_kg = kg_alim + kg_pain + kg_fruits + kg_serviettes + kg_emballages
    total_portions_perdues = equiv_repas + equiv_baguettes + equiv_fruits
    impact_co2 = total_masse_kg * 2.0
    km_voiture_equiv = impact_co2 / 0.120

    # --- CONTEXTE INSTITUTIONNEL ---
    st.markdown(
        """
        <div class='institution-box'>
        <h5 style='margin:0 0 2px 0; font-size:12px; font-weight:bold;'>🛡️ CONTEXTE CLASSE DÉFENSE (CDSG)</h5>
        <p style='font-size: 11px; margin: 0; line-height:1.3;'>Modélisation quantitative de résilience locale 
        face au gaspillage de ressources stratégiques. Répond aux exigences de l'<b>ODD 12</b> de l'ONU.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- ENCADRÉS KPIs ---
    k1, k2, k3 = st.columns(3)
    k1.markdown(f'<div class="kpi-card kpi-green"><p style="margin:0; font-size:10px;">Masse Globale (Jour)</p><h3 style="color:#2ECC71 !important; margin:1px 0; font-size:18px;">{total_masse_kg:.2f} kg</h3></div>', unsafe_allow_html=True)
    k2.markdown(f'<div class="kpi-card kpi-orange"><p style="margin:0; font-size:10px;">Volume Perdu</p><h3 style="
