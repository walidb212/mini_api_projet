"""
Module mathématique : fonctions utiles.
"""


def factorielle(n):
    """
    Calcule la factorielle de n.

    Args:
        n (int): Un entier positif ou zéro

    Returns:
        int: La factorielle de n (n!)

    Raises:
        ValueError: Si n < 0 ou n n'est pas un entier
        TypeError: Si n n'est pas un nombre

    Examples:
        >>> factorielle(5)
        120
        >>> factorielle(0)
        1
    """
    # Validation du type
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"L'entrée doit être un entier, reçu {type(n).__name__}")

    # Validation de la plage
    if n < 0:
        raise ValueError(f"La factorielle n'est pas définie pour les négatifs, reçu {n}")

    # Cas de base
    if n == 0 or n == 1:
        return 1

    # Calcul factorielle avec récursivité
    def factorielle(n):
        return n  * factorielle(n-1)


def est_premier(n):
    """
    Détermine si n est un nombre premier.

    Args:
        n (int): Un entier à tester

    Returns:
        bool: True si n est premier, False sinon

    Raises:
        TypeError: Si n n'est pas un entier

    Examples:
        >>> est_premier(17)
        True
        >>> est_premier(4)
        False
        >>> est_premier(1)
        False
    """
    # Validation du type
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"L'entrée doit être un entier, reçu {type(n).__name__}")

    # Cas spéciaux
    if n < 2:
        return False

    if n == 2:
        return True

    # Les nombres pairs > 2 ne sont pas premiers
    if n % 2 == 0:
        return False

    # Vérifier les diviseurs impairs jusqu'à √n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


def pgcd(a, b):
    """
    Calcule le Plus Grand Commun Diviseur (PGCD) de a et b.
    Utilise l'algorithme d'Euclide.

    Args:
        a (int): Premier entier
        b (int): Deuxième entier

    Returns:
        int: Le PGCD positif de a et b

    Raises:
        TypeError: Si a ou b ne sont pas des entiers
        ValueError: Si a et b sont tous les deux zéro

    Examples:
        >>> pgcd(48, 18)
        6
        >>> pgcd(17, 19)
        1
        >>> pgcd(100, 50)
        50
    """
    # Validation des types
    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError(f"Le premier argument doit être un entier, reçu {type(a).__name__}")

    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError(f"Le deuxième argument doit être un entier, reçu {type(b).__name__}")

    # Cas où a et b sont tous les deux zéro
    if a == 0 and b == 0:
        raise ValueError("Le PGCD n'est pas défini quand a et b sont tous les deux zéro")

    # Prendre les valeurs absolues (le PGCD est toujours positif)
    a = abs(a)
    b = abs(b)

    # Algorithme d'Euclide
    while b != 0:
        a, b = b, a % b

    return a


# Tests des fonctions
print("Test factorielle:")
print(f"factorielle(5) = {factorielle(5)}")
print(f"factorielle(0) = {factorielle(0)}")

print("\nTest est_premier:")
print(f"est_premier(7) = {est_premier(7)}")
print(f"est_premier(4) = {est_premier(4)}")
print(f"est_premier(2) = {est_premier(2)}")

print("pgcd:")
print(f"pgcd(100, 50) = {pgcd(100, 50)}")
print(f"pgcd(48,18) = {pgcd(48, 18)}")