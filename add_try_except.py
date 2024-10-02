
test_list = ["apple", "banana", "cherry"]
print(test_list)
#print(test_list[4])


try:
    print(test_list[0])
    print(test_list[4])
except Exception as e:
    print("IndexError: list index out of range.  There is no index 4. \n")


print(test_list)