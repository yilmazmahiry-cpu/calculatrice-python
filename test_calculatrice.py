import pytest
from calculatrice import addition, soustraction, multiplication, division


def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0


def test_soustraction():
    assert soustraction(10, 4) == 6
    assert soustraction(0, 5) == -5


def test_multiplication():
    assert multiplication(3, 5) == 15
    assert multiplication(0, 99) == 0
    assert multiplication(-2, 3) == -6


def test_division():
    assert division(8, 2) == 4.0
    assert division(7, 2) == 3.5


def test_division_par_zero():
    with pytest.raises(ValueError, match="Division par zéro impossible"):
        division(5, 0)
