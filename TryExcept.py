# print("This is the before-print!\n")

# try:
#     #4 / 0
#     #print(f"This is my name: {name}. \n")
#     print(age)
#     #print(salary)
# #except NameError as e:
# #   print(e)
#     #print("This is the NameError.\n")
# except ZeroDivisionError:
#     print("Hey! Division by O is not allowed! \n")
# except Exception as e: 
#     print(f"This is how you print out the error:\n ", {e})
#     #print("This is the catch-all error.\n ")

# print("This is the after-print!\n")

#How to raise your own expections:
class errorRaisedBySm(Exception):
    pass
    #print("This is the code block that Shandra wrote to point out errors. \n\n\n")

def changeToUpper(words):
    if len(words) <= 0:
        raise errorRaisedBySm("\n\nThe words you provided contain no letters to make into UpperCase.\n\n\n\n\n\n")
    return words.upper()

print(changeToUpper(""))
#print(changeToUpper("arches national park is fun to visit"))