import math

def squares(n):
    currentNum = 1
    while currentNum <= n:
        yield currentNum * currentNum
        currentNum += 1

#print(list(squares(5)))

def genrange (start: int, end: int):
    while start <= end:
        yield start
        start += 1

#print(list(genrange(1, 10)))

def reverse_text (someString: str):
    currentIndex = len(someString) - 1
    while currentIndex >= 0:
        yield someString[currentIndex]
        currentIndex -= 1
    
for char in reverse_text("step"):

    print(char, end='')