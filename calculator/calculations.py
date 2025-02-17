class Calculations:
    history = []

    @staticmethod
    def add_calculation(calc):
        """ Adds a calculation to history """
        Calculations.history.append(calc)

    @staticmethod
    def get_last_calculation():
        """ Retrieves the last calculation """
        if Calculations.history:
            return Calculations.history[-1]
        return None

    @staticmethod
    def clear_history():
        """ Clears the history """
        Calculations.history = []

