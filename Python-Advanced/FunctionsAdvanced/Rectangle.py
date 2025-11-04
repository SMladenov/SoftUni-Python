#Rectangle

def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return f"Enter valid values!"
    else:
        def area():
            return f"Rectangle area: {length * width}"
        def perimeter():
            return f"Rectangle perimeter: {2 * (length + width)}"
            
        return f"{area()}\n{perimeter()}"