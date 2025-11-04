#Memory Game

elements = input().split(' ')
cmd = input()

moves = 0
isWinner = False

while cmd != "end":
    cmdSplit = cmd.split(' ')
    index1 = int(cmdSplit[0])
    index2 = int(cmdSplit[1])
    moves += 1
    inRange = False
    equalIndexes = False

    if index1 == index2:
        equalIndexes = True
        inRange = True
        strToAdd = f"-{moves}a"
        indexToAdd = len(elements) // 2
        elements.insert(indexToAdd, strToAdd)
        elements.insert(indexToAdd + 1, strToAdd)
        print (f"Invalid input! Adding additional elements to the board")
        
    if 0 <= index1 <= (len(elements) - 1) and 0 <= index2 <= (len(elements) - 1) and not equalIndexes:
        inRange = True
        value = elements[index1]
        if elements[index1] == elements[index2]:
            print (f"Congrats! You have found matching elements - {elements[index1]}!")
            if index1 > index2:
                elements.pop(index1)
                elements.pop(index2)
            else:
                elements.pop(index2)
                elements.pop(index1)
        else:
            print ("Try again!")

    if not inRange:
        strToAdd = f"-{moves}a"
        indexToAdd = len(elements) // 2
        elements.insert(indexToAdd, strToAdd)
        elements.insert(indexToAdd + 1, strToAdd)
        print (f"Invalid input! Adding additional elements to the board")
        
    if len(elements) == 0:
        print (f"You have won in {moves} turns!")
        isWinner = True
        break
    cmd = input()

if cmd == "end" and not isWinner:
    print (f"Sorry you lose :(\n{' '.join(elements)}")