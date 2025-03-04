class DivideCommand:
    def execute(self, a, b):  # Make sure it takes two arguments
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

