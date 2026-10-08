from fastapi import FastAPI, HTTPException

from app.erreurs import valeur_invalide
from app.outils.convert import celsius_fahrenheit

app = FastAPI(title="Mini API")
app.add_exception_handler(ValueError, valeur_invalide)


@app.get("/sante")
def route_sante():
    return {"statut": "ok"}


@app.get("/celsius_fahrenheit/{celsius}")
def route_celsius_fahrenheit(celsius: float):
    try:
        return {"celsius": celsius, "fahrenheit": celsius_fahrenheit(celsius)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))