# Comparaison catégorielle : Crée un Bar Chart représentant le nombre de matchs joués par chaque championnat présent dans le dataset.

import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/matchs.csv", low_memory=False)


matchs_par_championnat = df["Division"].value_counts().reset_index()
matchs_par_championnat.columns = ["Championnat", "Nombre de matchs"]

fig = px.bar(
    matchs_par_championnat,
    x="Championnat",
    y="Nombre de matchs",
    title="Nombre de matchs joués par championnat",
    labels={"Championnat": "Championnat", "Nombre de matchs": "Nombre de matchs"},
)
fig.update_layout(xaxis_tickangle=-45)
fig.show()