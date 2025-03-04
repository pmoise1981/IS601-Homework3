import pytest
from calculator.calculator import register_commands

@pytest.fixture(autouse=True)
def reset_registry():
    register_commands()  # Reset and register commands before every test

