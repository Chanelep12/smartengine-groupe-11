# Agent Data Engineer - Sprint 2

Cet agent est responsable de la transformation des données brutes en une table analytique prête pour la modélisation prédictive du churn.

## Rôle
L'agent Data Engineer assure l'intégrité, la cohérence et la richesse du dataset final. Il automatise le passage des fichiers CSV bruts (`data/raw/`) vers une table consolidée et enrichie (`data/processed/analytics.csv`).

## Étapes de Nettoyage (`src/clean_data.py`)
Le nettoyage traite les anomalies identifiées lors de l'exploration initiale :
- **Correction du Churn Flag** : Recalcul de la cible dans `accounts` en se basant sur la présence réelle d'événements dans `churn_events`.
- **Gestion des Doublons** : Suppression des entrées dupliquées basées sur les identifiants uniques (notamment dans `feature_usage`).
- **Traitement des Valeurs Manquantes** : 
    - Imputation par la moyenne pour les scores de satisfaction.
    - Valeurs par défaut ("No feedback") pour les commentaires textuels.
- **Normalisation des Types** : Conversion systématique des colonnes de dates au format `datetime`.

## Construction de la Table Analytique (`src/build_analytics.py`)
La table est construite par agrégation au niveau `account_id` (une ligne par compte) :
- **Abonnements** : Somme du MRR/ARR, moyenne des sièges, comptage des upgrades/downgrades.
- **Usage** : Somme du volume d'utilisation, de la durée et des erreurs rencontrées.
- **Support** : Nombre total de tickets, temps de résolution moyen et score de satisfaction moyen.
- **Variable Cible** : Création de `target_churn` (0 ou 1).

## Feature Engineering (`src/build_features.py`)
Enrichissement de la table avec des indicateurs prédictifs avancés :
- **Ancienneté (`tenure_months`)** : Nombre de mois depuis l'inscription (calculé au 30/03/2026).
- **Ratio Tickets Critiques** : Part des tickets de priorité 'urgent' ou 'high' sur le total des tickets du compte.
- **Ratio Jours Actifs** : Proportion de jours avec au moins une action d'usage par rapport à la durée de vie du compte dans le dataset.
- **Tendance d'Usage (3m)** : Comparaison de l'activité du dernier trimestre (Q4 2024) par rapport au précédent (Q3 2024) pour détecter une baisse d'engagement.

## Sorties
- **Données nettoyées** : `data/cleaned/`
- **Table finale** : `data/processed/analytics.csv`
- **Rapport de nettoyage** : `outputs/rapport-nettoyage.md`
