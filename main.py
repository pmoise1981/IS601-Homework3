from calculator.calculator import Calculator
from calculator.plugin_registry import PluginRegistry
import calculator.commands.add
import calculator.commands.subtract
import calculator.commands.multiply
import calculator.commands.divide

def main():
    print("Welcome to the Interactive Calculator!")
    print("Type 'menu' to see available commands or 'exit' to quit.")

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "exit":
            print("Exiting the calculator. Goodbye!")
            break
        elif command == "menu":
            print("Available commands:", ", ".join(PluginRegistry.get_available_commands()))
        else:
            args = input("Enter two numbers separated by space: ").split()
            if len(args) != 2:
                print("Please enter exactly two numbers.")
                continue
            
            try:
                a, b = map(float, args)
                result = Calculator.execute_command(command, a, b)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()

