def process_input(user_input):
    # Split the input into components
    parts = user_input.split()
    
    if len(parts) == 3:
        num1 = int(parts[0])
        num2 = int(parts[2])
        operation = parts[1]
        
        # Handle the 'add' operation
        if operation == "add":
            result = num1 + num2
            return f"Result: {result}"
        
        # You can add more operations (e.g., subtract, multiply, divide) here as needed
        elif operation == "subtract":
            result = num1 - num2
            return f"Result: {result}"
        elif operation == "multiply":
            result = num1 * num2
            return f"Result: {result}"
        elif operation == "divide":
            if num2 == 0:
                return "Error: Cannot divide by zero"
            result = num1 / num2
            return f"Result: {result}"
    
    # If the input doesn't match the expected format
    return f"Processed: {user_input}"

