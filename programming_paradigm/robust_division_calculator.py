def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        return f"The result of the division is {result}"
    
    except ZeroDivisionError as e:
        return f"Error: Cannot divide by zero."
    
    except ValueError as e:
        return f"Error: Please enter numeric values only."
