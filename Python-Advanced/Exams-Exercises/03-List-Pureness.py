#List-Pureness

def best_list_pureness (*args):
    listNumbers = list(args[0])
    rotateTimes = args[1]

    dicRotationResults = {}

    for rotation in range (0, rotateTimes + 1):
        rotationSum = 0
        for index, el in enumerate(listNumbers):
            tempSum = el * index
            rotationSum += tempSum
        dicRotationResults[rotation] = rotationSum
        
        valueFirstIndex = listNumbers.pop()
        listNumbers.insert(0, valueFirstIndex)

    sortedRotation = dict(sorted(dicRotationResults.items(), key=lambda x: (-x[1], x[0])))

    for bestRotation, bestPureness in sortedRotation.items():
        return f"Best pureness {bestPureness} after {bestRotation} rotations"

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
