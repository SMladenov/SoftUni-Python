#Matrix of Palindromes

rowNum, colNum = [int(i) for i in input().split()]

matrix = []
charPrimary = 97
charMiddle = 97

for rIndex in range (0, rowNum):
    rowData = []
    matrix.append(rowData)
    for cIndex in range (0, colNum):
        colData = f"{chr(charPrimary)}{chr(charMiddle)}{chr(charPrimary)}"
        matrix[rIndex].append(colData)
        charMiddle += 1

    charPrimary += 1
    charMiddle = charPrimary

for _ in matrix:
    print (f"{' '.join(_)}")
