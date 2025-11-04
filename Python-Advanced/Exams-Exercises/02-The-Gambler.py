#The Gambler

rows = int(input())

matrix = []

for row in range(rows):
    rowData = [i for i in input()]
    matrix.append(rowData)

startRow = 0
startCol = 0

#Determine the start index
for row in range (len(matrix)):
    for col in range (len(matrix[row])):
        if matrix[row][col] == "G":
            startRow = row
            startCol = col

cmd = input()

cash = 100
wasted = False

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
        
    #Check for going outside
    if currentRow < 0 or currentRow >= len(matrix) or currentCol < 0 or currentCol >= len(matrix[currentRow]):
        print (f"Game over! You lost everything!")
        wasted = True
        break

    newPosition = matrix[currentRow][currentCol]

    if newPosition == "-":
        matrix[startRow][startCol] = '-'
        matrix[currentRow][currentCol] = 'G'
            
    elif newPosition == "W":
        matrix[startRow][startCol] = '-'
        matrix[currentRow][currentCol] = 'G'
        cash += 100
            
    elif newPosition == "P":
        cash -= 200
        matrix[startRow][startCol] = '-'
        matrix[currentRow][currentCol] = 'G'
        if cash <= 0:
            print("Game over! You lost everything!")
            wasted = True
        break
        
    elif newPosition == "J":
        matrix[startRow][startCol] = '-'
        matrix[currentRow][currentCol] = 'G'
        cash += 100000
        print (f"You win the Jackpot!")
        break

    startRow = currentRow
    startCol = currentCol

    cmd = input()

if not wasted:
    print (f"End of the game. Total amount: {cash}$")
    for row in matrix:
        print("".join(row))
