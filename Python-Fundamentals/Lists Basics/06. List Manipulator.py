#List Manipulator

listInput = input().split(' ')
cmd = input()

while cmd != "end":
    cmdSplit = cmd.split(' ')
    #Condition 1
    if cmdSplit[0] == "exchange":
        index = int(cmdSplit[1])
        if index >= len(listInput) or index < 0:
            print (f"Invalid index")
        else:
            listInput = listInput[index + 1:] + listInput[:index + 1]
            
    #Condition 2
    if cmdSplit[0] == "max":
        if cmdSplit[1] == "even":
            tempList = [int(i) for i in listInput if int(i) % 2 == 0]
            tempList.reverse()
            if tempList:
                maxNum = max(tempList)
                print(f"{len(listInput) - 1 - listInput[::-1].index(str(maxNum))}")
            else:
                print ("No matches")
        elif cmdSplit[1] == "odd":
            tempList = [int(i) for i in listInput if int(i) % 2 == 1]
            tempList.reverse()
            if tempList:
                maxNum = max(tempList)
                print(f"{len(listInput) - 1 - listInput[::-1].index(str(maxNum))}")
            else:
                print ("No matches")
    #Condition 3
    if cmdSplit[0] == "min":
        if cmdSplit[1] == "even":
            tempList = [int(i) for i in listInput if int(i) % 2 == 0]
            tempList.reverse()
            if tempList:
                minNum = min(tempList)
                print(f"{len(listInput) - 1 - listInput[::-1].index(str(minNum))}")
            else:
                print ("No matches")
        elif cmdSplit[1] == "odd":
            tempList = [int(i) for i in listInput if int(i) % 2 == 1]
            tempList.reverse()
            if tempList:
                minNum = min(tempList)
                print(f"{len(listInput) - 1 - listInput[::-1].index(str(minNum))}")
            else:
                print ("No matches")
    #Condition 4
    if cmdSplit[0] == "first":
        if cmdSplit[2] == "even":
            tempList = [int(i) for i in listInput if int(i) % 2 == 0]
            numberOfElements = int(cmdSplit[1])
            if numberOfElements > len(listInput):
                print (f"Invalid count")
            elif tempList:
                if numberOfElements <= len(tempList):
                    print (f"{tempList[:numberOfElements]}")
                else:
                    print (f"{tempList}")
            else:
                print (f"[]")
        if cmdSplit[2] == "odd":
            tempList = [int(i) for i in listInput if int(i) % 2 == 1]
            numberOfElements = int(cmdSplit[1])
            if numberOfElements > len(listInput):
                print (f"Invalid count")
            elif tempList:
                if numberOfElements <= len(tempList):
                    print (f"{tempList[:numberOfElements]}")
                else:
                    print (f"{tempList}")
            else:
                print (f"[]")
    #Condition 5
    if cmdSplit[0] == "last":
        if cmdSplit[2] == "even":
            tempList = [int(i) for i in listInput if int(i) % 2 == 0]
            tempList.reverse()
            numberOfElements = int(cmdSplit[1])
            if numberOfElements > len(listInput):
                print (f"Invalid count")
            elif tempList:
                if numberOfElements <= len(tempList):
                    print (f"{tempList[:numberOfElements]}")
                else:
                    print (f"{tempList}")
            else:
                print (f"[]")
        if cmdSplit[2] == "odd":
            tempList = [int(i) for i in listInput if int(i) % 2 == 1]
            tempList.reverse()
            numberOfElements = int(cmdSplit[1])
            if numberOfElements > len(listInput):
                print (f"Invalid count")
            elif tempList:
                if numberOfElements <= len(tempList):
                    print (f"{tempList[:numberOfElements]}")
                else:
                    print (f"{tempList}")
            else:
                print (f"[]")
                
    cmd = input()

print (f"[{', '.join(listInput)}]")