#Zeros to Back

randomStr = input()
randomStr = [int(i) for i in randomStr.split(', ')]

zeros = []

while 0 in randomStr:
    zeros.append(0)
    randomStr.remove(0)
    
randomStr = randomStr + zeros
print (f"{randomStr}")
