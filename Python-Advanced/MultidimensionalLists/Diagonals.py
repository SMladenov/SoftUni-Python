#Diagonals

numRows = int(input())

matrix = []

for row in range (numRows):
    rowData = [int(i) for i in input().split(', ')]
    matrix.append(rowData)

listPrimaryDiagonal = []
listSecondaryDiagonal = []

for rowIndex in range (len(matrix)):
    for colIndex in range (len(matrix[rowIndex])):
        if rowIndex == colIndex:
            listPrimaryDiagonal.append(matrix[rowIndex][colIndex])

for rowIndex in range (len(matrix)):
    colIndex = (len(matrix[rowIndex]) - 1) - rowIndex
    listSecondaryDiagonal.append(matrix[rowIndex][colIndex])

print (f"Primary diagonal: {', '.join(map(str, listPrimaryDiagonal))}. Sum: {sum(listPrimaryDiagonal)}")
print (f"Secondary diagonal: {', '.join(map(str, listSecondaryDiagonal))}. Sum: {sum(listSecondaryDiagonal)}")
