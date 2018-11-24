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

    # Insert node at the beginning of list.
    def insert_beg(self, data4):
        # Create new node.
        new = Node(data4)
        # Create connection. The head is now the new node created.
        new.next = self.head
        self.head = new

    # Insert node at the end of the list.
    def insert_end(self, data5):
        newest = Node(data5)
        # check if this is the head node.
        if self.head is None:
            self.head = newest
            return
        # Go to the end of the list.
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        # When lastNode.next points to Null, assign the next value as newest.
        lastNode.next = newest

    # Insert node after given node.
    def insert_between(self, node, data):
        newOfAll = Node(data)
        # Make connection.
        newOfAll.next = node.next
        node.next = newOfAll

# === Create ===
x = LinkedList()
x.head = Node("Renee Marsland")
data2 = Node("Adelaide")
data3 = Node("Australia")

# === Connect ===
x.head.next = data2
data2.next = data3

# === Insert ===
x.insert_beg("VFX Layout TD")
x.insert_end("2018")
# Insert after x.head.next ("VFX Layout TD"(HEAD) -> "Renee Marsland" -> "+===========+")
x.insert_between(x.head.next, "+===========+")
# Insert "Rising Sun Pictures" after head node.
x.insert_between(x.head, "Rising Sun Pictures")

# === Print ===
x.printing()

