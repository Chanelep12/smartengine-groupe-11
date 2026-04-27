# Rapport de Modélisation Churn - smartEngine

## Introduction
Ce rapport présente les résultats de la modélisation prédictive du churn pour RavenStack. L'objectif était de maximiser la détection des comptes à risque (Recall).

## Analyse du Dataset
- **Volume total** : 500 comptes analysés.
- **Déséquilibre des classes** :
    - Churn (1) : 70.4%
    - Non-Churn (0) : 29.6%
*Note : Le dataset présente un taux de churn inhabituellement élevé.*

## Méthodologie
- **Prétraitement** :
    - Normalisation des variables numériques (StandardScaler).
    - Encodage One-Hot des variables catégorielles.
- **Split** : 80% entraînement / 20% test, stratifié sur la cible.
- **Modèles testés** : Régression Logistique, Random Forest.
- **Critère de sélection** : Meilleur Recall sur la classe Churn.

## Performances du Modèle Retenu
Le modèle **Random Forest** a été sélectionné.

| Métrique | Valeur |
| :--- | :--- |
| Accuracy | 0.68 |
| Precision | 0.69 |
| **Recall (Churn)** | **0.97** |
| F1-Score | 0.81 |
| AUC-ROC | 0.51 |

### Analyse des performances
Le modèle est excellent pour identifier les clients qui vont churner (Recall 97%), mais il a tendance à sur-prédire le churn (faible spécificité pour la classe 0). L'AUC-ROC de 0.51 indique que le pouvoir de discrimination entre les deux classes reste faible avec les features actuelles.

## Facteurs de Churn (Top 10 Features)
Les variables les plus influentes dans la prédiction sont :
1. **usage_trend_3m** : Tendance d'utilisation sur les 3 derniers mois.
2. **avg_seats** : Nombre moyen de sièges.
3. **total_usage_count** : Nombre total d'actions d'utilisation.
4. **avg_satisfaction_score** : Score moyen de satisfaction.
5. **tenure_months** : Ancienneté du compte en mois.
6. **total_arr** : Revenu Annuel Récurrent total.
7. **seats** : Nombre de sièges actuels.
8. **avg_resolution_time** : Temps moyen de résolution des tickets.
9. **active_days_ratio** : Ratio de jours actifs.
10. **total_usage_duration** : Durée totale d'utilisation.

## Segmentation du Risque
Répartition des 500 comptes selon leur niveau de risque calculé :
- **High (Score >= 0.70)** : 338 comptes
- **Medium (0.40 <= Score < 0.70)** : 44 comptes
- **Low (Score < 0.40)** : 118 comptes

## Recommandations
1. **Focus sur l'engagement** : La tendance d'utilisation (`usage_trend_3m`) est le premier signal. Une baisse d'activité doit déclencher une alerte immédiate.
2. **Amélioration du modèle** : Explorer de nouvelles features liées aux interactions spécifiques avec les fonctionnalités clés pour améliorer la discrimination (AUC-ROC).
3. **Action Prioritaire** : Cibler les 338 comptes en risque "High" avec des campagnes de Customer Success personnalisées.
