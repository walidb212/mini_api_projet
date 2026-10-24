from fastapi import FastAPI, HTTPException

from app.outils.convert import celsius_fahrenheit, km_miles

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

@app.get("/km_miles/{km}")
def route_km_miles(km: float):
    try:
        return {"km": km, "miles": km_miles(km)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))