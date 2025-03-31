# removesuffix() remove the characters at the end of the string that matches the function parameter. 
# Create a program that do the same functionality without using removesuffix() function.

# ask user for a string input and what suffix they want to remove
string_input = input("Enter a string: ")
suffix = input("Enter the suffix you wish to remove: ")

# check if the string ends with the suffix input
if string_input.endswith(suffix):
    # remove the suffix manually by slicing
    removed_suffix = string_input[:len(string_input) - len(suffix)]

# print the string without the given suffix