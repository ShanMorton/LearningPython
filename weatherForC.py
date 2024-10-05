import requests

# Import this library to use some of it's functions.

# d29ed9d06fffc17f2715092156ee12eb  Remember that this would be kept secret in the real world.
# find a way to hide this

#this is the api call https://api.openweathermap.org/data/2.5/weather?lat=5.5234&lon=-122.6762&appid=d29ed9d06fffc17f2715092156ee12eb
#use the Lat/Long for PDX  [45.5234, -122.6762]

###Challenge 
#Change the print out of the units to be F or C as needed

class City():

    #The initialize method
    # Ask for info when creating a new city instance
    # Ask for the city's name, latitude, longitude and the unit designation which we have set as default "imperial"
    def __init__(self, name, lat, long, units = "imperial"):
        # set the incoming values from self to the variables in the method
        self.name = name
        self.lat = lat
        self.long = long
        self.units = units
        ## this is how I solved the challenge. it seems to work
        ## I asked if the units were imperial or metric and set a method variable to
        ## use in the print statment.
        if self.units == "imperial":
            self.temp_degree = "F"
        else:
            self.temp_degree = "C"
        #Call the GetData method for the city we want to create
        self.getData()

    #query the city from the data in put to the method call.
    def getData(self):
        try:
            responce = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.long}&appid=d29ed9d06fffc17f2715092156ee12e")
            # if this cmd runs it'll print good data below
        except:
            print("This is not working for you at this time!\n")
            #Other wise I get this print for an error.
        
        # this will put the result in a variable and put it json format, so that it's easy to read.
        # added self to the next lines on the right side of the ='s sign
        #Why?
        # This line we set the object's json to be what comes in from the query.
        self.responce_json = responce.json()
        
        # To get data from the dictonary
        #set the method variables to what comes back from the query. 
        #set the incoming info from the json repl to the method variables. 
        self.temp = self.responce_json["main"]["temp"]
        #print(self.temp)
        self.temp_min = self.responce_json["main"]["temp_min"]
        #print(self.temp_min)
        self.temp_max = self.responce_json["main"]["temp_max"]
        #print(self.temp_max)
        
        #print the information from the query. 
    def temp_print(self):
        print(f"\nIn {self.name}, the temp is {self.temp} \u00B0{self.temp_degree}. The MinTemp is {self.temp_min}\u00B0{self.temp_degree}, and the MaxTemp is {self.temp_max}\u00B0{self.temp_degree}.")



#call/create a city object
# I didn't supply a unit value b/c is has a default at this time, it can be supplied as needed in the call.
# put the object I call into the variable "myCity"
myCity = City("Portland", 5.5234,-122.6762, "metric")
myCity.temp_print()

nextCity = City("Dallas", 32.7831, -96.8067, "metric")
nextCity.temp_print()
#print(nextCity.responce_json)