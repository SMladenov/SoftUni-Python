#Record Unique Names

numberNames = int(input())
setNames = set()

for _ in range (numberNames):
    setNames.add(input())

print ('\n'.join(setNames))