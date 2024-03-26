# replace.py

# Save the sentence
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Reprint the sentence with exclamation marks replaced by blank spaces
modified_sentence = sentence.replace("!", " ")
print(modified_sentence)

# Reprint the modified sentence in uppercase
uppercase_sentence = modified_sentence.upper()
print(uppercase_sentence)

# Print the sentence in reverse
reversed_sentence = sentence[::-1]
print(reversed_sentence)
# This code uses the replace() function to replace exclamation marks with blank spaces, the upper() function to convert the sentence to uppercase, and slicing to print the sentence in reverse.