# Séries temporelles : Convertis la colonne des dates au format approprié et crée une nouvelle colonne contenant uniquement le mois du match.

import pandas as pd

df = pd.read_csv("../data/matchs.csv")


df["MatchDate"] = pd.to_datetime(df["MatchDate"])

df["MoisMatch"] = df["MatchDate"].dt.month

print(df[["MatchDate", "MoisMatch"]].head(10))