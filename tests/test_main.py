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