import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report
from sklearn.model_selection import train_test_split
import os

# 1. Chargement des données et du modèle
df = pd.read_csv('data/processed/analytics.csv')
if 'target_churn' in df.columns:
    df = df.rename(columns={'target_churn': 'churn'})

model = joblib.load('outputs/models/churn_model.joblib')

# 2. Séparation Features / Target (même logique que train_model.py)
drop_cols = ['churn', 'account_id', 'account_name', 'churn_flag', 'signup_date']
X = df.drop(columns=[c for c in drop_cols if c in df.columns])
y = df['churn']

# On garde les colonnes pour l'analyse par sous-groupe
X_full = df.drop(columns=['churn'])

# Split (même random_state pour cohérence)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42
)

# 3. Évaluation globale
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

metrics = {
    'Accuracy': accuracy_score(y_test, y_pred),
    'Precision': precision_score(y_test, y_pred),
    'Recall': recall_score(y_test, y_pred),
    'F1-Score': f1_score(y_test, y_pred),
    'AUC-ROC': roc_auc_score(y_test, y_proba)
}

print("Tableau Comparatif des Métriques (Meilleur Modèle) :")
print(pd.Series(metrics))

print("\nRapport de Classification :")
print(classification_report(y_test, y_pred))

# 4. Importance des features
# Pour un Pipeline avec Random Forest
classifier = model.named_steps['classifier']
preprocessor = model.named_steps['preprocessor']

# Récupération des noms de colonnes après encodage
cat_features = preprocessor.named_transformers_['cat'].get_feature_names_out()
num_features = preprocessor.named_transformers_['num'].get_feature_names_out() # En fait ce sont les mêmes noms
all_features = np.concatenate([num_features, cat_features])

importances = classifier.feature_importances_
feature_imp = pd.Series(importances, index=all_features).sort_values(ascending=False)

print("\nTop 10 des features les plus importantes :")
print(feature_imp.head(10))

# 5. Évaluation par sous-groupe (plan_tier, industry)
test_indices = X_test.index
df_test = df.loc[test_indices].copy()
df_test['pred'] = y_pred

print("\nPerformance par Plan (Recall) :")
plan_perf = df_test.groupby('plan_tier').apply(lambda x: recall_score(x['churn'], x['pred']))
print(plan_perf)

print("\nPerformance par Secteur (Recall) :")
industry_perf = df_test.groupby('industry').apply(lambda x: recall_score(x['churn'], x['pred']))
print(industry_perf)

# Sauvegarde des résultats pour le rapport
results = {
    'metrics': metrics,
    'feature_importance': feature_imp.head(10).to_dict(),
    'plan_performance': plan_perf.to_dict(),
    'industry_performance': industry_perf.to_dict()
}
joblib.dump(results, 'outputs/models/evaluation_results.joblib')
