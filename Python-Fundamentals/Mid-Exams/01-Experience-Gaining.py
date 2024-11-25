#Experience Gaining

neededExperience = float(input())
battles = int(input())

gainedExperience = 0
unlocked = True

for i in range (1, battles + 1):
    gained = float(input())

    if i % 3 == 0:
        if i % 5 == 0:
            gained *= 1.05
        else:
            gained *= 1.15
    if i % 5 == 0:
        gained *= 0.9

    gainedExperience += gained
    if gainedExperience >= neededExperience:
        print (f"Player successfully collected his needed experience for {i} battles.")
        unlocked = False
        break

if unlocked:
    print (f"Player was not able to collect the needed experience, {(neededExperience - gainedExperience):.2f} more needed.")