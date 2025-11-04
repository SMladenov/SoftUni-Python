#Flights

def flights (*args):

    dicFlights = {}

    counterArg = 0

    destination = ""
    
    for flight in args:
        counterArg += 1
        
        if flight == "Finish":
            break
        else:
            if counterArg % 2 == 1:
                destination = flight
            elif counterArg % 2 == 0:

                passengers = int(flight)
                if destination not in dicFlights.keys():
                    dicFlights[destination] = passengers
                else:
                    dicFlights[destination] += passengers

    return dicFlights

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
