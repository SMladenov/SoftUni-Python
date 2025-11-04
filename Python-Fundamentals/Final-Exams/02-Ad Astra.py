#Ad Astra

import re

inputFood = input()

patternFood = r"([\#|\|])([A-Za-z ]+\1\d{2}\/\d{2}\/\d{2}\1\d+)\1"
matchFood = re.findall(patternFood, inputFood)

totalCalories = 0
days = 0

for i in matchFood:
    calories = int(i[1].split(i[0])[2])
    totalCalories += calories

while (totalCalories - 2000) >= 0:
    days += 1
    totalCalories -= 2000

print (f"You have food to last you for: {days} days!")
for i in matchFood:
    listItems = i[1].split(i[0])
    print (f"Item: {listItems[0]}, Best before: {listItems[1]}, Nutrition: {listItems[2]}")