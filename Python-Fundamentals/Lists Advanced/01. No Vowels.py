#No Vowels

listVowels = ['a', 'A', 'u', 'U', 'o', 'O', 'e', 'E', 'i', 'I']
stringInput = input()

finalList = [i for i in stringInput if i not in listVowels]

print (f"{''.join(finalList)}")
