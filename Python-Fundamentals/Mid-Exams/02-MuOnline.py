#Mu Online

health = 100
bitcoins = 0

rooms = input().split('|')
room = 0
killed = False

for i in rooms:
    iSplit = i.split(' ')
    cmd = iSplit[0]
    number = int(iSplit[1])
    room += 1
    if cmd == "potion":
        if health + number > 100:
            print (f"You healed for {100 - health} hp.")
            health = 100
            print (f"Current health: {health} hp.")
        else:
            health += number
            print (f"You healed for {number} hp.")
            print (f"Current health: {health} hp.")
    elif cmd == "chest":
        bitcoins += number
        print (f"You found {number} bitcoins.")
    else:
        health -= number
        if health <= 0:
            print (f"You died! Killed by {cmd}.\nBest room: {room}")
            killed = True
            break
        else:
            print (f"You slayed {cmd}.")


if not killed:
    print (f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")