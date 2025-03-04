from calculator.commands.add_command import AddCommand
from calculator.commands.subtract_command import SubtractCommand
from calculator.commands.multiply_command import MultiplyCommand
from calculator.commands.divide_command import DivideCommand
from calculator.plugin_registry import PluginRegistry

# Register commands only if not already registered
def register_commands():
    if "add" not in PluginRegistry._commands:
        PluginRegistry.register("add", AddCommand)
    if "subtract" not in PluginRegistry._commands:
        PluginRegistry.register("subtract", SubtractCommand)
    if "multiply" not in PluginRegistry._commands:
        PluginRegistry.register("multiply", MultiplyCommand)
    if "divide" not in PluginRegistry._commands:
        PluginRegistry.register("divide", DivideCommand)

class Calculator:
    """A simple calculator that executes registered commands."""

    @classmethod
    def execute_command(cls, command_name, a, b):
        """Executes a registered command with given arguments."""
        command = PluginRegistry._commands.get(command_name)
        if not command:
            raise ValueError(f"Command '{command_name}' is not registered.")
        return command().execute(a, b)

# Ensure commands are registered when this module is imported
register_commands()

