import subprocess

def test_main_add():
    result = subprocess.run(
        ['python', 'main.py', '5', '3', 'add'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Check if the output matches the expected string
    assert result.stdout.decode() == "The result of 5 add 3 is equal to 8\n"

