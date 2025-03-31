# rstrip() remove the space characters at the end of the string. 
# Create a program that do the same functionality without using rstrip() function.

# ask user for string input
string_input = input("Enter a string with trailing spaces: ")

# initialize an index variable at the last position of the string
index = len(string_input) -1

# loop backward through the string until a non-space character is found
for character in range(len(string_input) - 1, -1, -1):
    # slice the string to exclude trailing spaces
    if string_input[character] != " ":
        index = character
        break

string_without_trailing_spaces = string_input[:index + 1]

# print the modified string
print(f"'{string_without_trailing_spaces}'")