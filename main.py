import sys
from calculator.calculator import Calculator

def format_result(a, b, operation, result):
    a = int(a) if a.is_integer() else a
    b = int(b) if b.is_integer() else b
    result = int(result) if result.is_integer() else result
    return f"The result of {a} {operation} {b} is equal to {result}"

if __name__ == "__main__":
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        operation = sys.argv[3]
        result = Calculator.calculate(a, b, operation)
        print(format_result(a, b, operation, result))
    except ValueError as e:
        print(f"Invalid input: {e}", file=sys.stderr)  # <-- Print errors to stderr
    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero", file=sys.stderr)  # <-- Print errors to stderr

