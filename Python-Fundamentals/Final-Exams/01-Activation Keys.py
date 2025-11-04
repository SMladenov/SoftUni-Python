#Activation Keys

inputKey = input()

cmd = input()

while cmd != "Generate":
    cmdSplit = cmd.split(">>>")
    action = cmdSplit[0]
    if action == "Contains":
        substring = cmdSplit[1]
        if substring in inputKey:
            print (f"{inputKey} contains {substring}")
        else:
            print (f"Substring not found!")
    if action == "Flip":
        action2 = cmdSplit[1]
        startIndex = int(cmdSplit[2])
        endIndex = int(cmdSplit[3])
        if action2 == "Upper":
            inputKey = inputKey[:startIndex] + inputKey[startIndex:endIndex].upper() + inputKey[endIndex:]
            print (f"{inputKey}")
        elif action2 == "Lower":
            inputKey = inputKey[:startIndex] + inputKey[startIndex:endIndex].lower() + inputKey[endIndex:]
            print (f"{inputKey}")
    if action == "Slice":
        startIndex = int(cmdSplit[1])
        endIndex = int(cmdSplit[2])
        inputKey = inputKey[:startIndex] + inputKey[endIndex:]
        print (f"{inputKey}")
    cmd = input()

print (f"Your activation key is: {inputKey}")