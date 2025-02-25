from calculator.plugin_registry import PluginRegistry

class Calculator:
    @staticmethod
    def execute_command(command_name, *args):
        command_class = PluginRegistry.get_command(command_name)
        if command_class:
            command = command_class(*args)
            return command.execute()
        else:
            raise ValueError(f"Command '{command_name}' not found.")


