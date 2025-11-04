#Count Symbols

randomStr = tuple([i for i in input()])

dicChecked = {}

for i in randomStr:
    if i not in dicChecked.keys():
        dicChecked[i] = randomStr.count(i)

for key, value in sorted (dicChecked.items(), key=lambda item: item[0]):
    print (f"{key}: {value} time/s")