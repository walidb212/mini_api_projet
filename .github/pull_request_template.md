📝 Description

Décrivez les changements que vous apportez en quelques phrases.

🎯 Type de changement
 Nouvelle fonctionnalité (ajout d'une nouvelle fonction ou module)
 Correction de bug
 Amélioration de performance
 Refactorisation
 Documentation
📋 Checklist
Code
 J'ai suivi le style de code du projet (Ruff ✓)
 J'ai ajouté/mis à jour les docstrings
 Les noms de variables sont clairs et explicites
 Le code est DRY (pas de répétition)
Tests
 J'ai ajouté des tests unitaires
 Tous les tests passent (pytest tests/ -v)
 La couverture de tests est ≥ 80%
 Test normal (cas courant)
 Test limite (cas aux limites)
 Test erreur (gestion d'erreur)
Documentation
 J'ai mis à jour le README si nécessaire
 Les docstrings sont complètes et à jour
Commit
 Les commits sont atomiques et bien nommés
 Le message de commit explique le pourquoi, pas le comment
🔍 Résultat de CI/CD
 ✅ Linting avec Ruff réussi
 ✅ Tests avec Pytest réussis (80% couverture minimum)
 ✅ Build Docker réussi
🔗 Lien vers l'issue

Fixes #(issue_number)

📸 Screenshots / Exemples

Si applicable, ajoutez des screenshots ou des résultats d'API (curl, Postman, etc.)

bash
curl "http://localhost:5000/math/factorielle?n=5"
{"result": 120}
📚 Notes supplémentaires

Toute information supplémentaire qui pourrait aider au review.

Reviewer: @username (assigned by lead)

Approval required: ✅ Minimum 1