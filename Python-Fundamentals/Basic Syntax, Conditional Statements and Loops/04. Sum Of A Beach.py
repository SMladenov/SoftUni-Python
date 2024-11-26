#Sum Of A Beach

randomStr = input().lower()
words = ['sand', 'water', 'fish', 'sun']

counter = 0
exist = True

for i in words:
    while i in randomStr:
        startIndex = randomStr.find(i)
        if startIndex != -1:
            randomStr = randomStr[:startIndex] + randomStr[(startIndex + len(i)):]
            counter += 1

print (f"{counter}")
