# Analyse de répartition : Génère un Histogramme montrant la distribution des buts marqués à domicile.

import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/matchs.csv", low_memory=False)

buts_domicile = df["FTHome"].dropna()

fig = px.histogram(
    x=buts_domicile,
    title="Distribution des buts marqués à domicile",
    labels={"x": "Buts marqués à domicile", "y": "Nombre de matchs"},
    nbins=int(buts_domicile.max() - buts_domicile.min() + 1),
)
fig.update_layout(bargap=0.2)
fig.show()