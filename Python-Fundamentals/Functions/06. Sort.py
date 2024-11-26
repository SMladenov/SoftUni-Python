numbers = input().split(' ')
numbersInt = [int(i) for i in numbers]
sortedNums = sorted(numbersInt, reverse=False)
print(f"{sortedNums}")