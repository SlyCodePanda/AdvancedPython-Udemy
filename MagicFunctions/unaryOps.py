class Unary:
    def __init__(self, y):
        self.y = y

    def __neg__(self):
        return self.y

    def __pos__(self):
        return self.y

    def __invert__(self):
        return self.y

if __name__ == '__main__':
    obj1 = Unary(-2)

    # Neg.
    print(-obj1)
    # Pos.
    print(+obj1)
    # Invert.
    print(~obj1)

