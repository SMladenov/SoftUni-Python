#Character Multiplier

def countTheSum (smaller, bigger):
    totalSum = 0
    for i in range (0, len(smaller)):
        firstSum = ord(smaller[i])
        secondSum = ord(bigger[i])
        totalSum += firstSum * secondSum
        if (i == len(smaller) - 1) and (len(smaller) != len(bigger)):
            for b in range (len(smaller), len(bigger)):
                leftSum = ord(bigger[b])
                totalSum += leftSum
    return totalSum

words = input().split(' ')

if len(words[0]) <= len(words[1]):
    print (f"{countTheSum(words[0], words[1])}")
else:
    print (f"{countTheSum(words[1], words[0])}")