#Game of Words

randomString = input()

rows = int(input())

matrix = []

for row in range(rows):
    rowData = [i for i in input()]
    matrix.append(rowData)

startRow = 0
startCol = 0

#Determine the start index
for row in range (len(matrix)):
    for col in range (len(matrix[row])):
        if matrix[row][col] == "P":
            startRow = row
            startCol = col

numberCmds = int(input())

for _ in range (numberCmds):
    cmd = input()

    currentRow = startRow
    currentCol = startCol
    
    if cmd == "up":
        currentRow -= 1
    elif cmd == "down":
        currentRow += 1
    elif cmd == "left":
        currentCol -= 1
    elif cmd == "right":
        currentCol += 1

    #Check for going outside
    if currentRow < 0 or currentRow >= len(matrix) or currentCol < 0 or currentCol >= len(matrix[currentRow]):
        if randomString != "":
            randomString = randomString[:len(randomString) - 1]
        continue

    newPosition = matrix[currentRow][currentCol]

    if newPosition != "-" and newPosition != "P":
        randomString += newPosition
        matrix[startRow][startCol] = "-"
        matrix[currentRow][currentCol] = "P"

    elif newPosition == "-" or newPosition == "P":
        matrix[startRow][startCol] = "-"
        matrix[currentRow][currentCol] = "P"
    
    startRow = currentRow
    startCol = currentCol


print (f"{randomString}")
for row in matrix:
    print("".join(row))
