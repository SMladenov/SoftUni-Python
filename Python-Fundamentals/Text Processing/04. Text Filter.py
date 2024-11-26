#Text Filter

bannedWords = input().split(', ')
text = input()

for i in bannedWords:
    while i in text:
        text = text.replace(i, '*' * len(i))

print (f"{text}")