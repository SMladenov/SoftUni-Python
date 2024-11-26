#Bakery

inputStr = input().split(' ')
dict = {}
for i in range (0, len(inputStr), + 2):
    key = inputStr[i]
    value = int(inputStr[i + 1])
    dict[key] = value

print (f"{dict}")