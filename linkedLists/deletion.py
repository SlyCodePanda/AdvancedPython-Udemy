class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printing(self):
        printvalue = self.head
        while printvalue is not None:
            print(printvalue.data)
            printvalue = printvalue.next

    def del_Node(self, delData):
        # Create pointer pointing to head.
        new = self.head
        # If the starting data is not None
        if new is not None:
            # If this data on the head node is equal to the data we want to delete. Remove it from the chain.
            if new.data == delData:
                self.head = new.next
                new = None
                return
        # Iterate through the whole list searching for data we want to delete.
        while new is not None:
            # If we find it, break.
            if new.data == delData:
                break
            # prev keeps track of the node before the node we want to delete.
            prev = new
            # new now points to the node after the one we want to delete.
            new = new.next

        if new is None:
            return

        # the node after prev (new) now is the node after the one we want to delete.
        prev.next = new.next
        new = None


# Create list.
x = LinkedList()
x.head = Node("Spider-Man")
data2 = Node("Doctor Strange")
data3 = Node("X-Men")
data4 = Node("Captain Marvel")

# Connections.
x.head.next = data2
data2.next = data3
data3.next = data4

# Delete.
x.del_Node("X-Men")

# Print.
x.printing()