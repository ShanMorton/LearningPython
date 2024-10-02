import random

class Animal:
    print("This is in the class Animal \n")
    dog_info = "An organism that feeds on matter to live."

    def __init__(self, legs):
        print("Inside the Class Animal Init function. An animal is created. \n")
        self.legs = legs
      

# #blue print plan of something you want to create
# #how to make a class?   
# # lower case 'class' and the name of the class you want to create with 
# # the name having a single capital letter like below Line 8

# to make the class dog a child of class animal:
#
#class Dog:
# put the name of the parent class in the ()'s of the child class
class Dog(Animal):
    info = "A dog is a creature that loves you all of his days!!!!"
    
    # self is the object being created
    # can add another variable, after self, example "legs" and you can assign that to a variable inside the class
    # when you call the object or supply the number of legs the dogs has, it is assigned to the variable
    def __init__(self):
        super().__init__(legs)
        print("Inside class Dog, A dog is created!")

        self.legs = legs
        # isntance variable or instace attributes:
        # to it up you'll use "self"
        self.dogAge = random.randint(1,15)
        #print(f"This dog is {self.dogAge} years old! \n")

        # This is a method!!!  a method is a function inside a class. Not sure what it's different than the 
        # first function on line 14.
    def bark(self):
        print("Dogs bark bark bark!!!\n\n")
        print(f"I am {self.dogAge} years old, and I have {self.legs} legs to run on! \n")

# # to print the informaton kept in variable "dog.info"  You have to tell print statment the class name dot variable name    
        #print(Dog.info)

# this is an "instance" or an "object" of the "Dog" class.

#Dog()
Animal(4)

# you can assign variable to hold the instance of the dog class
reno = Dog()
print(reno.dog_info)


#print out the dog's age:
print(f" Reno is {reno.dogAge} years old and has {reno.legs} legs. \n")


#Can assigne instance variables on the fly as well
reno.dogBreed = "Labrador"
print(f"Reno's breed is {reno.dogBreed}. So Handsome!! \n\n")

# Call the method from line 25
reno.bark()


# ###  Tinyhouse CLASS
# class Tinyhouse():
#     sqft = 264
#     story = 2
#     name = 'Morton Manor'
#     area = "PDX"

#     def __init__(self, color):
#         self.color = color

#     def location(self):
#         print(f"The location is {self.area}. \n\n\n\n")


# house_1 = Tinyhouse("blue")
# # print(Tinyhouse.sqft)
# # print(Tinyhouse.story)
# # print(Tinyhouse.name)
# # this is an example of passing in info to the object and printing it back out
# print(house_1.color)

# #this is an example of setting an instance variable/attribute on the fly.
# house_1.addr = "123 main street, Anywhere, ZZ, 78785"

# print(f"The address of house_1 is {house_1.addr}. \n")

# house_1.location()