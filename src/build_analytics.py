import pandas as pd
import os

def build_analytics():
    cleaned_dir = 'data/cleaned'
    processed_dir = 'data/processed'
    os.makedirs(processed_dir, exist_ok=True)
    
    # Chargement des fichiers nettoyés
    accounts = pd.read_csv(os.path.join(cleaned_dir, 'ravenstack_accounts.csv'))
    churn = pd.read_csv(os.path.join(cleaned_dir, 'ravenstack_churn_events.csv'))
    usage = pd.read_csv(os.path.join(cleaned_dir, 'ravenstack_feature_usage.csv'))
    subs = pd.read_csv(os.path.join(cleaned_dir, 'ravenstack_subscriptions.csv'))
    tickets = pd.read_csv(os.path.join(cleaned_dir, 'ravenstack_support_tickets.csv'))
    
    print("Construction de la table analytique...")
    
    # 1. Agrégation des abonnements par compte
    subs_agg = subs.groupby('account_id').agg({
        'subscription_id': 'count',
        'mrr_amount': 'sum',
        'arr_amount': 'sum',
        'seats': 'mean',
        'upgrade_flag': 'sum',
        'downgrade_flag': 'sum'
    }).rename(columns={
        'subscription_id': 'total_subscriptions',
        'mrr_amount': 'total_mrr',
        'arr_amount': 'total_arr',
        'seats': 'avg_seats',
        'upgrade_flag': 'total_upgrades',
        'downgrade_flag': 'total_downgrades'
    }).reset_index()
    
    # 2. Agrégation de l'usage
    # On a besoin de mapper subscription_id à account_id pour agréger l'usage par compte
    usage_with_account = usage.merge(subs[['subscription_id', 'account_id']], on='subscription_id', how='left')
    usage_agg = usage_with_account.groupby('account_id').agg({
        'usage_count': 'sum',
        'usage_duration_secs': 'sum',
        'error_count': 'sum'
    }).rename(columns={
        'usage_count': 'total_usage_count',
        'usage_duration_secs': 'total_usage_duration',
        'error_count': 'total_usage_errors'
    }).reset_index()
    
    # 3. Agrégation des tickets de support
    tickets_agg = tickets.groupby('account_id').agg({
        'ticket_id': 'count',
        'resolution_time_hours': 'mean',
        'satisfaction_score': 'mean',
        'escalation_flag': 'sum'
    }).rename(columns={
        'ticket_id': 'total_tickets',
        'resolution_time_hours': 'avg_resolution_time',
        'satisfaction_score': 'avg_satisfaction_score',
        'escalation_flag': 'total_escalations'
    }).reset_index()
    
    # 4. Assemblage final
    # On part de la table accounts
    analytics = accounts.merge(subs_agg, on='account_id', how='left')
    analytics = analytics.merge(usage_agg, on='account_id', how='left')
    analytics = analytics.merge(tickets_agg, on='account_id', how='left')
    
    # Variable cible Churn (0 ou 1)
    # Note: churn_flag a été corrigé lors du nettoyage pour correspondre aux événements de churn
    analytics['target_churn'] = analytics['churn_flag'].astype(int)
    
    # Remplissage des valeurs manquantes pour les comptes sans activité (ex: pas de tickets)
    fill_values = {
        'total_subscriptions': 0, 'total_mrr': 0, 'total_arr': 0, 'avg_seats': 0,
        'total_upgrades': 0, 'total_downgrades': 0,
        'total_usage_count': 0, 'total_usage_duration': 0, 'total_usage_errors': 0,
        'total_tickets': 0, 'avg_resolution_time': 0, 'avg_satisfaction_score': 0, 'total_escalations': 0
    }
    analytics = analytics.fillna(value=fill_values)
    
    # Sauvegarde
    output_path = os.path.join(processed_dir, 'analytics.csv')
    analytics.to_csv(output_path, index=False)
    
    print(f"Table analytique générée : {output_path}")
    print(f"Dimensions : {analytics.shape}")
    print(f"Distribution du churn :\n{analytics['target_churn'].value_counts()}")

if __name__ == "__main__":
    build_analytics()
