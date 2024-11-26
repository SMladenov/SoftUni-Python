#Triples of Latin Letters

num1 = int(input())

for i in range (0, num1):
    for b in range (0, num1):
        for c in range (0, num1):
            char1 = chr(97 + i)
            char2 = chr(97 + b)
            char3 = chr(97 + c)
            print (f"{char1}{char2}{char3}")
            