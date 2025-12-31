# -*- coding: utf-8 -*-
"""
Tableau de bord commercial pour analyse des données Excel
Structure avec filtres et visualisations
"""
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
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

# En-tête avec logo
col_header1, col_header2, col_header3 = st.columns([1, 2, 1])
with col_header2:
    st.title("📊 Tableau de Bord Commercial")
st.markdown("---")

# Fonction pour charger les données
@st.cache_data
def load_data(file_path='1.xlsx'):
    """Charge les données Excel"""
    try:
        df = pd.read_excel(file_path)
        
        # Informations sur le fichier
        if os.path.exists(file_path):
            stat = os.stat(file_path)
            file_info = {
                'date_creation': datetime.fromtimestamp(stat.st_ctime),
                'date_modification': datetime.fromtimestamp(stat.st_mtime),
                'taille': stat.st_size / 1024
            }
        else:
            file_info = {
                'date_creation': datetime.now(),
                'date_modification': datetime.now(),
                'taille': 0
            }
        
        return df, file_info
    except Exception as e:
        st.error(f"Erreur lors du chargement du fichier : {e}")
        return pd.DataFrame(), {}

# Upload de fichier Excel (optionnel)
st.sidebar.markdown("---")
st.sidebar.markdown("### 📤 Mettre à jour les données")
uploaded_file = st.sidebar.file_uploader(
    "Télécharger un nouveau fichier Excel",
    type=['xlsx', 'xls'],
    help="Téléchargez un fichier Excel pour mettre à jour les données"
)

if uploaded_file is not None:
    # Sauvegarder le fichier téléchargé
    with open('1.xlsx', 'wb') as f:
        f.write(uploaded_file.getbuffer())
    st.sidebar.success("✅ Fichier téléchargé avec succès !")
    # Vider le cache pour recharger les nouvelles données
    st.cache_data.clear()
    st.rerun()  # Redémarre l'application automatiquement

# Bouton de rafraîchissement manuel
st.sidebar.markdown("---")
if st.sidebar.button("🔄 Actualiser les données", use_container_width=True):
    st.cache_data.clear()
    st.rerun()

# Charger les données
df, file_info = load_data()

# Sidebar - Filtres
st.sidebar.header("🔍 Filtres")

# Filtre par Type
types = ['Tous'] + sorted(df['Type'].dropna().unique().tolist())
type_selected = st.sidebar.selectbox("Type", types)

# Filtre par Famille
familles = ['Toutes'] + sorted(df['Famille'].dropna().unique().tolist())
famille_selected = st.sidebar.selectbox("Famille", familles)

# Filtre par Fournisseur
fournisseurs = ['Tous'] + sorted(df['Fournisseur principal'].dropna().unique().tolist())
fournisseur_selected = st.sidebar.selectbox("Fournisseur principal", fournisseurs)

# Filtre par Stock
stock_filter = st.sidebar.radio(
    "État du stock",
    ['Tous', 'En stock', 'Rupture de stock', 'Stock faible (< 10)']
)

# Filtre par Marge
marge_min = st.sidebar.number_input("Marge minimale (%)", min_value=0, max_value=100, value=0)
marge_max = st.sidebar.number_input("Marge maximale (%)", min_value=0, max_value=100, value=100)

# Filtre par Prix de vente
prix_min = st.sidebar.number_input("Prix de vente min", min_value=0.0, value=0.0)
prix_max = st.sidebar.number_input("Prix de vente max", min_value=0.0, value=float(df['Prix de vente'].max()))

# Application des filtres
df_filtered = df.copy()

if type_selected != 'Tous':
    df_filtered = df_filtered[df_filtered['Type'] == type_selected]

if famille_selected != 'Toutes':
    df_filtered = df_filtered[df_filtered['Famille'] == famille_selected]

if fournisseur_selected != 'Tous':
    df_filtered = df_filtered[df_filtered['Fournisseur principal'] == fournisseur_selected]

if stock_filter == 'En stock':
    df_filtered = df_filtered[df_filtered['Stock réel'] > 0]
