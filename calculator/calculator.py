class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    @staticmethod
    def calculate(a, b, operation):
        if operation == "add":
            return Calculator.add(a, b)
        elif operation == "subtract":
            return Calculator.subtract(a, b)
        elif operation == "multiply":
            return Calculator.multiply(a, b)
        elif operation == "divide":
            return Calculator.divide(a, b)
        else:
            raise ValueError(f"Unknown operation: {operation}")


