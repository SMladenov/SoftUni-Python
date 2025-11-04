#Magic Triangle

def get_magic_triangle (number):
    matrix = [[1], [1, 1]]

    for row in range (2, number):
        rowData = [1, 1]
        for col in range (1, len(matrix[row - 1])):
            dataToInsert = matrix[row - 1][col - 1] + matrix[row - 1][col]
            rowData.insert(col, dataToInsert)

        matrix.append(rowData)
        
    return matrix
        
get_magic_triangle(5)