elif stock_filter == 'Rupture de stock':
    df_filtered = df_filtered[(df_filtered['Stock réel'] == 0) | (df_filtered['Stock réel'].isna())]
elif stock_filter == 'Stock faible (< 10)':
    df_filtered = df_filtered[(df_filtered['Stock réel'] > 0) & (df_filtered['Stock réel'] < 10)]

# Calcul de la marge
df_filtered['Marge'] = df_filtered['Prix de vente'] - df_filtered['Prix d\'achat']
df_filtered['Marge %'] = ((df_filtered['Prix de vente'] - df_filtered['Prix d\'achat']) / 
                          df_filtered['Prix de vente'] * 100).round(2)
df_filtered['Marge %'] = df_filtered['Marge %'].fillna(0)

# Filtre par marge
df_filtered = df_filtered[
    (df_filtered['Marge %'] >= marge_min) & 
    (df_filtered['Marge %'] <= marge_max)
]

# Filtre par prix
df_filtered = df_filtered[
    (df_filtered['Prix de vente'] >= prix_min) & 
    (df_filtered['Prix de vente'] <= prix_max)
]

# Métriques principales
date_fichier = file_info['date_modification'].strftime("%d/%m/%Y")
st.markdown(f"### 📈 KPIs Articles ({date_fichier})")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total articles", len(df_filtered))
    
with col2:
    total_stock = df_filtered['Stock réel'].sum()
    st.metric("Stock total", f"{total_stock:,.0f}")
    
with col3:
    valeur_stock = (df_filtered['Stock réel'] * df_filtered['Prix d\'achat']).sum()
    st.metric("Valeur du stock", f"{valeur_stock:,.0f} DH")
    
with col4:
    marge_moyenne = df_filtered['Marge %'].mean()
    st.metric("Marge moyenne", f"{marge_moyenne:.1f}%")
    
with col5:
    prix_moyen = df_filtered['Prix de vente'].mean()
    st.metric("Prix moyen", f"{prix_moyen:.2f} DH")

st.markdown("---")

# Configuration des graphiques Plotly (pas de barre d'outils, plein écran sur double-clic, pas d'interaction clavier)
plotly_config = {
    'displayModeBar': False,  # Cache la barre d'outils
    'doubleClick': 'autosize',  # Double-clic pour plein écran
    'displaylogo': False,    # Cache le logo Plotly
    'scrollZoom': False,     # Désactive le zoom avec la molette
    'showAxisDragHandles': False,  # Cache les poignées de redimensionnement
    'editable': False,       # Désactive l'édition
    'staticPlot': False,     # Garde l'interactivité pour le hover et double-clic
}

# Graphiques
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Répartition par Famille")
    famille_counts = df_filtered['Famille'].value_counts().head(10)
    # Convertir en DataFrame pour plus de compatibilité
    df_famille = pd.DataFrame({
        'Famille': famille_counts.index,
        'Nombre': famille_counts.values
    })
    fig_famille = px.pie(
        df_famille,
        values='Nombre',
        names='Famille',
        title="Top 10 Familles"
    )
    # Désactiver les interactions au clavier
    fig_famille.update_layout(dragmode=False)
    st.plotly_chart(fig_famille, use_container_width=True, config=plotly_config)

with col2:
    st.markdown("### 📊 Répartition par Fournisseur")
    fournisseur_counts = df_filtered['Fournisseur principal'].value_counts().head(10)
    # Convertir en DataFrame pour Plotly Express
    df_fournisseur = pd.DataFrame({
        'Fournisseur': fournisseur_counts.index,
        'Nombre': fournisseur_counts.values
    })
    fig_fournisseur = px.bar(
        df_fournisseur,
        x='Fournisseur',
        y='Nombre',
        title="Top 10 Fournisseurs",
        labels={'Fournisseur': 'Fournisseur', 'Nombre': 'Nombre d\'articles'}
    )
    fig_fournisseur.update_xaxes(tickangle=45)
    # Désactiver les interactions au clavier
    fig_fournisseur.update_layout(dragmode=False)
    st.plotly_chart(fig_fournisseur, use_container_width=True, config=plotly_config)

