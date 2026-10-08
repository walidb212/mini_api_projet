import json

from app.erreurs import valeur_invalide


def test_valeur_invalide_renvoie_400():
    reponse = valeur_invalide(None, ValueError("entrée invalide"))
    assert reponse.status_code == 400


def test_valeur_invalide_renvoie_le_message():
    reponse = valeur_invalide(None, ValueError("entrée invalide"))
    assert json.loads(reponse.body) == {"detail": "entrée invalide"}
