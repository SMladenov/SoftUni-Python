#Take/Skip Rope

inputStr = input()

nums = [i for i in inputStr if i.isdigit()]
chars = [i for i in inputStr if not i.isdigit()]

takeList = [int(i) for index,i in enumerate(nums) if index % 2 == 0]
skipList = [int(i) for index,i in enumerate(nums) if index % 2 == 1]

finalString = ""
currentIndex = 0

for index,i in enumerate(takeList):
    take = int(takeList[index])
    skip = int(skipList[index])
    for b in range (currentIndex, (currentIndex + take)):
        if b >= len(chars):
            break
        finalString += chars[b]

    currentIndex += (take + skip)

#print (f"{nums}\n{chars}\n{takeList}\n{skipList}")
print (f"{finalString}")
