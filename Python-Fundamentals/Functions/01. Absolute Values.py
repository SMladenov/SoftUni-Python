#Absolute Values

def getAbsolete(list):
    listFloat = [float(i) for i in list]
    listAbs = [abs(i) for i in listFloat]
    return listAbs

listInput = input().split(' ')

print (f"{getAbsolete(listInput)}")
