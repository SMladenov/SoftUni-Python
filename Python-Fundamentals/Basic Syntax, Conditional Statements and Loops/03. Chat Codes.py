#Chat Codes

def getCode(code):
    codesDic = {code == 88: "Hello", code == 86: "How are you?", 88 > code != 86: "GREAT!", code > 88: "Bye."}
    return codesDic.get(True)

numTries = int(input())

for i in range (numTries):
    code = int(input())
    print (f"{getCode(code)}")
