import pytest
from calculator.calculator import Calculator

def test_addition():
    assert Calculator.execute_command("add", 2, 3) == 5

def test_subtraction():
    assert Calculator.execute_command("subtract", 5, 2) == 3

def test_multiplication():
    assert Calculator.execute_command("multiply", 3, 4) == 12

def test_division():
    assert Calculator.execute_command("divide", 10, 2) == 5

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.execute_command("divide", 10, 0)

