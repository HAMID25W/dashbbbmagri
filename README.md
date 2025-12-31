# Tableau de Bord Commercial - BBM AGRI

## 📋 Description

Application de tableau de bord commercial pour analyser les données Excel importées depuis Sage Commercial.

## 📊 Contenu du fichier Excel

Le fichier `1.xlsx` contient :
- **1720 lignes** de données produits
- **9 colonnes** :
  - Type
  - Référence article
  - Désignation
  - Nomenclature
  - Famille
  - Prix d'achat
  - Prix de vente
  - Fournisseur principal
  - Stock réel

**Informations du fichier :**
- Date de création : 2025-12-31 09:07:30
- Date de modification : 2025-12-30 18:41:56
- Taille : 113.57 KB

## 🚀 Installation

1. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## 💻 Utilisation

### Analyse du fichier Excel
```bash
python analyze_excel.py
```

### Lancer le tableau de bord localement
```bash
streamlit run dashboard_commercial.py
```
L'application sera accessible sur : http://localhost:8501

### Déployer sur le web
Consultez le fichier `DEPLOYMENT.md` pour les instructions complètes de déploiement.

**Option rapide - Streamlit Cloud (Gratuit) :**
1. Créez un compte sur https://streamlit.io/cloud
2. Connectez votre dépôt GitHub
3. Déployez en un clic !

Votre tableau de bord sera accessible via une URL publique.

## 🔍 Fonctionnalités du tableau de bord

### Filtres disponibles :
1. **Type** : Filtrer par type d'article
2. **Famille** : Filtrer par famille de produits
3. **Fournisseur principal** : Filtrer par fournisseur
4. **État du stock** : Tous / En stock / Rupture / Stock faible (< 10)
5. **Marge** : Filtrer par marge minimale et maximale (%)
6. **Prix de vente** : Filtrer par fourchette de prix

### Visualisations :
- Répartition par famille (graphique en camembert)
- Répartition par fournisseur (graphique en barres)
- Distribution des marges (histogramme)
- Relation prix d'achat vs prix de vente (nuage de points)
- Analyse du stock (ruptures et stocks faibles)

### Indicateurs clés :
- Total articles
- Stock total
- Valeur du stock
- Marge moyenne
- Prix moyen

### Export :
- Téléchargement des données filtrées en CSV

## 📁 Structure des fichiers

```
Dashbbbmagri/
├── 1.xlsx                    # Fichier Excel source
├── Logo bbm agri.jpg         # Logo de l'entreprise
├── analyze_excel.py          # Script d'analyse du fichier Excel
├── dashboard_commercial.py   # Application Streamlit
├── requirements.txt          # Dépendances Python
└── README.md                 # Documentation
```

