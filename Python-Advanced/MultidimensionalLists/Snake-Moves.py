#Snake Moves 2

rowNum, colNum = [int(i) for i in input().split()]

matrix = []

randomMsg = input()

currentChar = 0

for rIndex in range (0, rowNum):
    rowData = [''] * colNum
    matrix.append(rowData)
    
    for cIndex in range (0, colNum):
        if rIndex % 2 == 0:
            matrix[rIndex][cIndex] = randomMsg[currentChar]
        else:
            matrix[rIndex][(colNum - 1) - cIndex] = randomMsg[currentChar]
        
        currentChar += 1
        if currentChar > len(randomMsg) - 1:
            currentChar = 0

for _ in matrix:
    print (f"{''.join(_)}")
