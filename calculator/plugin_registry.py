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

