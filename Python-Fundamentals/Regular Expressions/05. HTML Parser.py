#HTML Parser

import re

htmlExample = input()

#. - any character ; * - zero or more ; ? - non-greedy - stops matching at the first <\/title>
patternTitle = r"<title>(.*?)<\/title>"
resultTitle = re.search(patternTitle, htmlExample)
if resultTitle:
    #Pattern to match HTML tags, matching any character that is not '>', so we can clean them
    patternTags = r"<[^>]+>"
    cleanText = re.sub(patternTags, ' ', resultTitle.group(1))
    cleanText2 = re.sub(r"\\n", ' ', cleanText)
    listCleanBody = cleanText2.split(' ')
    listCleanBody = [i.strip() for i in listCleanBody if i.strip()]
    print (f"Title: {' '.join(listCleanBody)}")

patternBody = r"<body>(.*?)<\/body>"
resultBody = re.search(patternBody, htmlExample)
if resultBody:
    patternTags = r"<[^>]+>"
    cleanText = re.sub(patternTags, ' ', resultBody.group(1))
    #print (f"{cleanText}")
    cleanText2 = re.sub(r"\\n", ' ', cleanText)
    listCleanBody = cleanText2.split(' ')
    listCleanBody = [i.strip() for i in listCleanBody if i.strip()]
    print (f"Content: {' '.join(listCleanBody)}")