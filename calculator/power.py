from .command import Command
from .plugin_registry import PluginRegistry

class PowerCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a ** self.b

# Register the new command
PluginRegistry.register("pow", PowerCommand)

