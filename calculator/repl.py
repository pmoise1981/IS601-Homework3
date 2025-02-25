from .operations import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from .invoker import CalculatorInvoker

def repl():
    print("Welcome to the Interactive Calculator!")
    print("Enter operations in the format: <num1> <operator> <num2>")
    print("Supported operators: add, sub, mul, div")
    print("Type 'exit' to quit.\n")

    calculator = CalculatorInvoker()

    while True:
        user_input = input(">>> ").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            break

        try:
            parts = user_input.split()
            if len(parts) != 3:
                raise ValueError("Invalid input format. Use: <num1> <operator> <num2>")

            num1, operation, num2 = parts
            num1, num2 = float(num1), float(num2)

            command_map = {
                "add": AddCommand(num1, num2),
                "sub": SubtractCommand(num1, num2),
                "mul": MultiplyCommand(num1, num2),
                "div": DivideCommand(num1, num2)
            }

            if operation not in command_map:
                raise ValueError("Unsupported operation!")

            command = command_map[operation]
            result = calculator.execute_command(command)
            print(f"Result: {result}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()

