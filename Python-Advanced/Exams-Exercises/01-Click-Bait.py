#Click Bait

links = [int(i) for i in input().split()]
articles = [int(i) for i in input().split()]

target = int(input())

finalFeed = []

while links and articles:
    currentLink = links[0]
    currentArticle = articles[-1]

    if currentArticle == 0:
        articles.pop()
        continue

    if currentLink == 0:
        links.pop(0)
        continue

    remainder = 0

    if currentArticle > currentLink:
        remainder = currentArticle % currentLink
        finalFeed.append(remainder)
        links.pop(0)
        articles.pop()
        #if articles > 0:
        articles.append(remainder * 2)
        
    elif currentLink > currentArticle:
        remainder = currentLink % currentArticle
        finalFeed.append(-remainder)
        links.pop(0)
        articles.pop()
        links.append(remainder * 2)

    elif currentLink == currentArticle:
        links.pop(0)
        articles.pop()
        finalFeed.append(0)

print (f"Final Feed: {', '.join(map(str, finalFeed))}")

totalValue = sum(finalFeed)

if totalValue >= target:
    print (f"Goal achieved! Engagement Value: {totalValue}")
else:
    print (f"Goal not achieved! Short by: {target - totalValue}")
