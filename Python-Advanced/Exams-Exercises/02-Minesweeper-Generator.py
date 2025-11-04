#Minesweeper Generator

rows = int(input())

matrix = []

for row in range(rows):
    rowData = ["0" for i in range (rows)]
    matrix.append(rowData)

bombs = int(input())

for _ in range (bombs):
    startRow, startCol = map(int, input().strip("()").split(", "))
    matrix[startRow][startCol] = "*"


for rowIndex in range (0, len(matrix)):
    for colIndex in range (0, len(matrix[rowIndex])):

        if matrix[rowIndex][colIndex] != "*":
            currentRow = rowIndex
            currentCol = colIndex
            currentBombsAround = 0
    
            #Check Up
            if currentRow - 1 >= 0:
                if matrix[currentRow - 1][currentCol] == "*":
                    currentBombsAround += 1
                    
            #Check Down
            if currentRow + 1 <= len(matrix) - 1:
                if matrix[currentRow + 1][currentCol] == "*":
                    currentBombsAround += 1
                    
            #Check Left
            if currentCol - 1 >= 0:
                if matrix[currentRow][currentCol - 1] == "*":
                    currentBombsAround += 1
    
            #Check Right
            if currentCol + 1 <= len(matrix[rowIndex]) - 1:
                if matrix[currentRow][currentCol + 1] == "*":
                    currentBombsAround += 1

            #Check Main Diagonal
            #Up Left
            if currentRow - 1 >= 0 and currentCol - 1 >= 0:
                if matrix[currentRow - 1][currentCol - 1] == "*":
                    currentBombsAround += 1
            #Down Right
            if currentRow + 1 <= len(matrix) - 1 and currentCol + 1 <= len(matrix[rowIndex]) - 1:
                if matrix[currentRow + 1][currentCol + 1] == "*":
                    currentBombsAround += 1

            #Check Secondary Diagonal
            #Up Right
            if currentRow - 1 >= 0 and currentCol + 1 <= len(matrix[rowIndex]) - 1:
                if matrix[currentRow - 1][currentCol + 1] == "*":
                    currentBombsAround += 1
            
            #Down Left
            if currentRow + 1 <= len(matrix) - 1 and currentCol - 1 >= 0:
                if matrix[currentRow + 1][currentCol - 1] == "*":
                    currentBombsAround += 1

            matrix[currentRow][currentCol] = currentBombsAround


for row in matrix:
    print(" ".join(map(str, row)))


