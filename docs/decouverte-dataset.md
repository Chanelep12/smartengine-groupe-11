# Fiche collective — Découverte du dataset RavenStack

## Tableau récapitulatif des fichiers CSV

| Fichier | Nombre de lignes | Colonnes clés | Observations |
|---|---|---|---|
| ravenstack_accounts.csv | ~500 | account_id, plan_tier, industry, country, seats, is_trial, churn_flag | Contient la variable cible churn_flag. Fichier central pour la modélisation. |
| ravenstack_subscriptions.csv | ~5 000 | account_id, plan, start_date, end_date, status | Historique des abonnements. Utile pour détecter les downgrades et résiliations. |
| ravenstack_feature_usage.csv | ~60 000 | account_id, feature_name, usage_month, usage_count | Le plus volumineux. Une faible utilisation peut signaler un risque de churn. |
| ravenstack_support_tickets.csv | ~15 000 | account_id, ticket_date, priority, status | Un volume élevé de tickets critiques peut indiquer une insatisfaction client. |
| ravenstack_churn_events.csv | ~1 200 | account_id, churn_date, churn_reason | Recense les résiliations effectives. Essentiel pour entraîner le modèle. |

## Colonnes les plus utiles pour prédire le churn

- `churn_flag` (accounts) : variable cible
- `plan_tier` (accounts) : le niveau d'abonnement influence la rétention
- `is_trial` (accounts) : les comptes en essai churnnent davantage
- `usage_count` (feature_usage) : une baisse d'usage précède souvent le churn
- `priority` (support_tickets) : les tickets critiques signalent une insatisfaction
- `churn_reason` (churn_events) : permet de comprendre les causes réelles

## 5 questions métier à explorer

1. Les clients en période d'essai churnnent-ils davantage que les autres ?
2. Certains plans d'abonnement sont-ils plus exposés au churn ?
3. Une baisse d'utilisation des fonctionnalités précède-t-elle le churn ?
4. Les comptes avec beaucoup de tickets de support résilient-ils davantage ?
5. L'ancienneté du compte influence-t-elle le risque de churn ?
