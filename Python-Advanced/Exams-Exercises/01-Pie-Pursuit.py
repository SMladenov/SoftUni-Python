#Pie Pursuit

contestants = [int(i) for i in input().split()]
pies = [int(i) for i in input().split()]

while contestants and pies:
    currentContest = contestants[0]
    currentPie = pies[-1]
    if currentContest >= currentPie:
        difference = currentContest - currentPie
        pies.pop(-1)
        if difference == 0:
            contestants.pop(0)
        else:
            contestants.pop(0)
            contestants.append(difference)

    elif currentPie > currentContest:
        pies[-1] -= currentContest
        contestants.pop(0)
        if pies[-1] == 1:
            if len(pies) > 1:
                pies.pop(-1)
                pies[-1] += 1

if not pies and contestants:
    print (f"We will have to wait for more pies to be baked!\nContestants left: {', '.join(map(str, contestants))}")
if not pies and not contestants:
    print (f"We have a champion!")
if not contestants and pies:
    print (f"Our contestants need to rest!\nPies left: {', '.join(map(str, pies))}")
