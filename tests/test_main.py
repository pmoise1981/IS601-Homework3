import pytest
import subprocess

def test_main_add():
    result = subprocess.run(
        ['python', 'main.py', '5', '3', 'add'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    assert result.stdout.decode() == "The result of 5 add 3 is equal to 8\n"

def test_main_invalid_input():
    result = subprocess.run(
        ['python', 'main.py', 'a', '3', 'add'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    assert "Invalid input" in result.stderr.decode()

