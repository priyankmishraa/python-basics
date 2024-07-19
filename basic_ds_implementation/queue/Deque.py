class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        items = []
        current = self.head
        while current:
            items.append(current.value)
            current = current.next
        return f"Deque({items})"

    def append_left(self, value):
        """Add an item to the front of the deque."""
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def append_right(self, value):
        """Add an item to the end of the deque."""
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop_left(self):
        """Remove and return the item from the front of the deque. Raises an IndexError if the deque is empty."""
        if self.is_empty():
            raise IndexError("Pop from an empty deque")
        value = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return value

    def pop_right(self):
        """Remove and return the item from the end of the deque. Raises an IndexError if the deque is empty."""
        if self.is_empty():
            raise IndexError("Pop from an empty deque")
        value = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return value

    def peek_left(self):
        """Return the item from the front of the deque without removing it. Raises an IndexError if the deque is empty."""
        if self.is_empty():
            raise IndexError("Peek from an empty deque")
        return self.head.value

    def peek_right(self):
        """Return the item from the end of the deque without removing it. Raises an IndexError if the deque is empty."""
        if self.is_empty():
            raise IndexError("Peek from an empty deque")
        return self.tail.value

    def is_empty(self):
        """Return True if the deque is empty, False otherwise."""
        return self.size == 0

    def get_size(self):
        """Return the number of items in the deque."""
        return self.size

# Example usage
deque = Deque()
deque.append_left(1)
deque.append_right(2)
deque.append_left(0)
deque.append_right(3)

print("Deque after operations:", deque)  # Output: Deque([0, 1, 2, 3])

print("Left peek:", deque.peek_left())  # Output: Left peek: 0
print("Right peek:", deque.peek_right())  # Output: Right peek: 3

print("Pop left:", deque.pop_left())  # Output: Pop left: 0
print("Pop right:", deque.pop_right())  # Output: Pop right: 3

print("Deque after pops:", deque)  # Output: Deque([1, 2])

print("Is deque empty?", deque.is_empty())  # Output: Is deque empty? False
print("Deque size:", deque.get_size())  # Output: Deque size: 2
