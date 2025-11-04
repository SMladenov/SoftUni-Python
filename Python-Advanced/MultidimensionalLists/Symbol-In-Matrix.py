#Symbol in Matrix

numRows = int(input())

matrix = []

for row in range (numRows):
    rowData = [i for i in input()]
    matrix.append(rowData)

symbol = input()

isFound = False

for rowIndex in range (len(matrix)):
    for colIndex in range (len(matrix[rowIndex])):
        if matrix[rowIndex][colIndex] == symbol:
            print (f"({rowIndex}, {colIndex})")
            isFound = True
            break
    if isFound:
        break

if not isFound:
    print (f"{symbol} does not occur in the matrix")
