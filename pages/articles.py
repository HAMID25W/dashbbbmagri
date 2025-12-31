# -*- coding: utf-8 -*-
"""
Page ARTICLES - Analyse des articles et stocks
"""
import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime
import os

# Configuration de la page
st.set_page_config(
    page_title="Articles - Tableau de Bord Commercial",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Fonction pour charger les données
@st.cache_data
def load_data(file_path='1.xlsx'):
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

# Configuration des graphiques Plotly
plotly_config = {
    'displayModeBar': True,
    'displaylogo': False,
    'scrollZoom': False,
    'showAxisDragHandles': False,
    'editable': False,
    'staticPlot': False,
    'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d', 'autoScale2d', 'resetScale2d', 'zoomIn2d', 'zoomOut2d'],
    'doubleClick': 'reset',
}

# En-tête avec bouton Source Articles
col_title, col_button = st.columns([3, 1])
with col_title:
    st.title("📦 ARTICLES")
with col_button:
    st.markdown("<br>", unsafe_allow_html=True)  # Alignement vertical
    # Style personnalisé : masquer tous les éléments sauf le bouton "Source_Articles"
    st.markdown("""
    <style>
    /* Masquer le label "Source_Articles" */
    div[data-testid="stFileUploader"] > label {
        display: none !important;
    }
    /* Masquer la zone "Drag and drop file here" */
    div[data-testid="stFileUploader"] > div[data-baseweb="file-uploader"] {
        display: none !important;
    }
    /* Masquer le texte "Limit 200MB per file • XLSX, XLS, CSV" */
    div[data-testid="stFileUploader"] p,
    div[data-testid="stFileUploader"] small,
    div[data-testid="stFileUploader"] span[class*="caption"] {
        display: none !important;
    }
    /* Remplacer le texte "Browse files" par "Source_Articles" */
    div[data-testid="stFileUploader"] button {
        position: relative;
    }
    /* Masquer le texte original du bouton */
    div[data-testid="stFileUploader"] button > * {
        visibility: hidden;
    }
    /* Ajouter "Source_Articles" comme contenu du bouton */
    div[data-testid="stFileUploader"] button::before {
        content: "Source_Articles";
        visibility: visible;
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        white-space: nowrap;
    }
    </style>
    <script>
    // Script pour remplacer le texte du bouton
    window.addEventListener('load', function() {
        const fileUploader = document.querySelector('div[data-testid="stFileUploader"]');
        if (fileUploader) {
            const button = fileUploader.querySelector('button');
            if (button) {
                // Trouver et remplacer le texte du bouton
                const spans = button.querySelectorAll('span');
                spans.forEach(span => {
                    if (span.textContent.trim() === 'Browse files' || span.textContent.includes('Browse')) {
                        span.textContent = 'Source_Articles';
                    }
                });
                // Si le texte est directement dans le bouton
                if (button.textContent.includes('Browse files')) {
                    button.textContent = button.textContent.replace('Browse files', 'Source_Articles');
                }
            }
        }
    });
    </script>
    """, unsafe_allow_html=True)
    uploaded_file_articles = st.file_uploader(
        "Source_Articles",
        type=['xlsx', 'xls', 'csv'],
        help="Cliquez pour télécharger le fichier Excel ou CSV",
        key="upload_articles",
        label_visibility="collapsed"
    )

if uploaded_file_articles is not None:
    # Déterminer l'extension du fichier
    file_extension = uploaded_file_articles.name.split('.')[-1].lower()
    
    if file_extension in ['xlsx', 'xls']:
        # Fichier Excel
        with open('1.xlsx', 'wb') as f:
            f.write(uploaded_file_articles.getbuffer())
        st.success("✅ Fichier Excel Articles téléchargé avec succès !")
    elif file_extension == 'csv':
        # Fichier CSV - convertir en Excel
        df_csv = pd.read_csv(uploaded_file_articles)
        df_csv.to_excel('1.xlsx', index=False)
        st.success("✅ Fichier CSV Articles converti et téléchargé avec succès !")
    
    st.cache_data.clear()
    st.rerun()

