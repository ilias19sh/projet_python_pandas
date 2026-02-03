import pandas as pd 

df_rating = pd.read_csv("../data/rating.csv")
df_matchs = pd.read_csv("../data/matchs.csv")

df_equipes_scores = df_matchs[["Date", "Home_Team", "Away_Team", "Home_Score", "Away_Score"]]

print(df_equipes_scores.head())