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
Another this that can be done with decorator functions is checking the validity of arguments passed using a decorator function.<br>
```python

```