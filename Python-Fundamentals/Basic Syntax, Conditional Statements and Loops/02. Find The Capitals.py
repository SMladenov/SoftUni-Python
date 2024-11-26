#Find The Capitals

randomStr = input()

listIndexes = []

for index, i in enumerate(randomStr):
    if i.isalpha() and i.isupper():
        listIndexes.append(index)
    
print (f"{listIndexes}")
