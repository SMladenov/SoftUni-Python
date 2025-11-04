#Periodic Table

numberLines = int(input())

chemicals = set()

for _ in range (numberLines):
    listChem = [i for i in input().strip().split() if i.strip()]
    for b in listChem:
        chemicals.add(b)

print ('\n'.join(chemicals))
