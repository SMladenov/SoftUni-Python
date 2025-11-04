#Word Filter

strInput = input().split(' ')
filtered = [i for i in strInput if len(i) % 2 == 0]
for i in filtered:
    print (f"{i}")
    