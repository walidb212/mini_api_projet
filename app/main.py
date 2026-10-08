from fastapi import FastAPI

from app.erreurs import valeur_invalide


app = FastAPI(title="Mini API")
app.add_exception_handler(ValueError, valeur_invalide)


@app.get("/sante")
def route_sante():
    return {"statut": "ok"}