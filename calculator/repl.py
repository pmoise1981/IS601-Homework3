        except ValueError as ve:
            print(f"Input Error: {ve}")
        except ZeroDivisionError:
            print("Math Error: Division by zero is not allowed.")
        except Exception as e:
            print(f"Unexpected Error: {e}")

