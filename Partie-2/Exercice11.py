# Performance relative : Identifie les 5 dates où il y a eu la plus grande moyenne de buts marqués.

import pandas as pd

df = pd.read_csv("../data/matchs.csv", low_memory=False)


df["ButsTotaux"] = df["FTHome"].fillna(0) + df["FTAway"].fillna(0)

moyenne_par_date = df.groupby("MatchDate")["ButsTotaux"].mean()

top5_dates = moyenne_par_date.nlargest(5)

print(top5_dates.to_string())