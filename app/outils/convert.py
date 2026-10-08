def celsius_fahrenheit(celsius: float) -> float:
    if celsius < -273.15:
        raise ValueError("Température impossible")
    return celsius * 9 / 5 + 32