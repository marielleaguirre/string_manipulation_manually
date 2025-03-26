# center() add space characters at the beginning and at the end of the string to print the string at the center. 
# Create a program that do the same functionality without using center() function.

# ask user for string input and how long they want their string to be
string_input = input("Enter a string: ")
desired_length = int(input("Enter the total length you want: "))

# if the string input is shorter than their desired length
#   calculate the total spaces needed, divide equally to both sides, then add space/s to both sides
# print center align string