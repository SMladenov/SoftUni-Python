#Replace Repeating Chars

inputStr = input()

finalStr = ""

for i in range(0, len(inputStr) - 1):
    if inputStr[i] != inputStr[i + 1]:
        finalStr += inputStr[i]
finalStr += inputStr[len(inputStr) - 1]
        
print (f"{finalStr}")