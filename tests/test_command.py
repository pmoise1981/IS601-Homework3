import pytest
from calculator.command.add import AddCommand 
from calculator.command.sub import SubtractCommand 

def test_add_command():
    command = AddCommand(2, 3)
    assert command.execute() == 5

def test_subtract_command():
    command = SubtractCommand(5, 3)
