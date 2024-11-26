#Faro Shuffle

listCards = input().split(' ')
numberOfShuffles = int(input())

halfCards = len(listCards) // 2

listFaroFinal = []

for i in range(numberOfShuffles):
    listLeftFaro = listCards[:halfCards]
    listRightFaro = listCards[halfCards:]
    
    for i in range (0, halfCards):
        listFaroFinal.append(listLeftFaro[i])
        listFaroFinal.append(listRightFaro[i])
    listCards = listFaroFinal
    listFaroFinal = []

print (f"{listCards}")
