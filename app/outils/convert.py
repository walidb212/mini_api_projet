def celsius_fahrenheit(celsius: float) -> float:
    if celsius < -273.15:
        raise ValueError("Température impossible")
    return celsius * 9 / 5 + 32


def km_miles(km: float) -> float:
    if km < 0:
        raise ValueError("La distance ne peut pas être négative")
    return km * 0.621371