st.markdown("---")

# Bouton de rafraîchissement manuel pour ARTICLES
if st.sidebar.button("🔄 Actualiser Articles", use_container_width=True, type="primary", key="refresh_articles"):
    st.cache_data.clear()
    st.rerun()

# Charger les données ARTICLES
df, file_info = load_data('1.xlsx')

if df.empty:
    st.warning("⚠️ Aucune donnée articles disponible. Veuillez télécharger un fichier Excel.")
else:
    # Sidebar - Filtres ARTICLES
    st.sidebar.markdown("---")
    st.sidebar.header("🔍 Filtres ARTICLES")
    
    # Filtre par Type - seulement si plusieurs types différents
    types_unique = df['Type'].dropna().unique().tolist() if 'Type' in df.columns else []
    if len(types_unique) > 1:
        types = ['Tous'] + sorted(types_unique)
        type_selected = st.sidebar.selectbox("Type", types, key="type_articles")
    else:
        type_selected = 'Tous'
    
    # Filtre par Famille
    if 'Famille' in df.columns:
        familles = ['Toutes'] + sorted(df['Famille'].dropna().unique().tolist())
        famille_selected = st.sidebar.selectbox("Famille", familles, key="famille_articles")
        
        # Bouton pour télécharger les données de la famille sélectionnée
        if famille_selected != 'Toutes':
            famille_filtered = df[df['Famille'] == famille_selected]
            if len(famille_filtered) > 0:
                csv_famille = famille_filtered.to_csv(index=False).encode('utf-8-sig')
                st.sidebar.download_button(
                    label=f"📥 Télécharger famille: {famille_selected}",
                    data=csv_famille,
                    file_name=f"articles_famille_{famille_selected}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv",
                    key="download_famille"
                )
    else:
        famille_selected = 'Toutes'
    
    # Filtre par Fournisseur
    if 'Fournisseur principal' in df.columns:
        fournisseurs = ['Tous'] + sorted(df['Fournisseur principal'].dropna().unique().tolist())
        fournisseur_selected = st.sidebar.selectbox("Fournisseur principal", fournisseurs, key="fournisseur_articles")
    else:
        fournisseur_selected = 'Tous'
    
    # Filtre par Stock
    stock_filter = st.sidebar.radio(
        "État du stock",
        ['Tous', 'En stock', 'Rupture de stock', 'Stock faible (< 10)'],
        key="stock_articles"
    )
    
    # Filtre par Marge
    marge_min = st.sidebar.number_input("Marge minimale (%)", min_value=0, max_value=100, value=0, key="marge_min_articles")
    marge_max = st.sidebar.number_input("Marge maximale (%)", min_value=0, max_value=100, value=100, key="marge_max_articles")
    
    # Filtre par Prix de vente
    prix_max_default = float(df['Prix de vente'].max()) if 'Prix de vente' in df.columns and not df['Prix de vente'].isna().all() else 10000.0
    prix_min = st.sidebar.number_input("Prix de vente min", min_value=0.0, value=0.0, key="prix_min_articles")
    prix_max = st.sidebar.number_input("Prix de vente max", min_value=0.0, value=prix_max_default, key="prix_max_articles")
    
    # Application des filtres
    df_filtered = df.copy()
    
    if type_selected != 'Tous' and 'Type' in df.columns:
        df_filtered = df_filtered[df_filtered['Type'] == type_selected]
    
    if famille_selected != 'Toutes' and 'Famille' in df.columns:
        df_filtered = df_filtered[df_filtered['Famille'] == famille_selected]
    
    if fournisseur_selected != 'Tous' and 'Fournisseur principal' in df.columns:
        df_filtered = df_filtered[df_filtered['Fournisseur principal'] == fournisseur_selected]
    
    if 'Stock réel' in df.columns:
        if stock_filter == 'En stock':
            df_filtered = df_filtered[df_filtered['Stock réel'] > 0]
        elif stock_filter == 'Rupture de stock':
            df_filtered = df_filtered[(df_filtered['Stock réel'] == 0) | (df_filtered['Stock réel'].isna())]
        elif stock_filter == 'Stock faible (< 10)':
            df_filtered = df_filtered[(df_filtered['Stock réel'] > 0) & (df_filtered['Stock réel'] < 10)]
    
    # Calcul de la marge
    if 'Prix de vente' in df_filtered.columns and 'Prix d\'achat' in df_filtered.columns:
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
    if 'Prix de vente' in df_filtered.columns:
        df_filtered = df_filtered[
            (df_filtered['Prix de vente'] >= prix_min) & 
            (df_filtered['Prix de vente'] <= prix_max)
        ]
    
    # Métriques principales
    date_fichier = file_info['date_modification'].strftime("%d/%m/%Y") if file_info else datetime.now().strftime("%d/%m/%Y")
    st.markdown(f"""
    <div style='background-color: #f0f2f6; padding: 15px; border-radius: 10px; border-left: 5px solid #1f77b4; margin-bottom: 20px;'>
        <h2 style='color: #1f77b4; margin: 0; font-weight: bold;'>📈 KPIs Articles ({date_fichier})</h2>
    </div>
    """, unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Total articles", len(df_filtered))
    
    with col2:
        if 'Stock réel' in df_filtered.columns:
            total_stock = df_filtered['Stock réel'].sum()
            st.metric("Stock total", f"{total_stock:,.0f}")
        else:
            st.metric("Stock total", "N/A")
    
    with col3:
        if 'Stock réel' in df_filtered.columns and 'Prix d\'achat' in df_filtered.columns:
            valeur_stock = (df_filtered['Stock réel'] * df_filtered['Prix d\'achat']).sum()
            st.metric("Valeur du stock", f"{valeur_stock:,.0f} DH")
        else:
            st.metric("Valeur du stock", "N/A")
    
    with col4:
        if 'Marge %' in df_filtered.columns:
            marge_moyenne = df_filtered['Marge %'].mean()
            st.metric("Marge moyenne", f"{marge_moyenne:.1f}%")
        else:
            st.metric("Marge moyenne", "N/A")
    
    with col5:
        if 'Prix de vente' in df_filtered.columns:
            prix_moyen = df_filtered['Prix de vente'].mean()
            st.metric("Prix moyen", f"{prix_moyen:.2f} DH")
        else:
            st.metric("Prix moyen", "N/A")
    
    st.markdown("---")
    
    # Graphiques
    col1, col2 = st.columns(2)
    
    with col1:
        if 'Famille' in df_filtered.columns:
            st.markdown("### 📊 Répartition par Famille")
            famille_counts = df_filtered['Famille'].value_counts().head(10)
            df_famille = pd.DataFrame({
                'Famille': famille_counts.index,
                'Nombre': famille_counts.values
            })
            fig_famille = px.pie(df_famille, values='Nombre', names='Famille', title="Top 10 Familles")
            fig_famille.update_layout(dragmode=False)
            st.plotly_chart(fig_famille, use_container_width=True, config=plotly_config)
    
    with col2:
        if 'Fournisseur principal' in df_filtered.columns:
            st.markdown("### 📊 Répartition par Fournisseur")
            fournisseur_counts = df_filtered['Fournisseur principal'].value_counts().head(10)
            df_fournisseur = pd.DataFrame({
                'Fournisseur': fournisseur_counts.index,
                'Nombre': fournisseur_counts.values
            })
            fig_fournisseur = px.bar(df_fournisseur, x='Fournisseur', y='Nombre', title="Top 10 Fournisseurs",
                                    labels={'Fournisseur': 'Fournisseur', 'Nombre': 'Nombre d\'articles'})
            fig_fournisseur.update_xaxes(tickangle=45)
            fig_fournisseur.update_layout(dragmode=False)
            st.plotly_chart(fig_fournisseur, use_container_width=True, config=plotly_config)
    
    # Graphique de marge
    if 'Marge %' in df_filtered.columns:
        st.markdown("### 💰 Analyse des Marges")
        col1, col2 = st.columns(2)
        
        with col1:
            fig_marge = px.histogram(df_filtered, x='Marge %', nbins=50, title="Distribution des marges (%)",
                                    labels={'Marge %': 'Marge (%)', 'count': 'Nombre d\'articles'})
            fig_marge.update_layout(dragmode=False)
            st.plotly_chart(fig_marge, use_container_width=True, config=plotly_config)
        
        with col2:
            if 'Prix d\'achat' in df_filtered.columns and 'Prix de vente' in df_filtered.columns:
                df_scatter = df_filtered[df_filtered['Prix d\'achat'].notna() & df_filtered['Prix de vente'].notna()].copy()
                if len(df_scatter) > 0:
                    df_scatter['Stock réel'] = df_scatter['Stock réel'].fillna(0) if 'Stock réel' in df_scatter.columns else 0
                    df_scatter['Marge %'] = df_scatter['Marge %'].fillna(0)
                    fig_prix = px.scatter(df_scatter, x='Prix d\'achat', y='Prix de vente', size='Stock réel' if 'Stock réel' in df_scatter.columns else None,
                                        size_max=50, color='Marge %', hover_data=['Désignation', 'Famille'] if 'Désignation' in df_scatter.columns else [],
                                        title="Relation Prix d'achat vs Prix de vente",
                                        labels={'Prix d\'achat': 'Prix d\'achat (DH)', 'Prix de vente': 'Prix de vente (DH)'})
                    fig_prix.update_layout(dragmode=False)
                    st.plotly_chart(fig_prix, use_container_width=True, config=plotly_config)
                else:
                    st.info("Pas assez de données pour afficher le graphique")
    
    # Analyse du stock
    if 'Stock réel' in df_filtered.columns:
        st.markdown("### 📦 Analyse du Stock")
        col1, col2 = st.columns(2)
        
        with col1:
            rupture = df_filtered[(df_filtered['Stock réel'] == 0) | (df_filtered['Stock réel'].isna())]
            st.markdown("#### Articles en rupture de stock")
            if len(rupture) > 0:
                cols_to_show = [c for c in ['Référence article', 'Désignation', 'Famille', 'Prix de vente'] if c in rupture.columns]
                st.dataframe(rupture[cols_to_show].head(20), use_container_width=True)
            else:
                st.info("Aucun article en rupture de stock")
        
        with col2:
            stock_faible = df_filtered[(df_filtered['Stock réel'] > 0) & (df_filtered['Stock réel'] < 10)]
            st.markdown("#### Articles à faible stock (< 10)")
            if len(stock_faible) > 0:
                cols_to_show = [c for c in ['Référence article', 'Désignation', 'Famille', 'Stock réel', 'Prix de vente'] if c in stock_faible.columns]
                st.dataframe(stock_faible[cols_to_show].head(20), use_container_width=True)
            else:
                st.info("Aucun article à faible stock")
    
    # Tableau de données
    st.markdown("### 📋 Données détaillées")
    cols_to_show = [c for c in ['Type', 'Référence article', 'Désignation', 'Famille', 'Prix d\'achat', 
                                'Prix de vente', 'Marge', 'Marge %', 'Fournisseur principal', 'Stock réel'] if c in df_filtered.columns]
    st.dataframe(df_filtered[cols_to_show], use_container_width=True, height=400)
    
    # Bouton d'export
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        csv = df_filtered.to_csv(index=False).encode('utf-8-sig')
        st.download_button(
            label="📥 Télécharger les données filtrées (CSV)",
            data=csv,
            file_name=f"articles_filtres_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )

