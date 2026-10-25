def verifier_texte(texte: str) -> None:
    if not texte.strip():
        raise ValueError("Le texte ne peut pas être vide")


def est_palindrome(texte: str) -> bool:
    verifier_texte(texte)
    propre = texte.lower().replace(" ", "")
    return propre == propre[::-1]


def compter_voyelles(texte: str) -> int:
    verifier_texte(texte)
    return sum(1 for c in texte.lower() if c in "aeiouyàâéèêëîïôùûü")
