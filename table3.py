#create a class and set up a class variale
class Furniture:
    print('A piece of furniture has been created')
    
    def __init__(self, material):
        self.material = material
        print(f"The furniture is made from {self.material}\n")


class Table(Furniture):
    #shape = "square"
    print("A Table has been created.\n")

    def __init__(self, material):
        super().__init__(material)
        # this is an instance variable
        self.size = "large"
        print(f"The size of the table is {self.size}\n")


#print(f"\n\n The shape of the table is {Table.shape}\n")


# Table()

# sam_table = Table("Hickory Wood")

# #this is an instance variable, on the fly
# sam_table.cost = 25500.00

# print(f"The cost of Sam\'s Table is {sam_table.cost}")


#test inheritance:
sam_table = Table("Hickory Wood")
joe_table = Table("MDF")