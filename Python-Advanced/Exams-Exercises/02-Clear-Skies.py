#Clear Skies

rows = int(input())

matrix = []

for row in range(rows):
    rowData = [i for i in input()]
    matrix.append(rowData)

startRow = 0
startCol = 0
enemyPlanes = 0
initialArmor = 300

#Determine the start index
for row in range (len(matrix)):
    for col in range (len(matrix[row])):
        if matrix[row][col] == "J":
            startRow = row
            startCol = col
        if matrix[row][col] == "E":
            enemyPlanes += 1

cmd = input()

while cmd != "end":
    
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
        matrix[startRow][startCol] = '-'
        matrix[currentRow][currentCol] = 'J'

    elif newPosition == "R":
        initialArmor = 300
        matrix[startRow][startCol] = '-'
        matrix[currentRow][currentCol] = 'J'

    elif newPosition == "E":
        matrix[startRow][startCol] = '-'
        matrix[currentRow][currentCol] = 'J'
        if enemyPlanes > 1:
            initialArmor -= 100
            if initialArmor <= 0:
                print (f"Mission failed, your jetfighter was shot down! Last coordinates [{currentRow}, {currentCol}]!")
                break
            else:
                enemyPlanes -= 1
        else:
            print (f"Mission accomplished, you neutralized the aerial threat!")
            break
        
    startRow = currentRow
    startCol = currentCol

    cmd = input()


for row in matrix:
    print("".join(row))
