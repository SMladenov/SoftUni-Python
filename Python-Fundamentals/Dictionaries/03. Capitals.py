#Capitals

listCountries = input().split(', ')
listCapitals = input().split(', ')

dictCombined = {key: value for key, value in zip(listCountries, listCapitals)}

for key, value in dictCombined.items():
    print (f"{key} -> {value}")