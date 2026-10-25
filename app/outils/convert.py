def celsius_fahrenheit(celsius: float) -> float:
    if celsius < -273.15:
        raise ValueError("Température impossible")
    return celsius * 9 / 5 + 32


TAUX = {"USD": 1.08, "DZD": 150.0, "GBP": 0.86, "JPY": 163.0}


def euros_devise(montant: float, devise: str) -> float:
    if montant < 0:
        raise ValueError("Le montant ne peut pas être négatif")
    if devise.upper() not in TAUX:
        raise ValueError(f"Devise inconnue : {devise}")
    return montant * TAUX[devise.upper()]