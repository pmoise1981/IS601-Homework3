import pytest
from calculator.calculation import Calculation

def test_addition():
    calc = Calculation(5, 3, "add")
    assert calc.perform() == 8

def test_subtraction():
    calc = Calculation(10, 2, "subtract")
    assert calc.perform() == 8

def test_multiplication():
    calc = Calculation(4, 5, "multiply")
    assert calc.perform() == 20

def test_division():
    calc = Calculation(20, 4, "divide")
    assert calc.perform() == 5

def test_division_by_zero():
    calc = Calculation(1, 0, "divide")
    with pytest.raises(ZeroDivisionError):
        calc.perform()

def test_unknown_operation():
    calc = Calculation(5, 3, "unknown")
    with pytest.raises(ValueError):
        calc.perform()

