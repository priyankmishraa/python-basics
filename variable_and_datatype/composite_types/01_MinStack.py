"""
Implement a custom data structure using a list to simulate a stack with push, pop, and min operations in constant time.
"""

class MinStack:
    def __init__(self):
        """
        Initialize the stack and a stack to keep track of minimum values.
        """
        self.stack = []
        self.min_stack = []

    def push(self, value):
        """
        Push a new value onto the stack.

        Args:
            value (int): The value to be added to the stack.
        """
        self.stack.append(value)
        # Push the new minimum value onto the min_stack
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        """
        Remove and return the top value from the stack.

        Returns:
            int: The value at the top of the stack.
        """
        if not self.stack:
            return None
        value = self.stack.pop()
        # Remove the top value from the min_stack if it is the current minimum
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def min(self):
        """
        Get the minimum value from the stack.

        Returns:
            int: The minimum value in the stack.
        """
        if not self.min_stack:
            return None
        return self.min_stack[-1]

# Example usage
min_stack = MinStack()
min_stack.push(3)
min_stack.push(5)
print(min_stack.min())   # Output: 3
min_stack.push(2)
min_stack.push(2)
print(min_stack.min())   # Output: 2
min_stack.pop()
print(min_stack.min())   # Output: 2
min_stack.pop()
print(min_stack.min())   # Output: 3
