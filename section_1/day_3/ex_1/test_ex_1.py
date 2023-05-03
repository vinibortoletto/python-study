from ex_1 import get_number_list
import pytest


def test_get_number_list_when_arg_is_5():
    mock = [1, 2, "Fizz", 4, "Buzz"]
    assert get_number_list(5) == mock


def test_get_number_list_when_arg_is_10():
    mock = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]
    assert get_number_list(10) == mock


def test_get_number_list_when_arg_is_string():
    with pytest.raises(TypeError):
        get_number_list("1")
