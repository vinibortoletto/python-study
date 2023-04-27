from ex_2 import decode
import pytest


def test_decode_when_arg_is_uppercase():
    """
    Test the 'decode' function when the input argument is a string of
    uppercase letters.

    The function should return the expected output of "8464" when given
    the input "VINI".
    """
    mock = "VINI"
    output = "8464"
    assert decode(mock) == output


def test_decode_when_arg_is_lowercase():
    """
    Test the 'decode' function when the input argument is a string of
    lowercase letters.

    The function should return the expected output of "8464" when given
    the input "vini".
    """
    mock = "vini"
    output = "8464"
    assert decode(mock) == output


def test_decode_when_arg_is_number():
    """
    Test the 'decode' function when the input argument is a number.

    The function should raise an 'AttributeError' exception when given
    a number as input.
    """
    with pytest.raises(AttributeError):
        decode(123)
