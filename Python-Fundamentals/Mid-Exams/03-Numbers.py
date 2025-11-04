#Numbers

nums = [int(i) for i in input().split(' ')]
average = sum(nums) / len(nums)
greaterThanAvg = [i for i in nums if i > average]
greaterThanAvg.sort()
if len(greaterThanAvg) > 5:
    tempList = [str(greaterThanAvg[i]) for i in range (len(greaterThanAvg) - 1, (len(greaterThanAvg) - 1) - 5, -1)]
    print (f"{' '.join(tempList)}")
elif 0 < len(greaterThanAvg) <= 5:
    greaterThanAvg.reverse()
    greaterThanAvg = [str(i) for i in greaterThanAvg]
    print (f"{' '.join(greaterThanAvg)}")
else:
    print (f"No")