#ASCII Values

listKeys = input().split(', ')
#dict = {i: ord(i) for i in listKeys}
#print (f"{dict}")
dict = {}
for i in listKeys:
    dict[i] = ord(i)
print (f"{dict}")