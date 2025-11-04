#Rally Racing

rows = int(input())
racingNumber = input()

matrix = []

for row in range(rows):
    rowData = [i for i in input().split()]
    matrix.append(rowData)

startRow = 0
startCol = 0
tunnelStartRow1 = 0
tunnelStartCol1 = 0
tunnelStartRow2 = 0
tunnelStartCol2 = 0
tunnelStart = False

kilometers = 0

#Determine the start index
for row in range (len(matrix)):
    for col in range (len(matrix[row])):
        if matrix[row][col] == "T" and not tunnelStart:
            tunnelStartRow1 = row
            tunnelStartCol1 = col
            tunnelStart = True
        elif matrix[row][col] == "T" and tunnelStart:
            tunnelStartRow2 = row
            tunnelStartCol2 = col


cmd = input()

finished = False

while cmd != "End":

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
    
    if newPosition == ".":
        kilometers += 10
        matrix[startRow][startCol] = "."
        matrix[currentRow][currentCol] = "C"
        # for row in matrix:
        #     print("".join(row))

    elif newPosition == "T":
        kilometers += 30
        if currentRow == tunnelStartRow1 and currentCol == tunnelStartCol1:
            matrix[startRow][startCol] = "."
            matrix[currentRow][currentCol] = "."
            matrix[tunnelStartRow2][tunnelStartCol2] = "C"
            startRow = tunnelStartRow2
            startCol = tunnelStartCol2
            # for row in matrix:
            #     print("".join(row))
            cmd = input()
            continue
        else:
            matrix[startRow][startCol] = "."
            matrix[currentRow][currentCol] = "."
            matrix[tunnelStartRow1][tunnelStartCol1] = "C"
            startRow = tunnelStartRow1
            startCol = tunnelStartCol1
            # for row in matrix:
            #     print("".join(row))
            cmd = input()
            continue

    elif newPosition == "F":
        kilometers += 10
        matrix[startRow][startCol] = "."
        matrix[currentRow][currentCol] = "C"
        print (f"Racing car {racingNumber} finished the stage!")
        finished = True
        # for row in matrix:
        #     print("".join(row))
        break

    startRow = currentRow
    startCol = currentCol
    
    cmd = input()

if cmd == "End" and not finished:
    print (f"Racing car {racingNumber} DNF.")

print (f"Distance covered {kilometers} km.")

for row in matrix:
    print("".join(row))
