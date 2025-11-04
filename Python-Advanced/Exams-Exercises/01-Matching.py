#Matching

males = [int(i) for i in input().split()]
females = [int(i) for i in input().split()]

matches = 0

while males and females:
    currentMale = males[-1]
    currentFemale = females[0]


    if currentMale <= 0:
        males.pop()
        continue
    if currentFemale <= 0:
        females.pop()
        continue
    
    if currentMale % 25 == 0:
        if currentMale % 25 == 0:
            if len(males) > 1:
                males.pop()
                males.pop()
            else:
                males.pop()
                if not males:
                    break
            continue
   
    if currentFemale % 25 == 0:
        if currentFemale % 25 == 0:
            if len(females) > 1:
                females.pop(0)
                females.pop(0)
            else:
                females.pop(0)
                if not females:
                    break
            continue
    
    if currentMale == currentFemale:
        matches += 1
        males.pop()
        females.pop(0)

    else:
        females.pop(0)
        males[-1] -= 2
    
print (f"Matches: {matches}")
if males:
    males.reverse()
    print (f"Males left: {', '.join(map(str, males))}")
else:
    print (f"Males left: none")

if females:
    print (f"Females left: {', '.join(map(str, females))}")
else:
    print (f"Females left: none")
