#Water Overflow

tankCapacity = 255
lines = int(input())

while lines > 0:
    lines -= 1
    liters = int(input())
    if (tankCapacity - liters) < 0:
        print ("Insufficient capacity!")
    else:
        tankCapacity -= liters

print (f"{255 - tankCapacity}")
