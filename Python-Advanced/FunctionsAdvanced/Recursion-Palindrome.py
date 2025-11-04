def palindrome (string, index, stringReverse=""):
    #if recursionList == "":
    #    recursionList = []
    if index == len(string):
        stringReverse = stringReverse[::-1]
        #recursionList = f"{''.join(recursionList[::-1])}"
        if stringReverse == string:
            return f"{string} is a palindrome"
        else:
            return f"{string} is not a palindrome"
    
    #recursionList.append(string[index])
    stringReverse += string[index]
    return palindrome(string, index + 1, stringReverse)
