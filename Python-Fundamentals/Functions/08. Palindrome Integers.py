#Palindrome Integers

def isPalindrome(numbers):
    listValues = []
    isPalindrome = True
    for i in numbers:
        isPalindrome = True
        for b in range (0, len(i) // 2):
            if i[b] != i[(len(i) -1) - b]:
                isPalindrome = False
                listValues.append("False")
                break
        if isPalindrome:
            listValues.append("True")
    return listValues
    
numbers = input().split(', ')

values = isPalindrome(numbers)

for i in values:
    print (i)
    