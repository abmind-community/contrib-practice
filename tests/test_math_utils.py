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
    # TODO: replace this placeholder with real assertions
    assert divide(1, 2) == 0.5
    assert divide(-1, 1) == -1
    assert divide(-1, -1) == 1
    assert divide(1, -1) == -1
    assert divide(0, 1) == 0


def test_divide_by_zero() -> None:
    """Test the ``divide`` function with zero denominator."""
    # TODO: replace this placeholder with real assertions
    assert divide(1, 0) is None
