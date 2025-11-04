#Math Operations

def math_operations(*args, **kwargs):

    listResult = []
    dictKwargs = kwargs

    counter = 0
    for i in args:
        counter += 1
        if counter == 5:
            counter = 1
            
        if counter % 4 == 0:
            dictKwargs['m'] *= i
        elif counter % 3 == 0:
            if i != 0 and i != 0.0 and dictKwargs['d'] != 0 and dictKwargs['d'] != 0.0:
                dictKwargs['d'] /= i
        elif counter % 2 == 0:
            dictKwargs['s'] -= i
        elif counter % 1 == 0:
            dictKwargs['a'] += i

    sortedDict = dict(sorted(dictKwargs.items(), key=lambda x: (-x[1], x[0])))

    for key, value in sortedDict.items():
        listResult.append(f"{key}: {value:.1f}")

    return '\n'.join(listResult)
