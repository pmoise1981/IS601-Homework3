from calculator.repl import process_input  # Add this import statement

def test_repl_addition():
    # Call process_input with the string '2 add 3'
    result = process_input("2 add 3")
    assert result == "Result: 5"

