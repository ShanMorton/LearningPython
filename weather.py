import requests

# Import this library to use some of it's functions.

# d29ed9d06fffc17f2715092156ee12eb  Remember that this would be kept secret in the real world.
# find a way to hide this

# this is the api call https://api.openweathermap.org/data/2.5/weather?lat=5.5234&lon=-122.6762&appid=d29ed9d06fffc17f2715092156ee12eb
# use the Lat/Long for PDX  [45.5234, -122.6762]
try:
    responce = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat=5.5234&lon=-122.6762&appid=d29ed9d06fffc17f2715092156ee12eb")
    # fif this cmd runs it'll print good data below
except:
    print("This is not working for you at this time!\n")
    #Other wise I get this print for an error.

responce_json = responce.json()
# this will put the result in a variable and put it json format, so that it's easy to read.

# To get data from the dictonary
temperature = responce_json["main"]["temp"]
#print(temperature)
temp_min = responce_json["main"]["temp_min"]
#print(temp_min)
temp_max = responce_json["main"]["temp_max"]
#print(temp_max)
print(f"\n\nIn Portland OR, the temp is {temperature} \u00B0F. The MinTemp is {temp_min}\u00B0F, and the MaxTemp is {temp_max}\u00B0F.\n\n")

class City():

    #The initialize method
    # Ask for info when creating a new city instance
    # Ask for the city's name, latitude, longitude and the unit designation which we have set as default "imperial"
    def __init__(self, name, lat, long, units = "imperial"):
        self.name = name
        self.lat = lat
        self.long = long
        self.units = units

#call/create a city object
# I didn't supply a unit value b/c is has a default at this time, it can be supplied as needed in the call.
myCity = City("Portland", 5.5234,-122.6762)
# put the object I call into the variable "myCity"
