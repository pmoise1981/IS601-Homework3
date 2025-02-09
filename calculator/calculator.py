from calculator.calculation import Calculation

class Calculator:
    """Calculator with static methods and history storage."""

    history = []

    @staticmethod
    def add(a: float, b: float) -> float:
        result = a + b
        Calculator.history.append(Calculation(a, b, "add", result))
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        result = a - b
        Calculator.history.append(Calculation(a, b, "subtract", result))
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        result = a * b
        Calculator.history.append(Calculation(a, b, "multiply", result))
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        Calculator.history.append(Calculation(a, b, "divide", result))
        return result

    @staticmethod
    def get_last_calculation():
        return Calculator.history[-1] if Calculator.history else None


