from .plugin_registry import PluginRegistry
from .invoker import CalculatorInvoker
import importlib
import pkgutil
import calculator

def load_plugins():
    """Dynamically load all modules in the 'calculator' package."""
    package = calculator
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        importlib.import_module(f"calculator.{module_name}")

def repl():
    """Interactive calculator using dynamically loaded commands."""
    load_plugins()  # Load all available plugins
    print("Welcome to the Interactive Calculator!")
    print("Enter operations in the format: <num1> <operator> <num2>")
    print(f"Supported operators: {', '.join(PluginRegistry.get_all_commands().keys())}")
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

            command_class = PluginRegistry.get_command(operation)
            if not command_class:
                raise ValueError(f"Unsupported operation! Available: {', '.join(PluginRegistry.get_all_commands().keys())}")

            command = command_class(num1, num2)
            result = calculator.execute_command(command)
            print(f"Result: {result}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()

