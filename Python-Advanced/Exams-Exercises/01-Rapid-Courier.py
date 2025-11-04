#Rapid Courier

packages = [int(i) for i in input().split()]
courries = [int(i) for i in input().split()]

totalPackages = 0

while packages and courries:
    currentPackage = packages[-1]
    currentCourrier = courries[0]
    if currentCourrier >= currentPackage:
        if currentCourrier > currentPackage:
            currentCourrier -= currentPackage * 2
            if currentCourrier > 0:
                courries.pop(0)
                courries.append(currentCourrier)
            else:
                courries.pop(0)
        elif currentCourrier == currentPackage:
            courries.pop(0)
        totalPackages += currentPackage
        packages.pop()

    elif currentCourrier < currentPackage:
        packages[-1] -= currentCourrier
        totalPackages += currentCourrier
        courries.pop(0)

print (f"Total weight: {totalPackages} kg")

if not packages and not courries:
    print (f"Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not courries:
    print (f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")
elif courries and not packages:
    print (f"Couriers are still on duty: {', '.join(map(str, courries))} but there are no more packages to deliver.")
