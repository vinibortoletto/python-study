from sum import sum
import pytest


def test_sum_when_numbers_are_passed_as_args_return_sum():
    assert sum(2, 2) == 4
    assert sum(0, 0) == 0
    assert sum(-1, 5) == 4


def test_sum_when_letters_are_passed_as_args_raises_an_exception():
    with pytest.raises(ValueError):
        sum("a", "b")
    with pytest.raises(ValueError):
        sum("a", 1)
    with pytest.raises(ValueError):
        sum(1, "b")
