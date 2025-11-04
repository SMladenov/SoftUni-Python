#Rotate Matrix

class MatrixContentError(Exception):
    pass

class MatrixSizeError(Exception):
    pass

def isSquare(matrix):
    square = True
    size = len(matrix)
    for i in matrix:
        if len(i) != size:
            square = False
            break
    return square

def containOnlyInts(row):
    isInt = True
    for i in row:
        if not i.isdigit():
            isInt = False
            break
    return isInt

def rotate_matrix(matrix): 
    matrix_length = len(matrix)

    for indexRow in range(matrix_length): 
        for indexCol in range(indexRow, matrix_length): 
            value1 = matrix[indexRow][indexCol]
            value2 = matrix[indexCol][indexRow]
            matrix[indexRow][indexCol] = value2
            matrix[indexCol][indexRow] = value1

    for i in range(matrix_length): 
        matrix[i].reverse()

mtrx = []
validMtrx = True

while True: 
    line = input().split()
    
    if not line: 
        break 
    try:
        if not containOnlyInts(line):
            raise MatrixContentError("The matrix must consist of only integers")
        mtrx.append([int(i) for i in line])
    except MatrixContentError as e:
        print (e)
        validMtrx = False
        
if validMtrx:
    try:
        if not isSquare(mtrx):
            raise MatrixSizeError("The size of the matrix is not a perfect square")
        rotate_matrix(mtrx)
        for row in mtrx:
            print(*row, sep=' ')
    except MatrixSizeError as e:
        print (e)
