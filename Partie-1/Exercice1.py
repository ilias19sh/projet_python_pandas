#Charge le fichier matches.csv et affiche ses dimensions globales (nombre de lignes et de colonnes)

import pandas as pd

df = pd.read_csv('../data/matchs.csv')
print(df.shape)