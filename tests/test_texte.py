import pytest

from app.outils.texte import compter_voyelles, est_palindrome, inverser


def test_est_palindrome_normal():
    assert est_palindrome("kayak") is True
    assert est_palindrome("python") is False


def test_est_palindrome_limite():
    assert est_palindrome("a") is True
    assert est_palindrome("Kayak") is True
    assert est_palindrome("esope reste ici et se repose") is True


def test_est_palindrome_erreur():
    with pytest.raises(ValueError):
        est_palindrome("")
    with pytest.raises(ValueError):
        est_palindrome("   ")


def test_compter_voyelles_normal():
    assert compter_voyelles("bonjour") == 3


def test_compter_voyelles_limite():
    assert compter_voyelles("bcd") == 0
    assert compter_voyelles("Élève à l'école") == 7


def test_compter_voyelles_erreur():
    with pytest.raises(ValueError):
        compter_voyelles("")


def test_inverser_normal():
    assert inverser("abc") == "cba"


def test_inverser_limite():
    assert inverser("a") == "a"


def test_inverser_erreur():
    with pytest.raises(ValueError):
        inverser("")
