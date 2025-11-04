#SoftUni Bar Income

import re

patternName = r"\b(?<=%)[A-Z][a-z]+(?=%)\b"
patternProduct = r"\b(?<=<)\w+(?=>)\b"
patternQuantity = r"\b(?<=\|)\d+(?=\|)\b"
patternPrice = r"(?<!\d)\d+(?:[.]\d+)*(?=\$)"

cmd = input()

totalIncome = 0

while cmd != "end of shift":
    listName = re.findall(patternName, cmd)
    listProduct = re.findall(patternProduct, cmd)
    listQuantity = re.findall(patternQuantity, cmd)
    listPrice = re.findall(patternPrice, cmd)
    
    if listName and listProduct and listQuantity and listPrice:
        productOf = (int(listQuantity[0]) * float(listPrice[0]))
        totalIncome += productOf
        print (f"{listName[0]}: {listProduct[0]} - {productOf:.2f}")
    cmd = input()

print (f"Total income: {totalIncome:.2f}")
