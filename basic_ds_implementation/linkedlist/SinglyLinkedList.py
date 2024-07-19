class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return " -> ".join(nodes)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        current = self.head

        # If the head node itself holds the key to be deleted
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key to be deleted, keep track of the previous node
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next

        # If the key was not present in the list
        if not current:
            return

        # Unlink the node from the linked list
        previous.next = current.next
        current = None

    def search(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next
        return current

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
ll.insert_at_beginning(3)
ll.insert_at_end(5)
ll.insert_at_beginning(2)
ll.insert_at_end(7)
print("Linked List: ", ll)  # Output: Node(2) -> Node(3) -> Node(5) -> Node(7)
ll.traverse()  # Output: 2 -> 3 -> 5 -> 7 -> None
ll.delete_node(3)
print("Linked List after deleting 3: ", ll)  # Output: Node(2) -> Node(5) -> Node(7)
ll.traverse()  # Output: 2 -> 5 -> 7 -> None
node = ll.search(5)
print("Search result: ", node)  # Output: Node(5)
