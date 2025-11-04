#Wolf in Sheep's Clothing

sheeps = input().split(', ')

for index, i in enumerate(sheeps):
    if i == "wolf":
        if index == (len(sheeps) - 1):
            print (f"Please go away and stop eating my sheep")
        else:
            print (f"Oi! Sheep number {(len(sheeps) - 1) - index}! You are about to be eaten by a wolf!")
