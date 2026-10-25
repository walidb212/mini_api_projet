def verifier_texte(texte: str) -> None:
    if not texte.strip():
        raise ValueError("Le texte ne peut pas être vide")


def est_palindrome(texte: str) -> bool:
    verifier_texte(texte)
    propre = [c for c in texte.lower() if c.isalnum()]
    return propre == propre[::-1]
