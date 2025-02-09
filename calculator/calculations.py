from calculator.calculation import Calculation

class Calculations:
    """Stores a history of calculations."""

    history = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls):
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls):
        cls.history.clear()

