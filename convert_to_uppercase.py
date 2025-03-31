# upper() converts all characters of the string into upper case. 
# Create a program that do the same functionality without using upper() function.

# ask user for string input and initialize an empty string, upper_case_string
string_input = input("Enter a string: ")
upper_case_string = ""

# using for loop, loop through each characters in the string
for character in string_input:
    # if a character is a lowercase character, convert to uppercase by subtracting 32 to its ASCII value
    if 'a' <= character <= 'z':
        upper_case_string += chr(ord(character) - 32)
    else: 
        upper_case_string += character

# print the string input in uppercase
print(upper_case_string)