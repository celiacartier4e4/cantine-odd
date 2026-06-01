import streamlit as st

# Titre principal de la page
st.title("🍏 Objectif Zéro Gaspi - Collège Jean Giono")
st.subheader("Suivi des déchets pour 700 demi-pensionnaires (ODD 12)")

st.write("""
**À vous de jouer !** Entrez les poids mesurés à la cantine dans les cases ci-dessous pour voir l'impact de notre gaspillage.
""")

st.markdown("### 📊 Nos Pesées Hebdomadaires")

# --- CATEGORIE 1 ---
with st.container(border=True):
    st.subheader("🗑️ Déchets Alimentaires")
    # On crée la case modifiable par l'utilisateur (42.0 est la valeur de départ)
    poids_alim = st.number_input("Entrez le poids des déchets alimentaires (en kg) :", min_value=0.0, value=42.0, step=0.5, key="alim")
    st.caption("Restes d'assiettes — Objectif : Réduire le gaspillage direct !")

# --- CATEGORIE 2 ---
with st.container(border=True):
    st.subheader("🥖 Poubelle à Pain")
    # Case modifiable pour le pain (8.0 au départ)
    poids_pain = st.number_input("Entrez le poids du pain jeté (en kg) :", min_value=0.0, value=8.0, step=0.5, key="pain")
    # Calcul en direct du nombre de baguettes
    nb_baguettes = int(poids_pain / 0.25)
    st.write(f"💡 *Cela représente environ **{nb_baguettes} baguettes** perdues !*")

# --- CATEGORIE 3 ---
with st.container(border=True):
    st.subheader("🍎 Fruits entamés")
    poids_fruits = st.number_input("Entrez le poids des fruits jetés (en kg) :", min_value=0.0, value=5.0, step=0.5, key="fruits")

# --- CATEGORIE 4 ---
with st.container(border=True):
    st.subheader("🧻 Serviettes en papier")
    poids_serviettes = st.number_input("Entrez le poids des serviettes (en kg) :", min_value=0.0, value=3.0, step=0.5, key="serviettes")

# --- CATEGORIE 5 ---
with st.container(border=True):
    st.subheader("📦 Emballages")
    poids_emballages = st.number_input("Entrez le poids des emballages (en kg) :", min_value=0.0, value=6.0, step=0.5, key="emballages")
