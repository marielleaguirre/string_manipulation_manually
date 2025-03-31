# startswith() check if the string beginning part matches the function parameter. 
# Create a program that do the same functionality without using startswith() function.

# ask user for string input and prefix they want to check
string_input = input("Enter a string: ")
prefix_to_check = input("Enter the prefix you wish to check: ")

# compare the beginning of the string input with the prefix input
if string_input[:len(prefix_to_check)] == prefix_to_check:
    is_character_prefix = True
else:
    is_character_prefix = False
    
# print True if the string starts with the prefix input, otherwise print False