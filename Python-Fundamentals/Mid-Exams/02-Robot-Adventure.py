#Robot's Adventure

numbers = [int(i) for i in input().split('|')]
cmd = input()

totalValue = 0

while cmd != "Adventure over":
    cmdSplit = cmd.split(' ')
    action = cmdSplit[0]

    if action == "Double":
        index = int(cmdSplit[1])
        if 0 <= index < len(numbers):
            value = numbers[index]
            numbers[index] = value * 2

    if action == "Switch":
        numbers.reverse()

    if action == "Step":
        secondSplit = cmdSplit[1].split('$')
        secondAction = secondSplit[0]

        if secondAction == "Backward":
            startIndex = int(secondSplit[1])
            steps = int(secondSplit[2])
            if 0 <= startIndex < len(numbers):
                actualIndex = startIndex - steps
                while actualIndex < 0:
                    actualIndex += len(numbers)
                totalValue += numbers[actualIndex]
                numbers[actualIndex] = 0
                
        if secondAction == "Forward":
            startIndex = int(secondSplit[1])
            steps = int(secondSplit[2])
            if 0 <= startIndex < len(numbers):
                actualIndex = steps + startIndex
                while actualIndex > len(numbers) - 1:
                    actualIndex -= len(numbers)
                totalValue += numbers[actualIndex]
                numbers[actualIndex] = 0
    cmd = input()

numbers = [str(i) for i in numbers]
print (f"{'-'.join(numbers)}\nRobo finished the adventure with {totalValue} items!")