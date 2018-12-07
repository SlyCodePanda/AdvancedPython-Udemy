# === Encapsulation in function decorators ===


def outer_function(a):
    def inner_function(b):
        return a + b
    return inner_function


def repeatable(b):
    x = outer_function("Hello ")
    y = x(b)
    print(y)


repeatable("Renee")
repeatable("Dan")


# === Add attributes to an existing function ===


# Receives a another function as a parameter/attribute.
def join(function):
    # Add data element '2' to passed in function.
    function.data = 2
    return function


# Add 'z' attribute without changing the 'def add(x, y)' line.
def add(x, y):
    return x + y + add.data


join(add)
# Equivalent to passing add(5, 4, 2) but without adding the extra parameter to the add function.
c = add(5, 4)
print(c)


# === Check the validity of arguments passed using a decorator function ===


# e.g 01
# Create a nested function.
def x(a):
    # We need to validate the first passed argument here.
    validate_a = "hello "
    if a is not validate_a:
        print("Not a valid input")

    def y(b):
        # We need to validate the second passed argument here.
        validate_b = "Renee"
        if b is not validate_b:
            print("Not a valid name")

        return a + b

    return y

# Create  a repeatable function to help us encapsulate the code.
def repeatable(a, b):
    c = x(a)
    d = c(b)
    print(d)


repeatable("hey ", "Bilal")


# e.g 02
def argument(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not a positive integer value.")

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


z = factorial(5)
print(z)
