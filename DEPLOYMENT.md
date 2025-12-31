# 🌐 Guide de Déploiement Web - Tableau de Bord Commercial

## Options de déploiement

### Option 1 : Streamlit Cloud (Recommandé - Gratuit)

Streamlit Cloud est la solution la plus simple pour déployer votre tableau de bord.

#### Étapes :

1. **Créer un compte sur Streamlit Cloud**
   - Allez sur https://streamlit.io/cloud
   - Connectez-vous avec votre compte GitHub

2. **Préparer votre dépôt GitHub**
   ```bash
   git init
   git add .
   git commit -m "Tableau de bord commercial BBM AGRI"
   git branch -M main
   git remote add origin https://github.com/VOTRE_USERNAME/dashbbbmagri.git
   git push -u origin main
   ```

3. **Déployer sur Streamlit Cloud**
   - Connectez votre dépôt GitHub
   - Sélectionnez le dépôt `dashbbbmagri`
   - Fichier principal : `dashboard_commercial.py`
   - Cliquez sur "Deploy"

4. **Accéder à votre application**
   - Votre tableau de bord sera accessible via une URL : `https://votre-app.streamlit.app`

#### Fichiers nécessaires :
- ✅ `dashboard_commercial.py` (fichier principal)
- ✅ `requirements.txt` (dépendances)
- ✅ `1.xlsx` (fichier de données)
- ✅ `Logo bbm agri.jpg` (logo)
- ✅ `.streamlit/config.toml` (configuration)

---

### Option 2 : Heroku

#### Étapes :

1. **Installer Heroku CLI**
   - Téléchargez depuis https://devcenter.heroku.com/articles/heroku-cli

2. **Se connecter à Heroku**
   ```bash
   heroku login
   ```

3. **Créer une application**
   ```bash
   heroku create dashbbbmagri
   ```

4. **Déployer**
   ```bash
   git push heroku main
   ```

5. **Ouvrir l'application**
   ```bash
   heroku open
   ```

---

### Option 3 : VPS/Serveur dédié

#### Installation sur un serveur Linux :

1. **Installer Python et les dépendances**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   pip3 install -r requirements.txt
   ```

2. **Lancer Streamlit en arrière-plan**
   ```bash
   nohup streamlit run dashboard_commercial.py --server.port=8501 --server.address=0.0.0.0 &
   ```

3. **Configurer Nginx (optionnel)**
   ```nginx
   server {
       listen 80;
       server_name votre-domaine.com;
       
       location / {
           proxy_pass http://localhost:8501;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
           proxy_set_header Host $host;
       }
   }
   ```

4. **Configurer SSL avec Let's Encrypt (optionnel)**
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d votre-domaine.com
   ```

---

### Option 4 : Docker

#### Créer un Dockerfile :

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "dashboard_commercial.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### Construire et lancer :

```bash
docker build -t dashbbbmagri .
docker run -p 8501:8501 dashbbbmagri
```

---

## 🔧 Configuration pour la production

### Variables d'environnement

Créez un fichier `.env` (ou configurez dans votre plateforme) :

```env
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

### Sécurité

1. **Authentification** (optionnel) :
   - Utilisez Streamlit Authenticator
   - Ou configurez l'authentification au niveau du serveur web (Nginx)

2. **HTTPS** :
   - Toujours utiliser HTTPS en production
   - Configurer SSL/TLS avec Let's Encrypt

---

## 📝 Checklist de déploiement

- [ ] Tous les fichiers sont dans le dépôt
- [ ] `requirements.txt` est à jour
- [ ] Le fichier Excel `1.xlsx` est inclus
- [ ] Le logo est inclus
- [ ] Les tests locaux fonctionnent
- [ ] La configuration `.streamlit/config.toml` est correcte
- [ ] Les variables d'environnement sont configurées
- [ ] HTTPS est activé (production)
- [ ] Les sauvegardes sont configurées

---

## 🚀 Mise à jour des données

Pour mettre à jour les données Excel :

1. **Streamlit Cloud** :
   - Remplacez le fichier `1.xlsx` dans le dépôt
   - Poussez les changements : `git push`
   - L'application se redéploiera automatiquement

2. **Autres plateformes** :
   - Remplacez le fichier `1.xlsx`
   - Redémarrez l'application

---

## 📞 Support

Pour toute question sur le déploiement, consultez :
- Documentation Streamlit : https://docs.streamlit.io/
- Streamlit Cloud : https://docs.streamlit.io/streamlit-community-cloud

