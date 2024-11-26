#Center Point

import math

def closerPoint (x1, y1, x2, y2):
    listValues = [x1, y1, x2, y2]
    for index, i in enumerate(listValues):
        if i < 0:
            listValues[index] *= -1
    if (listValues[0] + listValues[1]) < (listValues[2] + listValues[3]):
        return f"({math.floor(x1)}, {math.floor(y1)})"
    elif (listValues[0] + listValues[1]) > (listValues[2] + listValues[3]):
        return f"({math.floor(x2)}, {math.floor(y2)})"
    elif (listValues[0] + listValues[1]) == (listValues[2] + listValues[3]):
        return f"({math.floor(x1)}, {math.floor(y1)})"
        
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print (f"{closerPoint(x1, y1, x2, y2)}")
