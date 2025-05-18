#  Write a program that accepts a comma separated sequence of words as input and
#  prints the words in a comma-separated sequence after sorting them alphabetically.
#  Suppose the following input is supplied to the program:
#  without,hello,bag,world
#  Then, the output should be:
#  bag,hello,without,world

# Accept a comma separated sequence of words as input and prints the words in a
input_sequence = input("Enter a comma-separated sequence of words: ")

# Split the input string into a list of words
words = input_sequence.split(",")

# Sort the list of words alphabetically
sorted_words = sorted(words)

# Join the sorted list back into a comma-separated string
sorted_sequence = ",".join(sorted_words)

# Print the sorted sequence
print("Sorted sequence:", sorted_sequence)