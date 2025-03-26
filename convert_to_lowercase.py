# lower() converts all characters of the string into lower case. 
# Create a program that do the same functionality without using lower() function.

# ask user for string input and initialize an empty string, lower_case_string
string_input = input("Enter a string: ")
lower_case_string = ""

# using for loop to loop through each characters in the string
# if a character is an uppercase character, convert to lowercase by adding 32 to its ASCII value
# print the string input in lowercase