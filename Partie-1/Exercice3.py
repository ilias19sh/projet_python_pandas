# Résumé technique : Affiche le type de chaque colonne et vérifie s'il y a des valeurs nulles dans le dataset.

import pandas as pd

df = pd.read_csv('../data/matchs.csv')

# Types de chaque colonne
print("=== Types des colonnes ===")
print(df.dtypes)
print()


print("=== Valeurs nulles par colonne ===")
nulles = df.isnull().sum()
print(nulles)
print()


colonnes_avec_nulles = nulles[nulles > 0]
if len(colonnes_avec_nulles) > 0:
    print("Colonnes contenant des valeurs nulles :")
    print(colonnes_avec_nulles)
else:
    print("Aucune valeur nulle dans le dataset.")