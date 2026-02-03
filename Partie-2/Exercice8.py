import pandas as pd

df_matchs = pd.read_csv("../data/matchs.csv")

df_matchs["Goal_Diff"] = df_matchs["FTHome"] - df_matchs["FTAway"]

print(df_matchs[["HomeTeam", "AwayTeam", "FTHome", "FTAway", "Goal_Diff"]].head())