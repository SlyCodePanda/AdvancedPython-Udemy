class Extended:
    # If no value passed, x = 0 & y = 0 by default.
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Returns self in a designated format when printing.
    def __str__(self):
        # 0 = x, 1 = y
        return "({0},{1})".format(self.x, self.y)

    # +=
    def __iadd__(self, other):
        # x = x + some number
        x = self.x + other.x
        y = self.y + other.y
        return Extended(x, y)

    # -=
    def __isub__(self, other):
        x = self.x = other.x
        y = self.x - other.y
        return Extended(x, y)


obj1 = Extended(4, 3)
obj1 -= Extended(3, 5)

# This will print in vector format because of the overloading __str__ function.
print(obj1)
