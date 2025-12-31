@echo off
setlocal enabledelayedexpansion

REM ============================================================
REM Lancer le tableau de bord Streamlit en local (Windows)
REM - Crée .venv si absent
REM - Installe requirements.txt
REM - Lance: streamlit run dashboard_commercial.py
REM ============================================================

REM Aller dans le dossier du script (racine du projet)
cd /d "%~dp0"

REM Vérifier que Python est disponible
python --version >NUL 2>&1
if errorlevel 1 (
  echo [ERREUR] Python n'est pas trouve dans le PATH.
  echo Installez Python puis relancez ce fichier.
  pause
  exit /b 1
)

REM Creer l'environnement virtuel si absent
if not exist ".venv\Scripts\python.exe" (
  echo [INFO] Creation de l'environnement virtuel .venv ...
  python -m venv .venv
  if errorlevel 1 (
    echo [ERREUR] Echec de creation de .venv
    pause
    exit /b 1
  )
)

REM Activer l'environnement virtuel
call ".venv\Scripts\activate.bat"
if errorlevel 1 (
  echo [ERREUR] Impossible d'activer .venv
  pause
  exit /b 1
)

REM Installer / mettre a jour les dependances
echo [INFO] Installation des dependances (requirements.txt) ...
python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
  echo [ERREUR] Echec de l'installation des dependances.
  pause
  exit /b 1
)

REM Lancer Streamlit
echo.
echo [INFO] Lancement de l'application ...
echo Ouvrez ensuite: http://localhost:8501
echo (Pour arreter: Ctrl+C dans cette fenetre)
echo.

streamlit run "dashboard_commercial.py"

REM Si Streamlit se ferme, garder la fenetre ouverte
pause

