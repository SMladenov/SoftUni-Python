#Fill the Box

def fill_the_box(*args):
    
    bigBox = args[0] * args[1] * args[2]
    totalCubes = 0
    
    for i in range (3, len(args)):
        if args[i] == "Finish":
            break
        else:
            totalCubes += args[i] 

    if bigBox - totalCubes > 0:
        return f"There is free space in the box. You could put {bigBox - totalCubes} more cubes."
    elif bigBox - totalCubes <= 0:
        return f"No more free space! You have {totalCubes - bigBox} more cubes."
