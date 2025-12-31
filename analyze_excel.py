# -*- coding: utf-8 -*-
import pandas as pd
import os
import sys
from datetime import datetime

# Configuration de l'encodage pour Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Informations sur le fichier
file_path = '1.xlsx'
stat = os.stat(file_path)

print('=' * 60)
print('ANALYSE DU FICHIER EXCEL')
print('=' * 60)
print(f'\nDate de creation: {datetime.fromtimestamp(stat.st_ctime)}')
print(f'Date de modification: {datetime.fromtimestamp(stat.st_mtime)}')
print(f'Taille du fichier: {stat.st_size / 1024:.2f} KB')

# Lire le fichier Excel
excel_file = pd.ExcelFile(file_path)
print(f'\nNombre de feuilles: {len(excel_file.sheet_names)}')
print(f'Noms des feuilles: {excel_file.sheet_names}')

# Analyser chaque feuille
for sheet_name in excel_file.sheet_names:
    print(f'\n{"=" * 60}')
    print(f'FEUILLE: {sheet_name}')
    print(f'{"=" * 60}')
    
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    print(f'\nDimensions: {df.shape[0]} lignes x {df.shape[1]} colonnes')
    
    print(f'\nColonnes ({len(df.columns)}):')
    for i, col in enumerate(df.columns, 1):
        print(f'  {i:2d}. {col} ({df[col].dtype})')
    
    print(f'\nTypes de donnees:')
    print(df.dtypes)
    
    print(f'\nApercu des donnees (10 premieres lignes):')
    print(df.head(10).to_string())
    
    print(f'\nStatistiques descriptives:')
    print(df.describe())
    
    print(f'\nValeurs manquantes:')
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print(missing[missing > 0])
    else:
        print('Aucune valeur manquante')

