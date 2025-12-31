# 🚀 Démarrage Rapide - Tableau de Bord Web

## Installation locale (pour tester)

```bash
# 1. Installer les dépendances
pip install -r requirements.txt

# 2. Lancer l'application
streamlit run dashboard_commercial.py
```

L'application sera accessible sur : **http://localhost:8501**

---

## Déploiement sur le web (Streamlit Cloud - Gratuit)

### Méthode la plus simple :

1. **Créer un compte GitHub** (si vous n'en avez pas)
   - https://github.com

2. **Créer un dépôt GitHub**
   - Cliquez sur "New repository"
   - Nom : `dashbbbmagri`
   - Cochez "Public" (gratuit) ou "Private"
   - Cliquez sur "Create repository"

3. **Uploader vos fichiers**
   ```bash
   git init
   git add .
   git commit -m "Tableau de bord commercial BBM AGRI"
   git branch -M main
   git remote add origin https://github.com/VOTRE_USERNAME/dashbbbmagri.git
   git push -u origin main
   ```
   
   Ou utilisez l'interface GitHub pour uploader les fichiers directement.

4. **Déployer sur Streamlit Cloud**
   - Allez sur https://streamlit.io/cloud
   - Cliquez sur "Sign in" et connectez-vous avec GitHub
   - Cliquez sur "New app"
   - Sélectionnez votre dépôt : `dashbbbmagri`
   - Fichier principal : `dashboard_commercial.py`
   - Cliquez sur "Deploy"

5. **Votre application est en ligne !**
   - Vous recevrez une URL comme : `https://dashbbbmagri.streamlit.app`
   - Partagez cette URL avec votre équipe

---

## Mettre à jour les données

### Option 1 : Via l'interface web
1. Ouvrez votre tableau de bord
2. Dans la barre latérale, cliquez sur "📤 Mettre à jour les données"
3. Téléchargez votre nouveau fichier Excel
4. Rechargez la page

### Option 2 : Via GitHub
1. Remplacez le fichier `1.xlsx` dans votre dépôt
2. Poussez les changements : `git push`
3. Streamlit Cloud redéploiera automatiquement

---

## Fichiers nécessaires pour le déploiement

✅ `dashboard_commercial.py` - Application principale
✅ `requirements.txt` - Dépendances Python
✅ `1.xlsx` - Fichier de données
✅ `Logo bbm agri.jpg` - Logo de l'entreprise
✅ `.streamlit/config.toml` - Configuration Streamlit

---

## Support

Pour plus de détails, consultez `DEPLOYMENT.md`

