# count() return how many time the function parameter appear in the string. 
# Create a program that do the same functionality without using count() function.

# ask user for string input and word/substring to count
string_input = input("Enter a string: ")
search_word = input("Enter the word/substring to count: ")

# initialize counter and index
occurrence_count = 0
index = 0

# loop to count occurrences, allowing overlaps
while index < len(string_input):
    index = string_input.find(search_word, index)
    if index == -1:
        break
    # move forward by 1 to check overlapping occurrences
    occurrence_count += 1
    index += 1

# print the result