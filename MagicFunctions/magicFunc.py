class x:
    # Anything with a double underscore at the front and end is a "magic method/function".
    # This init function is called automatically when you create an instance of this class.
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

obj1 = x(3, 4)
print(obj1.sum())

obj2 = x(4, 2)
print(obj2.sum())
