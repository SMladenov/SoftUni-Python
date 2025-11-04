#Ball-Game

strength = [int(i) for i in input().split()]
accuracy = [int(i) for i in input().split()]

goals = 0

while strength and accuracy:
    currentStrength = strength[-1]
    currentAccuracy = accuracy[0]

    if currentStrength + currentAccuracy == 100:
        strength.pop()
        accuracy.pop(0)
        goals += 1

    elif currentStrength + currentAccuracy < 100:
        if currentStrength < currentAccuracy:
            strength.pop()
        elif currentStrength > currentAccuracy:
            accuracy.pop(0)
        elif currentStrength == currentAccuracy:
            sumOfBoth = currentStrength + currentAccuracy
            accuracy.pop(0)
            strength[-1] += currentAccuracy

    elif currentStrength + currentAccuracy > 100:
        strength[-1] -= 10
        accuracy.pop(0)
        accuracy.append(currentAccuracy)

if goals > 3:
    print (f"Paul performed remarkably well!")
elif goals == 3:
    print (f"Paul scored a hat-trick!")
elif goals == 0:
    print (f"Paul failed to score a single goal.")
elif 0 < goals < 3:
    print (f"Paul failed to make a hat-trick.")

if goals > 0:
    print (f"Goals scored: {goals}")
if strength:
    print (f"Strength values left: {', '.join(map(str, strength))}")
if accuracy:
    print (f"Accuracy values left: {', '.join(map(str, accuracy))}")
