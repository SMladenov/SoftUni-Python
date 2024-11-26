#Search

num1 = int(input())
word = input()

listAll = []
listFiltered = []

for i in range (num1):
    word2 = input()
    listAll.append(word2)

for i in listAll:
    if word in i:
        listFiltered.append(i)

print (f"{listAll}\n{listFiltered}")
