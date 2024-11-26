#Stock

inputStr = input().split(' ')
dict = {}
for i in range (0, len(inputStr), + 2):
    key = inputStr[i]
    value = int(inputStr[i + 1])
    dict[key] = value

inputStr2 = input().split(' ')
for i in inputStr2:
    if i in dict.keys():
        print (f"We have {dict[i]} of {i} left")
    else:
        print (f"Sorry, we don't have {i}")