"""
Write a function to convert a list of integers to a single concatenated integer (e.g., [1, 2, 3] -> 123).
    Convert a list of integers to a single concatenated integer.

    Args:
        int_list (list of int): The list of integers to be concatenated.

    Returns:
        int: The single concatenated integer.

    Example:
        >>> concatenate_integers([1, 2, 3])
        123
        >>> concatenate_integers([4, 5, 6, 7])
        4567
"""
#################################################################
# Solution 1
#################################################################

def concatenate_integers(int_list):
    concatenated_str = ''.join(map(str, int_list))
    return int(concatenated_str)

# Example usage
print(concatenate_integers([1, 2, 3]))  # Output: 123
print(concatenate_integers([4, 5, 6, 7]))  # Output: 4567
print(concatenate_integers([0, 1, 0]))  # Output: 10


#################################################################
# Solution 2
#################################################################
def concatenate_integers(int_list):
    concatenated_number = 0
    for num in int_list:
        concatenated_number = concatenated_number * 10 + num
    return concatenated_number

# Example usage
print(concatenate_integers([1, 2, 3]))  # Output: 123
print(concatenate_integers([4, 5, 6, 7]))  # Output: 4567
print(concatenate_integers([0, 1, 0]))  # Output: 10


# For Small to Medium-Sized Lists: The first solution is generally preferred due to its simplicity and readability.
# For Very Large Lists: The second solution might be better due to its potential memory efficiency and direct computation.