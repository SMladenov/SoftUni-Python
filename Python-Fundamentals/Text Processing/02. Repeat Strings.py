#Repeat Strings

inputStr = input().split(' ')

finalStr = ""

for i in inputStr:
    finalStr += len(i) * i

print (f"{finalStr}")