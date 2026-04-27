# Brief Client — Projet smartEngine

## 1. Qui est le client ?

**RavenStack** est une entreprise SaaS B2B (Software as a Service Business-to-Business) qui commercialise une plateforme de gestion de projets destinée aux équipes tech. Elle propose trois niveaux d'abonnement :

- **Starter** : pour les petites équipes
- **Growth** : pour les équipes en croissance
- **Enterprise** : pour les grandes organisations

Son modèle économique repose entièrement sur des abonnements récurrents (MRR — Monthly Recurring Revenue), ce qui signifie que chaque client perdu représente une perte directe et prévisible de revenus.

---

## 2. Quel est son problème ?

RavenStack perd chaque mois une partie de ses clients : c'est ce qu'on appelle le **churn** (ou taux d'attrition). Chaque résiliation d'abonnement réduit le MRR et génère un manque à gagner difficile à anticiper sans outil de prédiction.

Aujourd'hui, les équipes **Customer Success** (les collaborateurs chargés de la relation client après la vente) ne savent pas à l'avance quels clients sont sur le point de résilier. Elles agissent en réaction, trop tard, plutôt qu'en prévention.

Le problème est donc double :
1. **Pas de visibilité anticipée** sur les clients à risque
2. **Pas de système d'alerte** permettant d'intervenir au bon moment

---

## 3. Ce que nous allons construire

Nous développons **smartEngine**, un système intelligent de prédiction du churn composé de trois briques :

1. **Un modèle de scoring prédictif** : à partir des données comportementales des clients (utilisation des fonctionnalités, tickets de support, historique d'abonnement), le modèle calcule pour chaque compte une probabilité de résiliation.

2. **Un dashboard interactif** (construit avec Streamlit) : accessible aux équipes Customer Success, il affiche en temps réel les comptes classés par niveau de risque (faible, moyen, élevé).

3. **Un système d'alertes automatisées** (via n8n) : lorsqu'un compte dépasse un seuil de risque défini, une alerte est envoyée automatiquement à l'équipe concernée.

---

## 4. Données disponibles

RavenStack met à notre disposition un dataset synthétique de 5 fichiers CSV :

| Fichier | Contenu | Volume |
|---|---|---|
| accounts.csv | Profil des comptes clients | ~5 000 lignes |
| subscriptions.csv | Historique des abonnements | ~5 000 lignes |
| feature_usage.csv | Utilisation des fonctionnalités | ~60 000 lignes |
| support_tickets.csv | Tickets de support | ~15 000 lignes |
| churn_events.csv | Résiliations constatées | ~1 200 lignes |

---

## 5. Critères de succès

Le projet sera considéré comme réussi si les trois critères mesurables suivants sont atteints :

1. **Précision du modèle ≥ 75 %** : le modèle de scoring identifie correctement au moins 75 % des clients qui vont effectivement churner dans les 30 jours.

2. **Dashboard opérationnel** : les équipes Customer Success peuvent consulter en moins de 2 clics la liste des comptes à risque élevé, avec le score et les signaux d'alerte associés.

3. **Alertes automatisées fonctionnelles** : pour tout compte dont le score de churn dépasse 70 %, une notification est déclenchée automatiquement sans intervention manuelle.

---

## 6. Contraintes

- **RGPD** : les données personnelles des clients sont traitées conformément au Règlement Général sur la Protection des Données. Le scoring respecte l'article 22 (décisions automatisées) : les résultats sont utilisés comme aide à la décision humaine, pas comme décision automatique définitive.
- **Éthique** : le score de churn est un outil de rétention bienveillante, pas de discrimination commerciale.
- **Technique** : la stack est imposée (Python, scikit-learn, Streamlit, n8n, Gemini CLI).
