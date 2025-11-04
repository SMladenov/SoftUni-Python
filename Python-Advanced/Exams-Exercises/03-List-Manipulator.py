#List Manipulator

def list_manipulator (*args):

    listNumbers = list(args[0])
    cmd = args[1]
    where = args[2]

    listOtherNumbers = []
    
    if len(args) > 3:
        listOtherNumbers = list(args[3:])

    if cmd == "add":
        if where == "beginning":
            return listOtherNumbers + listNumbers
        elif where == "end":
            return listNumbers + listOtherNumbers

    elif cmd == "remove":
        if where == "beginning":
            if listOtherNumbers:
                return listNumbers[listOtherNumbers[0]:]
            else:
                return listNumbers[1:]
        if where  == "end":
            if listOtherNumbers:
                return listNumbers[:(len(listOtherNumbers) - 1) - listOtherNumbers[0]]
            else:
                return listNumbers[:len(listOtherNumbers) - 1]

print(list_manipulator([1,2,3], "remove", "end"))                   
print(list_manipulator([1,2,3], "remove", "beginning"))             
print(list_manipulator([1,2,3], "add", "beginning", 20))            
print(list_manipulator([1,2,3], "add", "end", 30))                  
print(list_manipulator([1,2,3], "remove", "end", 2))                
print(list_manipulator([1,2,3], "remove", "beginning", 2))          
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))    
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))          
