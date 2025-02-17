import pytest
from calculator.calculator import Calculator

def test_calculator_addition():
    assert Calculator.add(5, 3) == 8

def test_calculator_subtraction():
    assert Calculator.subtract(10, 2) == 8

def test_calculator_multiplication():
    assert Calculator.multiply(4, 5) == 20

def test_calculator_division():
    assert Calculator.divide(20, 4) == 5

def test_calculator_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(1, 0)

def test_calculator_calculate():
    assert Calculator.calculate(5, 3, "add") == 8
    assert Calculator.calculate(10, 2, "subtract") == 8
    assert Calculator.calculate(4, 5, "multiply") == 20
    assert Calculator.calculate(20, 4, "divide") == 5

def test_calculator_unknown_operation():
    with pytest.raises(ValueError):
        Calculator.calculate(5, 3, "unknown")

