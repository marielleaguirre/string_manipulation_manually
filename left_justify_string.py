# ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. 
# Create a program that do the same functionality without using ljust() function.

# ask user for string input and how long they want their string to be
string_input = input("Enter a string: ")
desired_length = int(input("Enter the total length you want: "))

# if the string input is shorter than their desired length, add spaces to the right
if len(string_input) < desired_length:
    string_input = string_input + " " * (desired_length - len(string_input))

# print the string with added spaces to the right