import pandas as pd

df_matchs = pd.read_csv("../data/matchs.csv")

df_focus = df_matchs[["MatchDate", "HomeTeam", "AwayTeam", "FTHome", "FTAway"]]

equipe_cible = "Real Madrid"
df_equipe = df_focus[(df_focus["HomeTeam"] == equipe_cible) | (df_focus["AwayTeam"] == equipe_cible)]

print(df_equipe.head())