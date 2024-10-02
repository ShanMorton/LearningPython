#create a class and set up a class variale

class Table:
    shape = "square"



    def __init__(self):
        # this is an instance variable
        self.size = "large"
        print(f"The size of the table is {self.size}\n")


print(f"\n\n The shape of the table is {Table.shape}\n")

Table()

sam_table = Table()

#this is an instance variable, on the fly
sam_table.cost = 25500.00

print(f"The cost of Sam\'s Table is {sam_table.cost}")
