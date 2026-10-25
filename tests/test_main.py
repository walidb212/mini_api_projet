import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sante_repond_ok():
    reponse = client.get("/sante")
    assert reponse.status_code == 200
    assert reponse.json() == {"statut": "ok"}


def test_route_celsius_fahrenheit():
    reponse = client.get("/celsius_fahrenheit/100")
    assert reponse.status_code == 200
    assert reponse.json()["fahrenheit"] == 212


def test_route_celsius_fahrenheit_erreur():
    reponse = client.get("/celsius_fahrenheit/-300")
    assert reponse.status_code == 400


def test_route_km_miles():
    reponse = client.get("/km_miles/100")
    assert reponse.status_code == 200
    assert reponse.json()["miles"] == pytest.approx(62.1371)


def test_route_km_miles_erreur():
    reponse = client.get("/km_miles/-1")
    assert reponse.status_code == 400
def test_route_email_valide():
    reponse = client.get("/email_valide/lea@mail.fr")
    assert reponse.status_code == 200
    assert reponse.json()["valide"] is True


def test_route_email_valide_incorrect():
    reponse = client.get("/email_valide/pas-un-mail")
    assert reponse.status_code == 200
    assert reponse.json()["valide"] is False


def test_route_euros_devise():
    reponse = client.get("/euros_devise/100/USD")
    assert reponse.status_code == 200
    assert reponse.json()["resultat"] == pytest.approx(108)


def test_route_euros_devise_devise_inconnue():
    reponse = client.get("/euros_devise/100/XYZ")
    assert reponse.status_code == 400


def test_route_euros_devise_montant_negatif():
    reponse = client.get("/euros_devise/-5/USD")
    assert reponse.status_code == 400
def test_route_code_postal():
    reponse = client.get("/code_postal/75001")
    assert reponse.status_code == 200
    assert reponse.json()["valide"] is True


def test_route_code_postal_zero_initial():
    reponse = client.get("/code_postal/01000")
    assert reponse.status_code == 200
    assert reponse.json()["valide"] is True


def test_route_code_postal_incorrect():
    reponse = client.get("/code_postal/7500")
    assert reponse.status_code == 200
    assert reponse.json()["valide"] is False


def test_route_euros_devise_minuscule():
    reponse = client.get("/euros_devise/100/usd")
    assert reponse.status_code == 200
    assert reponse.json()["devise"] == "USD"


def test_route_est_palindrome():
    reponse = client.get("/est_palindrome", params={"texte": "kayak"})
    assert reponse.status_code == 200
    assert reponse.json()["est_palindrome"] is True


def test_route_est_palindrome_erreur():
    reponse = client.get("/est_palindrome", params={"texte": " "})
    assert reponse.status_code == 400


def test_route_compter_voyelles():
    reponse = client.get("/compter_voyelles", params={"texte": "école"})
    assert reponse.status_code == 200
    assert reponse.json()["voyelles"] == 3


def test_route_compter_voyelles_erreur():
    reponse = client.get("/compter_voyelles", params={"texte": " "})
    assert reponse.status_code == 400


def test_route_inverser():
    reponse = client.get("/inverser", params={"texte": "abc"})
    assert reponse.status_code == 200
    assert reponse.json()["inverse"] == "cba"


def test_route_inverser_erreur():
    reponse = client.get("/inverser", params={"texte": " "})
    assert reponse.status_code == 400


def test_route_inverser_caracteres_speciaux():
    reponse = client.get("/inverser", params={"texte": "a/b?c#d"})
    assert reponse.status_code == 200
    assert reponse.json()["inverse"] == "d#c?b/a"


def test_route_est_palindrome_avec_slash():
    reponse = client.get("/est_palindrome", params={"texte": "a/a"})
    assert reponse.status_code == 200
    assert reponse.json()["est_palindrome"] is True


def test_route_compter_voyelles_avec_point_interrogation():
    reponse = client.get("/compter_voyelles", params={"texte": "ça va ?"})
    assert reponse.status_code == 200
    assert reponse.json()["voyelles"] == 2


def test_route_texte_manquant():
    reponse = client.get("/inverser")
    assert reponse.status_code == 422


def test_route_pgcd():
    reponse = client.get("/pgcd/48/18")
    assert reponse.status_code == 200
    assert reponse.json()["pgcd"] == 6


def test_route_pgcd_erreur():
    reponse = client.get("/pgcd/0/0")
    assert reponse.status_code == 400
