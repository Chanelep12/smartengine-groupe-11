# Agent : Exploration du dataset RavenStack

## Objectif
Explorer les 5 fichiers CSV du dataset RavenStack et produire un rapport
de découverte structuré pour chaque fichier.

## Contexte
Les fichiers CSV sont disponibles dans le dossier racine du projet :
- ravenstack_accounts.csv
- ravenstack_subscriptions.csv
- ravenstack_feature_usage.csv
- ravenstack_support_tickets.csv
- ravenstack_churn_events.csv

## Tâches à effectuer

Pour chaque fichier CSV, tu dois :

1. Charger le fichier avec pandas
2. Afficher le nombre de lignes et de colonnes (shape)
3. Afficher le nom et le type de chaque colonne (info)
4. Afficher les 5 premières lignes (head)
5. Identifier les valeurs manquantes (isna().sum())
6. Identifier les valeurs aberrantes ou incohérentes
7. Indiquer quelles colonnes semblent utiles pour prédire le churn

## Format du rapport de sortie

Le rapport doit être sauvegardé dans outputs/rapport-exploration.md
avec la structure suivante pour chaque fichier :

### [nom du fichier]
- Nombre de lignes :
- Nombre de colonnes :
- Colonnes et types :
- Valeurs manquantes :
- Observations :
- Colonnes utiles pour le churn :

## Contraintes
- Ne jamais modifier les fichiers dans data/raw/
- Tous les rapports sont rédigés en français
- Le code Python généré doit être sauvegardé dans src/exploration.py