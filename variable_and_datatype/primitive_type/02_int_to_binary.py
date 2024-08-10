"""
Implement a function that converts a given integer to its binary representation without using built-in functions.

Convert an integer to its binary representation.

The binary number system is a base-2 numeral system that uses only two symbols: 0 and 1. Each digit is referred to as a bit. 
For example:
- The integer 5 is represented as 101 in binary.
- The integer 10 is represented as 1010 in binary.
- The integer 0 is represented as 0 in binary.

Args:
number (int): The integer to convert.

Returns:
str: A string representing the binary form of the given number.

Example:
>>> int_to_binary(5)
'101'
>>> int_to_binary(10)
'1010'
>>> int_to_binary(0)
'0'
>>> int_to_binary(7)
'111'

"""

def int_to_binary(number):
    # Handle the special case for zero
    if number == 0:
        return '0'
    
    # Initialize an empty list to store binary digits
    binary_digits = []

    # Iterate until the number becomes zero
    while number > 0:
        # Get the remainder when the number is divided by 2 (this gives the binary digit)
        binary_digit = number % 2
        # Append the digit to the list (binary digits are collected in reverse order)
        binary_digits.append(str(binary_digit))
        # Update the number by performing integer division by 2
        number //= 2

    # Reverse the list of binary digits to get the correct order and join them into a string
    return ''.join(binary_digits[::-1])

# Test cases
print(int_to_binary(5))   # Output: '101'
print(int_to_binary(10))  # Output: '1010'
print(int_to_binary(0))   # Output: '0'
print(int_to_binary(7))   # Output: '111'
