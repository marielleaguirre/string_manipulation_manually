# rstrip() remove the space characters at the end of the string. 
# Create a program that do the same functionality without using rstrip() function.

# ask user for string input
string_input = input("Enter a string with trailing spaces: ")

# initialize an index variable at the last position of the string
# loop backward through the string until a non-space character is found
# slice the string to exclude trailing spaces
# print the modified string