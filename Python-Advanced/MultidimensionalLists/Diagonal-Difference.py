#Diagonal Difference

import math

numRows = int(input())

matrix = []

for row in range (numRows):
    rowData = [int(i) for i in input().split()]
    matrix.append(rowData)

sumPrimaryDiagonal = 0
sumSecondaryDiagonal = 0

for rowIndex in range (len(matrix)):
    for colIndex in range (len(matrix[rowIndex])):
        if rowIndex == colIndex:
            sumPrimaryDiagonal += matrix[rowIndex][colIndex]

for rowIndex in range (len(matrix)):
    colIndex = (len(matrix[rowIndex]) - 1) - rowIndex
    sumSecondaryDiagonal += matrix[rowIndex][colIndex]

print (f"{abs(sumPrimaryDiagonal - sumSecondaryDiagonal)}")
