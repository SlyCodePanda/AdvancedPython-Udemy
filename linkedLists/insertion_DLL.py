class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Doubly Linked List.
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new = Node(value)
        new.next = self.head

        if self.head is not None:
            self.head.prev = new

        self.head = new

    # Add value to the end of the list.
    def append(self, value):
        new = Node(value)
        new.next = None

        # If the node we want to append is the head node.
        if self.head is None:
            new.prev = None
            self.head = new
            return

        # else, iterate through entire list until we reach the end, where we append the new node.
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next

        pointer.next = new
        new.prev = pointer
        return

    def printing(self, node):
        while node is not None:
            print(node.data)
            node = node.next

    # Insert value after given node.
    def insertion(self, node, value):
        new = Node(value)
        new.next = node.next
        node.next = new
        new.prev = node

        if new.next is not None:
            new.next.prev = new


# Create.
x = LinkedList()

# Add.
x.add(2)
x.add(5)
x.add(7)
x.add(9)

# Insert.
x.insertion(x.head.next, 12)

# Append.
x.append(20)

# Print.
x.printing(x.head)
