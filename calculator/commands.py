from .plugin_registry import PluginRegistry

class Command:
    def execute(self):
        raise NotImplementedError("Each command must implement the execute method.")

    @classmethod
    def register(cls, name):
        """Automatically register the class with the given name."""
        PluginRegistry.register(name, cls)

