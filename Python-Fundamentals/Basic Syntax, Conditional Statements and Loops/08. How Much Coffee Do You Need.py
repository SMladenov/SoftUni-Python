#How Much Coffee Do You Need?

cmd = input()

numberOfCoffees = 0

listUpper = ['CODING', 'DOG', 'CAT', 'MOVIE']
listLower = ['coding', 'dog', 'cat', 'movie']

while cmd != "END":
    if cmd in listUpper:
        numberOfCoffees += 2
    elif cmd in listLower:
        numberOfCoffees += 1
    cmd = input()

if numberOfCoffees > 5:
    print (f"You need extra sleep")
else:
    print (f"{numberOfCoffees}")
