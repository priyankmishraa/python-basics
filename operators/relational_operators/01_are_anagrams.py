"""
Write a function that checks if two given strings are anagrams.
    Check if two strings are anagrams.

    Two strings are anagrams if they contain the same characters in the same frequencies.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.

    Example:
        >>> are_anagrams("listen", "silent")
        True
        >>> are_anagrams("hello", "world")
        False
        >>> are_anagrams("triangle", "integral")
        True
"""

def are_anagrams(str1, str2):
    # If lengths of both strings are not the same, they cannot be anagrams
    if len(str1) != len(str2):
        return False

    # Use dictionaries to count the frequency of each character in both strings
    char_count1 = {}
    char_count2 = {}

    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1

    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1

    # Compare character counts
    return char_count1 == char_count2

# Example usage
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False
print(are_anagrams("triangle", "integral"))  # Output: True
print(are_anagrams("evil", "vile"))  # Output: True
