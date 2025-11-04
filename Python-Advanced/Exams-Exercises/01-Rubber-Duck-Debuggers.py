#Rubber Duck Debuggers

time = [int(i) for i in input().split()]
numberOfTasks = [int(i) for i in input().split()]

dicDucks = {"Darth Vader Ducky": 0,
            "Thor Ducky": 0,
            "Big Blue Rubber Ducky": 0,
            "Small Yellow Rubber Ducky": 0}

def getDuckType (time):
    dicDucks = {0 <= time <= 60: "Darth Vader Ducky",
                61 <= time <= 120: "Thor Ducky",
                121 <= time <= 180: "Big Blue Rubber Ducky", 
                181 <= time <= 240: "Small Yellow Rubber Ducky"}
    return dicDucks.get(True, None)

while time and numberOfTasks:
    currentTime = time[0] * numberOfTasks[-1]

    duckType = getDuckType(currentTime)
    
    if duckType is not None:
        dicDucks[duckType] += 1
        time.pop(0)
        numberOfTasks.pop(-1)
    else:
        numberOfTasks[-1] -= 2
        timeValue = time.pop(0)
        time.append(timeValue)

print (f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, value in dicDucks.items():
    print (f"{key}: {value}")
