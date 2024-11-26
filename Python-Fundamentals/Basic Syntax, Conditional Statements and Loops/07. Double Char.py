#Double Char

inputStr = input()

while inputStr != "End":
    if inputStr != "SoftUni":
        for i in inputStr:
            print (f"{i * 2}", end = "")
        print()
    inputStr = input()
