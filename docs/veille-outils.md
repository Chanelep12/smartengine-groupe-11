# Rapport de veille outils — Projet smartEngine

## Introduction

Ce rapport présente les six outils de la stack technique imposée pour le projet smartEngine. Pour chacun, nous documentons son rôle dans le projet, ses avantages, ses limites et ses alternatives.

---

## 1. Gemini CLI

### Présentation
Gemini CLI est un outil en ligne de commande développé par Google qui permet d'interagir avec un agent IA (Gemini) directement depuis le terminal. Il peut lire, créer et modifier des fichiers de manière autonome à partir d'instructions rédigées en langage naturel.

### Rôle dans le projet
Gemini CLI est l'outil d'orchestration central du projet. Il lit le fichier GEMINI.md (contexte permanent) et les agents définis dans `.gemini/agents/`, génère du code Python, l'exécute et produit les résultats. Il nous permet de diriger le projet sans coder directement.

### Avantages
- Aucune compétence en programmation requise pour utiliser les agents
- Automatisation des tâches répétitives (exploration, nettoyage, modélisation)
- Mémoire de contexte via GEMINI.md à chaque démarrage
- Agents réutilisables et partageables entre membres de l'équipe

### Limites
- Nécessite une connexion internet et un compte Google
- Résultats variables selon la qualité des instructions rédigées
- Pas de mémoire entre deux sessions sans GEMINI.md bien renseigné
- Dépendance à un fournisseur externe (Google)

### Alternatives
- GitHub Copilot CLI
- OpenAI Codex (via API)
- Claude Code (Anthropic)

