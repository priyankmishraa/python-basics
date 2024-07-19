class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"Node({self.data})"


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return " <-> ".join(nodes)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_node(self, key):
        current = self.head

        # If the head node itself holds the key to be deleted
        if current and current.data == key:
            if current.next:
                self.head = current.next
                self.head.prev = None
            else:
                self.head = None
            return

        # Search for the key to be deleted, keep track of the previous node
        while current and current.data != key:
            current = current.next

        # If the key was not present in the list
        if not current:
            return

        # Unlink the node from the doubly linked list
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
        current = None

    def search(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next
        return current

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        # Move to the end of the list
        current = self.head
        while current and current.next:
            current = current.next
        # Traverse backward from the end
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Example usage
dll = DoublyLinkedList()
dll.insert_at_beginning(3)
dll.insert_at_end(5)
dll.insert_at_beginning(2)
dll.insert_at_end(7)
print("Doubly Linked List: ", dll)  # Output: Node(2) <-> Node(3) <-> Node(5) <-> Node(7)
dll.traverse_forward()  # Output: 2 <-> 3 <-> 5 <-> 7 <-> None
dll.traverse_backward()  # Output: 7 <-> 5 <-> 3 <-> 2 <-> None
dll.delete_node(3)
print("Doubly Linked List after deleting 3: ", dll)  # Output: Node(2) <-> Node(5) <-> Node(7)
dll.traverse_forward()  # Output: 2 <-> 5 <-> 7 <-> None
node = dll.search(5)
print("Search result: ", node)  # Output: Node(5)
