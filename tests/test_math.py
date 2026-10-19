import pytest

from app.outils.math import est_premier, factorielle

# ============================================================================

# Tests
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

class TestEstPremier:
    """Tests de la fonction est_premier."""
    
    def test_est_premier_normal(self):
        """Test est_premier avec des valeurs courantes."""
        assert est_premier(2) is True
        assert est_premier(3) is True
        assert est_premier(17) is True
        assert est_premier(4) is False
        assert est_premier(10) is False
    
    def test_est_premier_limite(self):
        """Test est_premier aux limites."""
        assert est_premier(1) is False
        assert est_premier(2) is True
        assert est_premier(97) is True
    
    def test_est_premier_erreur(self):
        """Test est_premier avec erreurs."""
        with pytest.raises(TypeError):
            est_premier(5.5)
        with pytest.raises(TypeError):
            est_premier("17")