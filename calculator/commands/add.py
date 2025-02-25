from calculator.plugin_registry import PluginRegistry

class AddCommand:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a + self.b

PluginRegistry.register("add", AddCommand)

