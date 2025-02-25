import pytest
from calculator.repl import process_input

def test_repl_addition():
    assert process_input("2 add 3") == "Result: 5"

def test_repl_invalid_command():
    assert process_input("2 unknown 3") == "Error: Unknown command 'unknown'"

