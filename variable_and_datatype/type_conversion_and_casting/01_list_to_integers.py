"""
Write a function to convert a list of integers to a single concatenated integer.

Convert a list of integers into a single integer by concatenating their string representations.

Args:
int_list (list of int): A list of integers.

Returns:
int: A single integer obtained by concatenating the integer values.

Example:
>>> list_to_integer([1, 2, 3])
123
>>> list_to_integer([4, 5, 6, 7])
4567
>>> list_to_integer([9, 0, 1])
901
"""

def list_to_integer(int_list):
    # Convert each integer in the list to a string
    str_list = map(str, int_list)
    
    # Concatenate all strings into one single string
    concatenated_str = ''.join(str_list)
    
    # Convert the concatenated string back to an integer
    result = int(concatenated_str)
    
    return result

# Example usage:
print(list_to_integer([1, 2, 3]))  # Output: 123
print(list_to_integer([4, 5, 6, 7]))  # Output: 4567
print(list_to_integer([9, 0, 1]))  # Output: 901