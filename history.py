import logging

class CalculationHistory:
    def __init__(self):
        self.history = []

    def add_entry(self, operation, a, b, result):
        entry = {"operation": operation, "a": a, "b": b, "result": result}
        self.history.append(entry)
        logging.info(f"History updated: {entry}")

    def get_history(self):
        return self.history

