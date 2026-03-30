import pandas as pd
import numpy as np
import os
from datetime import datetime

def build_features():
    # Today's date from session context
    today = datetime(2026, 3, 30)
    
    # Load analytics and raw cleaned data
    analytics = pd.read_csv('data/processed/analytics.csv')
    accounts = pd.read_csv('data/cleaned/ravenstack_accounts.csv')
    usage = pd.read_csv('data/cleaned/ravenstack_feature_usage.csv')
    subs = pd.read_csv('data/cleaned/ravenstack_subscriptions.csv')
    tickets = pd.read_csv('data/cleaned/ravenstack_support_tickets.csv')
    
    # Convert dates
    accounts['signup_date'] = pd.to_datetime(accounts['signup_date'])
    usage['usage_date'] = pd.to_datetime(usage['usage_date'])
    # Dataset ends on 2024-12-31 based on exploration
    max_data_date = datetime(2024, 12, 31)
    
    print("Ajout des variables dérivées...")
    
    # 1. Ancienneté en mois (basé sur today 2026-03-30)
    # On calcule la différence en jours et on divise par 30
    analytics['tenure_months'] = analytics['signup_date'].apply(lambda x: (today - pd.to_datetime(x)).days / 30.44).round(1)
    
    # 2. Ratio tickets critiques (urgent + high)
    # On groupe par account_id
    critical_tickets = tickets[tickets['priority'].isin(['urgent', 'high'])].groupby('account_id').size()
    total_tickets = tickets.groupby('account_id').size()
    critical_ratio = (critical_tickets / total_tickets).fillna(0).reset_index(name='critical_ticket_ratio')
    analytics = analytics.merge(critical_ratio, on='account_id', how='left').fillna({'critical_ticket_ratio': 0})
    
    # 3. Ratio jours actifs (jours avec usage / jours totaux depuis signup jusqu'à max_data_date)
    # Mapper sub_id -> account_id pour l'usage
    usage_with_account = usage.merge(subs[['subscription_id', 'account_id']], on='subscription_id', how='left')
    active_days = usage_with_account.groupby('account_id')['usage_date'].nunique().reset_index(name='active_days')
    analytics = analytics.merge(active_days, on='account_id', how='left').fillna({'active_days': 0})
    
    # Jours possibles depuis signup jusqu'à max_data_date (fin des données d'usage)
    def calc_potential_days(row):
        signup = pd.to_datetime(row['signup_date'])
        # Si signup est après la fin des données (peu probable ici), on met 1 pour éviter div par 0
        days = (max_data_date - signup).days
        return max(days, 1)
    
    potential_days = accounts.apply(calc_potential_days, axis=1)
    analytics['active_days_ratio'] = (analytics['active_days'] / potential_days).round(3)
    analytics.drop(columns=['active_days'], inplace=True)
    
    # 4. Tendance d'usage sur 3 mois (Trimestre 4 2024 vs Trimestre 3 2024)
    # On utilise les 3 derniers mois du dataset (Oct-Nov-Dec 2024) vs les 3 précédents (Jul-Aug-Sep 2024)
    q4_usage = usage_with_account[(usage_with_account['usage_date'] >= '2024-10-01') & (usage_with_account['usage_date'] <= '2024-12-31')]
    q3_usage = usage_with_account[(usage_with_account['usage_date'] >= '2024-07-01') & (usage_with_account['usage_date'] <= '2024-09-30')]
    
    q4_agg = q4_usage.groupby('account_id')['usage_count'].sum().reset_index(name='usage_q4')
    q3_agg = q3_usage.groupby('account_id')['usage_count'].sum().reset_index(name='usage_q3')
    
    analytics = analytics.merge(q4_agg, on='account_id', how='left').fillna({'usage_q4': 0})
    analytics = analytics.merge(q3_agg, on='account_id', how='left').fillna({'usage_q3': 0})
    
    # Tendance = ratio (Q4 / Q3). On ajoute 1 au dénominateur pour éviter division par zéro
    analytics['usage_trend_3m'] = (analytics['usage_q4'] / (analytics['usage_q3'] + 1)).round(3)
    analytics.drop(columns=['usage_q4', 'usage_q3'], inplace=True)
    
    # Sauvegarde
    analytics.to_csv('data/processed/analytics.csv', index=False)
    print("Variables dérivées ajoutées avec succès.")
    print(f"Colonnes finales : {analytics.columns.tolist()}")

if __name__ == "__main__":
    build_features()
