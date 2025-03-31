# index() return the first location of the function parameter in the string. 
# Create a program that do the same functionality without using index() function.

# ask user for string input and the word/substring to find
string_input = input("Enter a string: ")
search_word = input("Enter the word/substring to find: ")

# use for loop to loop through the string to find the first occurrence
for i in range(len(string_input) - len(search_word) + 1):
    # if a match is found, print the index and break the loop
    if string_input[i:i + len(search_word)] == search_word:
        print(f"The word/substring '{search_word}' first appears at the index {i}.")
        break

# if no match is found after the loop, print a message saying it was not found