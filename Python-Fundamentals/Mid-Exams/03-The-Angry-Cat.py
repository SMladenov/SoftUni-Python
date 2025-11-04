#The Angry Cat

prices = [int(i) for i in input().split(', ')]
entryPoint = int(input())
type = input()

sumLeft = []
sumRight = []

if type == "cheap":
    value = prices[entryPoint]
    sumLeft = [prices[i] for i in range (0, entryPoint) if prices[i] < value]
    sumRight = [prices[i] for i in range (entryPoint + 1, len(prices)) if prices[i] < value]
if type == "expensive":
    value = prices[entryPoint]
    sumLeft = [prices[i] for i in range (0, entryPoint) if prices[i] >= value]
    sumRight = [prices[i] for i in range (entryPoint + 1, len(prices)) if prices[i] >= value]
    
if sum(sumLeft) < sum(sumRight):
    print (f"Right - {sum(sumRight)}")
elif sum(sumLeft) >= sum(sumRight):
    print (f"Left - {sum(sumLeft)}")