import pandas as pd

df_matchs = pd.read_csv("../data/matchs.csv")

df_matchs["Division"] = df_matchs["Division"].str.strip().str.upper()

print(df_matchs["Division"].unique())