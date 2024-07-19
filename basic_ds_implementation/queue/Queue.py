class Queue:
    def __init__(self):
        self.queue = []

    def __repr__(self):
        return f"Queue({self.queue})"

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue. Raises an IndexError if the queue is empty."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)

    def peek(self):
        """Return the item at the front of the queue without removing it. Raises an IndexError if the queue is empty."""
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[0]

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)

# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue after enqueues:", queue)  # Output: Queue([1, 2, 3])

print("Front item:", queue.peek())  # Output: Front item: 1

print("Dequeued item:", queue.dequeue())  # Output: Dequeued item: 1
print("Queue after dequeue:", queue)  # Output: Queue([2, 3])

print("Is queue empty?", queue.is_empty())  # Output: Is queue empty? False
print("Queue size:", queue.size())  # Output: Queue size: 2
