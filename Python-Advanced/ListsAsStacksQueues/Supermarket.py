#Supermarket

people = input()
queueList = []
paidPeople = []

while people != "End":
    if people != "Paid":
        queueList.append(people)
    else:
        for i in range (0, len(queueList)):
            paidPeople.append(queueList.pop(0))
    people = input()

if paidPeople:
    print ("\n".join(paidPeople))
print (f"{len(queueList)} people remaining.")