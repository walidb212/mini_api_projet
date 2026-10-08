def email_valide(email: str) -> bool:
    if " " in email or email.count("@") != 1:
        return False
    local, domaine = email.split("@")
    if not local or "." not in domaine:
        return False
    nom, _, extension = domaine.rpartition(".")
    return bool(nom) and len(extension) >= 2