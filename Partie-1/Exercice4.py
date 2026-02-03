import pandas as pd 

df_rating = pd.read_csv("../data/rating.csv")
df_matchs = pd.read_csv("../data/matchs.csv")

df_equipes_scores = df_matchs[["MatchDate", "HomeTeam", "AwayTeam", "FTHome", "FTAway"]]

print(df_equipes_scores.head())