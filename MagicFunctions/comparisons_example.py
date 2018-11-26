class comp:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        return self.x < other.x

    def __gt__(self, other):
        return self.x > other.x

    def __eq__(self, other):
        return self.x == other.x


if __name__ == '__main__':
    x = comp(2)
    y = comp(5)
    print(x > y)
    print(x < y)
    print(x == y)

