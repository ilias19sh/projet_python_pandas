Dataset Link : https://github.com/xgabora/Club-Football-Match-Data-2000-2025

Partie I : Fondamentaux (Pandas)
Exploration, sélection et nettoyage de base.

Chargement : Charge le fichier matches.csv et affiche ses dimensions globales (nombre de lignes et de colonnes).

Inspection : Affiche un échantillon aléatoire de 10 lignes du dataset pour comprendre sa structure.

Résumé technique : Affiche le type de chaque colonne et vérifie s'il y a des valeurs nulles dans le dataset.

Sélection ciblée : Crée un nouveau DataFrame contenant uniquement les colonnes relatives aux équipes, à la date et aux scores.

Recherche spécifique : Filtre le dataset pour n'afficher que les matchs joués par une équipe précise (ex: 'Real Madrid' ou 'Liverpool').

Partie II : Technique & Réflexion (Analyse avancée)
Transformation, calculs et logique métier.

Normalisation : Nettoie les noms des championnats (colonne League) pour supprimer les espaces en début/fin de chaîne et les mettre en majuscules.

Séries temporelles : Convertis la colonne des dates au format approprié et crée une nouvelle colonne contenant uniquement le mois du match.

Ingénierie de données : Calcule la différence de buts entre l'équipe à domicile et l'équipe à l'extérieur pour chaque match dans une nouvelle colonne.

Logique métier : Crée une colonne catégorielle qui identifie le résultat du match (Victoire domicile / Nul / Victoire extérieur).

Statistiques groupées : Calcule le nombre total de buts marqués par championnat pour chaque saison.

Performance relative : Identifie les 5 dates où il y a eu la plus grande moyenne de buts marqués.

Déduplication : Vérifie si des matchs apparaissent en double dans le dataset et procède à leur suppression si nécessaire.

Partie III : Visualisation (Plotly)
Représentation graphique des tendances.

Analyse de répartition : Génère un Histogramme montrant la distribution des buts marqués à domicile.

Comparaison catégorielle : Crée un Bar Chart représentant le nombre de matchs joués par chaque championnat présent dans le dataset.

Exploration de relations : Réalise un Scatter Plot mettant en relation le nombre de buts à domicile et le nombre de buts à l'extérieur, en utilisant une couleur pour distinguer les saisons.