# smartEngine — Groupe 11

Système de prédiction de churn pour RavenStack, un SaaS B2B.  
Projet réalisé dans le cadre du MSc2 Manager Data Marketing — INSEEC.

## L'équipe

### Sprint 3 (rôles actuels)
| Rôle | Membre |
|---|---|
| Product Owner | Morgane |
| Scrum Master | Marius |
| Développeur IA | Chanel |
| Développeur IA | Enzo |

### Sprint 2
| Rôle | Membre |
|---|---|
| Product Owner | Chanel |
| Scrum Master | Morgane |
| Développeur IA | Marius |
| Développeur IA | Enzo |

### Sprint 1
| Rôle | Membre |
|---|---|
| Scrum Master | Chanel |
| Product Owner | Enzo |
| Développeur IA | Marius |
| Développeur IA | Morgane |

## Stack technique
- Gemini CLI — orchestration des agents IA
- Python / pandas — manipulation des données
- scikit-learn — modélisation prédictive
- XGBoost / LightGBM — gradient boosting
- SHAP — interprétabilité du modèle
- imbalanced-learn — gestion du déséquilibre des classes
- joblib — sauvegarde du modèle
- Streamlit — dashboard interactif
- n8n — automatisation des alertes
- GitHub — gestion du code source

## Structure du dépôt
```
smartengine-groupe-11/
├── .gemini/agents/
│   ├── data-explorer.md       # Agent Sprint 1
│   ├── data-engineer.md       # Agent Sprint 2
│   └── model-trainer.md       # Agent Sprint 3
├── data/
│   ├── raw/                   # CSV RavenStack bruts
│   ├── cleaned/               # CSV nettoyés
│   └── processed/
│       └── analytics.csv      # Table analytique (Sprint 2)
├── docs/
│   ├── standups/              # Comptes-rendus daily & sprint reviews
│   ├── dossier-conception.docx
│   └── ...
├── outputs/
│   ├── rapport-nettoyage.md   # Sprint 2
│   ├── rapport-modele.md      # Sprint 3
│   ├── scores.csv             # Sprint 3 — scores de churn par compte
│   └── models/
│       └── churn_model.joblib # Sprint 3 — modèle entraîné
├── src/
│   ├── clean_data.py          # Sprint 2
│   ├── build_features.py      # Sprint 2
│   ├── build_analytics.py     # Sprint 2
│   ├── train_model.py         # Sprint 3
│   ├── evaluate_model.py      # Sprint 3
│   └── generate_scores.py     # Sprint 3
├── GEMINI.md
└── README.md
```

## Backlog
🔗 [Backlog Sprint 1, 2 & 3 — Trello](https://trello.com/invite/b/69ca4324cef1c613da43eaab/ATTI84ab81071c736b7ceb95fc760536d328F50F6CB3/smartengine-groupe-11)

## Sprints
| Sprint | Dates | Thème | Statut |
|---|---|---|---|
| Sprint 1 | 9-11 mars 2026 | Découverte et mise en place | ✅ Terminé |
| Sprint 2 | 30 mars 2026 | Traitement des données | ✅ Terminé |
| Sprint 3 | 27 avril 2026 | Modélisation prédictive | 🔄 En cours |
| Sprint 4 | 26-29 mai 2026 | Déploiement et soutenance | ⏳ À venir |