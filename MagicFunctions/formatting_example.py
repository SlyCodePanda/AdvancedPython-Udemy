# Converting to metres (m)
class LengthConversion:
    value = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000, "inch": 0.0254,
             "ft": 0.3048, "yd": 0.9144, "mi": 1609.344}

    def convertToMetres(self):
        return self.x * LengthConversion.value[self.valueUnit]

    def __init__(self, x, valueUnit="m"):
        self.x = x
        self.valueUnit = valueUnit

    # Add terms.
    def __add__(self, other):
        ans = self.convertToMetres() + other.convertToMetres()
        return LengthConversion(ans/LengthConversion.value[self.valueUnit], self.valueUnit)

    # Convert to string.
    def __str__(self):
        return str(self.convertToMetres())

    # Evaluate the output in certain format (repr = representation)
    def __repr__(self):
        return "LengthConversion(" + str(self.x) + " , "+ self.valueUnit + ")"


# Main function.
if __name__ == '__main__':
    # Convert 5.5 yards into metres.
    obj1 = LengthConversion(5.5, "yd") + LengthConversion(1)
    print(repr(obj1))
    print(obj1)