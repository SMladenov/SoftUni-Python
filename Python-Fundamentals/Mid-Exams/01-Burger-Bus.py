#Burger Bus

numCities = int(input())

totalMoney = 0
totalExpenses = 0

for i in range (1, numCities + 1):
    cityName = input()
    moneyEarned = float(input())
    expenses = float(input())
    if i % 3 == 0:
        if i % 5 != 0:
            expenses *= 1.5
    if i % 5 == 0:
        moneyEarned *= 0.9
    
    totalMoney += moneyEarned
    totalExpenses += expenses
    
    print (f"In {cityName} Burger Bus earned {(moneyEarned - expenses):.2f} leva.")

print (f"Burger Bus total profit: {(totalMoney - totalExpenses):.2f} leva.")