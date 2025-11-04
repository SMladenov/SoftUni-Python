#Worms&Holes

worms = [int(i) for i in input().split()]
holes = [int(i) for i in input().split()]

matches = 0
initialSize = len(worms)

while worms and holes:
    currentWorm = worms[-1]
    currentHole = holes[0]
    if currentWorm == currentHole:
        worms.pop()
        holes.pop(0)
        matches += 1
    else:
        holes.pop(0)
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()
        
# Print matches or no matches
if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

# Print remaining worms or a success message if all worms found holes
if matches == initialSize:
    print("Every worm found a suitable hole!")
elif worms:
    print(f"Worms left: {', '.join(map(str, worms))}")
else:
    print ("Worms left: none")

# Print remaining holes
if holes:
    print(f"Holes left: {', '.join(map(str, holes))}")
else:
    print ("Holes left: none")
