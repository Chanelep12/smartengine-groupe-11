import pandas as pd

accounts = pd.read_csv("data/raw/ravenstack_accounts.csv")
subscriptions = pd.read_csv("data/raw/ravenstack_subscriptions.csv")
churn = pd.read_csv("data/raw/ravenstack_churn_events.csv")
usage = pd.read_csv("data/raw/ravenstack_feature_usage.csv")
tickets = pd.read_csv("data/raw/ravenstack_support_tickets.csv")

print(accounts.head())
print(subscriptions.head())
print(churn.head())
print(usage.head())
print(tickets.head())

print(accounts.info())
print(subscriptions.info())
print(churn.info())
print(usage.info())
print(tickets.info())

print(accounts.describe())

print(accounts["churn_flag"].value_counts())

print(accounts.groupby("plan_tier")["churn_flag"].mean())

print(accounts["churn_flag"].value_counts())

print(accounts.groupby("plan_tier")["churn_flag"].mean())

pd.read_csv(...)