#Prime Number Checker

def isPrime (num):
    if num <= 1:
        return False
    else:
        for i in range (2, (num // 2) + 1):
            if num % i == 0:
                return False
        return True

num = int(input())

print (f"{isPrime(num)}")
