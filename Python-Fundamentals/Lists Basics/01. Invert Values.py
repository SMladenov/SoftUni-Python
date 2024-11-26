#Invert Values

inputStr = input()

listExample = inputStr.split(' ')
for i in range (0, len(listExample)):
    listExample[i] = int(listExample[i]) * -1

print (listExample)
