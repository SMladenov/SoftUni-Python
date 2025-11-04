#Guinea Pig

food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())

monthFinished = True

for i in range (1, 31):
    requiredFood = 0.3
    if (food - requiredFood) < 0:
        print (f"Merry must go to the pet store!")
        monthFinished = False
        break
    else:
        food -= requiredFood
        if i % 2 == 0:
            hayToGive = food * 0.05
            if (hay - hayToGive) < 0:
                print (f"Merry must go to the pet store!")
                monthFinished = False
                break
            else:
                hay -= hayToGive
        if i % 3 == 0:
            coverToPut = weight / 3
            if (cover - coverToPut) < 0:
                print (f"Merry must go to the pet store!")
                monthFinished = False
                break
            else:
                cover -= coverToPut

if monthFinished:
    print (f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")