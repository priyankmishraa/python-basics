"""
Write a function to compute the power of a number without using the ** operator or pow() function.
    Compute the power of a number using exponentiation by squaring.

    Args:
        base (float): The base number.
        exponent (int): The exponent (must be a non-negative integer).

    Returns:
        float: The result of raising the base to the given exponent.

    Example:
        >>> power(2, 3)
        8
        >>> power(5, 0)
        1
        >>> power(2, 10)
        1024
"""

def power(base, exponent):
    if exponent < 0:
        raise ValueError("Exponent must be a non-negative integer")
    
    result = 1
    current_power = base

    while exponent > 0:
        if exponent % 2 == 1:  # If exponent is odd
            result *= current_power
        current_power *= current_power  # Square the base
        exponent //= 2  # Divide the exponent by 2

    return result

# Example usage
print(power(2, 3))  # Output: 8
print(power(5, 0))  # Output: 1
print(power(2, 10))  # Output: 1024
print(power(3, 5))  # Output: 243
