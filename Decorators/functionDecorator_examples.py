# === Example 01 ===


def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

my_get_text = p_decorate(get_text)

print(my_get_text("Renee"))


# === Example 02 ===
# Using the Python Decorator Syntax.


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


# === Example 03 ===
# Say we wanted to decorate our get_text function with 2 other functions, to wrap a div and a strong tag
# around the string output.


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


# === Example 04 ===
# Passing arguments to decorator to remove redundant code.


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


# === Example 05 ===
# Using functools.wraps


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
