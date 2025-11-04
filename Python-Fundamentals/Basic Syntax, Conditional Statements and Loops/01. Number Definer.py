num = float(input())

def definer(number):
    dicValues = {number == 0: "zero", -1 < number < 0: "small negative", 1 > number > 0: "small positive", number < -1000000: "large negative",
                number > 1000000: "large positive"}
    return dicValues.get(True)

resultDefiner = definer(num)

if resultDefiner is None:
    if num > 0:
        print ("positive")
    else:
        print ("negative")
else:
    print (f"{resultDefiner}")
    