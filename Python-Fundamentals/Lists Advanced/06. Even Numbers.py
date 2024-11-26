#Even Numbers

listInput = list(map(int, input().split(', ')))
listFoundIndexes = list(map(lambda i: i if listInput[i] % 2 == 0 else 'no', range(len(listInput))))
listFoundIndexes = list(filter(lambda i: i != 'no', listFoundIndexes))

print (f"{listFoundIndexes}")
