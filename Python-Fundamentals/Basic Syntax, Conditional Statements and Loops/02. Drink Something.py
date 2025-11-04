#Drink Something

def howOld (age):
    howOldDic = {age <= 14: "kid", 14 < age <= 18: "teen", 18 < age <= 21: "young adult", age > 21: "adult"}
    return howOldDic.get(True)

age = int(input())

oldRange = howOld(age)
if oldRange is not None:
    if oldRange == "kid":
        print (f"drink toddy")
    elif oldRange == "teen":
        print (f"drink coke")
    elif oldRange == "young adult":
        print (f"drink beer")
    else:
        print (f"drink whisky")
