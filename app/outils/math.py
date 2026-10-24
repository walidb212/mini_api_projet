def factorielle(n):
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


def est_premier(n):

    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"L'entrée doit être un entier, reçu {type(n).__name__}")
    
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True


print("Test est_premier:")
print(f"est_premier(5) = {est_premier(5)}")
print(f"est_premier(17) = {est_premier(17)}")



def pgcd(a, b):

    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError(f"Le premier argument doit être un entier, reçu {type(a).__name__}")
    
    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError(f"Le deuxième argument doit être un entier, reçu {type(b).__name__}")
    
    if a == 0 and b == 0:
        raise ValueError("Le PGCD n'est pas défini quand a et b sont tous les deux zéro")
    
    a = abs(a)
    b = abs(b)
    
    while b != 0:
        a, b = b, a % b
    
    return a

print("Test PGCD:")
print(f"pgcd(48, 18) = {pgcd(48, 18)}")
print(f"pgcd(17, 19) = {pgcd(17, 19)}")

