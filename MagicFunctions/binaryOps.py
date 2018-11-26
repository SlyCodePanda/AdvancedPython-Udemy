class Binary:
    def __init__(self, *arguments):
        if len(arguments) == 0:
            # Vector of (0, 0)
            self.numbers = (0, 0)
        else:
            self.numbers = arguments

    # Returns the vector addition of self (# of args received) and other.
    # '+' is now overloaded.
    def __add__(self, other):
        sum = tuple(x + y for x, y in zip(self.numbers, other.numbers))
        # (1, 5)
        # (2, 3)
        # Output = (3, 8)
        return Binary(*sum)

    def __mul__(self, other):
        mul = tuple(x * y for x, y in zip(self.numbers, other.numbers))
        return Binary(*mul)

    def __sub__(self, other):
        sub = tuple(x + y for x, y in zip(self.numbers, other.numbers))
        return Binary(*sub)

# Addition.
obj1 = Binary(2, 3)
obj2 = Binary(4, 5)
obj3 = Binary(3, 5)
# Because of our magic function '__add__', the '+' symbol is now overloaded to run what we have defined in the magic
# function. In our case we have told it to add vectors.
obj4 = obj1 + obj2 + obj3
print(obj4.numbers)

# Multiply.
obj5 = obj1 * obj2 * obj3
print(obj5.numbers)

# Subtract.
obj6 = Binary(3, 4)
obj7 = Binary(1, 2)
obj8 = obj6 - obj7
print(obj8.numbers)
