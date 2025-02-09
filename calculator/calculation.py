"""Stores a single calculation operation."""

class Calculation:
    """Represents a single arithmetic operation."""

    def __init__(self, a: float, b: float, operation: str, result: float):
        self.a = a
        self.b = b
        self.operation = operation
        self.result = result

    def __str__(self):
        return f"{self.a} {self.operation} {self.b} = {self.result}"

