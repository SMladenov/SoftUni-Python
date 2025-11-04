#File deletion

import os

fullPath = "C:\\Users\\Strahil.Mladenov\\Desktop\\fileCreation2.txt"

#Or with if statement
#if os.path.exists(fullPath):
#    os.remove(fullPath)

try:
    os.remove(fullPath)
    print (f"File Deleted")
except FileNotFoundError:
    print ("File does not exist")
