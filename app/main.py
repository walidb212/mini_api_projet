from fastapi import FastAPI, HTTPException

from app.erreurs import valeur_invalide
from app.outils.convert import celsius_fahrenheit, euros_devise, km_miles
from app.outils.math import est_premier, factorielle
from app.outils.validation import code_postal, email_valide

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

@app.get("/km_miles/{km}")
def route_km_miles(km: float):
    try:
        return {"km": km, "miles": km_miles(km)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))

@app.get("/email_valide/{email}")
def route_email_valide(email: str):
    return {"email": email, "valide": email_valide(email)}


@app.get("/factorielle/{n}")
def route_factorielle(n: str):
    try:
        n = int(n)
        return {"n": n, "factorielle": factorielle(n)}
    except (ValueError, TypeError) as e:
        raise HTTPException(400, detail=str(e))


@app.get("/est_premier/{n}")
def route_est_premier(n: str):
    try:
        n = int(n)
        return {"n": n, "est_premier": est_premier(n)}
    except TypeError as e:
        raise HTTPException(400, detail=str(e))


@app.get("/euros_devise/{montant}/{devise}")
def route_euros_devise(montant: float, devise: str):
    try:
        return {
            "montant": montant,
            "devise": devise.upper(),
            "resultat": euros_devise(montant, devise),
        }
    except ValueError as e:
        raise HTTPException(400, detail=str(e))


@app.get("/code_postal/{code}")
def route_code_postal(code: str):
    return {"code": code, "valide": code_postal(code)}    
