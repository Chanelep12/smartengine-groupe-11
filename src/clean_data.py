import pandas as pd
import os

def clean_data():
    raw_dir = 'data/raw'
    output_dir = 'outputs'
    os.makedirs(output_dir, exist_ok=True)
    
    report = "# Rapport de Nettoyage des Données\n\n"
    
    files = {
        'accounts': 'ravenstack_accounts.csv',
        'churn': 'ravenstack_churn_events.csv',
        'usage': 'ravenstack_feature_usage.csv',
        'subs': 'ravenstack_subscriptions.csv',
        'tickets': 'ravenstack_support_tickets.csv'
    }
    
    dfs = {}
    for key, filename in files.items():
        dfs[key] = pd.read_csv(os.path.join(raw_dir, filename))
        
    # --- 1. Accounts ---
    report += "## 1. ravenstack_accounts.csv\n"
    before_count = len(dfs['accounts'])
    # Incohérence churn_flag identifiée
    churned_ids = set(dfs['churn']['account_id'])
    old_churn_count = dfs['accounts']['churn_flag'].sum()
    dfs['accounts']['churn_flag'] = dfs['accounts']['account_id'].isin(churned_ids)
    new_churn_count = dfs['accounts']['churn_flag'].sum()
    
    report += f"- **Problèmes identifiés** : Incohérence du `churn_flag` (seulement {old_churn_count} marqués alors que {len(churned_ids)} événements existent).\n"
    report += "- **Stratégie** : Recalculer `churn_flag` basé sur le fichier `churn_events`.\n"
    report += f"- **Résultat** : {before_count} lignes. Churn flag corrigé de {old_churn_count} à {new_churn_count}.\n\n"

    # --- 2. Churn Events ---
    report += "## 2. ravenstack_churn_events.csv\n"
    before_nulls = dfs['churn']['feedback_text'].isnull().sum()
    dfs['churn']['feedback_text'] = dfs['churn']['feedback_text'].fillna('No feedback')
    
    report += f"- **Problèmes identifiés** : Valeurs manquantes dans `feedback_text` ({before_nulls}).\n"
    report += "- **Stratégie** : Remplacer les valeurs nulles par 'No feedback'.\n"
    report += f"- **Résultat** : {before_nulls} valeurs remplacées.\n\n"

    # --- 3. Feature Usage ---
    report += "## 3. ravenstack_feature_usage.csv\n"
    before_count = len(dfs['usage'])
    before_dupes = dfs['usage']['usage_id'].duplicated().sum()
    dfs['usage'] = dfs['usage'].drop_duplicates(subset=['usage_id'])
    after_count = len(dfs['usage'])
    
    report += f"- **Problèmes identifiés** : Doublons dans `usage_id` ({before_dupes}).\n"
    report += "- **Stratégie** : Supprimer les lignes avec des IDs de consommation en double.\n"
    report += f"- **Résultat** : Avant {before_count} -> Après {after_count}.\n\n"

    # --- 4. Subscriptions ---
    report += "## 4. ravenstack_subscriptions.csv\n"
    before_null_end = dfs['subs']['end_date'].isnull().sum()
    # end_date null signifie abonnement actif, on laisse tel quel mais on assure le type datetime
    dfs['subs']['start_date'] = pd.to_datetime(dfs['subs']['start_date'])
    dfs['subs']['end_date'] = pd.to_datetime(dfs['subs']['end_date'])
    
    report += f"- **Problèmes identifiés** : Dates au format texte, `end_date` vide ({before_null_end}) pour les abonnements actifs.\n"
    report += "- **Stratégie** : Conversion en datetime. Les `NaT` en `end_date` sont conservés comme indicateurs d'abonnements actifs.\n"
    report += f"- **Résultat** : Conversion de type effectuée.\n\n"

    # --- 5. Support Tickets ---
    report += "## 5. ravenstack_support_tickets.csv\n"
    before_null_score = dfs['tickets']['satisfaction_score'].isnull().sum()
    mean_score = dfs['tickets']['satisfaction_score'].mean()
    dfs['tickets']['satisfaction_score'] = dfs['tickets']['satisfaction_score'].fillna(mean_score)
    
    report += f"- **Problèmes identifiés** : Valeurs manquantes dans `satisfaction_score` ({before_null_score}).\n"
    report += "- **Stratégie** : Imputation par la moyenne ({:.2f}).\n".format(mean_score)
    report += f"- **Résultat** : {before_null_score} valeurs imputées.\n\n"

    # Sauvegarde des fichiers nettoyés
    clean_data_dir = 'data/cleaned'
    os.makedirs(clean_data_dir, exist_ok=True)
    for key, df in dfs.items():
        df.to_csv(os.path.join(clean_data_dir, files[key]), index=False)
        
    # Sauvegarde du rapport
    with open(os.path.join(output_dir, 'rapport-nettoyage.md'), 'w', encoding='utf-8') as f:
        f.write(report)
    
    print("Nettoyage terminé. Rapport généré dans outputs/rapport-nettoyage.md")

if __name__ == "__main__":
    clean_data()
