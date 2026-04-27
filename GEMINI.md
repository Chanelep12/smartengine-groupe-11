# Projet smartEngine - Groupe 11

## Contexte
Nous construisons smartEngine, un système de prédiction de churn pour RavenStack, un SaaS B2B.
RavenStack commercialise une plateforme de gestion de projets pour les équipes tech (offres Starter, Growth, Enterprise).
Les données sont dans /data/raw/ — ne jamais les modifier.

## Objectifs du projet
- Analyser et nettoyer les données clients
- Identifier les signaux comportementaux précurseurs du churn
- Construire un modèle de scoring prédictif
- Déployer un dashboard interactif pour les équipes Customer Success
- Automatiser des alertes pour les comptes à risque élevé

## Dataset (5 fichiers CSV dans /data/raw/)
- accounts.csv : données des comptes clients ~5 000 lignes
- subscriptions.csv : historique des abonnements ~5 000 lignes
- feature_usage.csv : utilisation mensuelle des fonctionnalités ~60 000 lignes
- support_tickets.csv : tickets de support ~15 000 lignes
- churn_events.csv : dates et motifs de résiliation ~1 200 lignes

## Conventions
- Scripts Python -> /src/
- Rapports -> /outputs/
- Agents IA -> /.gemini/agents/
- Livrables docs -> /docs/
- Ne JAMAIS modifier /data/raw/
- Tous les rapports sont rédigés en français

## Stack technique
- Gemini CLI : orchestration des agents IA
- Python / pandas : manipulation des données
- scikit-learn : modélisation machine learning
- Streamlit : dashboard interactif
- n8n : automatisation des alertes
- GitHub : gestion du code source

## Sprint en cours
Sprint 2 - Traitement des données (30 mars 2026)

## Équipe - Groupe 11
- Scrum Master : Chanel
- Product Owner : à définir
- Développeurs IA : Marius, Morgane, Enzo
- Sprint en cours
Sprint 2 - Traitement des données (30 mars 2026)
Objectifs Sprint 2

Nettoyer les 5 fichiers CSV (valeurs manquantes, doublons, types, outliers)
Construire la table analytique (data/processed/analytics.csv)
Créer les features pour la modélisation (feature engineering)
Rédiger le rapport de nettoyage (outputs/rapport-nettoyage.md)
Ajouter la section 2 au dossier de conception

Équipe - Groupe 11

Product Owner : Chanel
Scrum Master : Morgane
Développeur IA : Marius
Développeur IA : Enzo
