# center() add space characters at the beginning and at the end of the string to print the string at the center. 
# Create a program that do the same functionality without using center() function.

# ask user for string input and how long they want their string to be
string_input = input("Enter a string: ")
desired_length = int(input("Enter the total length you want: "))

# if the string input is shorter than their desired length
if len(string_input) < desired_length:
    #calculate the total spaces needed, divide equally to both sides, then add space/s to both sides
    total_spaces = desired_length - len(string_input)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    string_input = " " * left_spaces + string_input + " " * right_spaces

# print center align string
print(f"Centered string: '{string_input}'")