def divide_numbers(a, b):
    """
    Function to divide two numbers.
    :param a: Numerator
    :param b: Denominator
    :return: Result of division
    """
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

# Example usage
if __name__ == "__main__":
    try:
        numerator = float(input("Enter numerator: "))
        denominator = float(input("Enter denominator: "))
        result = divide_numbers(numerator, denominator)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")