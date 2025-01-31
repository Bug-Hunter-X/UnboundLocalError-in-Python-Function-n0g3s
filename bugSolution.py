def function_with_uncommon_error(a, b):
    result = None  # Initialize result to a default value
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return result
    except TypeError:
        print("Error: Unsupported operand type(s) for / ")
        return result

# Now, the print statement will always work correctly.
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Division by zero
None
print(function_with_uncommon_error(10, "a"))  # Output: Error: Unsupported operand type(s) for / 
None