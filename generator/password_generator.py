import secrets
import string


SYMBOLS = "!@#$%^&*()_+-="


def generate_password(
    length: int,
    use_uppercase: bool,
    use_lowercase: bool,
    use_numbers: bool,
    use_symbols: bool,
) -> str:
    if length < 4:
        raise ValueError("O tamanho da senha deve ser no minimo 4.")

    charsets = []
    if use_uppercase:
        charsets.append(string.ascii_uppercase)
    if use_lowercase:
        charsets.append(string.ascii_lowercase)
    if use_numbers:
        charsets.append(string.digits)
    if use_symbols:
        charsets.append(SYMBOLS)

    if not charsets:
        raise ValueError("Selecione pelo menos um tipo de caractere.")

    if length < len(charsets):
        raise ValueError("O tamanho deve ser maior ou igual ao numero de tipos selecionados.")

    password_chars = [secrets.choice(charset) for charset in charsets]
    pool = "".join(charsets)

    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(pool))

    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)
