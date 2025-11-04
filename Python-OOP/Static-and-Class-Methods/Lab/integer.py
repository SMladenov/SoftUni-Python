from math import floor

class Integer:
    def __init__ (self, value: int):
        self.value = value

    @classmethod
    def from_float (cls, float_value: float) -> int:
        if isinstance(float_value, float):
            return cls(floor(float_value))
        else:
            return f"value is not a float"

    @classmethod
    def from_roman (cls, value) -> int:
        dictRomanValues = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        totalAmount = 0
        previousValue = 0

        for char in reversed(value):
            currentValue = dictRomanValues[char]

            if currentValue < previousValue:
                totalAmount -= currentValue
            else:
                totalAmount += currentValue
            
            previousValue = currentValue

        return cls(totalAmount)

    @classmethod
    def from_string (cls, value) -> int:
        if isinstance(value, str):
            for char in value:
                if not char.isdigit():
                    return f"wrong type"
            return cls(int(value))
        else:
            return f"wrong type"
        






