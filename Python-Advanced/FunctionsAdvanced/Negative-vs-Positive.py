#Negative vs Positive

def negative_positive (*args):
    negative = 0
    positive = 0
    nums = list(map(int, args))
    for num in nums:
        if num > 0:
            positive += num
        else:
            negative += num

    if abs(negative) > abs(positive):
        return f"{negative}\n{positive}\nThe negatives are stronger than the positives"
    else:
        return f"{negative}\n{positive}\nThe positives are stronger than the negatives"

print (negative_positive(*input().split()))