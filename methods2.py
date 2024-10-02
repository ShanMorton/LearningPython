
#classes are a blueprint

import random

class Dog:
    #print("This is in the Dog class")
    info = "A dog is a furry creature that loves to eat"


# create the init fuction/instance
# make sure to indent for the INIT function.
    def __init__(self, name):
        print("\n\nThis in the INIT function!  I am alive!!!\n")
        #instance vaiables created in the INIT function
        self.luckynumber = random.randint(1, 1000) 
        self.name = name


# print the "info" variable value from inside the Dog class.
##print("\n\n",Dog.info)


# Calling the Dog() class.  It'll run the INIT Function
# this is why you'll see the stmt in the INIT function.

# now put Dog object to variables:
dog1 = Dog("Reno")
dog2 = Dog("Ebony")

#print(dog1.luckynumber)
#print(dog2.luckynumber)

#can assign instance variables on the fly
#dog1.name = "Reno"
print(dog1.name)
print(dog2.name)

