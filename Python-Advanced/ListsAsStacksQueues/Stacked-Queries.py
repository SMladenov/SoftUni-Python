#Stacked Queries
#Stack

queryStack = []

numberQueries = int(input())
for i in range (numberQueries):
    query = input().strip().split(' ')
    if len(query) > 1:
        if query[0] == '1':
            queryStack.append(int(query[1]))
    else:
        action = query[0]
        if action == '2':
            if queryStack:
                queryStack.pop()
        elif action == '3':
            if queryStack:
                print (f"{max(queryStack)}")
        elif action == '4':
            if queryStack:
                print (f"{min(queryStack)}")
            
queryStack.reverse()
print (', '.join(map(str, queryStack)))
