#Multiplication Sign

def multiplicationSign (*args):
    minuses = 0
    for i in args:
        if i < 0:
            minuses += 1
        if i == 0:
            return f"zero"
    if minuses % 2 == 1:
        return f"negative"
    else:
        return f"positive"

num1 = int(input())
num2 = int(input())
num3 = int(input())

print (f"{multiplicationSign(num1, num2, num3)}")
