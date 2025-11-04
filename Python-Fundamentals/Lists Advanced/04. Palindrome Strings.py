#Palindrome Strings

listInput = input().split(' ')
palindrome = input()

listFound = []

isPalindrome = True

for i in listInput:
    isPalindrome = True
    for b in range (0, len(i) // 2):
        if i[b] != i[(len(i) - 1) - b]:
            isPalindrome = False
            break
    if isPalindrome:
        listFound.append(i)

listOccurancies = [i for i in listFound if i == palindrome]

print (f"{listFound}\nFound palindrome {len(listOccurancies)} times")
