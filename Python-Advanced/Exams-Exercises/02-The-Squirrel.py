#The Squirrel

rows = int(input())
commands = input().split(', ')

matrix = []

for row in range(rows):
    rowData = [i for i in input()]
    matrix.append(rowData)

startRow = 0
startCol = 0
hazelnuts = 0
hazelnutsCollected = False
gameStopped = False

#Determine the start index
for row in range (len(matrix)):
    for col in range (len(matrix[row])):
        if matrix[row][col] == "s":
            startRow = row
            startCol = col

for cmd in commands:
    
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
        print (f"The squirrel is out of the field.")
        gameStopped = True
        break

    newPosition = matrix[currentRow][currentCol]

    if newPosition == "h":
        hazelnuts += 1
        matrix[startRow][startCol] = "*"
        matrix[currentRow][currentCol] = "s"
        if hazelnuts == 3:
            print (f"Good job! You have collected all hazelnuts!")
            hazelnutsCollected = True
            gameStopped = True
            break

    elif newPosition == "*":
        matrix[startRow][startCol] = "*"
        matrix[currentRow][currentCol] = "s"

    elif newPosition == "t":
        matrix[startRow][startCol] = "*"
        matrix[currentRow][currentCol] = "s"
        print (f"Unfortunately, the squirrel stepped on a trap...")
        gameStopped = True
        break

    startRow = currentRow
    startCol = currentCol

if not hazelnutsCollected and not gameStopped:
    print (f"There are more hazelnuts to collect.")

print (f"Hazelnuts collected: {hazelnuts}")
