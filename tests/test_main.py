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