#Emoticon Finder

inputStr = input()

for i in range (0, len(inputStr)):
    if inputStr[i] == ':' and i < (len(inputStr) - 1):
        print (f"{inputStr[i] + inputStr[i + 1]}")