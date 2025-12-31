# 🔄 Guide d'Actualisation - Sans Redémarrer

## Méthodes pour actualiser les données

### ✅ Méthode 1 : Bouton de rafraîchissement (Recommandé)

1. **Dans la barre latérale**, cliquez sur le bouton **"🔄 Actualiser les données"**
2. L'application se rafraîchit automatiquement
3. **Aucun redémarrage nécessaire !**

---

### ✅ Méthode 2 : Upload de nouveau fichier

1. Dans la barre latérale, section **"📤 Mettre à jour les données"**
2. Cliquez sur **"Télécharger un nouveau fichier Excel"**
3. Sélectionnez votre fichier Excel mis à jour
4. L'application se rafraîchit **automatiquement** après l'upload
5. **Aucun redémarrage nécessaire !**

---

### ✅ Méthode 3 : Rafraîchissement du navigateur

Si vous voulez simplement recharger la page :

- **Windows/Linux** : Appuyez sur `F5` ou `Ctrl + R`
- **Mac** : Appuyez sur `Cmd + R`
- Ou cliquez sur le bouton de rafraîchissement de votre navigateur

---

### ✅ Méthode 4 : Mise à jour via GitHub (Automatique)

1. Remplacez le fichier `1.xlsx` dans votre dépôt GitHub
2. Poussez les changements : `git push origin main`
3. Streamlit Cloud **redéploie automatiquement** (quelques secondes)
4. L'application se met à jour **sans intervention manuelle**

---

## ⚠️ Quand redémarrer est nécessaire

Le redémarrage n'est **PAS nécessaire** pour :
- ✅ Mettre à jour les données Excel
- ✅ Changer les filtres
- ✅ Actualiser les graphiques

Le redémarrage est nécessaire **SEULEMENT** pour :
- ❌ Modifier le code Python (`dashboard_commercial.py`)
- ❌ Changer les dépendances (`requirements.txt`)
- ❌ Modifier la configuration (`.streamlit/config.toml`)

Dans ces cas, Streamlit Cloud redéploie automatiquement après un `git push`.

---

## 💡 Astuce : Actualisation automatique

L'application utilise un système de **cache intelligent** :
- Les données sont mises en cache pour de meilleures performances
- Le cache se vide automatiquement lors de l'upload d'un nouveau fichier
- Le bouton "Actualiser" vide le cache manuellement

---

## 🚀 Sur Streamlit Cloud

Sur Streamlit Cloud, vous pouvez aussi :

1. **Aller dans "Manage app"** (en bas à droite)
2. Cliquer sur **"Reboot app"** si nécessaire
3. Mais normalement, **aucun redémarrage n'est nécessaire** pour mettre à jour les données !

---

## 📝 Résumé

**Pour actualiser les données :**
- ✅ Utilisez le bouton **"🔄 Actualiser les données"** dans la barre latérale
- ✅ Ou uploadez un nouveau fichier Excel

**Aucun redémarrage manuel nécessaire !** 🎉

