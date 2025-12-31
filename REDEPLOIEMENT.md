# 🔄 Guide de Redéploiement Manuel - Streamlit Cloud

## Comment forcer un redéploiement manuel

Si Streamlit Cloud ne redéploie pas automatiquement après un `git push`, voici comment forcer un redéploiement :

### Méthode 1 : Via l'interface Streamlit Cloud (Recommandé)

1. **Allez sur https://share.streamlit.io** ou votre dashboard Streamlit Cloud
2. **Connectez-vous** avec votre compte GitHub
3. **Trouvez votre application** dans la liste
4. Cliquez sur **"Manage app"** (en bas à droite de l'application)
5. Dans le menu, cliquez sur **"Reboot app"** ou **"Redeploy"**
6. L'application va redémarrer et charger les dernières modifications

---

### Méthode 2 : Via les paramètres de l'application

1. Dans **"Manage app"**, allez dans **"Settings"**
2. Vérifiez que **"Auto-redeploy"** est activé (si disponible)
3. Si ce n'est pas le cas, activez-le
4. Faites un nouveau `git push` pour déclencher le redéploiement

---

### Méthode 3 : Push Git avec commit vide (Astuce)

Si le redéploiement automatique ne fonctionne pas, vous pouvez forcer un nouveau déploiement :

```bash
git commit --allow-empty -m "Force redeploy"
git push origin main
```

Cela crée un commit vide qui déclenchera le redéploiement.

---

### Méthode 4 : Vérifier les logs

1. Dans **"Manage app"**, cliquez sur **"Logs"**
2. Vérifiez s'il y a des erreurs qui empêchent le redéploiement
3. Les erreurs courantes :
   - Problèmes de dépendances (`requirements.txt`)
   - Erreurs de syntaxe dans le code
   - Fichiers manquants

---

## ⚙️ Configuration du redéploiement automatique

### Vérifier les paramètres

1. Allez dans **"Manage app"** → **"Settings"**
2. Vérifiez :
   - ✅ **Branch** : Doit être `main` (ou votre branche principale)
   - ✅ **Main file path** : Doit être `dashboard_commercial.py`
   - ✅ **Auto-redeploy** : Doit être activé

### Si le redéploiement automatique ne fonctionne pas

1. **Vérifiez que vous poussez sur la bonne branche** :
   ```bash
   git branch  # Vérifiez votre branche actuelle
   git push origin main  # Poussez sur main
   ```

2. **Vérifiez les notifications GitHub** :
   - Streamlit Cloud doit avoir accès à votre dépôt
   - Les webhooks GitHub doivent être configurés

3. **Attendez quelques minutes** :
   - Le redéploiement peut prendre 1-2 minutes
   - Vérifiez l'onglet "Activity" dans "Manage app"

---

## 🔍 Dépannage

### L'application ne se met pas à jour ?

1. **Videz le cache du navigateur** :
   - `Ctrl + Shift + R` (Windows/Linux)
   - `Cmd + Shift + R` (Mac)

2. **Vérifiez que le commit est bien sur GitHub** :
   - Allez sur https://github.com/HAMID25W/dashbbbmagri
   - Vérifiez que votre dernier commit est présent

3. **Redémarrez manuellement** :
   - "Manage app" → "Reboot app"

---

## 📝 Résumé

**Pour redéployer manuellement :**
1. Allez sur Streamlit Cloud
2. "Manage app" → "Reboot app"

**Pour forcer un redéploiement via Git :**
```bash
git commit --allow-empty -m "Force redeploy"
git push origin main
```

**Vérifiez toujours les logs** en cas de problème !

