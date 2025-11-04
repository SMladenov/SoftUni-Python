#Delivery Boy

rows, cols = [int(i) for i in input().split()]

matrix = []

for row in range(rows):
    rowData = [i for i in input()]
    matrix.append(rowData)

memoryFirstRow = 0
memoryFirstCol = 0
boyRow = 0
boyCol = 0

#Determine the start index
for row in range (len(matrix)):
    for col in range (len(matrix[row])):
        if matrix[row][col] == "B":
            boyRow = row
            boyCol = col
            memoryFirstRow = row
            memoryFirstCol = col

cmd = input()

while True:

    currentRow = boyRow
    currentCol = boyCol

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
        matrix[memoryFirstRow][memoryFirstCol] = " "
        print (f"The delivery is late. Order is canceled.")
        break

    newPosition = matrix[currentRow][currentCol]

    if newPosition == "*":
        cmd = input()
        continue

    elif newPosition == "-":
        matrix[currentRow][currentCol] = "."

    elif newPosition == "P":
        matrix[currentRow][currentCol] = "R"
        print (f"Pizza is collected. 10 minutes for delivery.")

    elif newPosition == "A":
        matrix[currentRow][currentCol] = "P"
        print (f"Pizza is delivered on time! Next order...")
        break
        
    boyRow = currentRow
    boyCol = currentCol

    cmd = input()

for row in matrix:
    print("".join(row))
