def is_palindrome(number):
    # Handle edge cases: negative numbers and numbers ending in zero (except zero itself)
    if number < 0 or (number % 10 == 0 and number != 0):
        return False
    
    # Initialize a variable to store the reversed half of the number
    reversed_half = 0
    
    # Process only half of the number
    while number > reversed_half:
        # Add the last digit of number to reversed_half
        reversed_half = reversed_half * 10 + number % 10
        # Remove the last digit from number
        number //= 10
    
    # Check if the number is equal to the reversed_half
    # For odd digits, discard the middle digit of reversed_half by // 10
    return number == reversed_half or number == reversed_half // 10

print(is_palindrome(101))  # Output: True
