import pytest

from app.outils.texte import est_palindrome


def test_est_palindrome_normal():
    assert est_palindrome("kayak") is True
    assert est_palindrome("python") is False


def test_est_palindrome_limite():
    assert est_palindrome("a") is True
    assert est_palindrome("Kayak") is True
    assert est_palindrome("esope reste ici et se repose") is True
    assert est_palindrome("Esope reste ici, et se repose") is True


def test_est_palindrome_erreur():
    with pytest.raises(ValueError):
        est_palindrome("")
    with pytest.raises(ValueError):
        est_palindrome("   ")
