#Bomb Has Been Planted

rows, cols = [int(i) for i in input().split(', ')]

matrix = []

for row in range(rows):
    rowData = [i for i in input()]
    matrix.append(rowData)


initialStartRow = 0
initialStartCol = 0
startRow = 0
startCol = 0
seconds = 16

#Determine the start index
for row in range (len(matrix)):
    for col in range (len(matrix[row])):
        if matrix[row][col] == "C":
            startRow = row
            startCol = col
            initialStartRow = row
            initialStartCol = col
            
onBomb = False

while True:
    cmd = input()
    
    currentRow = startRow
    currentCol = startCol
    defuse = False
    
    if cmd == "up":
        currentRow -= 1
    elif cmd == "down":
        currentRow += 1
    elif cmd == "left":
        currentCol -= 1
    elif cmd == "right":
        currentCol += 1
    elif cmd == "defuse":
        defuse = True
        if matrix[currentRow][currentCol] != "B":
            seconds -= 2
            if seconds <= 0:
                matrix[currentRow][currentCol] = "*"
                print (f"Terrorists win!\nBomb was not defused successfully!\nTime needed: {0} second/s.")
                break
            continue
        elif matrix[currentRow][currentCol] == "B":
            if seconds - 4 >= 0:
                matrix[currentRow][currentCol] = "D"
                # for row in matrix:
                #     print("".join(row))
                print (f"Counter-terrorist wins!\nBomb has been defused: {seconds - 4} second/s remaining.")
                break
            else:
                matrix[startRow][startCol] = "X"
                print (f"Terrorists win!\nBomb was not defused successfully!")
                print (f"Time needed: {abs(seconds - 4)} second/s.")
                break

    if seconds <= 0:
        print (f"Terrorists win!\nBomb was not defused successfully!\nTime needed: {0} second/s.")
        break
    
    if currentRow < 0 or currentRow >= len(matrix) or currentCol < 0 or currentCol >= len(matrix[currentRow]):
        currentRow = startRow
        currentCol = startCol
    
    newPosition = matrix[currentRow][currentCol]    

    if newPosition == '*':
        if matrix[startRow][startCol] != "B":
            matrix[startRow][startCol] = '*'
        # for row in matrix:
        #     print("".join(row))
    
    elif newPosition == 'B' and not defuse:
        matrix[startRow][startCol] = '*'
        # for row in matrix:
        #     print("".join(row))

    elif newPosition == "T":
        if matrix[startRow][startCol] != "B":
            matrix[startRow][startCol] = '*'
        matrix[currentRow][currentCol] = '*'
        print (f"Terrorists win!")
        # for row in matrix:
        #     print("".join(row))
        break

    if not defuse:
        startRow = currentRow
        startCol = currentCol
        seconds -= 1
    # print (seconds)

matrix[initialStartRow][initialStartCol] = 'C'
for row in matrix:
    print("".join(row))
