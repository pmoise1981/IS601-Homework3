from calculator.plugin_registry import PluginRegistry

class MultiplyCommand:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a * self.b

PluginRegistry.register("multiply", MultiplyCommand)

