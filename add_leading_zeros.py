# zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. 
# Create a program that do the same functionality without using zfill() function.

# ask user for string input and the total length they want
string_input = input("Enter a string: ")
desired_length = int(input("Enter the total length you want: "))

# if the string input is shorter than desired length, add zeros to the left 
if len(string_input) < desired_length:
    string_input = "0" * (desired_length - len(string_input)) + string_input

# print the modified string with added zeros to the left
print(f"Modified string: '{string_input}'")