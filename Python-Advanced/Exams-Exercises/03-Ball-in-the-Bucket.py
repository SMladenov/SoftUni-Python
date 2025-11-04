#Ball in the Bucket

def getScore (points):
    dicScores = {100 <= points <= 199: "Football", 200 <= points <= 299: "Teddy Bear", points >= 300: "Lego Construction Set"}
    return dicScores.get(True, None)

matrix = []
points = 0

for row in range (6):
    rowData = [i for i in input().split()]
    matrix.append(rowData)

for i in range (3):
    currentRow, currentCol = map(int, input().strip("()").split(", "))

    if currentRow < 0 or currentRow >= len(matrix) or currentCol < 0 or currentCol >= len(matrix[currentRow]):
        continue
    else:
        if matrix[currentRow][currentCol] == "B":
            tempPoints = 0
            for row in range (0, len(matrix)):
                if matrix[row][currentCol].isdigit():
                    tempPoints += int(matrix[row][currentCol])
            points += tempPoints
            matrix[currentRow][currentCol] = "H"

score = getScore(points)

if score is None:
    print (f"Sorry! You need {100 - points} points more to win a prize.")
else:
    print (f"Good job! You scored {points} points, and you've won {score}.")




