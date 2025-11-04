#Blind Man's Buff

rows, cols = map(int, input().split())

matrix = []

for row in range(rows):
    rowData = [i for i in input().split()]
    matrix.append(rowData)

startRow = 0
startCol = 0
touchedPlayers = 0
moves = 0

#Determine the start index
for row in range (len(matrix)):
    for col in range (len(matrix[row])):
        if matrix[row][col] == "B":
            startRow = row
            startCol = col

cmd = input()

while cmd != "Finish":

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
    if currentRow < 0 or currentRow >= len(matrix) or currentCol < 0 or currentCol >= len(matrix[currentRow]) or matrix[currentRow][currentCol] == "O":
        cmd = input()
        continue
        
    newPosition = matrix[currentRow][currentCol]

    if newPosition == "-":
        moves += 1
        matrix[startRow][startCol] = "-"
        matrix[currentRow][currentCol] = "B"

    elif newPosition == "P":
        moves += 1
        touchedPlayers += 1
        matrix[startRow][startCol] = "-"
        matrix[currentRow][currentCol] = "B"
        if touchedPlayers == 3:
            break

    startRow = currentRow
    startCol = currentCol
    
    cmd = input()

print (f"Game over!\nTouched opponents: {touchedPlayers} Moves made: {moves}")
