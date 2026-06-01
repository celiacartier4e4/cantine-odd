import streamlit as st

# Titre principal de la page
st.title("🍏 Objectif Zéro Gaspi - Collège Jean Giono, Orange")
st.subheader("Suivi des déchets pour 700 demi-pensionnaires (ODD 12)")

st.write("""
Dans le cadre de l'**ODD 12 (Consommation et production responsables)**, 
notre collège quantifie les déchets de la cantine pour sensibiliser la communauté.
""")

# Création des colonnes pour afficher les chiffres en gros (les compteurs)
st.markdown("### 📊 Nos Pesées Hebdomadaires")
st.markdown("### 📊 Nos Pesées Hebdomadaires")

# --- CATEGORIE 1 ---
with st.container(border=True):
    st.subheader("🗑️ Déchets Alimentaires")
    st.write("**Poids mesuré :** 42 kg")
    st.caption("Restes d'assiettes — Objectif : Réduire le gaspillage direct !")

# --- CATEGORIE 2 ---
with st.container(border=True):
    st.subheader("🥖 Poubelle à Pain")
    st.write("**Poids mesuré :** 8 kg")
    st.caption("Pain jeté — Objectif : Prendre juste ce qu'il faut.")

# --- CATEGORIE 3 ---
with st.container(border=True):
    st.subheader("🍎 Fruits entamés")
    st.write("**Poids mesuré :** 5 kg")
    st.caption("Fruits non terminés — Objectif : Mieux évaluer sa faim.")

# --- CATEGORIE 4 ---
with st.container(border=True):
    st.subheader("🧻 Serviettes en papier")
    st.write("**Poids mesuré :** 3 kg")
    st.caption("Déchets non alimentaires.")

# --- CATEGORIE 5 ---
with st.container(border=True):
    st.subheader("📦 Emballages")
    st.write("**Poids mesuré :** 6 kg")
    st.caption("Plastiques, pots de yaourts, etc.")

# Ligne de séparation
st.write("---")

# Un petit message d'explication
st.info("💡 Le saviez-vous ? 8 kg de pain jetés représentent environ 32 baguettes perdues !")
