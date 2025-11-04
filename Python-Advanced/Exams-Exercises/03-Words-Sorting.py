#Words Sorting

def words_sorting (*args):

    dicWords = {}

    for word in args:
        sumAllChars = 0
        for i in word:
            sumAllChars += ord(i)
        dicWords[word] = sumAllChars

    allValues = sum(dicWords.values())
    if allValues % 2 == 0:
        dicWordsSorted = dict(sorted(dicWords.items(), key= lambda x: x[0]))
    else:
        dicWordsSorted = dict(sorted(dicWords.items(), key= lambda x: -x[1]))

    listToOutput = []

    for key, value in dicWordsSorted.items():
        listToOutput.append(f"{key} - {value}")

    return '\n'.join(listToOutput)

# print(
#     words_sorting(
#         'escape', 
#         'charm', 
#         'mythology'
#   ))

# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'eye'
#   ))

print(
    words_sorting(
        'cacophony',         
        'accolade'
  ))
