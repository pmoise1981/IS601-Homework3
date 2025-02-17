from calculator.calculations import Calculations
from calculator.calculation import Calculation

def test_add_calculation():
    calc = Calculation(5, 3, "add")
    Calculations.add_calculation(calc)
    assert Calculations.get_last_calculation() == calc

def test_get_last_calculation_empty():
    Calculations.clear_history()
    assert Calculations.get_last_calculation() is None

def test_clear_history():
    calc = Calculation(10, 2, "subtract")
    Calculations.add_calculation(calc)
    Calculations.clear_history()
    assert len(Calculations.history) == 0

