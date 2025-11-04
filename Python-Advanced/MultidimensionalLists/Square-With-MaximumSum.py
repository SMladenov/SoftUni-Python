#Square with Maximum Sum

rowNum, colNum = [int(i) for i in input().split(', ')]

matrix = []

dicSubMatrixes = {}

for row in range (rowNum):
    rowData = [int(i) for i in input().split(', ')]
    matrix.append(rowData)

for rowIndex in range (len(matrix) - 1):
    for colIndex in range (len(matrix[rowIndex]) - 1):
        currentMatrix = [
            [matrix[rowIndex][colIndex], matrix[rowIndex][colIndex + 1]],
            [matrix[rowIndex + 1][colIndex], matrix[rowIndex + 1][colIndex + 1]]
        ]

        sumCurrentMatrix = sum([sum(el) for el in currentMatrix])

        if sumCurrentMatrix not in dicSubMatrixes.keys():
            dicSubMatrixes[sumCurrentMatrix] = currentMatrix

maxSum = max(dicSubMatrixes)
bestMatrix = dicSubMatrixes[maxSum]

for row in bestMatrix:
    print (f"{' '.join(map(str, row))}")
print (f"{maxSum}")
