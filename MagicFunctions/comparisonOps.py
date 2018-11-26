# Overloading the comparison operators.
class Comparison:
    def __init__(self, x):
        self.x = x

    # Less than.
    def __lt__(self, other):
        return self.x < other.x

    # Greater than.
    def __gt__(self, other):
        return self.x > other.x

    # Equal to.
    def __eq__(self, other):
        return self.x == other.x

if __name__ == '__main__':
    obj1 = Comparison(2)
    obj2 = Comparison(4)
    print(obj1 < obj2)
    print(obj1 > obj2)
    print(obj1 == obj2)