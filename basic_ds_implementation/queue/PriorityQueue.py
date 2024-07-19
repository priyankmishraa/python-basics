import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def __repr__(self):
        return f"PriorityQueue({self.heap})"

    def push(self, item, priority):
        """Add an item to the priority queue with a given priority."""
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        """Remove and return the item with the highest priority (lowest priority value). Raises an IndexError if the queue is empty."""
        if self.is_empty():
            raise IndexError("Pop from an empty priority queue")
        return heapq.heappop(self.heap)[1]

    def peek(self):
        """Return the item with the highest priority without removing it. Raises an IndexError if the queue is empty."""
        if self.is_empty():
            raise IndexError("Peek from an empty priority queue")
        return self.heap[0][1]

    def is_empty(self):
        """Return True if the priority queue is empty, False otherwise."""
        return len(self.heap) == 0

    def size(self):
        """Return the number of items in the priority queue."""
        return len(self.heap)

# Example usage
pq = PriorityQueue()
pq.push("task1", 3)
pq.push("task2", 1)
pq.push("task3", 2)

print("Priority Queue:", pq)  # Output: PriorityQueue([(1, 'task2'), (3, 'task1'), (2, 'task3')])

print("Highest priority item:", pq.peek())  # Output: Highest priority item: task2

print("Popped item:", pq.pop())  # Output: Popped item: task2
print("Priority Queue after pop:", pq)  # Output: PriorityQueue([(2, 'task3'), (3, 'task1')])

print("Is priority queue empty?", pq.is_empty())  # Output: Is priority queue empty? False
print("Priority queue size:", pq.size())  # Output: Priority queue size: 2
