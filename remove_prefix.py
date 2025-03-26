# removeprefix() remove the characters at the beginning of the string that matches the function parameter. 
# Create a program that do the same functionality without using removeprefix() function.

# ask user for string input and what prefix they want to remove
string_input = input("Enter a string: ")
remove_prefix = input("Enter the prefix you wish to remove: ")

# check if the string starts with the user input prefix
if string_input.startswith(remove_prefix):

# if it does, remove the prefix by slicing the string
    string_input = string_input[len(remove_prefix):]

# print the string input without the given prefix
