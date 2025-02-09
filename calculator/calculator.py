"""Calculator class with history storage."""

from calculator.calculations import Calculations
from calculator.calculation import Calculation

class Calculator:
    """Calculator with arithmetic operations and history."""

    @staticmethod
    def add(a: float, b: float) -> float:
        result = a + b
        Calculations.add_calculation(Calculation(a, b, "add", result))
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        result = a - b
        Calculations.add_calculation(Calculation(a, b, "subtract", result))
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        result = a * b
        Calculations.add_calculation(Calculation(a, b, "multiply", result))
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        Calculations.add_calculation(Calculation(a, b, "divide", result))
        return result


