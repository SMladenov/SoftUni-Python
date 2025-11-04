#Collecting Stars Game

rows = int(input())

matrix = []

for row in range(rows):
    rowData = [i for i in input().split()]
    matrix.append(rowData)

startRow = 0
startCol = 0
starsCollected = 2

#Determine the start index
for row in range (len(matrix)):
    for col in range (len(matrix[row])):
        if matrix[row][col] == "P":
            startRow = row
            startCol = col


while True:
    cmd = input()
    
    currentRow = startRow
    currentCol = startCol
    obstacle = False
    
    if cmd == "up":
        currentRow -= 1
    elif cmd == "down":
        currentRow += 1
    elif cmd == "left":
        currentCol -= 1
    elif cmd == "right":
        currentCol += 1

    if currentRow < 0 or currentRow >= len(matrix) or currentCol < 0 or currentCol >= len(matrix[currentRow]):
        currentRow = 0
        currentCol = 0
    
    newPosition = matrix[currentRow][currentCol]

    if newPosition == '*':
        matrix[startRow][startCol] = '.'
        matrix[currentRow][currentCol] = 'P'
        starsCollected += 1
        if starsCollected == 10:
            print (f"You won! You have collected 10 stars.")
            print (f"Your final position is [{currentRow}, {currentCol}]")
            break
            
    elif newPosition == '.':
        matrix[startRow][startCol] = '.'
        matrix[currentRow][currentCol] = 'P'
            
    elif newPosition == '#':
        obstacle = True
        starsCollected -= 1
        if starsCollected == 0:
            print (f"Game over! You are out of any stars.")
            print (f"Your final position is [{startRow}, {startCol}]")
            break


    if not obstacle:
        startRow = currentRow
        startCol = currentCol


for row in matrix:
    print(" ".join(row))
