from calculator.command import Command

class SubtractCommand(Command):
    def execute(self, a, b):
        return a - b

