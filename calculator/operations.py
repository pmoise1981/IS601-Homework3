from calculator.logger import logger

def add(a, b):
    result = a + b
    logger.info(f"Adding {a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logger.info(f"Subtracting {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logger.info(f"Multiplying {a} * {b} = {result}")
    return result

def divide(a, b):
    if b == 0:
        logger.error("Attempted division by zero")
        raise ValueError("Cannot divide by zero")
    result = a / b
    logger.info(f"Dividing {a} / {b} = {result}")
    return result

