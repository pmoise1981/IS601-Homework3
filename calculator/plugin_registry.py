import importlib
import pkgutil
import calculator.commands  # Import the commands package dynamically

class PluginRegistry:
    """Registry to store available calculator operations dynamically."""
    _commands = {}

    @classmethod
    def register(cls, name, command_class):
        """Register a command with a name."""
        cls._commands[name] = command_class

    @classmethod
    def get_command(cls, name):
        """Retrieve a command by name."""
        return cls._commands.get(name)

    @classmethod
    def get_all_commands(cls):
        """Return all registered commands."""
        return cls._commands

    @classmethod
    def get_available_commands(cls):
        """Return a formatted string of available commands."""
        commands_list = ", ".join(cls._commands.keys())
        return f"Available commands: {commands_list}" if commands_list else "No commands available."

    @classmethod
    def load_plugins(cls):
        """Dynamically discover and import all command plugins."""
        package = calculator.commands
        for _, module_name, _ in pkgutil.iter_modules(package.__path__):
            importlib.import_module(f"calculator.commands.{module_name}")

