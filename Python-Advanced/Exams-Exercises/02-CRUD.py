#CRUD

matrix = []

for row in range (6):
    rowData = [i for i in input().split()]
    matrix.append(rowData)

startRow, startCol = map(int, input().strip("()").split(", "))

cmd = input()

while cmd != "Stop":

    cmdSplit = cmd.split(', ')
    action = cmdSplit[0]
    direction = cmdSplit[1]
    
    currentRow = startRow
    currentCol = startCol
    
    if direction == "up":
        currentRow -= 1
    elif direction == "down":
        currentRow += 1
    elif direction == "left":
        currentCol -= 1
    elif direction == "right":
        currentCol += 1
         
    newPosition = matrix[currentRow][currentCol]

    if action == "Create":
        newValue = cmdSplit[2]
        if newPosition == ".":
            matrix[currentRow][currentCol] = newValue

    elif action == "Update":
        newValue = cmdSplit[2]
        if newPosition.isalpha() or newPosition.isdigit():
            matrix[currentRow][currentCol] = newValue

    elif action == "Delete":
        if newPosition.isalpha() or newPosition.isdigit():
            matrix[currentRow][currentCol] = "."

    elif action == "Read":
        if newPosition.isalpha() or newPosition.isdigit():
            print (f"{newPosition}")
            
    startRow = currentRow
    startCol = currentCol
    
    cmd = input()

for row in matrix:
    print(" ".join(row))
