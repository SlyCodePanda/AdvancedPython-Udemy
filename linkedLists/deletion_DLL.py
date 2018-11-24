class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new = Node(value)
        new.next = self.head

        if self.head is not None:
            self.head.prev = new

        self.head = new

    # node = where to start printing from.
    def printing(self, node):
        while node is not None:
            print(node.data)
            node = node.next

    def remove(self, node):
        if node.prev is None:
            # Make new variable and make it equal to the node after the deletion node.
            x = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            y = node.prev
        else:
            node.next.prev = node.prev


# Create.
x = LinkedList()

# Add.
x.add(2)
x.add(3)
x.add(4)
x.add(5)

# Remove.
x.remove(x.head.next) # Remove 4.

# Print.
x.printing(x.head)
