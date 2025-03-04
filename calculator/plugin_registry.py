class PluginRegistry:
    _commands = {}

    @classmethod
    def register(cls, command_name, command_class):
        if command_name in cls._commands:
            raise ValueError(f"Command '{command_name}' is already registered.")
        cls._commands[command_name] = command_class

    @classmethod
    def get_command(cls, command_name):
        return cls._commands.get(command_name)

    @classmethod
    def reset(cls):
        """Clears all registered commands."""
        cls._commands = {}

