#Parking Lot

numberCmd = int(input())
setCars = set()

for _ in range (numberCmd):
    action, car = input().split(', ')
    if action == "IN":
        setCars.add(car)
    elif action == "OUT":
        setCars.discard(car)

if setCars:
    print ('\n'.join(setCars))
else:
    print (f"Parking Lot is Empty")