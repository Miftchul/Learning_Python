#  Write a program that accepts a sequence of whitespace separated words as input
#  and prints the words after removing all duplicate words and sorting them
#  alphanumerically.
#  Suppose the following input is supplied to the program:
#  hello world and practice makes perfect and hello world again
#  Then, the output should be:
#  again and hello makes perfect practice world

# Accept a sequence of whitespace-separated words as input
input_sequence = input("Enter a whitespace-separated sequence of words: ")
# Split the input string into a list of words
words = input_sequence.split()
# Sort the list of words alphanumerically and remove duplicates
sorted_words = sorted(set(words))
# Join the sorted list back into a whitespace-separated string
result_sequence = " ".join(sorted_words)

# Print the result
print("Sorted sequence without duplicates:", result_sequence)