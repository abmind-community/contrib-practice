import pytest

from src.math_utils import add_numbers, divide_numbers


def test_add() -> None:
    """Test the ``add_numbers`` function."""
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, -1) == -2
    assert add_numbers(1, -1) == 0
    assert add_numbers(1, -1) == 0


def test_divide() -> None:
    """Test the ``divide_numbers`` function."""
    # TODO: replace this placeholder with real assertions
    assert divide_numbers(1, 2) == 0.5
    assert divide_numbers(-1, 1) == -1.0
    assert divide_numbers(0, 1) == 0.0
    assert divide_numbers(-1, -1) == 1.0
    assert divide_numbers(1, 3) == 0.3333333333333333


def test_divide_by_zero() -> None:
    """Test the ``divide_numbers`` function with zero denominator."""
    # TODO: replace this placeholder with real assertions
    with pytest.raises(ValueError, match="Division by zero"):
        divide_numbers(1, 0)
