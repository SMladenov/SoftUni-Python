#Directory Traversal

import os

def creationReport (dictExample, path):
    fullPath = os.path.join(path, "report.txt")
    if not os.path.isfile(fullPath):
        
        with open (fullPath, 'a') as report:
            if isinstance(dictExample, dict):
                for key, value in dictExample.items():
                    report.write(f"{key}\n")
                    for file in value:
                        report.write(f"- - - {file}\n")

def directoryTraversal (path):
    if os.path.isdir(path):
        listFiles = [el for el in os.listdir(path) if os.path.isfile(os.path.join(path, el))]
    
        dictExtensions = {}
    
        for file in listFiles:
            fileSplit = file.split('.')
            extension = fileSplit[len(fileSplit) - 1]
            if f".{extension}" not in dictExtensions.keys():
                dictExtensions[f".{extension}"] = [file]
            else:
                dictExtensions[f".{extension}"].append(file)
    
        sortedDict = dict(sorted(dictExtensions.items(), key=lambda x: (x[0], x[1])))

        #print (sortedDict)
        
        creationReport(sortedDict, path)
        
path = "C:\\Users\\Strahil.Mladenov\\Desktop\\FileManipulation\\task4"

directoryTraversal(path)
