#Sorting Names

listInput = input().split(', ')

sortedList = sorted(listInput, key=lambda i: (-len(i), i))

print (f"{sortedList}")