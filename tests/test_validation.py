from app.outils.validation import email_valide


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