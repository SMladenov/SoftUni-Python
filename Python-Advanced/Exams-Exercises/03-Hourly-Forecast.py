#Hourly Forecast

def forecast (*args):

    sunnyLocations = []
    cloudyLocations = []
    rainyWeather = []

    for location, weather in args:
        if weather == "Sunny":
            sunnyLocations.append(location)
        elif weather == "Cloudy":
            cloudyLocations.append(location)
        elif weather == "Rainy":
            rainyWeather.append(location)

    listToOutput = []

    sunnyLocations.sort()
    cloudyLocations.sort()
    rainyWeather.sort()

    for location in sunnyLocations:
        listToOutput.append(f"{location} - Sunny")
    for location in cloudyLocations:
        listToOutput.append(f"{location} - Cloudy")
    for location in rainyWeather:
        listToOutput.append(f"{location} - Rainy")

    return '\n'.join(listToOutput)

# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))

# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
 