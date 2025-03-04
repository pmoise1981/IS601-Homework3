class MultiplyCommand:
    def __init__(self, *args):
        self.args = args

    def execute(self):
        result = 1
        for arg in self.args:
            result *= arg
        return result

