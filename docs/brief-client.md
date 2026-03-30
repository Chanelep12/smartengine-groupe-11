# Brief client — Projet smartEngine

## Le client : RavenStack

RavenStack est une entreprise qui commercialise un logiciel de gestion
de projets en mode SaaS B2B (Software as a Service). Cela signifie que
le logiciel est accessible via internet par abonnement, sans installation
locale. Il s'adresse aux équipes techniques et propose trois niveaux
d'offre : Starter, Growth et Enterprise.

## Le problème

Chaque mois, une partie des clients de RavenStack résilie son abonnement.
C'est ce qu'on appelle le churn. Chaque résiliation entraîne une perte de
MRR (Monthly Recurring Revenue), c'est-à-dire le chiffre d'affaires
mensuel prévisible. Sans outil de prédiction, ces départs sont difficiles
à anticiper et les équipes Customer Success ne peuvent pas agir à temps.

## Ce que nous allons construire

Nous développons smartEngine, un système de prédiction de churn qui
permet à RavenStack d'identifier en avance les clients susceptibles de
résilier. Le système repose sur l'analyse des données clients existantes
(utilisation du produit, historique d'abonnement, tickets support) et
produit un score de risque par compte.

Ce score sera accessible via un dashboard interactif destiné aux équipes
Customer Success, avec des alertes automatiques pour les comptes à risque
élevé.

## Critères de succès

1. Le modèle de prédiction atteint un taux de précision d'au moins 75 %
   sur les données de test.
2. Le dashboard permet d'identifier en moins de 2 minutes les comptes
   les plus à risque sur le mois en cours.
3. Les alertes automatiques sont envoyées dans les 24 heures suivant la
   détection d'un compte à risque élevé.