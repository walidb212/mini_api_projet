# Mini API 🛠️

Une API REST minimaliste qui expose des petits outils utiles : mathématiques, texte, conversion et validation.

## 🟢 Badge CI

[![CI](https://github.com/walidb212/mini_api_projet/actions/workflows/ci.yml/badge.svg)](https://github.com/walidb212/mini_api_projet/actions)

## Installation

```bash
# 1. Cloner le repo
git clone https://github.com/walidb212/mini_api_projet.git
cd mini_api_projet

# 2. Créer l'environnement virtuel
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# ou
.venv\Scripts\activate  # Windows

# 3. Installer les dépendances
pip install -r requirements.txt
```

## Lancement

### Local

```bash
uvicorn app.main:app --reload
```

L'API écoute sur `http://localhost:8000`

### Docker

```bash
docker build -t mini-api .
docker run -p 8000:8000 mini-api
```

## Utilisation

### Santé
```bash
curl "http://localhost:8000/sante"
# {"statut": "ok"}
```

### Math

**Factorielle**
```bash
curl "http://localhost:8000/factorielle/5"
# {"n": 5, "factorielle": 120}
```

**Est premier**
```bash
curl "http://localhost:8000/est_premier/17"
# {"n": 17, "est_premier": true}
```

**PGCD**
```bash
curl "http://localhost:8000/pgcd/48/18"
# {"a": 48, "b": 18, "pgcd": 6}
```

### Conversion

**Celsius → Fahrenheit**
```bash
curl "http://localhost:8000/celsius_fahrenheit/100"
# {"celsius": 100, "fahrenheit": 212}
```

### Validation

**Email**
```bash
curl "http://localhost:8000/email_valide/test@example.com"
# {"email": "test@example.com", "valide": true}
```

## Tests

Lancer les tests avec couverture :

```bash
pytest tests/ -v --cov=app --cov-report=html
```

Vérifier la qualité du code :

```bash
ruff check app/ tests/
```

## Contribuer

### Branches

- Une issue = une branche : `feat/N-nom-de-la-tache`
- Exemple : `feat/17-est_premier`

### Commits

- Messages atomiques et explicites
- Format : `feat(module): description courte`
- Exemple : `feat(math): ajoute est_premier + tests`

### Pull Request

1. Crée une branche depuis `main`
2. Implémente la feature + tests
3. Vérifie : `pytest` + `ruff check`
4. Soumet la PR avec description
5. Attends l'approbation d'un autre

## Équipe

- **Jérémie Brissière** - Développeur principal
- **Walid Bouzidane** - Développeur principal
- **Dylan RAMI** - Développeur principal

