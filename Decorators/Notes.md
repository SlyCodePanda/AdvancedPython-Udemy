# Decorators (Meta Programming)

## Meta Programming (Intro)
Decorators dynamically alter the functionality of a function, method, or class without having to directly use subclasses.<br>
This is ideal when you need to extend the functionality of functions that you don't want to modify.<br>
### Features of Meta Programming
* Decorators
* Class Decorators
* Meta Classes

## Decorators (Intro)
A function that changes the functionality of other functions.<br>
A decorator expects to recieve a function as an argument.<br>
### Types of Decorators
* Function Decorators
* Class Decorators

## Function Decorators
### Features of Python Functions
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
Function decorators are simply wrappers to existing functions. Putting the ideas mentioned above together, we can build a decorator.<br>
In this example let's consider a function that wraps the string output of another function by p tags (paragraph tags).<br>
```python
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

my_get_text = p_decorate(get_text)

print(my_get_text("Renee"))
```
This will output:
```text
<p>lorem ipsum, Renee dolor sit amet</p>
```
That is a decorator. A function that takes another function as an argument, generates a new function, augmenting the work of the original function,<br>
and returning the generated function so we can use it anywhere.

## Python's Decorator Syntax
The name of the decorator should be prefaced with an @ symbol:<br>
```python
# The function decorator.
def p_decorate(func):
    # The wrapper function.
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper


# The function we are decorating with the p_decorate function.
# We can use "@p_decorate" instead of the above "my_get_text = p_decorate(get_text)".
@p_decorate
def get_text(name):
    return "lorem ipsum, {} dolor sit amet".format(name)


print(get_text("Renee"))
```
This does the exact same as the code above printing:
```text
<p>lorem ipsum, Renee dolor sit amet</p>
```
But with that delicious syntactical sugar.<p>

Now lets say we wanted to decorate our get_text function with 2 other functions, to wrap a div and a strong tag around the string output.<br>
```python
# Paragraph decorator.
def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper


# Strong decorator.
def strong_decorator(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper


# Div decorator.
def div_decorator(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper


# Now instead of having to write "get_text = div_decorate(p_decorate(strong_decorate(get_text)))" to decorate the
# get_text function, we can use Python's decorator syntax:
@div_decorator
@p_decorate
@strong_decorator
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)


print(get_text("Renee"))
```
This will print out:
```text
<div><p><strong>lorem ipsum, Renee dolor sit amet</strong></p></div>
```
<b>Note</b> : It is important to remember that the order of setting our decorators matters.

## Method Decorators
In Python, methods are functions that expect their first parameter to be a reference to the current object (self).<br>
We can build decorators for methods the same way, while taking self into consideration in the wrapper function.<br>
```python
def p_decorate(func):
    def func_wrapper(self):
        return "<p>{0}</p>".format(func(self))
    return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "Renee"
        self.family = "Marsland"

    @p_decorate
    def get_fullname(self):
        return self.name + " " + self.family


my_person = Person()
print(my_person.get_fullname())
```
This will return : 
```text
<p>Renee Marsland</p>
```
<p>

A much better approach would be to make our decorator useful for functions AND methods alike.<br>
This can be done by putting <b>*args and **kwargs</b> as parameters for the wrapper, then it can accept any arbitrary number of arguments and keyword arguments.<p>
<i>Side Note:----------------------------------------------------------------------------------------------------------------------------</i><br>
<u>What are args</u>?:<br>
Used to pass a variable number of arguments to a function.<br>
It allows you to take in more arguments than the number of formally declared arguments previously defined.<br>
Within <b>*args</b>, any number of extra arguments can be tacked on to your current formal parameters.<p>

<u>What are kwargs</u>?<br>
The special syntax <b>**kwargs</b> in function definitions in python is used to pass a keyworded, variable-length argument list.<br>
You can think of the kwargs as being a <b>dictionary</b> that maps each keyword to the value that we pass alongside it.<br>
<i>------------------------------------------------------------------------------------------------------------------------------------------</i><p>

```python
def p_decorate(func):
    def func_wrapper(*args, **kwargs):
        return "<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "Renee"
        self.family = "Marsland"

    @p_decorate
    def get_fullname(self):
        return self.name + " " + self.family


my_person = Person()

print(my_person.get_fullname())
```

## Passing arguments to decorators
Looking back at the example above when using the 3 decorators (div_decorate, p_decorate, strong_decorate), you can see the code is a little redundant.<br>
Lets try and have a more general implementation that takes the tag to wrap with as a string.<br>
```python
def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</0>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags("p")
def get_text(name):
    return "Hello " + name


print(get_text("Renee"))
```
We had to create that extra function "tags" to take the extra argument, as decorators expect to receive a function as their argument,<br>
but this code is far more efficient than the one we had above with the three separate decorators.<p>

## Debugging decorated functions
Wrapping our functions can be problematic in the case of debugging as the wrapper function does not carry the name, module, and docstring of the<br>
original function.<br>
We can reset them within the func_wrapper but Python provides a much nicer way with <b>Functools</b>.

### Using Functools.wraps
Wraps is a decorator for updating the attributes of the wrapping function (func_wrapper) to those of the original function (get_text).<br>
This is as simple as decorating func_wrapper by "@wraps(func)" :<br>
```python
from functools import wraps

def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags("p")
def get_text(name):
    """returns some text"""
    return "Hello" + name


print(get_text.__name__) # get_text
print(get_text.__doc__) # returns some text
print(get_text.__module__) # __main__
```
Using this will allow you to get the correct attributes for get_text.<p>

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


#### Refs
https://www.thecodeship.com/patterns/guide-to-python-function-decorators/