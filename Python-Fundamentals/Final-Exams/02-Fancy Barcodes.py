#Fancy Barcodes

import re

barcodes = int(input())

for i in range (barcodes):
    barcode = input()
    
    patternBarcode = r"\@\#+([A-Z][a-zA-Z0-9]{4,}[A-Z])\@\#+"
    barcodeMatches = re.findall(patternBarcode, barcode)

    tempGroup = ""

    if barcodeMatches:
        for b in barcodeMatches[0]:
            if b.isdigit():
                tempGroup += b
                
    if barcodeMatches:
        if tempGroup != "":
            print (f"Product group: {tempGroup}")
        else:
            print (f"Product group: 00")
    else:
        print (f"Invalid barcode")