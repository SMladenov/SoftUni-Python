#Space Mission

rows = int(input())

matrix = []

for row in range(rows):
    rowData = [i for i in input().split()]
    matrix.append(rowData)

startRow = 0
startCol = 0
units = 100

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

    #Check for going outside
    if currentRow < 0 or currentRow >= len(matrix) or currentCol < 0 or currentCol >= len(matrix[currentRow]):
        print (f"Mission failed! The spaceship was lost in space.")
        break

    newPosition = matrix[currentRow][currentCol]
    units -= 5
    
    if newPosition == ".":
        if matrix[startRow][startCol] != "R":
            matrix[startRow][startCol] = "."
        matrix[currentRow][currentCol] = "S"
        
    elif newPosition == "R":
        matrix[startRow][startCol] = "."
        units += 10
        if units > 100:
            units = 100
        
    elif newPosition == "M":
        units -= 5
        matrix[startRow][startCol] = "."
        matrix[currentRow][currentCol] = "S"
    
    elif newPosition == "P":
        if matrix[startRow][startCol] != "R":
            matrix[startRow][startCol] = "."
        print (f"Mission accomplished! The spaceship reached Planet B with {units} resources left.")
        break
        
    if units < 5:
        print (f"Mission failed! The spaceship was stranded in space.")
        break

    startRow = currentRow
    startCol = currentCol

for row in matrix:
    print(" ".join(row))
