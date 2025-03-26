# endswith() check if the string end part matches the function parameter. 
# Create a program that do the same functionality without using endswith() function.

# ask user for string input and a suffix to check
string_input = input("Enter a string: ")
suffix_to_check = input("Enter the suffix you wish to check: ")

# compare the end of the string input with the suffix input
if string_input[-len(suffix_to_check):] == suffix_to_check:
    is_character_suffix = True
else:
    is_character_suffix = False

# print True if string ends with the suffix input, otherwise print False
print(is_character_suffix)