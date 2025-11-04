#World Tour

stops = input()

cmd = input()

while cmd != "Travel":
    cmdSplit = cmd.split(':')
    action = cmdSplit[0]

    #Action 1
    if action == "Add Stop":
        index = int(cmdSplit[1])
        newStop = cmdSplit[2]
        if 0 <= index <= len(stops):
            stops = stops[:index] + newStop + stops[index:]
            #print (f"{stops}")
    #Action 2
    if action == "Remove Stop":
        startIndex = int(cmdSplit[1])
        endIndex = int(cmdSplit[2])
        if 0 <= startIndex < len(stops) and 0 <= endIndex < len(stops):
            stops = stops[:startIndex] + stops[endIndex + 1:]
            #print (f"{stops}")
    #Action 3
    if action == "Switch":
        oldString = cmdSplit[1]
        newString = cmdSplit[2]
        if oldString in stops:
            stops = stops.replace(oldString, newString)
            #print (f"{stops}")
    
    print (f"{stops}")
    cmd = input()

print (f"Ready for world tour! Planned stops: {stops}")