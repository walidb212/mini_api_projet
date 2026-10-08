import pytest

from app.outils.convert import celsius_fahrenheit


def test_celsius_fahrenheit_normal():
    assert celsius_fahrenheit(100) == 212


def test_celsius_fahrenheit_limite():
    assert celsius_fahrenheit(-273.15) == pytest.approx(-459.67)


def test_celsius_fahrenheit_erreur():
    with pytest.raises(ValueError):
        celsius_fahrenheit(-300)
        
def test_celsius_fahrenheit_moins_40():
    assert celsius_fahrenheit(-40) == -40


def test_celsius_fahrenheit_zero():
    assert celsius_fahrenheit(0) == 32
