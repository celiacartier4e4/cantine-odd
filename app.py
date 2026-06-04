import streamlit as st
import pandas as pd

# ==========================================
# CONFIGURATION
# ==========================================
st.set_page_config(page_title="Giono - CDSG", page_icon="🍏", layout="wide")

# URL de l'image du Théâtre Antique d'Orange
u_base = "https://provence-alpes-cotedazur.com/"
u_code = "app/uploads/crt-paca/2020/12/thumbs/"
u_file = "orange-f-2018-14945-1920x960.jpg"
fond_ecran = u_base + u_code + u_file

# Injection CSS en un seul bloc de texte pour éviter les coupures
css_glossy = f"""
<style>
[data-testid='stApp'] {{
    background-image: linear-gradient(rgba(15,23,42,0.45), rgba(15,23,42,0.65)), url('{fond_ecran}') !important;
    background-size: cover !important;
    background-position: center !important;
    background-attachment: fixed !important;
}}
[data-testid='stHeader'], [data-testid='stAppViewContainer'] {{
    background: transparent !important;
}}
h1, h2, h3, h4, h5, h6, p, label, span, div, text {{
    color: #ffffff !important;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.8) !important;
}}
div[data-testid='stVerticalBlockBorderWrapper'] > div {{
    background: linear-gradient(135deg, rgba(255,255,255,0.12), rgba(255,255,255,0.03)) !important;
    backdrop-filter: blur(10px) !important;
    -webkit-backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(255, 255, 255, 0.25) !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
    border-radius: 12px !important;
    padding: 18px !important;
}}
div[data-testid='stWidgetLabel'] p {{
    color: #ffffff !important;
    font-weight: bold !important;
}}
</style>
"""
st.markdown(css_glossy, unsafe_allow_html=True)

# ==========================================
# EN-TÊTE
# ==========================================
st.title("Collège Jean Giono d'Orange")
st.subheader("Projet Éco-Citoyen - CLASSE DÉFENSE (CDSG Giono)")

# ==========================================
# SAISIE DES DONNÉES
# ==========================================
col_gauche, col_droite = st.columns(2)

with col_gauche:
    with st.container(border=True):
        st.write("### 🥖 Reliquats de Pain (Boulangerie)")
        p_pain = st.number_input("Masse mesurée (kg) :", 0.0, 100.0, 4.0, 0.5, key="pain")
        st.write(f"Équivalent : {int(p_pain / 0.25)} baguettes perdues.")

    with st.container(border=True):
        st.write("### 🧻 Serviettes en Papier")
        p_serv = st.number_input("Masse mesurée (kg) :", 0.0, 100.0, 1.5, 0.1, key="serviettes")
        st.write(f"Équivalent : {int(p_serv / 0.003)} serviettes jetées.")

    with st.container(border=True):
        st.write("### 📦 Emballages Non Recyclés")
        p_emb = st.number_input("Masse mesurée (kg) :", 0.0, 100.0, 3.0, 0.5, key="emballages")
        st.write(f"Équivalent : {int(p_emb / 0.02)} emballages jetés.")

with col_droite:
    with st.container(border=True):
        st.write("### 🗑️ Biodéchets — Restes Cuisinés")
        p_bio = st.number_input("Masse mesurée (kg) :", 0.0, 100.0, 25.0, 1.0, key="biodechets")
        st.write(f"Équivalent : {int(p_bio / 0.15)} repas jetés.")

    with st.container(border=True):
        st.write("### 🍎 Pertes sur les Fruits")
        p_frt = st.number_input("Masse mesurée (kg) :", 0.0, 100.0, 2.0, 0.2, key="fruits")
        st.write(f"Équivalent : {int(p_frt / 0.12)} fruits gaspillés.")

    with st.container(border=True):
        st.write("### 🛡️ CONTEXTE CDSG")
        st.write("📋 **Établissement :** Collège Jean Giono d'Orange.")
        st.write("💡 Modélisation quantitative liée à l'ODD 12 de l'ONU.")
        st.write("🚀 Mesures d'impact pour les 700 demi-pensionnaires.")

# ==========================================
# RESTITUTION ET BILANS
# ==========================================
st.divider()
st.write("<h2>📊 Bilans et Indicateurs Centraux</h2>", unsafe_allow_html=True)

b1, b2 = st.columns([1.3, 1])

with b1:
    st.write("### 📈 Répartition Globale des Déchets")
    tot_masse = p_pain + p_serv + p_emb + p_bio + p_frt
    df_bilan = pd.DataFrame(
        [[p_bio, p_pain, p_frt, p_serv, p_emb]], 
        columns=["Biodéchets", "Pain", "Fruits", "Serviettes", "Emballages"]
    )
    st.bar_chart(df_bilan, horizontal=True, height=130)

with b2:
    st.write("### 📊 Calculs d'Impact")
    bilan_co2 = tot_masse * 2.0
    equiv_km = bilan_co2 / 0.12
    
    st.write(f"🔹 **Masse Globale Capturée :** {tot_masse:.2f} kg")
    st.write(f"🔹 **Bilan Carbone :** {bilan_co2:.2f} kg CO2e")
    st.write(f"🔹 **Équivalent Voiture :** {equiv_km:.0f} km")
    
    st.write("**🎯 Jauge d'Efficience Collective**")
    score_bar = max(0.0, min(1.0, (100.0 - tot_masse) / 100.0))
    st.progress(score_bar)
