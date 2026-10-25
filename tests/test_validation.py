from app.outils.validation import code_postal, email_valide


def test_email_valide_normal():
    assert email_valide("lea@mail.fr") is True


def test_email_valide_limite():
    assert email_valide("a@b.fr") is True
    assert email_valide("a@b.f") is False


def test_email_valide_erreur():
    assert email_valide("pas-un-mail") is False
    assert email_valide("@mail.fr") is False
    assert email_valide("lea@mail") is False
    assert email_valide("lea@@mail.fr") is False
    assert email_valide("lea@mail..fr") is False
    assert email_valide("lea@ mail.fr") is False
    assert email_valide("lea@.mail.fr") is False


def test_code_postal_normal():
    assert code_postal("75001") is True


def test_code_postal_limite():
    assert code_postal("01000") is True
    assert code_postal("7500") is False
    assert code_postal("750011") is False


def test_code_postal_erreur():
    assert code_postal("abcde") is False
    assert code_postal("7500a") is False
    assert code_postal("75 01") is False
    assert code_postal("") is False