#Journey to the Legendary Artifact

energy = float(input())

cmd = input()

legendaryArtifact = 0
mountains = 0
finished = True

while cmd != "Journey ends here!":
    if cmd == "mountain":
        if energy - 10 > 0:
            energy -= 10
            mountains += 1
            if mountains % 3 == 0:
                legendaryArtifact += 1
                if legendaryArtifact == 3:
                    print (f"The character reached the legendary artifact with {energy:.2f} energy left.")
                    finished = False
                    break
        else:
            print (f"The character is too exhausted to carry on with the journey.")
            finished = False
            break
    if cmd == "desert":
        if energy - 15 > 0:
            energy -= 15
        else:
            print (f"The character is too exhausted to carry on with the journey.")
            finished = False
            break
    if cmd == "forest":
        energy += 7
    cmd = input()

if finished:
    print (f"The character could not find all the pieces and needs {3 - legendaryArtifact} more to complete the legendary artifact.")