**Source :** [geminicli.com](https://geminicli.com)

---

## 2. Python / pandas

### Présentation
Python est un langage de programmation généraliste, très utilisé en data science. Pandas est une bibliothèque Python qui fournit des structures de données (DataFrames) et des outils d'analyse pour manipuler des tableaux de données de manière efficace.

### Rôle dans le projet
Python est le langage de base de tout le projet. Pandas est utilisé pour charger les 5 fichiers CSV, les nettoyer (valeurs manquantes, doublons, types incorrects), les fusionner et créer de nouvelles variables (feature engineering) nécessaires à la modélisation.

### Avantages
- Langage le plus répandu en data science (large communauté, nombreuses ressources)
- Pandas permet de manipuler des millions de lignes rapidement
- Intégration native avec scikit-learn et les outils de visualisation
- Open source et gratuit

### Limites
- Pandas charge les données en mémoire vive (RAM) : peut poser problème pour de très grands volumes
- Courbe d'apprentissage si on ne connaît pas Python
- Moins performant que SQL pour certaines opérations sur très grandes bases

### Alternatives
- R (tidyverse / dplyr) pour la manipulation de données
- Polars (alternative moderne et plus rapide à pandas)
- SQL pour les requêtes sur bases relationnelles

**Source :** [pandas.pydata.org](https://pandas.pydata.org)

---

## 3. scikit-learn

### Présentation
Scikit-learn est une bibliothèque Python open source dédiée au machine learning. Elle propose des algorithmes de classification, régression, clustering, ainsi que des outils de prétraitement, de sélection de modèles et d'évaluation des performances.

### Rôle dans le projet
Scikit-learn est utilisé pour construire le modèle de scoring prédictif du churn. Nous entraînerons des modèles de classification (par exemple une régression logistique ou une forêt aléatoire) sur les données historiques de RavenStack, puis nous évaluerons leur performance (précision, rappel, AUC-ROC).

### Avantages
- Documentation très complète et pédagogique
- Large choix d'algorithmes disponibles en quelques lignes de code
- Pipeline intégré (prétraitement + modèle + évaluation) facilement reproductible
- Standard de l'industrie pour le machine learning classique

### Limites
- Pas adapté au deep learning (utiliser PyTorch ou TensorFlow pour cela)
- Ne gère pas nativement les données en streaming ou très volumineuses
- Nécessite des données propres et bien préparées en amont

### Alternatives
- XGBoost / LightGBM pour des modèles à gradient boosting très performants
- PyCaret pour une approche AutoML low-code
- H2O.ai pour du machine learning distribué

**Source :** [scikit-learn.org](https://scikit-learn.org)

---

## 4. Streamlit

### Présentation
Streamlit est un framework Python open source qui permet de créer des interfaces web interactives (dashboards, applications de data visualisation) en Python pur, sans avoir besoin de connaissances en HTML, CSS ou JavaScript.

### Rôle dans le projet
Streamlit est utilisé pour construire le dashboard interactif destiné aux équipes Customer Success de RavenStack. Ce dashboard affichera les scores de churn par compte, les graphiques d'évolution du risque et les alertes pour les comptes prioritaires.

### Avantages
- Création d'une interface web complète en quelques dizaines de lignes Python
- Mise à jour en temps réel lors des modifications du code
- Déploiement facile sur Streamlit Cloud
- Nombreux composants interactifs natifs (filtres, graphiques, tableaux)

### Limites
- Moins flexible qu'un framework web complet (React, Vue.js) pour des interfaces très personnalisées
- Performance limitée pour de très nombreux utilisateurs simultanés
- Chaque interaction recharge toute l'application par défaut

### Alternatives
- Dash (Plotly) pour des dashboards analytiques avancés
- Gradio pour des démos de modèles ML rapides
- Flask / FastAPI + React pour une application web complète sur mesure

**Source :** [streamlit.io](https://streamlit.io)

---

## 5. n8n

### Présentation
n8n est un outil d'automatisation de workflows open source et auto-hébergeable. Il permet de connecter des applications entre elles et d'automatiser des tâches sans coder, via une interface visuelle de type "nœuds et connexions".

### Rôle dans le projet
n8n est utilisé pour automatiser les alertes churn. Lorsque le modèle détecte un compte à risque élevé (score > 70 %), n8n déclenche automatiquement l'envoi d'une notification (email, Slack, etc.) vers l'équipe Customer Success concernée, sans intervention manuelle.

### Avantages
- Open source et auto-hébergeable (maîtrise des données, pas de dépendance cloud)
- Interface visuelle intuitive pour créer des workflows complexes
- Connecteurs disponibles pour des centaines d'applications (Gmail, Slack, HubSpot…)
- Version cloud disponible si on ne veut pas gérer l'hébergement

### Limites
- Nécessite un serveur pour l'auto-hébergement (configuration technique)
- Moins connu que Zapier ou Make, donc moins de ressources en français
- Certains connecteurs avancés nécessitent la version payante

### Alternatives
- Zapier (payant, plus simple à prendre en main)
- Make (ex-Integromat) pour des automatisations avancées
- Apache Airflow pour des pipelines de données complexes en Python

**Source :** [n8n.io](https://n8n.io)

---

## 6. GitHub

### Présentation
GitHub est une plateforme web de gestion de code source basée sur Git (système de contrôle de versions). Elle permet de stocker du code, de collaborer à plusieurs sur un même projet via des branches, et de suivre l'historique de toutes les modifications.

### Rôle dans le projet
GitHub est le dépôt central du projet smartEngine. Il héberge l'ensemble du travail : scripts Python, agents Gemini CLI, rapports, dossier de conception. Il permet à tous les membres de l'équipe de travailler en parallèle sur leurs branches personnelles et de fusionner le travail validé dans la branche `main`.

### Avantages
- Référence absolue de l'industrie pour la gestion de code en équipe
- Historique complet de toutes les modifications (qui a fait quoi, quand)
- GitHub Projects intégré pour gérer le backlog Scrum
- Gratuit pour les dépôts privés (jusqu'à un certain nombre de collaborateurs)

### Limites
- Courbe d'apprentissage pour les commandes Git (clone, branch, merge, push…)
- Les conflits de fusion (merge conflicts) peuvent être difficiles à résoudre pour les débutants
- Ne convient pas pour stocker des fichiers très volumineux (données CSV > 100 Mo)

### Alternatives
- GitLab (alternative open source auto-hébergeable)
- Bitbucket (intégration native avec Jira/Atlassian)
- Azure DevOps pour les environnements Microsoft

**Source :** [docs.github.com](https://docs.github.com/fr/get-started)
