#Escape the Maze


rows = int(input())

matrix = []

for row in range(rows):
    rowData = [i for i in input()]
    matrix.append(rowData)

startRow = 0
startCol = 0
health = 100

#Determine the start index
for row in range (len(matrix)):
    for col in range (len(matrix[row])):
        if matrix[row][col] == "P":
            startRow = row
            startCol = col

cmd = input()

while cmd != "end":
    
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
        cmd = input()
        continue
        
    newPosition = matrix[currentRow][currentCol]

    if newPosition == "M":
        matrix[startRow][startCol] = '-'
        matrix[currentRow][currentCol] = 'P'
        health -= 40
        if health <= 0:
            print (f"Player is dead. Maze over!")
            break

    elif newPosition == "-":
        matrix[startRow][startCol] = '-'
        matrix[currentRow][currentCol] = 'P'

    elif newPosition == "H":
        health += 15
        if health > 100:
            health = 100
        matrix[startRow][startCol] = '-'
        matrix[currentRow][currentCol] = 'P'

    elif newPosition == "X":
        matrix[startRow][startCol] = '-'
        matrix[currentRow][currentCol] = 'P'
        print (f"Player escaped the maze. Danger passed!")
        break

    startRow = currentRow
    startCol = currentCol

    cmd = input()

if health <= 0:
    print (f"Player's health: 0 units")
else:
    print (f"Player's health: {health} units")

for row in matrix:
    print("".join(row))
