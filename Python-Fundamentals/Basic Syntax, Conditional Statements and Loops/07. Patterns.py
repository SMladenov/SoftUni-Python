numbers = int(input())

for i in range (1, numbers + 1):
    for b in range (0, i):
        print (f"*", end = "")
    print()
    if i == numbers:
        for c in range (i - 1, 0, -1):
            for d in range (c, 0, -1):
                print (f"*", end = "")
            print()
            