class PluginRegistry:
    _commands = {}

    @classmethod
    def register(cls, name, command):
        cls._commands[name] = command

    @classmethod
    def get_command(cls, name):
        return cls._commands.get(name)

    @classmethod
    def get_available_commands(cls):
        return list(cls._commands.keys())

