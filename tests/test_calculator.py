"""Unit tests for the calculator."""

import pytest
from calculator.calculator import Calculator
from calculator.calculations import Calculations

@pytest.fixture
def sample_numbers():
    return 10, 5

@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0)])
def test_add(a, b, expected):
    assert Calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(2, 3, -1), (5, 10, -5), (0, 0, 0)])
def test_subtract(a, b, expected):
    assert Calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(2, 3, 6), (-1, 1, -1), (0, 5, 0)])
def test_multiply(a, b, expected):
    assert Calculator.multiply(a, b) == expected

def test_divide(sample_numbers):
    a, b = sample_numbers
    assert Calculator.divide(a, b) == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(10, 0)

def test_calculations_history():
    """Tests storing and retrieving calculations."""
    Calculations.clear_history()
    Calculator.add(1, 1)
    last_calc = Calculations.get_last_calculation()
    assert last_calc is not None
    assert last_calc.result == 2

