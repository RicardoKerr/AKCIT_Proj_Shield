import pytest

from generator.password_generator import SYMBOLS, generate_password


def test_generate_password_respects_length():
    password = generate_password(16, True, True, True, True)
    assert len(password) == 16


def test_generate_password_has_selected_types():
    password = generate_password(12, True, True, True, True)
    assert any(c.isupper() for c in password)
    assert any(c.islower() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in SYMBOLS for c in password)


def test_generate_password_raises_when_no_charset_selected():
    with pytest.raises(ValueError):
        generate_password(12, False, False, False, False)


def test_generate_password_raises_when_too_small():
    with pytest.raises(ValueError):
        generate_password(3, True, True, False, False)


def test_generate_password_contains_only_allowed_characters():
    password = generate_password(24, True, False, True, False)
    assert all(c.isupper() or c.isdigit() for c in password)


def test_generate_password_has_variability_between_runs():
    attempts = {generate_password(14, True, True, True, True) for _ in range(8)}
    assert len(attempts) > 1
