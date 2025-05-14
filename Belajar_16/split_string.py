# Split a string into a list of words
input_str = "Python program to split and join a string"

# Split the string into a list of words (default split on whitespace)
word_list = input_str.split()

# Join the list of words into a string with a specified separator
separator = " "
output_str = separator.join(word_list)

# Print the results
print("Original String:", input_str)
print("List of Split Words:", word_list)
print("Joined String:", output_str)