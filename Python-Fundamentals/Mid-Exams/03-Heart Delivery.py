#Heart Delivery

inputStr = [int(i) for i in input().split('@')]
cmd = input()
lastHouse = 0
startIndex = 0

while cmd != "Love!":
    jumpSplit = cmd.split(' ')
    jumpLength = int(jumpSplit[1])
    newIndex = startIndex + jumpLength
    
    if newIndex >= len(inputStr):
        startIndex = 0
        currentValue = inputStr[0]
        lastHouse = 0
        if currentValue != 0:
            inputStr[0] -= 2
            if inputStr[0] == 0:
                print (f"Place {0} has Valentine's day.")
        elif currentValue == 0:
            print (f"Place {0} already had Valentine's day.")
    else:
        currentValue = inputStr[newIndex]
        startIndex = newIndex
        lastHouse = newIndex
        if currentValue != 0:
            inputStr[newIndex] -= 2
            if (currentValue - 2) == 0:
                print (f"Place {newIndex} has Valentine's day.")
        elif currentValue == 0:
            print (f"Place {newIndex} already had Valentine's day.")
    cmd = input()

checkIfSuccessfull = [i for i in inputStr if i != 0]
if len(checkIfSuccessfull) > 0:
    print (f"Cupid's last position was {lastHouse}.\nCupid has failed {len(checkIfSuccessfull)} places.")
else:
    print (f"Cupid's last position was {lastHouse}.\nMission was successful.")