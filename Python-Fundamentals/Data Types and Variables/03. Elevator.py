#Elevator

numberOfPeople = int(input())
capacity = int(input())

counter = 1

if capacity == numberOfPeople or capacity > numberOfPeople:
    print (1)
else:
    while numberOfPeople > 0:
        if (numberOfPeople - capacity) <= 0:
            break
        else:
            numberOfPeople -= capacity
            counter += 1
    print (counter)
