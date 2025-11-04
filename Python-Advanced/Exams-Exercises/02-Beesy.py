#Beesy

rows = int(input())

matrix = []

for row in range(rows):
    rowData = [i for i in input()]
    matrix.append(rowData)

startRow = 0
startCol = 0
energy = 15
nectarCollected = 0
energyRestored = False

#Determine the start index
for row in range (len(matrix)):
    for col in range (len(matrix[row])):
        if matrix[row][col] == "B":
            startRow = row
            startCol = col

while True:
    cmd = input()

    currentRow = startRow
    currentCol = startCol
    energy -= 1
    
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

            
    if newPosition == "H":
        matrix[startRow][startCol] = '-'
        matrix[currentRow][currentCol] = 'B'
        if nectarCollected >= 30:
            print (f"Great job, Beesy! The hive is full. Energy left: {energy}")
            break
        else:
            print (f"Beesy did not manage to collect enough nectar.")
            break

    elif newPosition == '-':
        matrix[startRow][startCol] = '-'
        matrix[currentRow][currentCol] = 'B'

    elif newPosition.isdigit():
        nectarCollected += int(newPosition)
        matrix[startRow][startCol] = '-'
        matrix[currentRow][currentCol] = 'B'
            
    if energy <= 0:
        if nectarCollected >= 30 and not energyRestored:
            energy += nectarCollected - 30
            energyRestored = True
            if energy == 0:
                print (f"This is the end! Beesy ran out of energy.")
                break
        else:
            print (f"This is the end! Beesy ran out of energy.")
            break
    
    startRow = currentRow
    startCol = currentCol

for row in matrix:
    print("".join(row))
