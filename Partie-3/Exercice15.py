# Exploration de relations : Réalise un Scatter Plot mettant en relation le nombre de buts à domicile et le nombre de buts à l'extérieur, en utilisant une couleur pour distinguer les saisons.

import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/matchs.csv", low_memory=False)

col_domicile = "FTHome" if "FTHome" in df.columns else df.filter(like="Home").columns[0] if len(df.filter(like="Home").columns) else "FTHome"
col_exterieur = "FTAway" if "FTAway" in df.columns else df.filter(like="Away").columns[0] if len(df.filter(like="Away").columns) else "FTAway"
col_date = "MatchDate" if "MatchDate" in df.columns else "date" if "date" in df.columns else df.columns[1]

# Conserver les lignes avec buts renseignés
df_plot = df[[col_date, col_domicile, col_exterieur]].copy()
df_plot = df_plot.dropna(subset=[col_domicile, col_exterieur])

# Saison = année (extraire de la date)
df_plot["Saison"] = pd.to_datetime(df_plot[col_date], errors="coerce").dt.year.astype("Int64").astype(str)
df_plot = df_plot.dropna(subset=["Saison"])

fig = px.scatter(
    df_plot,
    x=col_domicile,
    y=col_exterieur,
    color="Saison",
    title="Buts à domicile vs buts à l'extérieur (par saison)",
    labels={col_domicile: "Buts à domicile", col_exterieur: "Buts à l'extérieur"},
    opacity=0.6,
)
fig.update_layout(xaxis=dict(dtick=1), yaxis=dict(dtick=1))
fig.show()
