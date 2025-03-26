# lstrip() remove the space characters at the beginning of the string. 
# Create a program that do the same functionality without using lstrip() function.

# ask user for string input
string_input = input("Enter a string with leading spaces: ")

# initialize an empty result string, string_without_leading_spaces
string_without_leading_spaces = ""
non_space_character = 0

# using for loop, loop through each character in the string
for character in string_input:
    if not non_space_character and character == " ":
        continue

# if non-space character is found the value becomes True(1), then start adding characters to result string
    non_space_character = 1
    string_without_leading_spaces += character

# print the string input without leading spaces
print(string_without_leading_spaces)