#Shoot for the Win

shots = [int(i) for i in input().split(' ')]

cmd = input()

successfulShots = 0

while cmd != "End":
    index = int(cmd)
    if 0 <= index < len(shots):
        if shots[index] != -1:
            tempAmount = shots[index]
            shots[index] = -1
            successfulShots += 1
            for ind, item in enumerate(shots):
                if item != -1 and item > tempAmount:
                    shots[ind] -= tempAmount
                elif item != -1 and item <= tempAmount:
                    shots[ind] += tempAmount
    cmd = input()

print (f"Shot targets: {successfulShots} -> {' '.join(map(str, shots))}")