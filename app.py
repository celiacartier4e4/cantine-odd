import streamlit as st
import pandas as pd

# ==============================================================================
# CONFIGURATION DE LA PAGE
# ==============================================================================
st.set_page_config(
    page_title="Giono - CDSG",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Fonction de conversion technique simplifiée
def to_kg(poids, unite):
    return poids if unite == "kg" else poids / 1000.0

# ==============================================================================
# EN-TÊTE
# ==============================================================================
st.title("🍏 Collège Jean Giono d'Orange")
st.subheader("Projet Éco-Citoyen - CDSG Giono")
st.caption("Avenue Charles Dardun, 84100 Orange | Référent : M. Thierry Armant")

st.divider()

# ==============================================================================
# STRUCTURE EN COLONNES POUR LES 5 CATEGORIES ET LE CONTEXTE
# ==============================================================================
col1, col2 = st.columns(2)

with col1:
    # 1. Pain
    with st.container(border=True):
        st.markdown("### 🥖 Reliquats de Pain")
        p_pain = st.number_input("Masse Pain :", min_value=0.0, value=4.0, step=0.5, key="p_pain")
        u_pain = st.selectbox("Unité Pain :", ["kg", "g"], key="u_p")
        v_pain = to_kg(p_pain, u_pain)
        st.caption(f"Soit environ {int(v_pain / 0.25)} baguettes perdues.")

    # 2. Serviettes
    with st.container(border=True):
        st.markdown("### 🧻 Serviettes en Papier")
        p_serv = st.number_input("Masse Serviettes (kg) :", min_value=0.0, value=1.5, step=0.1, key="p_serv")
        st.caption(f"Soit environ {int(p_serv / 0.003)} unités jetées.")

    # 3. Emballages
    with st.container(border=True):
        st.markdown("### 📦 Emballages Non Recyclés")
        p_emb = st.number_input("Masse Emballages (kg) :", min_value=0.0, value=3.0, step=0.5, key="p_emb")
        st.caption(f"Soit environ {int(p_emb / 0.02)} unités d'emballages.")

with col2:
    # 4. Biodéchets
    with st.container(border=True):
        st.markdown("### 🗑️ Biodéchets - Plats Cuisinés")
        p_bio = st.number_input("Masse Biodéchets (kg) :", min_value=0.0, value=25.0, step=1.0, key="p_bio")
        st.caption(f"Soit environ {int(p_bio / 0.15)} repas complets jetés.")

    # 5. Fruits
    with st.container(border=True):
        st.markdown("### 🍎 Pertes sur les Fruits")
        p_frt = st.number_input("Masse Fruits (kg) :", min_value=0.0, value=2.0, step=0.2, key="p_frt")
        st.caption(f"Soit environ {int(p_frt / 0.12)} fruits gaspillés.")

    # 6. Cadre Institutionnel
    with st.container(border=True):
        st.markdown("### 🛡️ CONTEXTE CDSG")
        st.info("Collège Jean Giono — Impact environnemental de 700 demi-pensionnaires. Modélisation liée à l'ODD 12 de l'ONU.")

# ==============================================================================
# PANNEAU DE SYNTHÈSE DU BAS
# ==============================================================================
st.divider()
st.markdown("## 📊 Bilans et Indicateurs Centraux")

b_col1, b_col2 = st.columns([1.2, 1])

with b_col1:
    st.markdown("#### 📈 Répartition Globale des Déchets Capturés")
    df_chart = pd.DataFrame([[p_bio, v_pain, p_frt, p_serv, p_emb]], 
                            columns=["Biodéchets", "Pain", "Fruits", "Serviettes", "Emballages"])
    st.bar_chart(df_chart, horizontal=True, height=130)

with b_col2:
    # Calculs de synthèse
    total_masse = v_pain + p_serv + p_emb + p_bio + p_frt
    total_co2 = total_masse * 2.0
    total_km = total_co2 / 0.12

    # Métriques standards Streamlit (propres et incoupables)
    st.metric("Masse Globale Capturée", f"{total_masse:.2f} kg")
    st.metric("Bilan Carbone Équivalent", f"{total_co2:.2f} kg CO₂e")
    st.metric("Équivalence Distance Voiture", f"{total_km:.0f} km")

    # Jauge de progression
    st.markdown("**🎯 Jauge d'Efficience Collective**")
    score = max(0.0, min(1.0, (100.0 - total_masse) / 100.0))
    st.progress(score)
