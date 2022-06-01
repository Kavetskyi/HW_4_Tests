import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(10, 5) == 15
    assert Calculator.add(-5, -5) == -10
    assert Calculator.add(5, -5) == 0
    assert Calculator.add(0, 5) == 5
    assert Calculator.add(10, 0) == 10


def test_subtract():
    assert Calculator.subtract(10, 5) == 5
    assert Calculator.subtract(-5, -5) == 0
    assert Calculator.subtract(5, -5) == 10
    assert Calculator.subtract(0, 5) == -5
    assert Calculator.subtract(10, 0) == 10


def test_multiply():
    assert Calculator.multiply(10, 5) == 50
    assert Calculator.multiply(-5, -5) == 25
    assert Calculator.multiply(5, -5) == -25
    assert Calculator.multiply(0, 5) == 0
    assert Calculator.multiply(10, 0) == 0


def test_divide():
    assert Calculator.divide(10, 5) == 2
    assert Calculator.divide(-5, -5) == 1
    assert Calculator.divide(5, -5) == -1
    assert Calculator.divide(0, 5) == 0
    with pytest.raises(ValueError, match='Can not divide by zero!'):
        Calculator.divide(10, 0)
