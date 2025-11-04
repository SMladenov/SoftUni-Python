#Matrix Shuffling

rowNum, colNum = [int(i) for i in input().split()]

matrix = []

for rIndex in range (rowNum):
    rowData = [i for i in input().split()]
    matrix.append(rowData)

cmd = input().split()

while cmd[0] != "END":
    if len(cmd) == 5:
        if cmd[0] == "swap":
            row1 = int(cmd[1])
            col1 = int(cmd[2])
            row2 = int(cmd[3])
            col2 = int(cmd[4])

            if 0 <= row1 < rowNum and 0 <= col1 < colNum:
                if 0 <= row2 < rowNum and 0 <= col2 < colNum:
                    value1 = matrix[row1][col1]
                    value2 = matrix[row2][col2]
                    matrix[row1][col1] = value2
                    matrix[row2][col2] = value1

                    for _ in matrix:
                        print (f"{' '.join(_)}")
                    
                else:
                    print (f"Invalid input!")
            else:
                print (f"Invalid input!")
        else:
            print (f"Invalid input!")    
    else:
        print (f"Invalid input!")
    cmd = input().split()
