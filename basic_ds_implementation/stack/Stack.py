class Stack:
    def __init__(self):
        self.stack = []

    def __repr__(self):
        return f"Stack({self.stack})"

    def push(self, item):
        """Push an item onto the stack."""
        self.stack.append(item)

    def pop(self):
        """Pop an item off the stack and return it. Raises an IndexError if the stack is empty."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        """Return the top item from the stack without removing it. Raises an IndexError if the stack is empty."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.stack[-1]

    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack after pushes:", stack)  # Output: Stack([1, 2, 3])

print("Top item:", stack.peek())  # Output: Top item: 3

print("Popped item:", stack.pop())  # Output: Popped item: 3
print("Stack after pop:", stack)  # Output: Stack([1, 2])

print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False
print("Stack size:", stack.size())  # Output: Stack size: 2
