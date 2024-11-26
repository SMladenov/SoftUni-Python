#Race

import re

listNames = input().split(', ')
dicResults = {}

pattern1 = r"\d+"
pattern2 = r"[a-zA-Z]"

cmd = input()

while cmd != "end of race":
    total = 0
    listName = re.findall(pattern2, cmd)
    listScore = re.findall(pattern1, cmd)

    name = ""

    for i in listName:
        name += i
    for i in listScore:
        if len(i) > 1:
            for b in i:
                total += int(b)
        else:
            total += int(i)

    if name in listNames:
        if name not in dicResults.keys():
            dicResults[name] = total
        else:
            dicResults[name] += total
    
    cmd = input()


position = 1
for key, value in dicResults.items():
    if position < 4:
        getTheKey = max(dicResults, key=dicResults.get)
        if position == 1:
            print (f"{position}st place: {getTheKey}")
        elif position == 2:
            print (f"{position}nd place: {getTheKey}")
        elif position == 3:
            print (f"{position}rd place: {getTheKey}")
        dicResults[getTheKey] = 0
    else:
        break
    position += 1