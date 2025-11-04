#Martian Explorer

matrix = []

for row in range (6):
    rowData = [i for i in input().split()]
    matrix.append(rowData)

startRow = 0
startCol = 0

#Determine the start index
for row in range (len(matrix)):
    for col in range (len(matrix[row])):
        if matrix[row][col] == "E":
            startRow = row
            startCol = col

cmds = input().split(', ')

waterDeposit = 0
metalDeposit = 0
concreteDeposit = 0

for cmd in cmds:

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

    deposits = {'W': 'Water', 'M': "Metal", "C": 'Concrete'}
    
    if newPosition in deposits:
        print (f"{deposits[newPosition]} deposit found at ({currentRow}, {currentCol})")
        if newPosition == 'W':
            waterDeposit += 1
        elif newPosition == "M":
            metalDeposit += 1
        elif newPosition == "C":
            concreteDeposit += 1

    elif newPosition == "R":
        print (f"Rover got broken at ({currentRow}, {currentCol})")
        break
        
    startRow = currentRow
    startCol = currentCol

if waterDeposit > 0 and metalDeposit > 0 and concreteDeposit > 0:
    print (f"Area suitable to start the colony.")
else:
    print (f"Area not suitable to start the colony.")



