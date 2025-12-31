# -*- coding: utf-8 -*-
"""
Page VENTES - Analyse des ventes
"""
import pandas as pd
import streamlit as st
from datetime import datetime
import os

# Configuration de la page
st.set_page_config(
    page_title="Ventes - Tableau de Bord Commercial",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Fonction pour charger les données
@st.cache_data
def load_data(file_path='ventes.xlsx'):
    """Charge les données Excel"""
    try:
        if not os.path.exists(file_path):
            return pd.DataFrame(), {}
        df = pd.read_excel(file_path)
        
        # Informations sur le fichier
        stat = os.stat(file_path)
        file_info = {
            'date_creation': datetime.fromtimestamp(stat.st_ctime),
            'date_modification': datetime.fromtimestamp(stat.st_mtime),
            'taille': stat.st_size / 1024
        }
        
        return df, file_info
    except Exception as e:
        st.error(f"Erreur lors du chargement du fichier : {e}")
        return pd.DataFrame(), {}

# En-tête
st.title("💰 VENTES")
st.markdown("---")

# Upload de fichier Excel pour VENTES
st.sidebar.markdown("---")
st.sidebar.markdown("### 📤 Mettre à jour les données VENTES")
uploaded_file_ventes = st.sidebar.file_uploader(
    "Télécharger un nouveau fichier Excel (Ventes)",
    type=['xlsx', 'xls'],
    help="Téléchargez un fichier Excel pour mettre à jour les données ventes",
    key="upload_ventes"
)

if uploaded_file_ventes is not None:
    with open('ventes.xlsx', 'wb') as f:
        f.write(uploaded_file_ventes.getbuffer())
    st.sidebar.success("✅ Fichier Ventes téléchargé avec succès !")
    st.cache_data.clear()
    st.rerun()

# Bouton de rafraîchissement manuel pour VENTES
if st.sidebar.button("🔄 Actualiser Ventes", use_container_width=True, type="primary", key="refresh_ventes"):
    st.cache_data.clear()
    st.rerun()

# Charger les données VENTES
df_ventes, file_info_ventes = load_data('ventes.xlsx')

if df_ventes.empty:
    st.info("📊 **Section VENTES**")
    st.markdown("""
    <div style='background-color: #e8f4f8; padding: 20px; border-radius: 10px; border-left: 5px solid #1f77b4; margin: 20px 0;'>
        <h3 style='color: #1f77b4; margin-top: 0;'>Prêt pour les données de ventes</h3>
        <p>Pour commencer, téléchargez un fichier Excel contenant les données de ventes dans la barre latérale.</p>
        <p><strong>Le fichier sera sauvegardé sous le nom :</strong> <code>ventes.xlsx</code></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📋 Structure attendue du fichier Ventes")
    st.markdown("""
    Le fichier Excel de ventes devrait contenir des colonnes telles que :
    - Date de vente
    - Référence article / Code produit
    - Quantité vendue
    - Prix unitaire
    - Montant total
    - Client
    - etc.
    
    *La structure exacte sera déterminée lors de l'analyse du premier fichier téléchargé.*
    """)
else:
    # Afficher les informations sur le fichier
    date_fichier_ventes = file_info_ventes['date_modification'].strftime("%d/%m/%Y") if file_info_ventes else datetime.now().strftime("%d/%m/%Y")
    st.markdown(f"""
    <div style='background-color: #f0f2f6; padding: 15px; border-radius: 10px; border-left: 5px solid #28a745; margin-bottom: 20px;'>
        <h2 style='color: #28a745; margin: 0; font-weight: bold;'>💰 KPIs Ventes ({date_fichier_ventes})</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Afficher les colonnes disponibles
    st.markdown("### 📊 Colonnes disponibles dans le fichier Ventes")
    st.write(f"**Nombre de lignes :** {len(df_ventes)}")
    st.write(f"**Nombre de colonnes :** {len(df_ventes.columns)}")
    st.write("**Colonnes :**", ", ".join(df_ventes.columns.tolist()))
    
    # Aperçu des données
    st.markdown("### 📋 Aperçu des données")
    st.dataframe(df_ventes.head(20), use_container_width=True, height=400)
    
    st.info("ℹ️ Les filtres et graphiques pour les ventes seront ajoutés une fois la structure du fichier analysée.")

