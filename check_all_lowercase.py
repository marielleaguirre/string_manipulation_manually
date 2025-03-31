# islower() check if all characters of the string is on lower case. 
# Create a program that do the same functionality without using islower() function.

# ask user for string input and initialize is_character_lowercase to True
string_input = input("Enter a string: ")
is_character_lowercase = True

# using for loop, loop through each characters in the string
for character in string_input:
    # if at least one character is in uppercase, print False
    if 'A' <= character <= 'Z':
        is_character_lowercase = False
        break

# if all characters in the string are in lowercase, print True
print(is_character_lowercase)