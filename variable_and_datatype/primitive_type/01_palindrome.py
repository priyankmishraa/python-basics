"""
Implement a function that checks if a given number is a palindrome without converting it to a string.

Check if a given number is a palindrome.

A palindrome is a number that remains the same when its digits are reversed. For example:
- 121 is a palindrome because reversing it gives 121.
- 12321 is a palindrome because reversing it gives 12321.
- 123 is not a palindrome because reversing it gives 321.

Args:
number (int): The number to check.

Returns:
bool: True if the number is a palindrome, False otherwise.

Example:
>>> is_palindrome(121)
True
>>> is_palindrome(-121)
False
>>> is_palindrome(10)
False
>>> is_palindrome(12321)
True

"""

def is_palindrome(number):
    # Handle negative numbers and numbers ending in zero (except zero itself)
    if number < 0 or (number % 10 == 0 and number != 0):
        return False

    # Initialize variables
    original_number = number
    reversed_number = 0

    while number > 0:
        # Get the last digit of the number
        digit = number % 10
        # Append it to the reversed number
        reversed_number = reversed_number * 10 + digit
        # Remove the last digit from the original number
        number //= 10

    # Check if the reversed number is equal to the original number
    return reversed_number == original_number

print(is_palindrome(-121))
