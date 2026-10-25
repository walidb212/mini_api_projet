def est_palindrome(texte: str) -> bool:
    if not texte:
        raise ValueError("Le texte ne peut pas être vide")
    propre = texte.lower().replace(" ", "")
    return propre == propre[::-1]


def compter_voyelles(texte: str) -> int:
    return sum(1 for c in texte.lower() if c in "aeiouyàâéèêëîïôùûü")


def inverser(texte: str) -> str:
    return texte[::-1]
