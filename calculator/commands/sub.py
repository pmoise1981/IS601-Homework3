from calculator.plugin_registry import PluginRegistry

class SubtractCommand:
    def __init__(self, *args):
        self.args = args

    def execute(self):
        return self.args[0] - self.args[1]

# Register the SubtractCommand with PluginRegistry
PluginRegistry.register("subtract", SubtractCommand)

