#Next Happy Year

import sys

year = int(input())
maxNumber = sys.maxsize


for i in range (year + 1, maxNumber):
    isDistinct = True
    strYear = str(i)
    for c in range (0, len(strYear) - 1):
        for b in range (c + 1, len(strYear)):
            if strYear[c] == strYear[b]:
                isDistinct = False
                break
        if not isDistinct:
            break
    if isDistinct:
        print(i)
        break
    