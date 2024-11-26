#Maximum Multiple

divisor = int(input())
boundary = int(input())

finalResult = 0

while boundary > 0:
    boundary -= divisor
    if boundary < 0:
        break
    finalResult += divisor

print (finalResult)
