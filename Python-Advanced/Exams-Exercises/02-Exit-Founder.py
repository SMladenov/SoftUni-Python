#Exit Founder

player1, player2 = input().split(', ')

matrix = []

for row in range (6):
    rowData = [i for i in input().split()]
    matrix.append(rowData)

cmd = input()
cmdCounter = 0
wallHitPlayer1 = 0
wallHitPlayer2 = 0

while cmd != "":
    cmdCounter += 1
    startRow, startCol = map(int, cmd.strip("()").split(", "))

    newPosition = matrix[startRow][startCol]
    
    if cmdCounter % 2 == 1:
        if wallHitPlayer1 == 1:
            wallHitPlayer1 -= 1
            cmd = input()
            continue
        if newPosition == "E":
            print (f"{player1} found the Exit and wins the game!")
            break
        elif newPosition == "T":
            print (f"{player1} is out of the game! The winner is {player2}.")
            break
        elif newPosition == "W":
            wallHitPlayer1 += 1
            print (f"{player1} hits a wall and needs to rest.")

    elif cmdCounter % 2 == 0:
        if wallHitPlayer2 == 1:
            wallHitPlayer2 -= 1
            cmd = input()
            continue
        if newPosition == "E":
            print (f"{player2} found the Exit and wins the game!")
            break
        elif newPosition == "T":
            print (f"{player2} is out of the game! The winner is {player1}.")
            break
        elif newPosition == "W":
            wallHitPlayer2 += 1
            print (f"{player2} hits a wall and needs to rest.")

    cmd = input()

