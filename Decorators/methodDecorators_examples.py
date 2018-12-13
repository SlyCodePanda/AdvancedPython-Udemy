# === Example 01 ===


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



# === Example 02 ===
# Writing a decorator that will work for methods OR functions using args and kwargs.


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
