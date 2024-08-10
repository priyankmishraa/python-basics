"""
Implement a custom data structure using a list to simulate a stack with push, pop, and min operations in constant time.

Simulate a stack with constant time operations.

In this implementation, we use two stacks:
- The main stack holds all the elements.
- The min stack keeps track of the minimum values.

This allows the `min` operation to be performed in constant time.

Methods:
- push(x): Adds element x to the stack.
- pop(): Removes and returns the top element from the stack.
- min(): Returns the minimum element in the stack.

Example:
>>> stack = MinStack()
>>> stack.push(3)
>>> stack.push(5)
>>> stack.min()
3
>>> stack.push(2)
>>> stack.push(1)
>>> stack.min()
1
>>> stack.pop()
1
>>> stack.min()
2
"""

class MinStack:
    def __init__(self):
        # Initialize two stacks: one for the actual values and one for tracking the minimums
        self.stack = []
        self.min_stack = []

    def push(self, x):
        # Push the element onto the main stack
        self.stack.append(x)
        
        # Push the minimum value onto the min_stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    
    def pop(self):
        # Pop the element from the main stack
        if self.stack:
            popped = self.stack.pop()
            
            # If the popped element is the same as the top of the min_stack, pop the min_stack as well
            if popped == self.min_stack[-1]:
                self.min_stack.pop()
                
            return popped
        else:
            return None  # Handle case where stack is empty

    def min(self):
        # Return the minimum value, which is the top element of the min_stack
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None  # Handle case where stack is empty

# Example usage:
stack = MinStack()
stack.push(3)
stack.push(5)
print(stack.min())  # Output: 3
stack.push(2)
stack.push(1)
print(stack.min())  # Output: 1
stack.pop()
print(stack.min())  # Output: 2
