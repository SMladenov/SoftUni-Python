#Numbers search

def numbers_searching (*args):

    listNumbers = list(args)
    listNumbers.sort()
    
    listDuplicates = []
    listUniques = []
    missingNumber = 0
    
    while len(listNumbers) > 1:
        firstNumber = listNumbers[0]
        secondNumber = listNumbers[1]
        if firstNumber == secondNumber:
            if firstNumber not in listDuplicates:
                listDuplicates.append(firstNumber)
            listNumbers.pop(0)
            continue

        elif firstNumber + 1 == secondNumber:
            listUniques.append(firstNumber)
            listNumbers.pop(0)
            continue

        elif firstNumber + 1 != secondNumber:
            missingNumber = firstNumber + 1
            listUniques.append(firstNumber)
            listNumbers.pop(0)
            continue
        
    listUniques.append(listNumbers[0])

    listCombined = [missingNumber, listDuplicates]

    return listCombined
    #return f"[{missingNumber}, [{', '.join(map(str, listDuplicates))}]]" #-> Uniques: {', '.join(map(str, listUniques))}"



print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
