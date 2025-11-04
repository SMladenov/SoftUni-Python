#Scheduling

clockCycles = [int(i) for i in input().split(', ')]
jobIndex = int(input())

totalClockCycles = 0

targetJob = clockCycles[jobIndex]
currentTask = -1

while currentTask != targetJob:
    currentJob = min(clockCycles)
    currentTask = currentJob
    indexCurrentJob = clockCycles.index(currentJob)
    clockCycles.pop(indexCurrentJob)

    totalClockCycles += currentJob
    
print (f"{totalClockCycles}")