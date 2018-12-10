# Example 01


class x:
    def __init__(self):
        print("An instance or object was initialized")

    def __call__(self, *args, **kwargs):
        print("Arguments are ", args, kwargs)


a = x()
print("Calling Objects or Arguments")
# Use call function.
a(4, 5, z=12, v=20)
# Using the a object, we can call the 'call' function.

print("Calling Objects or Arguments AGAIN")
a(8, 9, r=30, t=40)


# Example 02


# Using a function decorator.
def x():
    print("Doing something using function decorators")
    def y():
        # Returns the name of this 'x'.
        print("Naming " + x.__name__)
    return y

def repeatable():
    outer = x()
    inner = outer()


repeatable()


# Example 03


class y:
    def __init__(self):
        print("Doing something using class decorator")

    def __call__(self, *args, **kwargs):
        print("naming " + x.__name__)


def repeatable():
    outer = y()
    outer()


repeatable()
