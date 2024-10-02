#classes are a blueprint
#import X to use the fuctions of "random"
import random

#this is the parent class 
#Inheritance flows from parent to child classes

class Animal():
    #print("This is in the class Animal!!\n")
    info = "a living thing that can move and eat and react to the world through its senses."

    def __init__(self, name):
        print("An Animal has been created, in class Animal")
        #we can give the Animal a name by setting this variable, and asking for the name
        #in the call of the function
        self.name = name



#This [Dog] is a child class of Animal()
#to make class dog a child of class animal put Animal in the () of the dog class
class Dog(Animal):
    
    #Line above:  This calls the animal class and runs the init function for the class Animal (the super)
    #then we'll see the print stmt in the class Animal, init function
    
    info = "A dog is a furry creature that loves to eat"

# create the init fuction/instance
# make sure to indent for the INIT function.
    def __init__(self, name):
        super().__init__(name)
        #Line above:  This calls the animal class and runs the init function for the class Animal (the super)
        #then we'll see the print stmt in the class Animal, init function
        print("A Dog has been created, in class Dog.")
        #print("\n\nThis in the INIT function!  I am alive!!!\n")
        #instance vaiables created in the INIT function
        self.luckynumber = random.randint(1, 1000) 
        self.fur = True
        
#create a class Bulldog 
# class Bulldog will inherite from class Dog (by putting Dog in the () when you call Bulldog)
class Bulldog(Dog):
    pass 
    #print("In class Bulldog!")

    def __init__(self, name):
        super().__init__(name)
        print("a Bulldog is created, in class Bulldog.")


# print the "info" variable value from inside the Dog class.
##print("\n\n",Dog.info)

# Calling the Dog() class.  It'll run the INIT Function
# this is why you'll see the stmt in the INIT function.

# now put Dog object to variable:
#dog1 = Dog("Reno")
dog1 = Bulldog("Jake")


#show that what is in class Animal can be passed to the child classes, print the info for an animal
#from the dog class
#this should print the def of an animal  with the line for the info inside the Dog class commented out
#on about line 16
#Once you uncomment line 16, you'll see the you can set the "info" vaiable to what you want
#at this time its the def of a dog.

#uncomment l16 and you'll get the def of a dog.  The value of "info" changes as the program runs throght
#and gets a new value for "info" from the dog class, that was previously assinged from the class Animal.


##print(dog1.info)




















#dog2 = Dog("Ebony")

# #print(dog1.luckynumber)
# #print(dog2.luckynumber)

# #can assign instance variables on the fly
# #dog1.name = "Reno"
# print(dog1.name)
# print(dog2.name)

