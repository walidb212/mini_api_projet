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
 
    # Calcul itératif (plus efficace)
    result = 1
    for i in range(2, n + 1):
        result *= i
 
    return result

# Tests des fonctions
print("Test factorielle:")
print(f"factorielle(5) = {factorielle(5)}")
print(f"factorielle(0) = {factorielle(0)}")