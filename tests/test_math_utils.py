import pytest

from src.math_utils import add, divide


def test_add() -> None:
    """Test the ``add`` function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add(1, -1) == 0
    assert add(1, -1) == 0


def test_divide() -> None:
    """Test the ``divide`` function."""
    assert divide(2, 4) == 0.5
    assert divide(6, -3) == -2
    assert divide(0, -3) == 0


def test_divide_by_zero() -> None:
    """Test the ``divide`` function with zero denominator."""
    with pytest.raises(ValueError):
        divide(8, 0)
