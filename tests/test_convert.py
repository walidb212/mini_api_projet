import pytest

from app.outils.convert import celsius_fahrenheit, euros_devise


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


def test_euros_devise_normal():
    assert euros_devise(100, "USD") == pytest.approx(108)
    assert euros_devise(100, "DZD") == pytest.approx(15000)


def test_euros_devise_limite():
    assert euros_devise(0, "USD") == 0
    assert euros_devise(100, "usd") == pytest.approx(108)


def test_euros_devise_erreur():
    with pytest.raises(ValueError):
        euros_devise(-1, "USD")
    with pytest.raises(ValueError):
        euros_devise(100, "XYZ")