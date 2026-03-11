# Découverte du dataset - Marius

## Objectif
Comprendre la structure des données fournies par RavenStack et identifier les variables les plus utiles pour prédire le churn dans un contexte SaaS B2B.

## Fichiers analysés
- ravenstack_accounts.csv
- ravenstack_subscriptions.csv
- ravenstack_feature_usage.csv
- ravenstack_support_tickets.csv
- ravenstack_churn_events.csv

## Analyse de accounts.csv
- Nombre de lignes : 500
- Nombre de colonnes : 10
- Colonnes : `account_id`, `account_name`, `industry`, `country`, `signup_date`, `referral_source`, `plan_tier`, `seats`, `is_trial`, `churn_flag`
- Types de données : colonnes principalement textuelles (`object`), avec des variables numériques comme `seats`, `is_trial` et `churn_flag`
- Valeurs manquantes : aucune valeur manquante observée sur les premières vérifications réalisées dans le notebook
- Observations : ce fichier contient les données de base des comptes clients. On y retrouve des informations d’identification, le secteur d’activité, le pays, la date d’inscription, la source d’acquisition, le plan souscrit, le nombre de sièges et le statut d’essai.
- Utilité pour le churn : ce fichier est central car il contient déjà la variable cible `churn_flag` et plusieurs variables explicatives potentielles comme `plan_tier`, `seats`, `is_trial`, `industry`, `country`, `referral_source` et `signup_date`.

## Analyse de subscriptions.csv
- Nombre de lignes : cohérent avec le rôle d’un historique d’abonnements, le PDF indique un volume indicatif d’environ 5 000 lignes
- Nombre de colonnes : à confirmer dans le notebook, mais ce fichier regroupe les informations liées au cycle de vie des abonnements
- Colonnes : fichier dédié à l’historique des abonnements et de leurs modifications
- Types de données : mélange attendu de dates, d’identifiants, de statuts et de variables catégorielles liées aux offres
- Valeurs manquantes : à vérifier dans le notebook, notamment sur les dates de fin ou de modification
- Observations : ce fichier retrace les changements d’abonnement, ce qui est très important pour comprendre la stabilité d’un client, les upgrades, downgrades ou interruptions.
- Utilité pour le churn : très forte utilité, car l’historique d’abonnement donne des signaux directs sur le risque de départ, notamment la fréquence des changements, la durée d’abonnement, le type d’offre et d’éventuelles ruptures.

## Analyse de feature_usage.csv
- Nombre de lignes : le PDF indique un volume indicatif d’environ 60 000 lignes
- Nombre de colonnes : à confirmer dans le notebook
- Colonnes : fichier centré sur l’utilisation mensuelle des fonctionnalités
- Types de données : mélange attendu d’identifiants, de périodes temporelles, de noms de fonctionnalités et de mesures d’usage
- Valeurs manquantes : à vérifier dans le notebook, en particulier sur certaines métriques d’usage
- Observations : ce fichier mesure l’usage produit. Dans un SaaS, le niveau d’adoption et d’utilisation réelle est un signal fort de rétention ou de churn.
- Utilité pour le churn : probablement l’un des fichiers les plus importants, car une baisse d’usage, une faible adoption de fonctionnalités clés ou une activité irrégulière peuvent annoncer un churn futur.

## Analyse de support_tickets.csv
- Nombre de lignes : le PDF indique un volume indicatif d’environ 15 000 lignes
- Nombre de colonnes : à confirmer dans le notebook
- Colonnes : fichier lié aux tickets de support ouverts par les comptes
- Types de données : mélange attendu d’identifiants, de catégories de tickets, de niveaux de priorité, de dates et de statuts de résolution
- Valeurs manquantes : à vérifier dans le notebook, notamment sur certains champs de catégorisation ou de résolution
- Observations : ce fichier permet d’analyser la relation support/client. Un volume élevé de tickets, des tickets critiques ou un temps de résolution important peuvent dégrader l’expérience client.
- Utilité pour le churn : utile car il peut révéler une insatisfaction ou des difficultés récurrentes. Les tickets peuvent donc servir d’indicateurs indirects du risque de résiliation.

## Analyse de churn_events.csv
- Nombre de lignes : le PDF indique un volume indicatif d’environ 1 200 lignes
- Nombre de colonnes : à confirmer dans le notebook
- Colonnes : fichier dédié aux dates et motifs de résiliation constatés
- Types de données : mélange attendu d’identifiants, de dates et de catégories ou motifs de churn
- Valeurs manquantes : à vérifier dans le notebook, notamment sur les motifs de résiliation
- Observations : ce fichier documente les événements de churn réellement observés. Il permet de relier les résiliations effectives aux comportements, usages et incidents observés dans les autres tables.
- Utilité pour le churn : essentielle, car il sert à comprendre la réalité métier du churn, ses dates, ses causes possibles et la cohérence avec les autres sources de données.

## Synthèse
- Fichiers les plus utiles : `accounts.csv`, `subscriptions.csv`, `feature_usage.csv` et `churn_events.csv` paraissent les plus stratégiques pour la prédiction du churn. `support_tickets.csv` apporte une information complémentaire sur l’expérience client.
- Variables intéressantes : `churn_flag`, le type de plan, le nombre de sièges, le statut d’essai, l’ancienneté du compte, l’historique des abonnements, l’intensité d’usage produit, ainsi que les données liées au support client.
- Problèmes de qualité : les points à surveiller sont les valeurs manquantes, les dates incohérentes, les écarts de granularité entre fichiers et les colonnes potentiellement peu exploitables si elles sont trop textuelles ou hétérogènes.

- Points à creuser :
  1. Les clients en période d’essai churnent-ils davantage que les autres ?
  2. Certains plans d’abonnement sont-ils plus exposés au churn ?
  3. Une baisse d’usage des fonctionnalités précède-t-elle le churn ?
  4. Les comptes ayant beaucoup de tickets de support résilient-ils davantage ?
  5. L’ancienneté du compte influence-t-elle le risque de churn ?