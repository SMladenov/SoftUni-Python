#Odd Occurrences

listItems = input().split(' ')
listItems = [i.lower() for i in listItems]

dict1 = {}

for i in listItems:
    if i in dict1.keys():
        dict1[i] += 1
    else:
        dict1[i] = 1

dictOddValues = {key: value for key, value in dict1.items() if value % 2 != 0}
#dictSorted = dict(sorted(dictOddValues.items(), key=lambda item: item[1], reverse=True))

for key in dictOddValues.keys():
    print (f"{key}", end = ' ')