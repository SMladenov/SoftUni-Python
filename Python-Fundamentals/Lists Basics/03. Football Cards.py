#Football Cards

teamACount = 11
teamBCount = 11
teamAPlayers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
teamBPlayers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

stringCards = input()
listCards = stringCards.split(' ')

listWithoutSpaces = []

isTerminated = False

for i in range (0, len(listCards)):
    if listCards[i]: #Check if a string is not empty
    #if listCards[i] != "":
        listWithoutSpaces.append(listCards[i])

for i in listWithoutSpaces:
    if i[0] == "A":
        splitChar = i.split('-')
        playerWithCard = int(splitChar[1])
        if playerWithCard in teamAPlayers:
            teamACount -= 1
            teamAPlayers.remove(playerWithCard)
            if teamACount < 7:
                isTerminated = True
                print (f"Team A - {teamACount}; Team B - {teamBCount}\nGame was terminated")
                break
    if i[0] == "B":
        splitChar = i.split('-')
        playerWithCard = int(splitChar[1])
        if playerWithCard in teamBPlayers:
            teamBCount -= 1
            teamBPlayers.remove(playerWithCard)
            if teamBCount < 7:
                isTerminated = True
                print (f"Team A - {teamACount}; Team B - {teamBCount}\nGame was terminated")
                break

if not isTerminated:
    print (f"Team A - {teamACount}; Team B - {teamBCount}")
    