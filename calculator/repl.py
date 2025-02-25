import readline  # Enables auto-completion in the terminal
from .plugin_registry import PluginRegistry
from .invoker import CalculatorInvoker

# Enable tab completion
readline.parse_and_bind("tab: complete")

def repl():
    """Interactive calculator using dynamically loaded commands."""
    PluginRegistry.load_plugins()  # Load all available plugins
    print("Welcome to the Interactive Calculator!")
    print(PluginRegistry.get_available_commands())  # Show menu at the start
    print("Enter operations in the format: <num1> <operator> <num2>")
    print("Type 'menu' to see available commands or 'exit' to quit.\n")

    calculator = CalculatorInvoker()

    while True:
        user_input = input(">>> ").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            break
        if user_input == "menu":  # Display the menu when user types "menu"
            print(PluginRegistry.get_available_commands())
            continue
        if user_input == "help":
            print("Enter operations in the format: <num1> <operator> <num2>")
            continue

        try:
            parts = user_input.split()
            if len(parts) != 3:
                raise ValueError("Invalid input format. Use: <num1> <operator> <num2>")

            num1, operation, num2 = parts
            num1, num2 = float(num1), float(num2)

            command_class = PluginRegistry.get_command(operation)
            if not command_class:
                raise ValueError(f"Unsupported operation! Type 'menu' for available commands.")

            command = command_class(num1, num2)
            result = calculator.execute_command(command)
            print(f"Result: {result}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()

