#List Statistics

num2 = int(input())

listPositive = []
listNegative = []

for i in range (num2):
    num3 = int(input())
    if num3 <= 0:
        listNegative.append(num3)
    else:
        listPositive.append(num3)

print (f"{listPositive}\n{listNegative}\nCount of positives: {len(listPositive)}\nSum of negatives: {sum(listNegative)}")
