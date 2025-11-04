#Scheduling

clockCycles = [int(i) for i in input().split(', ')]
jobIndex = int(input())

totalClockCycles = 0

targetJob = clockCycles[jobIndex]

dicCycles = {index: value for index, value in enumerate(clockCycles)}

sortedDicCycles = dict(sorted(dicCycles.items(), key=lambda x: (x[1], x[0])))

for index, value in sortedDicCycles.items():
    totalClockCycles += value
    if index == jobIndex:
        break

print (f"{totalClockCycles}")
