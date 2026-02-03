# Déduplication : Vérifie si des matchs apparaissent en double dans le dataset et procède à leur suppression si nécessaire.

import pandas as pd

df = pd.read_csv("../data/matchs.csv", low_memory=False)

# Colonnes identifiant un match unique
cles_match = ["Division", "MatchDate", "HomeTeam", "AwayTeam"]

# Vérification des doublons
nb_avant = len(df)
doublons = df.duplicated(subset=cles_match, keep=False)
nb_doublons = doublons.sum()

print(f"Nombre de lignes avant déduplication : {nb_avant}")
print(f"Lignes concernées par des doublons (même match) : {nb_doublons}")

# Suppression des doublons (on garde la première occurrence de chaque match)
df = df.drop_duplicates(subset=cles_match, keep="first")
nb_apres = len(df)

print(f"Nombre de lignes après déduplication : {nb_apres}")
print(f"Lignes supprimées : {nb_avant - nb_apres}")
print(f"\nDimensions du dataset nettoyé : {df.shape}")