# Graphique de marge
st.markdown("### 💰 Analyse des Marges")
col1, col2 = st.columns(2)

with col1:
    fig_marge = px.histogram(
        df_filtered,
        x='Marge %',
        nbins=50,
        title="Distribution des marges (%)",
        labels={'Marge %': 'Marge (%)', 'count': 'Nombre d\'articles'}
    )
    # Désactiver les interactions au clavier
    fig_marge.update_layout(dragmode=False)
    st.plotly_chart(fig_marge, use_container_width=True, config=plotly_config)

with col2:
    # Filtrer les valeurs NaN pour éviter les erreurs
    df_scatter = df_filtered[
        df_filtered['Prix d\'achat'].notna() & 
        df_filtered['Prix de vente'].notna()
    ].copy()
    
    if len(df_scatter) > 0:
        # Remplacer les valeurs NaN par 0 pour size et color
        df_scatter['Stock réel'] = df_scatter['Stock réel'].fillna(0)
        df_scatter['Marge %'] = df_scatter['Marge %'].fillna(0)
        
        # S'assurer que les valeurs sont numériques
        df_scatter['Stock réel'] = pd.to_numeric(df_scatter['Stock réel'], errors='coerce').fillna(0)
        df_scatter['Marge %'] = pd.to_numeric(df_scatter['Marge %'], errors='coerce').fillna(0)
        
        # Utiliser size_max pour limiter la taille des points
        max_stock = df_scatter['Stock réel'].max() if df_scatter['Stock réel'].max() > 0 else 1
        
        fig_prix = px.scatter(
            df_scatter,
            x='Prix d\'achat',
            y='Prix de vente',
            size='Stock réel',
            size_max=50,
            color='Marge %',
            hover_data=['Désignation', 'Famille'],
            title="Relation Prix d'achat vs Prix de vente",
            labels={'Prix d\'achat': 'Prix d\'achat (DH)', 'Prix de vente': 'Prix de vente (DH)'}
        )
        # Désactiver les interactions au clavier
        fig_prix.update_layout(dragmode=False)
        st.plotly_chart(fig_prix, use_container_width=True, config=plotly_config)
    else:
        st.info("Pas assez de données pour afficher le graphique")

# Analyse du stock
st.markdown("### 📦 Analyse du Stock")
col1, col2 = st.columns(2)

with col1:
    # Articles en rupture
    rupture = df_filtered[(df_filtered['Stock réel'] == 0) | (df_filtered['Stock réel'].isna())]
    st.markdown("#### Articles en rupture de stock")
    if len(rupture) > 0:
        st.dataframe(
            rupture[['Référence article', 'Désignation', 'Famille', 'Prix de vente']].head(20),
            use_container_width=True
        )
    else:
        st.info("Aucun article en rupture de stock")

with col2:
    # Articles à faible stock
    stock_faible = df_filtered[(df_filtered['Stock réel'] > 0) & (df_filtered['Stock réel'] < 10)]
    st.markdown("#### Articles à faible stock (< 10)")
    if len(stock_faible) > 0:
        st.dataframe(
            stock_faible[['Référence article', 'Désignation', 'Famille', 'Stock réel', 'Prix de vente']].head(20),
            use_container_width=True
        )
    else:
        st.info("Aucun article à faible stock")

# Tableau de données
st.markdown("### 📋 Données détaillées")
st.dataframe(
    df_filtered[[
        'Type', 'Référence article', 'Désignation', 'Famille',
        'Prix d\'achat', 'Prix de vente', 'Marge', 'Marge %',
        'Fournisseur principal', 'Stock réel'
    ]],
    use_container_width=True,
    height=400
)

# Bouton d'export
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    csv = df_filtered.to_csv(index=False).encode('utf-8-sig')
    st.download_button(
        label="📥 Télécharger les données filtrées (CSV)",
        data=csv,
        file_name=f"donnees_filtrees_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )

