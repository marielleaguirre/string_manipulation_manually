# title() makes all first letter of each word in the string, capital letter. And all other letter in small case. 
# Create a program that do the same functionality without using title() function.

# ask user for string input
string_input = input("Enter a string: ")

# split the string into words
words_in_string = string_input.split()

# for each word, convert the first character to uppercase, while the rest of characters in the word remain lowercase
title_cased_words = [word[:1].upper() + word[1:].lower() for word in words_in_string]

# join word into a string
title_cased_string = " ".join(title_cased_words)
# print the string in title case
print(f"String in Title case: '{title_cased_string}'")