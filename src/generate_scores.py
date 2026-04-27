import pandas as pd
import joblib
import os

# 1. Chargement des données et du modèle
df = pd.read_csv('data/processed/analytics.csv')
model = joblib.load('outputs/models/churn_model.joblib')

# 2. Préparation des features (exclure account_id etc.)
drop_cols = ['churn', 'target_churn', 'account_id', 'account_name', 'churn_flag', 'signup_date']
X = df.drop(columns=[c for c in drop_cols if c in df.columns])

# 3. Génération des probabilités (scores)
# La classe 1 est le churn
scores = model.predict_proba(X)[:, 1]

# 4. Création du DataFrame de sortie
results = pd.DataFrame({
    'account_id': df['account_id'],
    'churn_score': scores
})

# 5. Définition des niveaux de risque
def get_risk_level(score):
    if score >= 0.70:
        return 'high'
    elif score >= 0.40:
        return 'medium'
    else:
        return 'low'

results['risk_level'] = results['churn_score'].apply(get_risk_level)

# 6. Sauvegarde
os.makedirs('outputs', exist_ok=True)
results.to_csv('outputs/scores.csv', index=False)
print("Scores générés et sauvegardés dans outputs/scores.csv")
print("\nRépartition des niveaux de risque :")
print(results['risk_level'].value_counts())
