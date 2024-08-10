"""
Implement a function that takes a string of numbers separated by commas and returns a list of integers.

Convert a comma-separated string of numbers into a list of integers.

Args:
number_string (str): A string containing numbers separated by commas (e.g., '1,2,3').

Returns:
list of int: A list of integers parsed from the input string.

Example:
>>> parse_numbers('1,2,3')
[1, 2, 3]
>>> parse_numbers('4,5,6,7')
[4, 5, 6, 7]
>>> parse_numbers('9,0,1')
[9, 0, 1]
"""

def parse_numbers(number_string):
    # Split the string by commas
    str_numbers = number_string.split(',')
    
    # Convert each string to an integer
    int_numbers = [int(num) for num in str_numbers]
    
    return int_numbers

# Example usage:
print(parse_numbers('1,2,3'))  # Output: [1, 2, 3]
print(parse_numbers('4,5,6,7'))  # Output: [4, 5, 6, 7]
print(parse_numbers('9,0,1'))  # Output: [9, 0, 1]