# capitalize() makes the first letter of the string, capital letter. And all other letter in small case. 
# Create a program that do the same functionality without using capitalize() function.

# ask user for string input
string_input = input("Enter a string: ")

# check if string is not empty, then convert the first character to uppercase, while the rest remain lowercase
if string_input:
    capitalized_string = string_input[0].upper() + string_input[1:].lower()
else:
    capitalized_string = string_input

# print the string in capitalize string format
print(f"Capitalized string: '{capitalized_string}'")