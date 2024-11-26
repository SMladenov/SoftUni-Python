lines = int(input())

areEven = True

for i in range (lines):
    num1 = int(input())
    if num1 % 2 == 1:
        areEven = False
        print (f"{num1} is odd!")
        break
if areEven is True:
    print ("All numbers are even.")
    