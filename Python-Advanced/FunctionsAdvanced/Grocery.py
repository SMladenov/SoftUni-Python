#Grocery

def grocery_store(**kwargs):
    
    sortedReceipt = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))

    listResult = []

    for key, value in sortedReceipt.items():
        listResult.append(f"{key}: {value}")

    return '\n'.join(listResult)