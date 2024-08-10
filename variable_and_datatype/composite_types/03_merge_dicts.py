"""
Design a function to merge two dictionaries, giving priority to values from the second dictionary in case of key conflicts.

Merge two dictionaries with priority on the second dictionary.

This function takes two dictionaries as input and returns a new dictionary that contains all the key-value pairs from both dictionaries. If a key is present in both dictionaries, the value from the second dictionary will be used.

Args:
dict1 (dict): The first dictionary.
dict2 (dict): The second dictionary.

Returns:
dict: A new dictionary containing all key-value pairs from dict1 and dict2, with dict2's values taking priority in case of conflicts.

Example:
>>> dict1 = {'a': 1, 'b': 2, 'c': 3}
>>> dict2 = {'b': 20, 'c': 30, 'd': 40}
>>> merge_dicts(dict1, dict2)
{'a': 1, 'b': 20, 'c': 30, 'd': 40}
>>> merge_dicts({'x': 10}, {'y': 20, 'z': 30})
{'x': 10, 'y': 20, 'z': 30}
>>> merge_dicts({}, {'a': 1})
{'a': 1}
"""

def merge_dicts(dict1, dict2):
    # Create a copy of the first dictionary
    merged_dict = dict1.copy()

    # Update the merged_dict with the second dictionary
    merged_dict.update(dict2)

    return merged_dict

# Example usage:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 40}
print(merge_dicts(dict1, dict2))  # Output: {'a': 1, 'b': 20, 'c': 30, 'd': 40}
