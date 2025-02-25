# calculator/commands/add.py

from calculator.plugin_registry import PluginRegistry
from calculator.command import Command  # if you have a base Command class

class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a + self.b

# Register the command with a description
PluginRegistry.register("add", AddCommand, "Adds two numbers (Usage: num1 add num2)")

