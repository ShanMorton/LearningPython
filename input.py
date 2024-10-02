#fname = input("What is your name?\n")

#print(f"You said your first name is {fname}. \n")

#print(f" This is your name in uppercase. ", fname.upper())


#timestwo = input("What number do you want to multiply by 2? \n")
#print(timestwo * 2)
#print(" Since this is a sting, it just prints the string twice. Not the result we wanted. \n")

#print(int(timestwo) * 2, ", This is the results you were looking for. \n")
#print("Make sure you know the type of the answer you want to work with. \nInput always returns a string. \n")


caseText = input ("Type in some text that you want to change the case: \n")

choice = input("Do you want to make the text upper case (1) or lower case (2)? ")

if choice == '1':
    print(caseText.upper())
else:
    print(caseText.lower())
