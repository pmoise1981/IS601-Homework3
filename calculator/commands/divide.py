from calculator.plugin_registry import PluginRegistry

class DivideCommand:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.a = a
        self.b = b

    def execute(self):
        return self.a / self.b

PluginRegistry.register("divide", DivideCommand)

