"""
Create a function that accepts a float and returns its representation as a fraction without using the fractions module.

Convert a floating-point number to its simplest fraction representation by manually calculating the numerator and denominator.

Args:
num (float): The floating-point number to convert.

Returns:
str: A string representing the fraction in the form 'numerator/denominator'.

Example:
>>> float_to_fraction(0.75)
'3/4'
>>> float_to_fraction(1.5)
'3/2'
>>> float_to_fraction(0.2)
'1/5'
"""

import math

def float_to_fraction(num):
    # Handle special case for zero
    if num == 0:
        return '0/1'
    
    # Find the denominator by determining the number of decimal places
    precision = 1
    while num != int(num):
        num *= 10
        precision *= 10
    
    # Convert to integer numerator and denominator
    numerator = int(num)
    denominator = precision
    
    # Find the greatest common divisor
    gcd = math.gcd(numerator, denominator)
    
    # Simplify the fraction
    numerator //= gcd
    denominator //= gcd
    
    return f'{numerator}/{denominator}'

# Example usage:
print(float_to_fraction(0.75))  # Output: '3/4'
print(float_to_fraction(1.5))   # Output: '3/2'
print(float_to_fraction(0.2))   # Output: '1/5'
