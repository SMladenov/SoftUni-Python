#Mouse In The Kitchen

rows, cols = [int(i) for i in input().split(',')]

matrix = []

for row in range(rows):
    rowData = [i for i in input()]
    matrix.append(rowData)

startRow = 0
startCol = 0
totalCheese = 0

#Determine the start index
for row in range (len(matrix)):
    for col in range (len(matrix[row])):
        if matrix[row][col] == "M":
            startRow = row
            startCol = col
        elif matrix[row][col] == "C":
            totalCheese += 1

#print (f"Row: {startRow} Col: {startCol} {matrix[startRow][startCol]}\nTotal Cheese: {totalCheese}")

cmd = input()

while cmd != "danger":

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
        print (f"No more cheese for tonight!")
        break

    newPosition = matrix[currentRow][currentCol]
    
    if newPosition == "@":
        cmd = input()
        continue

    elif newPosition == "T":
        matrix[startRow][startCol] = "*"
        matrix[currentRow][currentCol] = "M"
        print (f"Mouse is trapped!")
        break

    elif newPosition == "C":
        totalCheese -= 1
        if totalCheese == 0:
            matrix[startRow][startCol] = "*"
            matrix[currentRow][currentCol] = "M"
            print (f"Happy mouse! All the cheese is eaten, good night!")
            break

    matrix[startRow][startCol] = "*"
    matrix[currentRow][currentCol] = "M"
    startRow = currentRow
    startCol = currentCol
    
    cmd = input()

if cmd == "danger":
    print("Mouse will come back later!")

for row in matrix:
    print("".join(row))
