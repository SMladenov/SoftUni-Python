#Mouse In The Kitchen

def printMatrix (matrix):
    for row in matrix:
        print (f"{' '.join(map(str, row))}")

n, m = map(int, input().split(','))

matrix = []

for i in range (n):
    rowData = [i for i in input()]
    matrix.append(rowData)

printMatrix(matrix)

cmd = input()

while cmd != "danger":
    indexMouse = matrix[0].index('M')

    cmd = input()
