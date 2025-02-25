from .command import Command
from .plugin_registry import PluginRegistry

class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a + self.b

# Registering the command
PluginRegistry.register("add", AddCommand)

class SubtractCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a - self.b

# Registering the command
PluginRegistry.register("sub", SubtractCommand)

class MultiplyCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a * self.b

# Registering the command
PluginRegistry.register("mul", MultiplyCommand)

class DivideCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            return "Error: Division by zero!"
        return self.a / self.b

# Registering the command
PluginRegistry.register("div", DivideCommand)

