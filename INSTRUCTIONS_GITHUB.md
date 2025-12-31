# 📤 Instructions pour pousser sur GitHub

## Étapes pour déployer sur Streamlit Cloud

### 1. Créer un dépôt sur GitHub

1. Allez sur https://github.com
2. Cliquez sur le bouton **"+"** en haut à droite → **"New repository"**
3. Nom du dépôt : `dashbbbmagri` (ou un autre nom)
4. Cochez **"Public"** (gratuit) ou **"Private"**
5. **NE PAS** cocher "Initialize with README" (on a déjà les fichiers)
6. Cliquez sur **"Create repository"**

### 2. Connecter votre dépôt local à GitHub

Copiez et exécutez ces commandes (remplacez VOTRE_USERNAME par votre nom d'utilisateur GitHub) :

```bash
git branch -M main
git remote add origin https://github.com/VOTRE_USERNAME/dashbbbmagri.git
git push -u origin main
```

**Exemple :**
Si votre nom d'utilisateur GitHub est `jean-dupont`, la commande sera :
```bash
git remote add origin https://github.com/jean-dupont/dashbbbmagri.git
```

### 3. Vérifier que les fichiers sont sur GitHub

1. Allez sur votre dépôt GitHub : `https://github.com/VOTRE_USERNAME/dashbbbmagri`
2. Vérifiez que vous voyez le fichier `dashboard_commercial.py`
3. Vérifiez que tous les fichiers sont présents :
   - ✅ dashboard_commercial.py
   - ✅ requirements.txt
   - ✅ 1.xlsx
   - ✅ Logo bbm agri.jpg
   - ✅ .streamlit/config.toml

### 4. Déployer sur Streamlit Cloud

1. Allez sur https://streamlit.io/cloud
2. Connectez-vous avec votre compte GitHub
3. Cliquez sur **"New app"**
4. Sélectionnez votre dépôt : `dashbbbmagri`
5. **Fichier principal** : `dashboard_commercial.py`
6. Cliquez sur **"Deploy"**

### 5. Votre application est en ligne !

Vous recevrez une URL comme : `https://dashbbbmagri.streamlit.app`

---

## ⚠️ Si vous avez déjà créé le dépôt GitHub

Si vous avez déjà créé le dépôt sur GitHub, utilisez ces commandes :

```bash
git branch -M main
git remote add origin https://github.com/VOTRE_USERNAME/dashbbbmagri.git
git push -u origin main
```

Si le dépôt existe déjà et contient des fichiers, vous devrez peut-être faire :
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

