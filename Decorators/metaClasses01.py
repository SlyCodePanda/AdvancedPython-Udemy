# === Example 01 ===


# In this example we have modified a class using an object of this class.
class x:
    pass


# Then we have attached a variable
x.variable = 10
c = x()

# Then accessed that variable using that object.
print(c.variable)


# === Example 02 ===
# Using the 'type' keyword.


def metaFunc():
    print("I am the meta class function")


class inherit:
    def func(self):
        print("I am the inherited method")


metaObject = type('meta', (inherit, ), dict(name="SomeDict", metafunction=metaFunc))

print(type(metaObject))

# Meta Class object
b = metaObject()

print(type(b))

b.func()

print(b.name)

