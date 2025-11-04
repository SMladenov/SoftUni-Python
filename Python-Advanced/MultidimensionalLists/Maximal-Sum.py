#Maximal Sum

rowNum, colNum = map(int, input().split())

matrix = []

dicSubMatrixes = {}

for row in range (rowNum):
    rowData = [int(i) for i in input().split()]
    matrix.append(rowData)

for rIndex in range (0, len(matrix) - 2):
    for cIndex in range (0, len(matrix[rIndex]) - 2):
        currentSubMatrix = [
            [matrix[rIndex][cIndex], matrix[rIndex][cIndex + 1], matrix[rIndex][cIndex + 2]],
            [matrix[rIndex + 1][cIndex], matrix[rIndex + 1][cIndex + 1], matrix[rIndex + 1][cIndex + 2]],
            [matrix[rIndex + 2][cIndex], matrix[rIndex + 2][cIndex + 1], matrix[rIndex + 2][cIndex + 2]]
        ]

        sumCurrentSubMatrix = sum([sum(el) for el in currentSubMatrix])
        if sumCurrentSubMatrix not in dicSubMatrixes.keys():
            dicSubMatrixes[sumCurrentSubMatrix] = currentSubMatrix

maxSum = max(dicSubMatrixes.keys())
maxSubMatrix = dicSubMatrixes[maxSum]

print (f"Sum = {maxSum}")

for _ in maxSubMatrix:
    print (f"{' '.join(map(str, _))}")
