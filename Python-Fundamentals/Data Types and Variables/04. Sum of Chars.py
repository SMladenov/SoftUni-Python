#Sum Of Chars

chars = int(input())

totalSum = 0

for i in range (chars):
    inputChar = input()
    totalSum += ord(inputChar)
    
print (f"The sum equals: {totalSum}")
