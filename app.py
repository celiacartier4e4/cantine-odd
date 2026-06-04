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

# --- CSS EN LIGNES TRÈS COURTES ---
css = [
    "<style>",
    ".stApp {",
    "background: linear-gradient(",
    "rgba(255,255,255,0.1),rgba(15,23,42,0.4)),",
    "url('https://images.unsplash.com/",
    "photo-1541339907198-e08756dedf3f?q=80&w=1920');",
    "background-size: cover;",
    "}",
    ".card { padding: 15px; border-radius: 12px;",
    "margin-bottom: 15px; color:black !important; }",
    ".bg-gold { background: #ffb703; }",
    ".bg-cyan { background: #00f5ff; }",
    ".bg-purple { background: #a855f7; color:white !important; }",
    ".bg-green { background: #22c55e; color:white !important; }",
    ".bg-red { background: #ef4444; color:white !important; }",
    ".bg-dark { background: #0f172a; color:white !important;",
    "border: 1px solid #38bdf8; }",
    ".bottom-panel { background: #090d16; border-radius:12px;",
    "padding: 20px; border: 1px solid #1e293b; }",
    "div[data-testid='stWidgetLabel'] p {",
    "color: inherit !important; font-weight: bold; }",
    "</style>"
]
st.markdown("\n".join(css), unsafe_allow_html=True)

# ==========================================
# EN-TÊTE
# ==========================================
st.header("Collège Jean Giono d'Orange")
st.subheader("Projet Éco-Citoyen - CDSG Giono")

# ==========================================
# COLONNES DE SAISIE (MÊME PARCOURS QUE LA PHOTO)
# ==========================================
col_g, col_d = st.columns(2)

with col_g:
    # 1. Pain
    st.markdown('<div class="card bg-gold">', unsafe_allow_html=True)
    st.markdown("### 🥖 Reliquats de Pain (Boulangerie)")
    p_pain = st.number_input("Masse (kg) :", 0.0, 100.0, 4.0, 0.5, key="p1")
    eq_p = int(p_pain / 0.25)
    st.markdown(f"Equiv: {eq_p} baguettes.", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. Serviettes
    st.markdown('<div class="card bg-cyan">', unsafe_allow_html=True)
    st.markdown("### 🧻 Serviettes en Papier")
    p_serv = st.number_input("Masse (kg) :", 0.0, 100.0, 1.5, 0.1, key="p2")
    eq_s = int(p_serv / 0.003)
    st.markdown(f"Equiv: {eq_s} serviettes.", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 3. Emballages
    st.markdown('<div class="card bg-purple">', unsafe_allow_html=True)
    st.markdown("### 📦 Emballages Non Recyclés")
    p_emb = st.number_input("Masse (kg) :", 0.0, 100.0, 3.0, 0.5, key="p3")
    eq_e = int(p_emb / 0.02)
    st.markdown(f"Equiv: {eq_e} emballages.", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_d:
    # 4. Biodéchets
    st.markdown('<div class="card bg-green">', unsafe_allow_html=True)
    st.markdown("### 🗑️ Biodéchets — Restes Cuisinés")
    p_bio = st.number_input("Masse (kg) :", 0.0, 100.0, 25.0, 1.0, key="p4")
    eq_b = int(p_bio / 0.15)
    st.markdown(f"Equiv: {eq_b} repas jetés.", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 5. Fruits
    st.markdown('<div class="card bg-red">', unsafe_allow_html=True)
    st.markdown("### 🍎 Pertes sur les Fruits")
    p_frt = st.number_input("Masse (kg) :", 0.0, 100.0, 2.0, 0.2, key="p5")
    eq_f = int(p_frt / 0.12)
    st.markdown(f"Equiv: {eq_f} fruits gaspillés.", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 6. Contexte
    st.markdown('<div class="card bg-dark">', unsafe_allow_html=True)
    st.markdown("###
