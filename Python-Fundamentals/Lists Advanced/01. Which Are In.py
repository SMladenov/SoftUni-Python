#Which Are In?

list1 = input().split(', ')
list2 = input().split(', ')

list3 = []

for i in list1:
    for b in list2:
        if i in b:
            if i not in list3:
                list3.append(i)

print (f"{list3}")
