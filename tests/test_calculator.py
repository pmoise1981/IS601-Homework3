import pytest
from calculator.calculator import Calculator

def test_add():
    result = Calculator.execute_command("add", 1, 2)
    assert result == 3

def test_subtract():
    result = Calculator.execute_command("subtract", 5, 2)
    assert result == 3

def test_multiply():
    result = Calculator.execute_command("multiply", 3, 4)
    assert result == 12

def test_divide():
    result = Calculator.execute_command("divide", 10, 2)
    assert result == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.execute_command("divide", 10, 0)

