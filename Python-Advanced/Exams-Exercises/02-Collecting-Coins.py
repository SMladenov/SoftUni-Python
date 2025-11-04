#Collecting Coins

import math

rows = int(input())

matrix = []

for row in range (rows):
    rowData = [i for i in input().split()]
    matrix.append(rowData)

startRow = 0
startCol = 0

#Determine the start index
for row in range (len(matrix)):
    for col in range (len(matrix[row])):
        if matrix[row][col] == "P":
            startRow = row
            startCol = col

listAllPositions = []

coins = 0
listAllPositions.append(f"[{startRow}, {startCol}]")

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
        if currentRow < 0:
            currentRow = len(matrix) - 1
        elif currentRow >= len(matrix):
            currentRow = 0
        elif currentCol < 0:
            currentCol = len(matrix[currentRow]) - 1
        elif currentCol >= len(matrix[currentRow]):
            currentCol = 0
    
    newPosition = matrix[currentRow][currentCol]

    listAllPositions.append(f"[{currentRow}, {currentCol}]")
    
    if newPosition.isdigit():
        coins += int(newPosition)
        matrix[currentRow][currentCol] = "P"
        if coins >= 100:
            print (f"You won! You've collected {coins} coins.")
            break
    elif newPosition == "X":
        coins /= 2
        coins = math.floor(coins)
        print (f"Game over! You've collected {coins} coins.")
        break
        
    startRow = currentRow
    startCol = currentCol

print (f"Your path:")
print ('\n'.join(listAllPositions))
