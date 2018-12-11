# === Example 01 ===


# This Cel class is our descriptor class.
class Cel:
    # Get the temp.
    def __get__(self, instance, owner):
        return 5*(instance.x - 32)/9

    # Set the temp.
    def __set__(self, instance, value):
        instance.x = 32 + 9 * value / 5


class Temp:
    y = Cel()

    def __init__(self, x):
        self.x = x


t = Temp(112)
print(t.y)
t.y = 0
print(t.x)
