#Tribonacci Sequence

def tribonacci (number):
    if number >= 4:
        finalList = [1, 1, 2]
        listNums = [1, 1, 2]
        for i in range (0, number - 3):
            tempNum = sum(listNums)
            listNums[0] = listNums[1]
            listNums[1] = listNums[2]
            listNums[2] = tempNum
            finalList.append(tempNum)
        return finalList
    else:
        allNums = [1]
        for i in range (1, number):
            temp = sum(allNums)
            allNums.append(temp)
        return allNums

number = int(input())

result = tribonacci(number)

for i in result:
    print (f"{i}", end = " ")
    