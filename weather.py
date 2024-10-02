import requests

# Import this library to use some of it's functions.

# d29ed9d06fffc17f2715092156ee12eb  Remember that this would be kept secret in the real world.
# find a way to hide this

# this is the api call https://api.openweathermap.org/data/2.5/weather?lat=5.5234&lon=-122.6762&appid=d29ed9d06fffc17f2715092156ee12eb
# use the Lat/Long for PDX  [45.5234, -122.6762]



class City():

    #The initialize method
    # Ask for info when creating a new city instance
    # Ask for the city's name, latitude, longitude and the unit designation which we have set as default "imperial"
    def __init__(self, name, lat, long, units = "imperial"):
        self.name = name
        self.lat = lat
        self.long = long
        self.units = units
        #Call the GetData for the city we want to create
        self.getData()

    def getData(self):
        try:
            responce = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.long}&appid=d29ed9d06fffc17f2715092156ee12eb")
            # if this cmd runs it'll print good data below
        except:
            print("This is not working for you at this time!\n")
            #Other wise I get this print for an error.

        responce_json = responce.json()
        # this will put the result in a variable and put it json format, so that it's easy to read.

        # To get data from the dictonary
        self.temp = responce_json["main"]["temp"]
        print(self.temp)
        self.temp_min = responce_json["main"]["temp_min"]
        print(self.temp_min)
        self.temp_max = responce_json["main"]["temp_max"]
        print(self.temp_max)
        
        
    def temp_print(self):
        print(f"\n\nIn Portland OR, the temp is {self.temp} \u00B0F. The MinTemp is {self.temp_min}\u00B0F, and the MaxTemp is {self.temp_max}\u00B0F.\n\n")



#call/create a city object
# I didn't supply a unit value b/c is has a default at this time, it can be supplied as needed in the call.
# put the object I call into the variable "myCity"
myCity = City("Portland", 5.5234,-122.6762)
myCity.temp_print()

