#File Manipulator

import os

cmd = input()

genericPath = "C:\\Users\\Strahil.Mladenov\\Desktop\\FileManipulation\\task3\\"

def fileExists (path):
    try:
        if os.path.isfile(path):
            return True
        else:
            raise FileNotFoundError("An error occured")
    except FileNotFoundError as e:
        print (e)

def createFile (fileName, path = genericPath):
    fullPath = f"{genericPath}{fileName}"
    with open(fullPath, 'wt') as file:
        pass

def addContent (fileName, content, path = genericPath):
    fullPath = f"{genericPath}{fileName}"
    with open(fullPath, 'a') as file:
        file.write(f"{content}\n")

def replaceContent (fileName, oldString, newString, path = genericPath):
    fullPath = f"{genericPath}{fileName}"
    if fileExists(fullPath):
        with open(fullPath, 'rt') as file:
            fileRead = file.read()
            
        fileRead = fileRead.replace(oldString, newString)    
        with open(fullPath, 'wt') as fileToWrite:
            fileToWrite.write(fileRead)

def deleteFile (fileName, path = genericPath):
    fullPath = f"{genericPath}{fileName}"
    if fileExists(fullPath):
        os.remove(fullPath)

while cmd != "End":
    cmdSplit = cmd.split('-')
    action = cmdSplit[0]
    fileName = cmdSplit[1]
    
    if action == "Create":
        createFile(fileName)

    elif action == "Add":
        content = cmdSplit[2]
        addContent(fileName, content)
    
    elif action == "Replace":
        oldString = cmdSplit[2]
        newString = cmdSplit[3]
        replaceContent(fileName, oldString, newString)

    elif action == "Delete":
        deleteFile(fileName)

    cmd = input()
