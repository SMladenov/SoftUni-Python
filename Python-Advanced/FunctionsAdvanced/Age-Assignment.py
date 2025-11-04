#Age Assignment

def age_assignment(*args, **kwargs):

    resultList = []
    listDictForFiltering = {}
    for key, value in kwargs.items():
        for name in args:
            if name.startswith(key):
                if name not in listDictForFiltering.keys():
                    listDictForFiltering[name] = value

    sortedDict = dict(sorted(listDictForFiltering.items(), key=lambda x: x[0]))
    for name, age in sortedDict.items():
        resultList.append(f"{name} is {age} years old.")
    
    return '\n'.join(resultList)
