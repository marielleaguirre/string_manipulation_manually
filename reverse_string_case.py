# swapcase() reverse the casing of each of the character of the string. 
# Create a program that do the same functionality without using swapcase() function.

# ask user for string input and initialize an empty result string, reverse_string_case
string_input = input("Enter a string: ")
reverse_string_case = ""

# using for loop, loop through each characters in the string
for character in string_input:
    if 'A' <= character <= 'Z':  # if character is uppercase, convert to lowercase
        reverse_string_case += chr(ord(character) + 32)
    elif 'a' <= character <= 'z':  # if character is lowercase, convert to uppercase
        reverse_string_case += chr(ord(character) - 32)
    else: 
        reverse_string_case += character

# print swapped casing of the string input 
print(f"Reverse casing: '{reverse_string_case}'")