# Logique métier : Crée une colonne catégorielle qui identifie le résultat du match (Victoire domicile / Nul / Victoire extérieur).

import pandas as pd

df = pd.read_csv("../data/matchs.csv")

resultat_map = {
    "H": "Victoire domicile",
    "D": "Nul",
    "A": "Victoire extérieur",
}

df["ResultatMatch"] = df["FTResult"].map(resultat_map).astype("category")


print(df[["HomeTeam", "AwayTeam", "FTResult", "ResultatMatch"]].head(10))