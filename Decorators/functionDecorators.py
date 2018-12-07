# === Function inside a function ===


def addition(a, b):
    def add(x, y):
        return x + y

    sum = "The sum of the two numbers is " + str(add(a, b))
    return sum


ans = addition(2, 3)
print(ans)

# === Passing a function as an argument to another function ===


def x(func):
    print("I am the function x")


def y():
    print('I am the function y')


x(y())

# === A function returning another function ===


# Find result of polynomial.
def poly(a, b, c):
    def pol(x):
        return a * x**2 + b*x + c

    return pol


ans1 = poly(1, 2, 3)
ans2 = poly(5, 6, 7)
# Initialize the x value for pol function.
z = ans1(4)
v = ans2(5)

# a = 1, b = 2, c = 3, x = 4
print(z)
# a = 5, b = 6, c = 7, x = 5
print(v)
