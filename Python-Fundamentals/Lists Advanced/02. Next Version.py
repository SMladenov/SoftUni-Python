#Next Version

numInput = input().split('.')
num = ""

for i in numInput:
    num += i

num = int(num)
num += 1

num = str(num)

print (f"{'.'.join(num)}")
