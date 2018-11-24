class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Doubly Linked List.
class LinkedList:
    def __init__(self):
        self.head = None

    # Add values to DLL at the beginning.
    def add(self, value):
        # Create new node.
        a = Node(value)
        # The next value after the newly added value is now the head.
        a.next = self.head

        # If the head is not None, the previous node is the new node.
        if self.head is not None:
            self.head.prev = a

        # The new value a is the new head.
        self.head = a

    def printing(self, node):
        # Iterate through list and print the data.
        while node is not None:
            print(node.data)
            last = node
            node = node.next

# Create.
x = LinkedList()

# Add.
x.add("Marvel")
x.add("DC")
x.add("Image")
x.add("Dark Horse")

# Print.
x.printing(x.head)
