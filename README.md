# Mini API 🛠️

[![CI](https://github.com/walidb212/mini_api_projet/actions/workflows/ci.yml/badge.svg)](https://github.com/walidb212/mini_api_projet/actions)


Une API REST minimaliste qui expose des petits outils utiles : mathématiques, texte, conversion et validation.

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

# Image publiée (après le tag v1.0.0)

```
docker run -p 8000:8000 ghcr.io/walidb212/mini_api_projet:v1.0.0

# Ou en local

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

**Km → Miles**
```bash
curl "http://localhost:8000/km_miles/160"
# {"km": 160.0, "miles": 99.41936}
```

**Euros → Devise**
```bash
curl "http://localhost:8000/euros_devise/100/USD"
# {"montant": 100.0, "devise": "USD", "resultat": 108.0}
```

### Validation

**Email**
```bash
curl "http://localhost:8000/email_valide/test@example.com"
# {"email": "test@example.com", "valide": true}
```

**Code postal**
```bash
curl "http://localhost:8000/code_postal/75001"
# {"code": "75001", "valide": true}
```

### Texte

**Inverse texte**
```bash
curl "http://localhost:8000/inverser?texte=hello"
# {"texte": "hello", "inverse": "olleh"}
```

**Compter Voyelles**
```bash
curl "http://localhost:8000/compter_voyelles?texte=école"
# {"texte": "école", "voyelles": 3}
```

**Est Palindrome**
```bash
curl "http://localhost:8000/est_palindrome?texte=kayak"
# {"texte": "kayak", "est_palindrome": true}
```

## Tests

Lancer les tests avec couverture :

```bash
pytest --cov=app --cov-fail-under=80
```

Vérifier la qualité du code :

```bash
ruff check .
```

## Contribuer

### Branches

Une issue = une branche avec le préfixe correspondant au type :

| Type | Préfixe | Exemple |
|------|---------|---------|
| Nouvelle fonctionnalité | `feat/N-…` | `feat/17-est_premier` |
| Bug fix | `fix/N-…` | `fix/12-erreur-pgcd` |
| Tests | `test/N-…` | `test/19-ajouter-tests` |
| Documentation | `docs/N-…` | `docs/14-readme` |
| Refactoring | `refactor/N-…` | `refactor/8-optimiser-math` |
| CI/CD | `ci/N-…` | `ci/6-github-actions` |
| Maintenance | `chore/N-…` | `chore/3-deps-update` |

### Commits

Messages atomiques et explicites avec le bon type :

**Types disponibles :** `feat`, `fix`, `test`, `docs`, `refactor`, `ci`, `chore`

**Exemples :**
- `feat(math): ajoute est_premier + tests`
- `fix(convert): corrige conversion celsius`
- `docs(readme): rédige le README complet`
- `test(math): ajoute tests pgcd`
- `ci(github): configure ruff et pytest`

### Pull Request

1. Crée une branche depuis `main`
2. Implémente la feature + tests
3. Vérifie : `pytest` + `ruff check`
4. Soumet la PR avec description
5. Attends l'approbation d'un autre

## Équipe

- **Jérémie Brissière** - module math, README, modèle de PR
- **Walid Bouzidane** - structure du projet, /sante, erreurs.py, module texte, CI et Docker/Deploy
- **Dylan RAMI** - modules conversion et validation

