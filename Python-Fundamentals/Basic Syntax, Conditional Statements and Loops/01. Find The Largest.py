#Find the Largest

num = list(input())
num = [int(i) for i in num]

finalResult = []

while len(num) > 0:
    maxTemp = max(num)
    num.remove(maxTemp)
    finalResult.append(maxTemp)

for i in finalResult:
    print (f"{i}", end = "")
