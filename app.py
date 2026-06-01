import streamlit as st

# Titre principal de la page
st.title("🍏 Objectif Zéro Gaspi - Collège Jean Giono")
st.subheader("Suivi des déchets pour 700 demi-pensionnaires (ODD 12)")

st.write("""
**À vous de jouer !** Tapez le poids mesuré dans la case, puis choisissez l'unité (g ou kg) pour chaque catégorie.
""")

st.markdown("### 📊 Nos Pesées Hebdomadaires")

# --- CATEGORIE 1 : Déchets Alimentaires ---
with st.container(border=True):
    st.subheader("🗑️ Déchets Alimentaires")
    # 1. La valeur en premier
    poids_alim = st.text_input("Entrez la valeur (ex: 42 ou 500) :", value="42", key="alim")
    # 2. L'unité en deuxième
    unite_alim = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_alim")
    st.write(f"**Poids enregistré :** {poids_alim} {unite_alim}")
    st.caption("Restes d'assiettes — Objectif : Réduire le gaspillage direct !")

# --- CATEGORIE 2 : Poubelle à Pain ---
with st.container(border=True):
    st.subheader("🥖 Poubelle à Pain")
    poids_pain = st.text_input("Entrez la valeur (ex: 8 ou 250) :", value="8", key="pain")
    unite_pain = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_pain")
    st.write(f"**Poids enregistré :** {poids_pain} {unite_pain}")
    
    # Calcul automatique du nombre de baguettes
    try:
        valeur_pain = float(poids_pain.replace(",", "."))
        if unite_pain == "g":
            valeur_pain = valeur_pain / 1000
        nb_baguettes = int(valeur_pain / 0.25)
        st.write(f"💡 *Cela représente environ **{nb_baguettes} baguettes** perdues !*")
    except:
        st.write("💡 *Entrez un chiffre valide pour voir l'équivalent en baguettes.*")

# --- CATEGORIE 3 : Fruits entamés ---
with st.container(border=True):
    st.subheader("🍎 Fruits entamés")
    poids_fruits = st.text_input("Entrez la valeur :", value="5", key="fruits")
    unite_fruits = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_fruits")
    st.write(f"**Poids enregistré :** {poids_fruits} {unite_fruits}")

# --- CATEGORIE 4 : Serviettes en papier ---
with st.container(border=True):
    st.subheader("🧻 Serviettes en papier")
    poids_serviettes = st.text_input("Entrez la valeur :", value="3", key="serviettes")
    unite_serviettes = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_serviettes")
    st.write(f"**Poids enregistré :** {poids_serviettes} {unite_serviettes}")

# --- CATEGORIE 5 : Emballages ---
with st.container(border=True):
    st.subheader("📦 Emballages")
    poids_emballages = st.text_input("Entrez la valeur :", value="6", key="emballages")
    unite_emballages = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_emballages")
    st.write(f"**Poids enregistré :** {poids_emballages} {unite_emballages}")
