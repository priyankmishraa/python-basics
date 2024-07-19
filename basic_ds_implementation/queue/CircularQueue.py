class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def __repr__(self):
        if self.is_empty():
            return "CircularQueue([])"
        items = []
        i = self.front
        for _ in range(self.size):
            items.append(self.queue[i])
            i = (i + 1) % self.capacity
        return f"CircularQueue({items})"

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        if self.is_full():
            raise OverflowError("Enqueue to a full queue")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        """Remove and return the item from the front of the queue. Raises an IndexError if the queue is empty."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        """Return the item at the front of the queue without removing it. Raises an IndexError if the queue is empty."""
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[self.front]

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.size == 0

    def is_full(self):
        """Return True if the queue is full, False otherwise."""
        return self.size == self.capacity

    def get_size(self):
        """Return the number of items in the queue."""
        return self.size

# Example usage
cq = CircularQueue(5)  # Create a circular queue with capacity 5
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print("Circular Queue after enqueues:", cq)  # Output: CircularQueue([1, 2, 3])
print("Front item:", cq.peek())  # Output: Front item: 1

print("Dequeued item:", cq.dequeue())  # Output: Dequeued item: 1
print("Circular Queue after dequeue:", cq)  # Output: CircularQueue([2, 3])

cq.enqueue(4)
cq.enqueue(5)
cq.enqueue(6)
print("Circular Queue after additional enqueues:", cq)  # Output: CircularQueue([2, 3, 4, 5, 6])

print("Is queue empty?", cq.is_empty())  # Output: Is queue empty? False
print("Is queue full?", cq.is_full())  # Output: Is queue full? True

cq.dequeue()
cq.enqueue(7)
print("Circular Queue after dequeue and enqueue:", cq)  # Output: CircularQueue([3, 4, 5, 6, 7])
