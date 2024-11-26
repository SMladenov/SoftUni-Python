#Rounding

def rounding(list):
    listfloat = [float(i) for i in list]
    finalList = [round(i) for i in listfloat]
    return finalList

listInput = input().split(' ')

print (f"{rounding(listInput)}")
