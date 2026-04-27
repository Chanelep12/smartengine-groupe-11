# Rapport de Nettoyage des Données

## 1. ravenstack_accounts.csv
- **Problèmes identifiés** : Incohérence du `churn_flag` (seulement 110 marqués alors que 352 événements existent).
- **Stratégie** : Recalculer `churn_flag` basé sur le fichier `churn_events`.
- **Résultat** : 500 lignes. Churn flag corrigé de 110 à 352.

## 2. ravenstack_churn_events.csv
- **Problèmes identifiés** : Valeurs manquantes dans `feedback_text` (148).
- **Stratégie** : Remplacer les valeurs nulles par 'No feedback'.
- **Résultat** : 148 valeurs remplacées.

## 3. ravenstack_feature_usage.csv
- **Problèmes identifiés** : Doublons dans `usage_id` (21).
- **Stratégie** : Supprimer les lignes avec des IDs de consommation en double.
- **Résultat** : Avant 25000 -> Après 24979.

## 4. ravenstack_subscriptions.csv
- **Problèmes identifiés** : Dates au format texte, `end_date` vide (4514) pour les abonnements actifs.
- **Stratégie** : Conversion en datetime. Les `NaT` en `end_date` sont conservés comme indicateurs d'abonnements actifs.
- **Résultat** : Conversion de type effectuée.

## 5. ravenstack_support_tickets.csv
- **Problèmes identifiés** : Valeurs manquantes dans `satisfaction_score` (825).
- **Stratégie** : Imputation par la moyenne (3.98).
- **Résultat** : 825 valeurs imputées.

