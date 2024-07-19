class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        if not self.head:
            return "Empty list"
        
        nodes = []
        current = self.head
        while True:
            nodes.append(repr(current))
            current = current.next
            if current == self.head:
                break
        return " -> ".join(nodes) + " -> ..."

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete_node(self, key):
        if not self.head:
            return
        
        current = self.head
        previous = None

        # Handle case where the node to delete is the head
        if current.data == key:
            if current.next == self.head:  # Only one node in the list
                self.head = None
            else:
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return

        # Traverse the list to find the node to delete
        previous = current
        current = current.next
        while current != self.head:
            if current.data == key:
                previous.next = current.next
                current = None
                return
            previous = current
            current = current.next

    def search(self, key):
        if not self.head:
            return None
        
        current = self.head
        while True:
            if current.data == key:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def traverse(self):
        if not self.head:
            print("Empty list")
            return
        
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

# Example usage
cll = CircularLinkedList()
cll.insert_at_beginning(3)
cll.insert_at_end(5)
cll.insert_at_beginning(2)
cll.insert_at_end(7)
print("Circular Linked List: ", cll)  # Output: Node(2) -> Node(3) -> Node(5) -> Node(7) -> ... 
cll.traverse()  # Output: 2 -> 3 -> 5 -> 7 -> (head)
cll.delete_node(3)
print("Circular Linked List after deleting 3: ", cll)  # Output: Node(2) -> Node(5) -> Node(7) -> ...
cll.traverse()  # Output: 2 -> 5 -> 7 -> (head)
node = cll.search(5)
print("Search result: ", node)  # Output: Node(5)
