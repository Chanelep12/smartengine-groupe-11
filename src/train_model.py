import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score
import joblib
import os

# 1. Chargement des données
df = pd.read_csv('data/processed/analytics.csv')

# Affichage du ratio churn
if 'target_churn' in df.columns:
    df = df.rename(columns={'target_churn': 'churn'})

print("Ratio Churn / Non-Churn :")
print(df['churn'].value_counts(normalize=True))

# 2. Séparation Features / Target
# On exclut account_id et les colonnes non-prédictives ou redondantes
drop_cols = ['churn', 'account_id', 'account_name', 'churn_flag', 'signup_date']
X = df.drop(columns=[c for c in drop_cols if c in df.columns])
y = df['churn']

# 3. Identification des colonnes
categorical_cols = X.select_dtypes(include=['object', 'category', 'bool']).columns.tolist()
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()

# 4. Prétraitement
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_cols)
    ]
)

# 5. Split Train/Test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42
)

# 6. Entraînement des modèles
ratio_churn = y_train.mean()
ratio_non_churn = 1 - ratio_churn
scale_pos_weight = ratio_non_churn / ratio_churn

models = {
    'Logistic Regression': LogisticRegression(class_weight='balanced', random_state=42, max_iter=1000),
    'Random Forest': RandomForestClassifier(class_weight='balanced', random_state=42, n_estimators=100),
}

best_recall = -1
best_model = None
best_model_name = ""

print("\nEntraînement des modèles...")
for name, model in models.items():
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', model)
    ])
    pipeline.fit(X_train, y_train)
    
    y_pred = pipeline.predict(X_test)
    recall = recall_score(y_test, y_pred)
    
    print(f"{name} - Recall: {recall:.4f}")
    
    if recall > best_recall:
        best_recall = recall
        best_model = pipeline
        best_model_name = name

# 7. Sauvegarde du meilleur modèle
print(f"\nMeilleur modèle retenu : {best_model_name} (Recall: {best_recall:.4f})")
os.makedirs('outputs/models', exist_ok=True)
joblib.dump(best_model, 'outputs/models/churn_model.joblib')
print("Modèle sauvegardé dans outputs/models/churn_model.joblib")
