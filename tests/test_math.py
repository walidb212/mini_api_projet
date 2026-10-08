import pytest
from app.outils.math import factorielle
 
 
# ============================================================================
# Tests pour factorielle(n)
# ============================================================================
 
class TestFactorielle:
    """Tests de la fonction factorielle."""
 
    # Cas normal
    def test_factorielle_normal(self):
        """Test factorielle avec des valeurs courantes."""
        assert factorielle(0) == 1
        assert factorielle(1) == 1
        assert factorielle(5) == 120
        assert factorielle(10) == 3628800
 
    # Cas limite
    def test_factorielle_limite(self):
        """Test factorielle aux limites (0, 1, nombres grands)."""
        assert factorielle(0) == 1  # Cas limite bas
        assert factorielle(1) == 1  # Cas limite bas
        assert factorielle(20) == 2432902008176640000  # Nombre grand
 
    # Cas erreur
    def test_factorielle_erreur_negatif(self):
        """Test factorielle avec un nombre négatif."""
        with pytest.raises(ValueError, match="n'est pas définie pour les négatifs"):
            factorielle(-1)
 
    def test_factorielle_erreur_type_float(self):
        """Test factorielle avec un float."""
        with pytest.raises(TypeError, match="doit être un entier"):
            factorielle(5.5)
 
    def test_factorielle_erreur_type_string(self):
        """Test factorielle avec une chaîne."""
        with pytest.raises(TypeError, match="doit être un entier"):
            factorielle("5")
 
    def test_factorielle_erreur_bool(self):
        """Test factorielle avec un booléen (qui est un int en Python)."""
        with pytest.raises(TypeError, match="doit être un entier"):
            factorielle(True)


