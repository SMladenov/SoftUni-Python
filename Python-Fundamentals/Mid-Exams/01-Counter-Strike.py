#Counter-Strike

initialEnergy = int(input())

cmd = input()

battlesWon = 0
won = True

while cmd != "End of battle":
    move = int(cmd)
    if (initialEnergy - move) < 0:
        print (f"Not enough energy! Game ends with {battlesWon} won battles and {initialEnergy} energy")
        won = False
        break
    else:
        initialEnergy -= move
        battlesWon += 1
        if battlesWon % 3 == 0:
            initialEnergy += battlesWon
    cmd = input()

if won:
    print (f"Won battles: {battlesWon}. Energy left: {initialEnergy}")