#Car Race

time = input()
time = [int(i) for i in time.split(' ')]

leftTime = 0
rightTime = 0

for i in range (0, (len(time) // 2)):
    if time[i] == 0 and i != 0:
        leftTime *= 0.8
    else:
        leftTime += time[i]

for i in range ((len(time) - 1), (len(time) // 2), -1):
    if time[i] == 0 and i != (len(time) - 1):
        rightTime *= 0.8
    else:
        rightTime += time[i]

if leftTime < rightTime:
    print (f"The winner is left with total time: {leftTime:.1f}")
else:
    print (f"The winner is right with total time: {rightTime:.1f}")
    