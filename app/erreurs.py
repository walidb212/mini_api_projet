from fastapi import Request
from fastapi.responses import JSONResponse


def valeur_invalide(request: Request, exc: ValueError) -> JSONResponse:
    """Transforme une ValueError levée par un outil en réponse 400."""
    return JSONResponse(status_code=400, content={"detail": str(exc)})
