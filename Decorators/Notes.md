# Decorators (Meta Programming)

## Meta Programming (Intro)
Writing programs that manipulate programs.<br>
Programs that read, transforms and analyzes other programs.<br>
### Features of Meta Programming
* Decorators
* Class Decorators
* Meta Classes

## Decorators (Intro)
A function that changes the functionality of other functions.
### Types of Decorators
* Function Decorators
* Class Decorators

## Function Decorators
### Features
* Function inside a function
* Function as an argument
* Return function

<b>A function inside a function.</b>
```python
def outside_function():
    def inside_function():
        print("I am the inside function")
        
    print("I am the outside function.")
    inside_function()

outside_function()
```
<b>Passing a function as an argument to another function.</b>
```python
def x(func):
    print("I am the function x")

def y():
    print('I am the function y')

x(y())
```
<b>A function returning another function.</b>
```python
def outer_function(a):
    def inner_function(b):
        return a + b

    return inner_function


z = outer_function(2)
v = outer_function(3)

ans1 = z(4)
ans2 = v(5)

print(ans1)
print(ans2)
```
Prints <b>6</b> (4 + 2) & <b>8</b> (5 + 3)

## More on function decorators
In previous examples we have had to use multiple lines of code to define objects for both the inner and outer functions.<br>
In the below example we can get rid of the extra lines by <b>encapsulating</b> function decorators.<br>
```python
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

```
This will print out 'Hello Renee' and 'Hello Dan'.<p>
You can also add attributes to an existing function:
```python
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
```
This will print '11'.<p>

## Class Decorators
<u>What are args</u>?:<br>
Used to pass a variable number of arguments to a function.<br>
It allows you to take in more arguments than the number of formally declared arguments previously defined.<br>
Within <b>*args</b>, any number of extra arguments can be tacked on to your current formal parameters.<p>

<u>What are kwargs</u>?<br>
The special syntax <b>**kwargs</b> in function definitions in python is used to pass a keyworded, variable-length argument list.<br>
You can think of the kwargs as being a <b>dictionary</b> that maps each keyword to the value that we pass alongside it.<p>
e.g:<br>
```python
class x:
    def __init__(self):
        print("An instance or object was initialized")

    def __call__(self, *args, **kwargs):
        print("Arguments are ", args, kwargs)


a = x()
print("Calling Objects or Arguments")
# Use call function.
a(4, 5, z=12, v=20)
```
This code will return:
```text
An instance or object was initialized
Calling Objects or Arguments
Arguments are  (4, 5) {'z': 12, 'v': 20}
```

## Meta Classes
The instance of a class is called a "Meta Class".<br>

### Creating Meta Classes
Here is a basic example of a meta class:<br>
```python
# In this example we have modified a class using an object of this class.
class x:
    pass


# Then we have attached a variable
x.variable = 10
c = x()

# Then accessed that variable using that object.
print(c.variable)
```

We Can also create meta objcts using the 'type' keyword:<br>
```python
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
```

This code will print the following:<br>
```text
<class 'type'>
<class '__main__.meta'>
I am the inherited method
SomeDict
```