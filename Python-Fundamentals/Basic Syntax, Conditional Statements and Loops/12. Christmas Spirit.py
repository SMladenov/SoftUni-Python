#Christmas Spirit

quantity = int(input())
days = int(input())

points = 0
cost = 0

for i in range (1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        cost += 2 * quantity
        points += 5
    if i % 3 == 0:
        cost += 8 * quantity
        points += 13
    if i % 5 == 0:
        if i % 15 == 0:
            points += 30
        cost += 15 * quantity
        points += 17
    if i % 10 == 0:
        points -= 20
        cost += (5 + 3 + 15)
        if i == days:
            points -= 30

print (f"Total cost: {cost}\nTotal spirit: {points}")
