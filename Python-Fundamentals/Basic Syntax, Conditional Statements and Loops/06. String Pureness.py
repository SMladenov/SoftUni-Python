#String Pureness

numberStrings = int(input())
listElements = [',', '.', '_']

isPure = True

for i in range (numberStrings):
    givenString = input()
    isPure = True
    for b in givenString:
        if b in listElements:
            isPure = False
            print (f"{givenString} is not pure!")
            break
    if isPure:
        print (f"{givenString} is pure.")
