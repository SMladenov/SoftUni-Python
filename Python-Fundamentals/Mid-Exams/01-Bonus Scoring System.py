#Bonus Scoring System

students = int(input())
lectures = int(input())
bonus = int(input())

maxBonus = 0
maxAttendances = 0

for i in range (students):
    attendances = int(input())
    tempMaxBonus = attendances / lectures * (5 + bonus)
    if maxBonus < tempMaxBonus:
        maxBonus = tempMaxBonus
        maxAttendances = attendances

print (f"Max Bonus: {round(maxBonus)}.\nThe student has attended {maxAttendances} lectures.")