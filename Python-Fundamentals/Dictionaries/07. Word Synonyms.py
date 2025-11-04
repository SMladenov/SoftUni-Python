#Word Synonyms

num = int(input())

dictSynonyms = {}

for i in range (num):
    word = input()
    synonym = input()
    if word not in dictSynonyms.keys():
        dictSynonyms[word] = []
        dictSynonyms[word].append(synonym)
    else:
        dictSynonyms[word].append(synonym)

for key, value in dictSynonyms.items():
    print (f"{key} - {', '.join(value)}")