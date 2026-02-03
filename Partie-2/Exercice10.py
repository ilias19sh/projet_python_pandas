import pandas as pd

df_matchs = pd.read_csv("../data/matchs.csv")
df_matchs["MatchDate"] = pd.to_datetime(df_matchs["MatchDate"])
df_matchs["Season"] = df_matchs["MatchDate"].dt.year
df_matchs["Total_Goals"] = df_matchs["FTHome"] + df_matchs["FTAway"]

stats_saison = df_matchs.groupby(["Division", "Season"])["Total_Goals"].sum().reset_index()

print(stats_saison)