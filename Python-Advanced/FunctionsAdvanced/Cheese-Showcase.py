#Cheese Showcase

def sorting_cheeses (**kwargs):
    
    sortedDict = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for tupl in sortedDict:
        sortedList = sorted(tupl[1], key=None, reverse=True)
        result.append(tupl[0])
        result.extend(sortedList)

    return '\n'.join(map(str, result))