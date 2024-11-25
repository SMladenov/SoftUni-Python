#Greenhouse

crops = input().split('&')
crops = [i.strip() for i in crops if i.strip()]
cmd = input()

while cmd != "Collect!":
    cmdSplit = cmd.split(' ')
    action = cmdSplit[0]
    if action == "Plant":
        crop = cmdSplit[1]
        if crop not in crops:
            crops.insert(0, crop)
    if action == "Transplant":
        crop = cmdSplit[1]
        if crop in crops:
            crops.remove(crop)
            crops.append(crop)
    if action == "Replace":
        index1 = int(cmdSplit[1])
        index2 = int(cmdSplit[2])
        if 0 <= index1 < len(crops) and 0 <= index2 < len(crops):
            value1 = crops[index1]
            value2 = crops[index2]
            crops[index1] = value2
            crops[index2] = value1
    if action == "Uproot":
        crop = cmdSplit[1]
        if crop in crops:
            crops.remove(crop)
    cmd = input()

print (f"{' | '.join(crops)}")
