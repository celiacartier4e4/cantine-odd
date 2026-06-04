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

# --- URL DECOUPÉE POUR EVITER LES COUPURES DE LIGNE ---
u1 = "https://images.unsplash.com/"
u2 = "photo-1541339907198-e08756dedf3f"
u3 = "?q=80&w=1920"
img_url = u1 + u2 + u3

# --- INJECTION DU FOND D'ECRAN SECURISE ---
css = [
    "<style>",
    ".stApp {",
    "background: linear-gradient(",
    "rgba(255,255,255,0.15),",
    "rgba(15,23,42,0.45)),",
    f"url('{img_url}');",
    "background-size: cover;",
    "background-position: center;",
    "background-attachment: fixed;",
    "}",
    "div[data-testid='stContainer'] {",
    "background-color: rgba(255,255,255,0.9);",
    "border-radius: 12px;",
    "padding: 15px;",
    "}",
    "h1, h2, h3, h4, p, span {",
    "color: #0f172a !important;",
    "}",
    "</style>"
]
st.markdown("\n".join(css), unsafe_allow_html=True)

# ==========================================
# EN-TÊTE
# ==========================================
st.title("Collège Jean Giono d'Orange")
st.subheader("Projet Éco-Citoyen - CDSG Giono")

# ==========================================
# COLONNES DE SAISIE (STRUCTURE PHOTO)
# ==========================================
col_g, col_d = st.columns(2)

with col_g:
    with st.container(border=True):
        st.write("### 🥖 Reliquats de Pain (Boulangerie)")
        p_pain = st.number_input("Masse (kg) :", 0.0, 100.0, 4.0, 0.5, key="p1")
        st.write(f"Equiv: {int(p_pain / 0.25)} baguettes.")

    with st.container(border=True):
        st.write("### 🧻 Serviettes en Papier")
        p_serv = st.number_input("Masse (kg) :", 0.0, 100.0, 1.5, 0.1, key="p2")
        st.write(f"Equiv: {int(p_serv / 0.003)} serviettes.")

    with st.container(border=True):
        st.write("### 📦 Emballages Non Recyclés")
        p_emb = st.number_input("Masse (kg) :", 0.0, 100.0, 3.0, 0.5, key="p3")
        st.write(f"Equiv: {int(p_emb / 0.02)} emballages.")

with col_d:
    with st.container(border=True):
        st.write("### 🗑️ Biodéchets — Restes Cuisinés")
        p_bio = st.number_input("Masse (kg) :", 0.0, 100.0, 25.0, 1.0, key="p4")
        st.write(f"Equiv: {int(p_bio / 0.15)} repas jetés.")

    with st.container(border=True):
        st.write("### 🍎 Pertes sur les Fruits")
        p_frt = st.number_input("Masse (kg) :", 0.0, 100.0, 2.0, 0.2, key="p5")
        st.write(f"Equiv: {int(p_frt / 0.12)} fruits gaspillés.")

    with st.container(border=True):
        st.write("### 🛡️ CONTEXTE CDSG")
        st.write("Collège Jean Giono — 700 élèves.")
        st.write("Analyse liée à l'ODD 12 de l'ONU.")

# ==========================================
# PANNEAU DE SYNTHÈSE DU BAS
# ==========================================
st.divider()
st.write("## 📊 Bilans et Indicateurs")

b1, b2 = st.columns([1.3, 1])

with b1:
    st.write("### 📈 Répartition des Déchets")
    tot = p_pain + p_serv + p_emb + p_bio + p_frt
    df = pd.DataFrame(
        [[p_bio, p_pain, p_frt, p_serv, p_emb]], 
        columns=["Bio", "Pain", "Fruits", "Serv", "Emb"]
    )
    st.bar_chart(df, horizontal=True, height=120)

with b2:
    st.write("### 📊 Indicateurs Centraux")
    co2 = tot * 2.0
    km = co2 / 0.12
    st.write(f"**Masse Globale :** {tot:.2f} kg")
    st.write(f"**Bilan Carbone :** {co2:.2f} kg CO2e")
    st.write(f"**Équivalent Voiture :** {km:.0f} km")
    
    st.write("**🎯 Jauge d'Efficience**")
    score = max(0.0, min(1.0, (100.0 - tot) / 100.0))
    st.progress(score)
