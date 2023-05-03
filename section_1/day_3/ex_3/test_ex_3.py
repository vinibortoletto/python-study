from ex_3 import validate_email, filter_valid_email
import pytest


def test_should_raise_error_if_email_is_not_string():
    input = 123
    with pytest.raises(TypeError):
        validate_email(input)


def test_should_raise_error_if_email_is_malformed():
    input = "email"
    with pytest.raises(TypeError):
        validate_email(input)


def test_should_raise_error_if_username_is_invalid():
    input = "$email@email.com"
    with pytest.raises(ValueError):
        validate_email(input)


def test_should_raise_error_if_provider_is_invalid():
    input = "email@$email.com"
    with pytest.raises(ValueError):
        validate_email(input)


def test_should_raise_error_if_extension_length_is_not_3():
    input = "email@email.com_"
    with pytest.raises(ValueError):
        validate_email(input)


def test_should_accept_valid_email():
    input = "email@email.com"
    result = validate_email(input)
    assert result is True


def test_should_filter_only_valid_emails():
    input = ["nome@dominio.com", "errad#@dominio.com", "outro@dominio.com"]
    output = ["nome@dominio.com", "outro@dominio.com"]
    result = filter_valid_email(input)
    assert result == output
