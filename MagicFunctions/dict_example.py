# We want to be able to add two dictionaries together. This can not be done with regular operators.
# e.g print(dict1 + dict2) will fail.


# Class that inherits from dict.
class Dictionary(dict):
    def __add__(self, other):
        self.update(other)
        return Dictionary(self)


dict1 = Dictionary({'firstName': 'Renee'})
dict2 = Dictionary({'lastName': 'Marsland'})

print(dict1 + dict2)