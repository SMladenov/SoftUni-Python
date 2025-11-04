#Sum Matrix Columns

rowIndex, colIndex = [int(i) for i in input().split(', ')]

matrix = []

for row in range (rowIndex):
    rowData = [int(i) for i in input().split()]
    matrix.append(rowData)

for col in range (colIndex):
    sum = 0
    for row in range (rowIndex):
        sum += matrix[row][col]
    print (f"{sum}")
