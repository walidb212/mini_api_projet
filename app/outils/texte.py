def est_palindrome(texte: str) -> bool:
    if not texte:
        raise ValueError("Le texte ne peut pas être vide")
    propre = texte.lower().replace(" ", "")
    return propre == propre[::-1]
