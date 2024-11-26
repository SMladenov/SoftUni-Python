#Number Classification

numInput = [int(i) for i in input().split(', ')]

pos = [str(i) for i in numInput if i > 0 or i == 0]
neg = [str(i) for i in numInput if i < 0]
even = [str(i) for i in numInput if i % 2 == 0]
odd = [str(i) for i in numInput if i % 2 == 1]

print (f"Positive: {', '.join(pos)}\nNegative: {', '.join(neg)}\nEven: {', '.join(even)}\nOdd: {', '.join(odd)}")
