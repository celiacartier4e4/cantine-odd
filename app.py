import streamlit as st

# Titre principal de la page
st.title("🍏 Objectif Zéro Gaspi - Collège Jean Giono")
st.subheader("Suivi des déchets pour 700 demi-pensionnaires (ODD 12)")

st.write("""
**À vous de jouer !** Utilisez les flèches pour augmenter ou diminuer le chiffre, puis choisissez l'unité (g ou kg).
""")

st.markdown("### 📊 Nos Pesées Hebdomadaires")

# --- CATEGORIE 1 : Déchets Alimentaires ---
st.markdown('<div style="background-color: #FFF2CC; padding: 15px; border-radius: 10px; border-left: 5px solid #F1C232; margin-bottom: 20px;">', unsafe_allow_html=True)
st.subheader("🗑️ Déchets Alimentaires")
# Case numérique avec flèches (valeur de départ : 42.0)
poids_alim = st.number_input("Ajustez la valeur :", min_value=0.0, value=42.0, step=0.5, key="alim")
unite_alim = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_alim")
st.write(f"**Poids enregistré :** {poids_alim} {unite_alim}")
st.caption("Restes d'assiettes — Objectif : Réduire le gaspillage direct !")
st.markdown('</div>', unsafe_allow_html=True)

# --- CATEGORIE 2 : Poubelle à Pain ---
st.markdown('<div style="background-color: #FFE5CC; padding: 15px; border-radius: 10px; border-left: 5px solid #E69138; margin-bottom: 20px;">', unsafe_allow_html=True)
st.subheader("🥖 Poubelle à Pain")
# Case numérique avec flèches (valeur de départ : 8.0)
poids_pain = st.number_input("Ajustez la valeur :", min_value=0.0, value=8.0, step=0.5, key="pain")
unite_pain = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_pain")
st.write(f"**Poids enregistré :** {poids_pain} {unite_pain}")

# Calcul automatique du nombre de baguettes
valeur_pain = poids_pain
if unite_pain == "g":
    valeur_pain = valeur_pain / 1000
nb_baguettes = int(valeur_pain / 0.25)
st.write(f"💡 *Cela représente environ **{nb_baguettes} baguettes** perdues !*")
st.markdown('</div>', unsafe_allow_html=True)

# --- CATEGORIE 3 : Fruits entamés ---
st.markdown('<div style="background-color: #E2EFDA; padding: 15px; border-radius: 10px; border-left: 5px solid #A9D08E; margin-bottom: 20px;">', unsafe_allow_html=True)
st.subheader("🍎 Fruits entamés")
# Case numérique avec flèches (valeur de départ : 5.0)
poids_fruits = st.number_input("Ajustez la valeur :", min_value=0.0, value=5.0, step=0.5, key="fruits")
unite_fruits = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_fruits")
st.write(f"**Poids enregistré :** {poids_fruits} {unite_fruits}")
st.markdown('</div>', unsafe_allow_html=True)

# --- CATEGORIE 4 : Serviettes en papier ---
st.markdown('<div style="background-color: #DDEBF7; padding: 15px; border-radius: 10px; border-left: 5px solid #9BC2E6; margin-bottom: 20px;">', unsafe_allow_html=True)
st.subheader("🧻 Serviettes en papier")
# Case numérique avec flèches (valeur de départ : 3.0)
poids_serviettes = st.number_input("Ajustez la valeur :", min_value=0.0, value=3.0, step=0.5, key="serviettes")
unite_serviettes = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_serviettes")
st.write(f"**Poids enregistré :** {poids_serviettes} {unite_serviettes}")
st.markdown('</div>', unsafe_allow_html=True)

# --- CATEGORIE 5 : Emballages ---
st.markdown('<div style="background-color: #E1D5E7; padding: 15px; border-radius: 10px; border-left: 5px solid #B4A7D6; margin-bottom: 20px;">', unsafe_allow_html=True)
st.subheader("📦 Emballages")
# Case numérique avec flèches (valeur de départ : 6.0)
poids_emballages = st.number_input("Ajustez la valeur :", min_value=0.0, value=6.0, step=0.5, key="emballages")
unite_emballages = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_emballages")
st.write(f"**Poids enregistré :** {poids_emballages} {unite_emballages}")
st.markdown('</div>', unsafe_allow_html=True)
