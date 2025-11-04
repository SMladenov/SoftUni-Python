#Darts

player1, player2 = input().split(', ')

matrix = []

for row in range (7):
    rowData = [i for i in input().split()]
    matrix.append(rowData)

cmdCounter = 0
pointsPlayer1 = 501
pointsPlayer2 = 501
turnsPlayer1 = 0
turnsPlayer2 = 0

while True:

    cmdCounter += 1
    currentRow, currentCol = map(int, input().strip("()").split(", "))

    #Check for going outside
    if currentRow < 0 or currentRow >= len(matrix) or currentCol < 0 or currentCol >= len(matrix[currentRow]):
        continue

    newPosition = matrix[currentRow][currentCol]

    if newPosition == "B":
        if cmdCounter % 2 == 1:
            turnsPlayer1 += 1
            print (f"{player1} won the game with {turnsPlayer1} throws!")
            break
        else:
            turnsPlayer2 += 1
            print (f"{player2} won the game with {turnsPlayer2} throws!")
            break
    
    elif newPosition.isdigit():
        if cmdCounter % 2 == 1:
            turnsPlayer1 += 1
            pointsPlayer1 -= int(newPosition)
            if pointsPlayer1 <= 0:
                print (f"{player1} won the game with {turnsPlayer1} throws!")
                break
        else:
            turnsPlayer2 += 1
            pointsPlayer2 -= int(newPosition)
            if pointsPlayer2 <= 0:
                print (f"{player2} won the game with {turnsPlayer2} throws!")
                break

    elif newPosition == "D" or newPosition == "T":
        totalPoints = 0
        totalPoints += (int(matrix[currentRow][0]) + int(matrix[currentRow][len(matrix[currentRow]) - 1]) + int(matrix[0][currentCol]) +
                        int(matrix[len(matrix) - 1][currentCol]))
        if newPosition == "D":
            totalPoints *= 2
        elif newPosition == "T":
            totalPoints *= 3

        if cmdCounter % 2 == 1:
            turnsPlayer1 += 1
            pointsPlayer1 -= totalPoints
            if pointsPlayer1 <= 0:
                print (f"{player1} won the game with {turnsPlayer1} throws!")
                break
        else:
            turnsPlayer2 += 1
            pointsPlayer2 -= totalPoints
            if pointsPlayer2 <= 0:
                print (f"{player2} won the game with {turnsPlayer2} throws!")
                break



