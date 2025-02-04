#Numbers Filter

num1 = int(input())

listNumbers = []

for i in range(num1):
    num2 = int(input())
    listNumbers.append(num2)

cmd = input()

listResult = []

if cmd == "even":
    for i in listNumbers:
        if i == 0 or (i % 2) == 0:
            listResult.append(i)
elif cmd == "odd":
    for i in listNumbers:
        if i % 2 == 1:
            listResult.append(i)
elif cmd == "negative":
    for i in listNumbers:
        if i < 0:
            listResult.append(i)
elif cmd == "positive":
    for i in listNumbers:
        if i >= 0:
            listResult.append(i)

print (f"{listResult}")
