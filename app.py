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

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Déchets Alimentaires", value="42 kg", delta="À réduire")
with col2:
    st.metric(label="Poubelle à Pain", value="8 kg", delta="Objectif 0g !")
with col3:
    st.metric(label="Fruits entamés", value="5 kg")

col4, col5 = st.columns(2)
with col4:
    st.metric(label="Serviettes en papier", value="3 kg")
with col5:
    st.metric(label="Emballages", value="6 kg")

# Un petit message d'explication
st.info("💡 Le saviez-vous ? 8 kg de pain jetés représentent environ 32 baguettes perdues !")
