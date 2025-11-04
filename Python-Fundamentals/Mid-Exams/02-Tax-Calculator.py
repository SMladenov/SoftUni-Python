#Tax Calculator

vehicles = input().split('>>')
types = ['family', 'heavyDuty', 'sports']

totalTaxes = 0

for i in vehicles:
    iSplit = i.split(' ')
    vehicleType = iSplit[0]
    years = int(iSplit[1])
    km = int(iSplit[2])

    tax = 0

    if vehicleType not in types:
        print (f"Invalid car type.")
    else:
        if vehicleType == "family":
            tax += 50
            while km >= 3000:
                tax += 12
                km -= 3000
            tax -= (5 * years)
            totalTaxes += tax
            print (f"A {vehicleType} car will pay {tax:.2f} euros in taxes.")
            
        if vehicleType == "heavyDuty":
            tax += 80
            while km >= 9000:
                tax += 14
                km -= 9000
            tax -= (8 * years)
            totalTaxes += tax
            print (f"A {vehicleType} car will pay {tax:.2f} euros in taxes.")

        if vehicleType == "sports":
            tax += 100
            while km >= 2000:
                tax += 18
                km -= 2000
            tax -= (9 * years)
            totalTaxes += tax
            print (f"A {vehicleType} car will pay {tax:.2f} euros in taxes.")

print (f"The National Revenue Agency will collect {totalTaxes:.2f} euros in taxes.")