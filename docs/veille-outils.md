# Veille outils — Projet smartEngine

## 1. Gemini CLI

**Présentation** : Outil en ligne de commande développé par Google permettant
d'interagir avec un agent IA directement depuis le terminal.

**Rôle dans le projet** : Orchestrer les agents IA qui génèrent et exécutent
le code Python d'analyse et de modélisation.

**Avantages** : Gratuit avec un compte Google, capable de lire/créer/modifier
des fichiers de manière autonome, intégration directe dans le workflow Git.

**Limites** : Nécessite Node.js, dépendant de la connexion internet,
pas de mémoire entre deux sessions sans fichier GEMINI.md.

**Alternatives** : Claude Code, ChatGPT (interface web), GitHub Copilot.

---

## 2. Python / pandas

**Présentation** : Python est le langage de programmation le plus utilisé
en data science. pandas est sa bibliothèque principale de manipulation
de données tabulaires.

**Rôle dans le projet** : Charger, nettoyer et transformer les 5 fichiers
CSV du dataset RavenStack pour préparer la modélisation.

**Avantages** : Très répandu, grande communauté, documentation abondante,
compatible avec toutes les bibliothèques de machine learning.

**Limites** : Peut être lent sur de très grands volumes de données,
courbe d'apprentissage pour les débutants.

**Alternatives** : R, Julia, Polars (plus rapide que pandas).

---

## 3. scikit-learn

**Présentation** : Bibliothèque Python de machine learning open source,
la plus utilisée pour les projets de classification et de régression.

**Rôle dans le projet** : Construire et évaluer le modèle de scoring
prédictif de churn (régression logistique, random forest, etc.).

**Avantages** : Simple d'utilisation, nombreux algorithmes disponibles,
bonne documentation, compatible avec pandas.

**Limites** : Moins adapté au deep learning, pas optimisé pour le
temps réel.

**Alternatives** : XGBoost, LightGBM, TensorFlow, PyTorch.

---

## 4. Streamlit

**Présentation** : Framework Python open source permettant de créer
des interfaces web interactives sans connaissances en développement web.

**Rôle dans le projet** : Déployer le dashboard interactif de visualisation
des scores de churn à destination des équipes Customer Success.

**Avantages** : Très rapide à mettre en place, entièrement en Python,
déploiement facile sur le cloud.

**Limites** : Moins flexible qu'une vraie application web, performances
limitées avec de nombreux utilisateurs simultanés.

**Alternatives** : Dash (Plotly), Gradio, Flask + React.

---

## 5. n8n

**Présentation** : Outil d'automatisation de workflows open source
et auto-hébergeable, similaire à Zapier ou Make.

**Rôle dans le projet** : Automatiser les alertes envoyées aux équipes
Customer Success lorsqu'un compte passe en zone de risque élevé.

**Avantages** : Open source, auto-hébergeable, interface visuelle
intuitive, nombreuses intégrations disponibles.

**Limites** : Nécessite un serveur pour l'auto-hébergement, moins
de connecteurs que Zapier en version gratuite.

**Alternatives** : Zapier, Make (ex-Integromat), Apache Airflow.

---

## 6. GitHub

**Présentation** : Plateforme de gestion de code source basée sur Git,
permettant la collaboration entre développeurs.

**Rôle dans le projet** : Héberger le dépôt du projet, gérer les branches
de chaque membre, centraliser les livrables et assurer le suivi des versions.

**Avantages** : Standard de l'industrie, gratuit pour les dépôts privés,
intégration avec VS Code, historique complet des modifications.

**Limites** : Courbe d'apprentissage pour les débutants avec Git,
interface parfois complexe.

**Alternatives** : GitLab, Bitbucket, Azure DevOps.