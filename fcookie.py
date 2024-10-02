import random


#Integers/Whole numbers
lucky_num = (random.randint(1,1000))



#float numbers
#print(random.random() )

mylist = [ "You will will the lottery this year",
          "You will pet a dog, today!",
          "You will hit all the green lights driving!",
          "You will be promoted at work and get a raise!",
           "Shandra will not have to work with/near Gus today!"
          ]

fortune = random.choice(mylist)

print(f"Your lucky number is {lucky_num}, and {fortune}!")


