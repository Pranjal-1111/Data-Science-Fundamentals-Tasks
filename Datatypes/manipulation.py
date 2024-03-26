# manipulation.py

# Ask the user to enter a sentence
str_manip = input("Enter a sentence: ")

# Calculate and display the length of str_manip
length_of_str = len(str_manip)
print(f"The length of the entered sentence is: {length_of_str}")

# Find the last letter in str_manip and replace every occurrence with '@'
last_letter = str_manip[-1]
str_manip = str_manip.replace(last_letter, '@')
print(f"Replacing every occurrence of '{last_letter}' with '@': {str_manip}")

# Print the last 3 characters in str_manip backwards
last_three_backwards = str_manip[-3:][::-1]
print(f"The last 3 characters in reverse: {last_three_backwards}")

# Create a five-letter word using the first three characters and last two characters
five_letter_word = str_manip[:3] + str_manip[-2:]
print(f"A five-letter word made up of the first three and last two characters: {five_letter_word}")
# This code takes user input, performs the specified manipulations on the entered string (str_manip), and displays the results accordingly.