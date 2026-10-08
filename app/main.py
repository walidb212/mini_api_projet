from fastapi import FastAPI, HTTPException

from app.outils.convert import celsius_fahrenheit
from app.outils.validation import email_valide

app = FastAPI(title="Mini API")


@app.get("/sante")
def route_sante():
    return {"statut": "ok"}


@app.get("/celsius_fahrenheit/{celsius}")
def route_celsius_fahrenheit(celsius: float):
    try:
        return {"celsius": celsius, "fahrenheit": celsius_fahrenheit(celsius)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))


@app.get("/email_valide/{email}")
def route_email_valide(email: str):
    return {"email": email, "valide": email_valide(email)}