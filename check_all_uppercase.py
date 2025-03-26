# isupper() check if all characters of the string is on upper case. 
# Create a program that do the same functionality without using isupper() function.

# ask user for string input and initialize is_character_uppercase to True
string_input = input("Enter a string: ")
is_character_uppercase = True

# using for loop, loop through each characters in the string
# if at least one character is in lowercase, print False
# if all characters in the string are uppercase, print True