#String Explosion

inputStr = input()

finalStr = ""

explosion = 0

for i in range (0, len(inputStr)):
    if inputStr[i] == '>':
        if inputStr[i + 1].isdigit():
            explosion += int(inputStr[i + 1])
            finalStr += ">"
    elif explosion > 0:
        explosion -= 1
    else:
        finalStr += inputStr[i]

print (f"{finalStr}")