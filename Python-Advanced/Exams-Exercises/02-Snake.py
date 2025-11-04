#Snake

rows = int(input())

matrix = []

for row in range(rows):
    rowData = [i for i in input()]
    matrix.append(rowData)

startRow = 0
startCol = 0
foodQuantity = 0
startRowBurrow1 = 0
startColBurrow1 = 0
startRowBurrow2 = 0
startColBurrow2 = 0

burrowFound = False

#Determine the start index
for row in range (len(matrix)):
    for col in range (len(matrix[row])):
        if matrix[row][col] == "S":
            startRow = row
            startCol = col
        elif matrix[row][col] == "B" and not burrowFound:
            startRowBurrow1 = row
            startColBurrow1 = col
            burrowFound = True
        elif matrix[row][col] == "B" and burrowFound:
            startRowBurrow2 = row
            startColBurrow2 = col
            

while True:

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
        matrix[startRow][startCol] = "."
        print (f"Game over!")
        break
    
    newPosition = matrix[currentRow][currentCol]

    if newPosition == "-":
        matrix[startRow][startCol] = "."
        matrix[currentRow][currentCol] = "S"
        
    elif newPosition == "*":
        foodQuantity += 1
        matrix[startRow][startCol] = "."
        matrix[currentRow][currentCol] = "S"
        if foodQuantity == 10:
            print (f"You won! You fed the snake.")
            break

    elif newPosition == "B":
        if currentRow == startRowBurrow1 and currentCol == startColBurrow1:
            matrix[startRow][startCol] = "."
            matrix[startRowBurrow1][startColBurrow1] = "."
            matrix[startRowBurrow2][startColBurrow2] = "S"
            startRow = startRowBurrow2
            startCol = startColBurrow2
            continue
        else:
            matrix[startRow][startCol] = "."
            matrix[startRowBurrow2][startColBurrow2] = "."
            matrix[startRowBurrow1][startColBurrow1] = "S"
            startRow = startRowBurrow1
            startCol = startColBurrow1
            continue

    

    startRow = currentRow
    startCol = currentCol

print (f"Food eaten: {foodQuantity}")
for row in matrix:
    print("".join(row))
