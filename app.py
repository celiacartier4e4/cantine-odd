import streamlit as st
import pandas as pd

# ==========================================
# CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Giono - CDSG",
    page_icon="🍏",
    layout="wide"
)

# --- URL DECOUPÉE POUR EVITER LES COUPURES ---
u1 = "https://images.unsplash.com/"
u2 = "photo-1541339907198-e08756dedf3f"
u3 = "?q=80&w=1920"
img_url = u1 + u2 + u3

# --- INJECTION DU DESIGN AVEC TEXTES BLANCS ---
css = [
    "<style>",
    ".stApp {",
    "background: linear-gradient(",
    "rgba(15,23,42,0.35),",
    "rgba(15,23,42,0.65)),",
    f"url('{img_url}');",
    "background-size: cover;",
    "background-position: center;",
    "background-attachment: fixed;",
    "}",
    /* Force TOUS les textes du site en blanc */
    "h1, h2, h3, h4, h5, h6, p, label, span, div {",
    "color: #ffffff !important;",
    "text-shadow: 1px 1px 3px rgba(0,0,0,0.9);",
    "}",
    /* Conteneurs de saisie en fond sombre transparent */
    "div[data-testid='stContainer'] {",
    "background-color: rgba(15, 23, 42, 0.85) !important;",
    "border: 1px solid #38bdf8 !important;",
    "border-radius: 12px;",
    "padding: 20px;",
    "}",
    /* Textes des étiquettes de saisie en blanc */
    "div[data-testid='stWidgetLabel'] p {",
    "color: #ffffff !important;",
    "font-weight: bold !important;",
    "}",
    "</style>"
]
st.markdown("\n".join(css), unsafe_allow_html=True)

# ==========================================
# EN-TÊTE
# ==========================================
st.markdown("<h1>Collège Jean Giono d'Orange</h1>", unsafe_allow_html=True)
st.markdown("<h3>Projet Éco-Citoyen - CDSG Giono</h3>", unsafe_allow_html=True)

# ==========================================
# COLONNES DE SAISIE (STRUCTURE PHOTO)
# ==========================================
col_g, col_d = st.columns(2)

with col_g:
    with st.container(border=True):
        st.markdown("<h3 style='color:#ffb703 !important;'>🥖 Reliquats de Pain (Boulangerie)</h3>", unsafe_allow_html=True)
        p_pain = st.number_input("Masse (kg) :", 0.0, 100.0, 4.0, 0.5)
        st.write(f"Equiv: {int(p_pain / 0.25)} baguettes de 250g perdues.")

    with st.container(border=True):
        st.markdown("<h3 style='color:#00f5ff !important;'>🧻 Serviettes en Papier</h3>", unsafe_allow_html=True)
        p_serv = st.number_input("Masse (kg) :", 0.0, 100.0, 1.5, 0.1)
        st.write(f"Equiv: {int(p_serv / 0.003)} serviettes jetées.")

    with st.container(border=True):
        st.markdown("<h3 style='color:#a855f7 !important;'>📦 Emballages Non Recyclés</h3>", unsafe_allow_html=True)
        p_emb = st.number_input("Masse (kg) :", 0.0, 100.0, 3.0, 0.5)
        st.write(f"Equiv: {int(p_emb / 0.02)} emballages industriels.")

with col_d:
    with st.container(border=True):
        st.markdown("<h3 style='color:#22c55e !important;'>🗑️ Biodéchets — Restes Cuisinés</h3>", unsafe_allow_html=True)
        p_bio = st.number_input("Masse (kg) :", 0.0, 100.0, 25.0, 1.0)
        st.write(f"Equiv: {int(p_bio / 0.15)} repas complets rejetés.")

    with st.container(border=True):
        st.markdown("<h3 style='color:#ef4444 !important;'>🍎 Pertes sur les Fruits</h3>", unsafe_allow_html=True)
        p_frt = st.number_input("Masse (kg) :", 0.0, 100.0, 2.0, 0.2)
        st.write(f"Equiv: {int(p_frt / 0.12)} fruits entiers gaspillés.")

    with st.container(border=True):
        st.markdown("<h3 style='color:#38bdf8 !important;'>🛡️ CONTEXTE CDSG</h3>", unsafe_allow_html=True)
        st.write("📋 **Collège Jean Giono :** Impact environnemental de 700 demi-pensionnaires.")
        st.write("💡 Analyse quantitative du gaspillage de ressources stratégiques.")
        st.write("🚀 Données liées aux indicateurs de l'ODD 12 de l'ONU.")

# ==========================================
# PANNEAU DE SYNTHÈSE DU BAS
# ==========================================
st.divider()
st.markdown("<h2>📊 Bilans et Indicateurs Centraux</h2>", unsafe_allow_html=True)

b1, b2 = st.columns([1.3, 1])

with b1:
    st.markdown("### 📈 Répartition Globale des Déchets", unsafe_allow_html=True)
    tot = p_pain + p_serv + p_emb + p_bio + p_frt
    df = pd.DataFrame(
        [[p_bio, p_pain, p_frt, p_serv, p_emb]], 
        columns=["Bio", "Pain", "Fruits", "Serv", "Emb"]
    )
    st.bar_chart(df, horizontal=True, height=120)

with b2:
    st.markdown("### 📊 Indicateurs", unsafe_allow_html=True)
    co2 = tot * 2.0
    km = co2 / 0.12
    st.write(f"🔹 **Masse Globale Capturée :** {tot:.2f} kg")
    st.write(f"🔹 **Bilan Carbone :** {co2:.2f} kg CO2e")
    st.write(f"🔹 **Équivalent Voiture :** {km:.0f} km")
    
    st.markdown("**🎯 Jauge d'Efficience Collective**", unsafe_allow_html=True)
    score = max(0.0, min(1.0, (100.0 - tot) / 100.0))
    st.progress(score)
