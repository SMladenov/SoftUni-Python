#2x2 Squares in Matrix

rowNum, colNum = map(int, input().split())

matrix = []
squaresFound = 0

for r in range (rowNum):
    rData = [i for i in input().split()]
    matrix.append(rData)

for rIndex in range (0, len(matrix) - 1):
    for cIndex in range (0, len(matrix[rIndex]) - 1):
        char1 = matrix[rIndex][cIndex]
        char2 = matrix[rIndex + 1][cIndex]
        char3 = matrix[rIndex][cIndex + 1]
        char4 = matrix[rIndex + 1][cIndex + 1]
        if char1 == char2 == char3 == char4:
            squaresFound += 1

print (f"{squaresFound}")
