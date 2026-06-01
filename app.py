import streamlit as st

# Titre principal de la page
st.title("🍏 Objectif Zéro Gaspi - Collège Jean Giono")
st.subheader("Suivi des déchets pour 700 demi-pensionnaires (ODD 12)")

st.write("""
**À vous de jouer !** Tapez le poids mesuré dans la case, puis choisissez l'unité (g ou kg) pour chaque catégorie.
""")

st.markdown("### 📊 Nos Pesées Hebdomadaires")

# --- CATEGORIE 1 : Déchets Alimentaires ---
st.markdown('<div style="background-color: #FFF2CC; padding: 15px; border-radius: 10px; border-left: 5px solid #F1C232; margin-bottom: 20px;">', unsafe_allow_html=True)
st.subheader("🗑️ Déchets Alimentaires")
# Changez le "42" ci-dessous par votre vrai chiffre par défaut
poids_alim = st.text_input("Entrez la valeur :", value="42", key="alim")  # <--- ICI
unite_alim = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_alim")
st.write(f"**Poids enregistré :** {poids_alim} {unite_alim}")
st.caption("Restes d'assiettes — Objectif : Réduire le gaspillage direct !")
st.markdown('</div>', unsafe_allow_html=True)

# --- CATEGORIE 2 : Poubelle à Pain ---
st.markdown('<div style="background-color: #FFE5CC; padding: 15px; border-radius: 10px; border-left: 5px solid #E69138; margin-bottom: 20px;">', unsafe_allow_html=True)
st.subheader("🥖 Poubelle à Pain")
# Changez le "8" ci-dessous par votre vrai chiffre par défaut
poids_pain = st.text_input("Entrez la valeur :", value="8", key="pain")  # <--- ICI
unite_pain = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_pain")
st.write(f"**Poids enregistré :** {poids_pain} {unite_pain}")

try:
    valeur_pain = float(poids_pain.replace(",", "."))
    if unite_pain == "g":
        valeur_pain = valeur_pain / 1000
    nb_baguettes = int(valeur_pain / 0.25)
    st.write(f"💡 *Cela représente environ **{nb_baguettes} baguettes** perdues !*")
except:
    st.write("💡 *Entrez un chiffre valide pour voir l'équivalent en baguettes.*")
st.markdown('</div>', unsafe_allow_html=True)

# --- CATEGORIE 3 : Fruits entamés ---
st.markdown('<div style="background-color: #E2EFDA; padding: 15px; border-radius: 10px; border-left: 5px solid #A9D08E; margin-bottom: 20px;">', unsafe_allow_html=True)
st.subheader("🍎 Fruits entamés")
# Changez le "5" ci-dessous par votre vrai chiffre par défaut
poids_fruits = st.text_input("Entrez la valeur :", value="5", key="fruits")  # <--- ICI
unite_fruits = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_fruits")
st.write(f"**Poids enregistré :** {poids_fruits} {unite_fruits}")
st.markdown('</div>', unsafe_allow_html=True)

# --- CATEGORIE 4 : Serviettes en papier ---
st.markdown('<div style="background-color: #DDEBF7; padding: 15px; border-radius: 10px; border-left: 5px solid #9BC2E6; margin-bottom: 20px;">', unsafe_allow_html=True)
st.subheader("🧻 Serviettes en papier")
# Changez le "3" ci-dessous par votre vrai chiffre par défaut
poids_serviettes = st.text_input("Entrez la valeur :", value="3", key="serviettes")  # <--- ICI
unite_serviettes = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_serviettes")
st.write(f"**Poids enregistré :** {poids_serviettes} {unite_serviettes}")
st.markdown('</div>', unsafe_allow_html=True)

# --- CATEGORIE 5 : Emballages ---
st.markdown('<div style="background-color: #E1D5E7; padding: 15px; border-radius: 10px; border-left: 5px solid #B4A7D6; margin-bottom: 20px;">', unsafe_allow_html=True)
st.subheader("📦 Emballages")
# Changez le "6" ci-dessous par votre vrai chiffre par défaut
poids_emballages = st.text_input("Entrez la valeur :", value="6", key="emballages")  # <--- ICI
unite_emballages = st.selectbox("Choisir l'unité :", ["kg", "g"], key="u_emballages")
st.write(f"**Poids enregistré :** {poids_emballages} {unite_emballages}")
st.markdown('</div>', unsafe_allow_html=True)
