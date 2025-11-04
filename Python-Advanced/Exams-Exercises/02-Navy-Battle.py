#Navy Battle

rows = int(input())

matrix = []

for row in range(rows):
    rowData = [i for i in input()]
    matrix.append(rowData)

startRow = 0
startCol = 0
minesHit = 0
batteCruisers = 0

#Determine the start index
for row in range (len(matrix)):
    for col in range (len(matrix[row])):
        if matrix[row][col] == "S":
            startRow = row
            startCol = col

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
         
    newPosition = matrix[currentRow][currentCol]

    if newPosition == "-":
        matrix[startRow][startCol] = "-"
        matrix[currentRow][currentCol] = "S"
        
    elif newPosition == "*":
        minesHit += 1
        matrix[startRow][startCol] = "-"
        matrix[currentRow][currentCol] = "S"
        if minesHit == 3:
            print (f"Mission failed, U-9 disappeared! Last known coordinates [{currentRow}, {currentCol}]!")
            break

    if newPosition == "C":
        batteCruisers += 1
        matrix[startRow][startCol] = "-"
        matrix[currentRow][currentCol] = "S"
        if batteCruisers == 3:
            print (f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

    startRow = currentRow
    startCol = currentCol

for row in matrix:
    print("".join(row))
