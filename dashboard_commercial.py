# -*- coding: utf-8 -*-
"""
Tableau de bord commercial - Page d'accueil
Navigation vers ARTICLES et VENTES
"""
import streamlit as st
import os

# Configuration de la page
st.set_page_config(
    page_title="Tableau de Bord Commercial - BBM AGRI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Charger le logo
logo_path = "Logo bbm agri.jpg"
if os.path.exists(logo_path):
    st.sidebar.image(logo_path, use_container_width=True)
else:
    st.sidebar.markdown("### BBM AGRI")
    st.sidebar.markdown("Tableau de Bord Commercial")

# En-tête - titre aligné à gauche
st.title("📊 Tableau de Bord Commercial")
st.markdown("---")

# Message d'accueil
st.markdown("""
<div style='background-color: #f0f2f6; padding: 30px; border-radius: 10px; margin: 20px 0;'>
    <h2 style='color: #1f77b4; margin-top: 0;'>Bienvenue sur le Tableau de Bord Commercial</h2>
    <p style='font-size: 1.1em;'>Utilisez le menu latéral pour accéder aux différentes sections :</p>
    <ul style='font-size: 1.1em;'>
        <li><strong>📦 ARTICLES</strong> - Analyse des articles et stocks</li>
        <li><strong>💰 VENTES</strong> - Analyse des ventes</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.info("💡 **Astuce :** Cliquez sur 'ARTICLES' ou 'VENTES' dans le menu latéral pour accéder aux analyses détaillées.")
