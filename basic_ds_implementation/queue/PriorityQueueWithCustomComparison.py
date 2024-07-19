import heapq

class Item:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Item(name={self.name}, priority={self.priority})"

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def __repr__(self):
        return f"PriorityQueue({self.heap})"

    def push(self, item):
        """Add an item to the priority queue."""
        heapq.heappush(self.heap, item)

    def pop(self):
        """Remove and return the item with the highest priority. Raises an IndexError if the queue is empty."""
        if self.is_empty():
            raise IndexError("Pop from an empty priority queue")
        return heapq.heappop(self.heap)

    def peek(self):
        """Return the item with the highest priority without removing it. Raises an IndexError if the queue is empty."""
        if self.is_empty():
            raise IndexError("Peek from an empty priority queue")
        return self.heap[0]

    def is_empty(self):
        """Return True if the priority queue is empty, False otherwise."""
        return len(self.heap) == 0

    def size(self):
        """Return the number of items in the priority queue."""
        return len(self.heap)

# Example usage
pq = PriorityQueue()
pq.push(Item("task1", 3))
pq.push(Item("task2", 1))
pq.push(Item("task3", 2))

print("Priority Queue:", pq)  # Output: PriorityQueue([Item(name=task2, priority=1), Item(name=task3, priority=2), Item(name=task1, priority=3)])

print("Highest priority item:", pq.peek())  # Output: Highest priority item: Item(name=task2, priority=1)

print("Popped item:", pq.pop())  # Output: Popped item: Item(name=task2, priority=1)
print("Priority Queue after pop:", pq)  # Output: PriorityQueue([Item(name=task3, priority=2), Item(name=task1, priority=3)])

print("Is priority queue empty?", pq.is_empty())  # Output: Is priority queue empty? False
print("Priority queue size:", pq.size())  # Output: Priority queue size: 2
