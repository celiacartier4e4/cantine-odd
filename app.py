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

# Injection CSS : Un seul grand rectangle glossy opaque à droite
css_glossy = f"""
<style>
[data-testid='stApp'] {{
    background-image: linear-gradient(rgba(15,23,42,0.4), rgba(15,23,42,0.6)), url('{fond_ecran}') !important;
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
/* Style du grand encadré glossy unique (colonne de droite) */
.glossy-panel {{
    background: linear-gradient(135deg, rgba(15, 23, 42, 0.85), rgba(30, 41, 59, 0.75)) !important;
    backdrop-filter: blur(15px) !important;
    -webkit-backdrop-filter: blur(15px) !important;
    border: 1px solid rgba(255, 255, 255, 0.25) !important;
    box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.6) !important;
    border-radius: 16px !important;
    padding: 25px !important;
}}
div[data-testid='stWidgetLabel'] p {{
    color: #ffffff !important;
    font-weight: bold !important;
}}
hr {{
    border-color: rgba(255, 255, 255, 0.15) !important;
}}
</style>
"""
st.markdown(css_glossy, unsafe_allow_html=True)

# ==========================================
# EN-TÊTE
# ==========================================
st.title("Collège Jean Giono d'Orange")
st.subheader("Projet Éco-Citoyen - CLASSE DÉFENSE (CDSG Giono)")
st.divider()

# ==========================================
# STRUCTURE PRINCIPALE (GAUCHE / DROITE)
# ==========================================
col_gauche, col_droite = st.columns([2.8, 1.2])

# --- COLONNE DE DROITE : UN SEUL GRAND PANNEAU GLOSSY ---
with col_droite:
    # Utilisation d'une div HTML customisée par notre CSS "glossy-panel"
    st.markdown('<div class="glossy-panel">', unsafe_allow_html=True)
    
    st.write("## 📝 Saisie des Données")
    st.write("---")
    
    st.write("### 🥖 Pain (Boulangerie)")
    p_pain = st.number_input("Masse (kg) :", 0.0, 100.0, 4.0, 0.5, key="pain")
    st.write(f"Équiv: {int(p_pain / 0.25)} baguettes.")

    st.write("---")
    st.write("### 🧻 Serviettes Papier")
    p_serv = st.number_input("Masse (kg) :", 0.0, 100.0, 1.5, 0.1, key="serviettes")
    st.write(f"Équiv: {int(p_serv / 0.003)} serviettes.")

    st.write("---")
    st.write("### 📦 Emballages")
    p_emb = st.number_input("Masse (kg) :", 0.0, 100.0, 3.0, 0.5, key="emballages")
    st.write(f"Équiv: {int(p_emb / 0.02)} unités.")

    st.write("---")
    st.write("### 🗑️ Biodéchets")
    p_bio = st.number_input("Masse (kg) :", 0.0, 100.0, 25.0, 1.0, key="biodechets")
    st.write(f"Équiv: {int(p_bio / 0.15)} repas.")

    st.write("---")
    st.write("### 🍎 Fruits")
    p_frt = st.number_input("Masse (kg) :", 0.0, 100.0, 2.0, 0.2, key="fruits")
    st.write(f"Équiv: {int(p_frt / 0.12)} fruits.")

    st.write("---")
    st.write("### 🛡️ CONTEXTE")
    st.write("📋 Collège Jean Giono d'Orange.")
    st.write("💡 Modélisation liée à l'ODD 12 (ONU).")
    st.write("🚀 Impact pour 700 demi-pensionnaires.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- COLONNE DE GAUCHE : LES GRAPHIQUES ET BILANS CENTRAUX ---
with col_gauche:
    st.write("<h2>📊 Bilans et Indicateurs Centraux</h2>", unsafe_allow_html=True)
    
    st.write("### 📈 Répartition Globale des Déchets")
    tot_masse = p_pain + p_serv + p_emb + p_bio + p_frt
    df_bilan = pd.DataFrame(
        [[p_bio, p_pain, p_frt, p_serv, p_emb]], 
        columns=["Biodéchets", "Pain", "Fruits", "Serviettes", "Emballages"]
    )
    st.bar_chart(df_bilan, horizontal=True, height=160)
    
    st.write(" ")
    st.write(" ")
    
    st.write("### 📊 Calculs d'Impact Environnemental")
    bilan_co2 = tot_masse * 2.0
    equiv_km = bilan_co2 / 0.12
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label="Masse Globale Capturée", value=f"{tot_masse:.2f} kg")
    with c2:
        st.metric(label="Bilan Carbone Estimé", value=f"{bilan_co2:.2f} kg CO2e")
    with c3:
        st.metric(label="Équivalent Routier", value=f"{equiv_km:.0f} km")
        
    st.write(" ")
    st.write("**🎯 Jauge d'Efficience Collective de l'Établissement**")
    score_bar = max(0.0, min(1.0, (100.0 - tot_masse) / 100.0))
    st.progress(score_bar)
