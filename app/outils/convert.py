##Convertir des données Celsius en données Fahrenheit 
def celsius_fahrenheit(c):
    if c < -273.15:
        raise ValueError("Température impossible")
    return c * 9 / 5 + 32

print(celsius_fahrenheit(100))