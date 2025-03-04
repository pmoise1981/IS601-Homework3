import sys
from calculator.calculator import Calculator

def main():
    # Get arguments from command line input
    if len(sys.argv) != 4:
        print("Usage: python main.py <num1> <num2> <operation>")
        return

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    operation = sys.argv[3]

    result = Calculator.execute_command(operation, a, b)

    # Output the result
    print(f"The result of {a} {operation} {b} is equal to {result}")

if __name__ == "__main__":
    main()

