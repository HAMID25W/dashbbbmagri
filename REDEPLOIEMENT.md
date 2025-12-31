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

**Note :** Les paramètres peuvent varier selon la version de Streamlit Cloud.

1. Dans **"Manage app"**, cherchez l'onglet **"Settings"** ou **"Configuration"**
2. Si vous ne voyez pas "Settings", essayez :
   - Cliquez sur les **3 points** (menu) en haut à droite
   - Ou cherchez **"App settings"** dans le menu latéral
3. Vérifiez les paramètres suivants (s'ils sont disponibles) :
   - **Branch** : Doit être `main`
   - **Main file path** : Doit être `dashboard_commercial.py`
   - **Auto-redeploy** : Si disponible, activez-le
4. Si ces options ne sont pas visibles, utilisez la **Méthode 1** (Reboot app) ou **Méthode 3** (commit vide)

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

**Important :** Si vous ne voyez pas les paramètres dans "Settings", c'est normal. Streamlit Cloud redéploie automatiquement par défaut lors d'un `git push`.

1. Allez dans **"Manage app"**
2. Cherchez **"Settings"**, **"Configuration"**, ou **"App settings"**
   - Si vous ne trouvez pas, les paramètres peuvent être dans :
     - Le menu en haut à droite (3 points)
     - L'onglet "Settings" dans le menu latéral
     - Directement dans "Manage app" → première section
3. Si les paramètres ne sont pas accessibles, vérifiez :
   - ✅ Que vous poussez sur la branche `main`
   - ✅ Que le fichier principal est `dashboard_commercial.py`
   - ✅ Que votre dépôt GitHub est bien connecté

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

