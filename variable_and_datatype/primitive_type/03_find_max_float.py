"""
Develop a function to find the maximum floating-point number in a list without using the max() function.

Find the maximum floating-point number in a list.

In this function, we'll manually iterate through the list to identify the largest floating-point number. We will assume that the list contains at least one element, and we'll handle negative numbers and zero appropriately.

Args:
numbers (list of float): A list of floating-point numbers.

Returns:
float: The maximum floating-point number in the list.

Example:
>>> find_max_float([3.5, 2.7, 8.9, 4.6])
8.9
>>> find_max_float([-1.2, -3.5, -0.4])
-0.4
>>> find_max_float([7.1])
7.1
>>> find_max_float([0.0, -2.3, -5.1, 3.0])
3.0
"""

def find_max_float(numbers):
    # Initialize the maximum value with the first element of the list
    max_value = numbers[0]

    # Iterate through the list starting from the second element
    for number in numbers[1:]:
        # Update max_value if the current number is greater
        if number > max_value:
            max_value = number
    
    # Return the maximum value found
    return max_value

# Test cases
print(find_max_float([3.5, 2.7, 8.9, 4.6]))   # Output: 8.9
print(find_max_float([-1.2, -3.5, -0.4]))     # Output: -0.4
print(find_max_float([7.1]))                  # Output: 7.1
print(find_max_float([0.0, -2.3, -5.1, 3.0])) # Output: 3.0
