"""
Write a function to flatten a nested list of integers.

Flatten a nested list.

The function will take a list that may contain other lists of integers as elements. The goal is to return a single list that contains all the integers from the nested structure, in the same order, without any nesting.

Args:
nested_list (list of int or list): A list that may contain integers and other lists.

Returns:
list: A flat list containing all the integers from the nested structure.

Example:
>>> flatten_list([1, [2, 3], [4, [5, 6]], 7])
[1, 2, 3, 4, 5, 6, 7]
>>> flatten_list([[1, 2], 3, [4, [5, [6, 7]]]])
[1, 2, 3, 4, 5, 6, 7]
>>> flatten_list([1, [2], [3, [4]], 5])
[1, 2, 3, 4, 5]
"""

def flatten_list(nested_list):
    # Initialize an empty list to store the flattened elements
    flat_list = []

    # Iterate over each element in the list
    for element in nested_list:
        # If the element is a list, recursively flatten it
        if isinstance(element, list):
            flat_list.extend(flatten_list(element))
        else:
            # If it's an integer, add it directly to the flat_list
            flat_list.append(element)
    
    return flat_list

# Example usage:
print(flatten_list([1, [2, 3], [4, [5, 6]], 7]))  # Output: [1, 2, 3, 4, 5, 6, 7]
print(flatten_list([[1, 2], 3, [4, [5, [6, 7]]]]))  # Output: [1, 2, 3, 4, 5, 6, 7]
print(flatten_list([1, [2], [3, [4]], 5]))  # Output: [1, 2, 3, 4, 5]
