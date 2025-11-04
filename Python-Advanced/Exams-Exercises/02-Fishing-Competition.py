#Fishing Competition

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
        if matrix[row][col] == "S":
            startRow = row
            startCol = col

cmd = input()

fishCought = 0
whirlpool = False

while cmd != "collect the nets":
    
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
        if currentRow < 0:
            currentRow = len(matrix) - 1
        elif currentRow >= len(matrix):
            currentRow = 0
        elif currentCol < 0:
            currentCol = len(matrix[currentRow]) - 1
        elif currentCol >= len(matrix[currentRow]):
            currentCol = 0
        
    newPosition = matrix[currentRow][currentCol]

    if newPosition == "W":
        print (f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{currentRow},{currentCol}]")
        whirlpool = True
        break

    elif newPosition.isdigit():
        fishCought += int(newPosition)
        matrix[startRow][startCol] = '-'
        matrix[currentRow][currentCol] = 'S'
        
    elif newPosition == "-":
        matrix[startRow][startCol] = '-'
        matrix[currentRow][currentCol] = 'S'

    startRow = currentRow
    startCol = currentCol

    cmd = input()

if not whirlpool:
    if fishCought >= 20:
        print (f"Success! You managed to reach the quota!")
    elif fishCought < 20:
        print (f"You didn't catch enough fish and didn't reach the quota! You need {20 - fishCought} tons of fish more.")
    if fishCought != 0:
        print (f"Amount of fish caught: {fishCought} tons.")
            
    for row in matrix:
        print("".join(row))
