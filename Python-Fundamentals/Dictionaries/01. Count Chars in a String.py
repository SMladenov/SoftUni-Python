#Count Chars in a String

inputStr = input()

dictOccurancies = {}

for i in inputStr:
    if i != " ":
        if i not in dictOccurancies.keys():
            dictOccurancies[i] = 1
        else:
            dictOccurancies[i] += 1

for key, value in dictOccurancies.items():
    print (f"{key} -> {value}")