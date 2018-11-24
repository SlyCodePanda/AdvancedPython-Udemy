class Node:
    def __init__(self, datavalue=None):
        self.datavalue = datavalue
        self.nextvalue = None

class LinkedList:
    # On linked list creation, create empty head value.
    def __init__(self):
        self.headvalue = None

    # Print list.
    def printing(self):
        printvalue = self.headvalue
        while printvalue is not None:
            # Print specific value.
            if printvalue.datavalue == "I am well.":
                print(printvalue.datavalue)
                printvalue = printvalue.nextvalue
            # Skip the rest.
            else:
                printvalue = printvalue.nextvalue

# Create linked list.
x = LinkedList()
# Add header nodes with their values.
x.headvalue = Node("Hello there")
data2 = Node("How are you?")
data3 = Node("I am well.")

# Connect the nodes.
# HEAD -> data2
x.headvalue.nextvalue = data2
# HEAD -> data2 -> data3
data2.nextvalue = data3

# Print the linked list.
x.printing()
